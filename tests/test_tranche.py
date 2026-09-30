"""Offline regressions: synthetic PRs and mocked acquisition/model transports."""

import argparse
import copy
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import tranche


def pr(number, **changes):
    item = {
        "number": number,
        "title": "Fix widget after suspend",
        "body": "Fix widget initialization.",
        "user": {"login": "fixture"},
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": "2026-01-02T00:00:00Z",
        "head": {"sha": f"head-{number}"},
        "draft": False,
        "labels": [],
    }
    item.update(changes)
    return item


def answers():
    return {
        "category": {"choice": "fix-misc"},
        "risk": {"score": 1},
        "finished_form": {"score": 2},
        "review_effort": {"score": 1},
        "is_fix": {"noul": 0.9},
        "security_flag": {"noul": 0.1},
    }


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.out = self.root / "out"
        self.pages = self.root / "data" / "pages"
        self.out.mkdir()
        self.pages.mkdir(parents=True)
        for name, value in {
            "ROOT": self.root,
            "OUT_DIR": self.out,
            "PAGES_DIR": self.pages,
            "JUDGMENTS_PATH": self.out / "judgments.jsonl",
            "PAIRS_PATH": self.out / "pair_verdicts.jsonl",
        }.items():
            context = patch.object(tranche, name, value)
            context.start()
            self.addCleanup(context.stop)
        self.stdout = redirect_stdout(io.StringIO())
        self.stdout.__enter__()
        self.addCleanup(self.stdout.__exit__, None, None, None)
        # An unexpected key read/network call must fail the test, never contact a service.
        self.key = patch.object(
            tranche, "read_key", side_effect=AssertionError("unexpected key read")
        ).start()
        self.network = patch.object(
            tranche.urllib.request, "urlopen", side_effect=AssertionError("unexpected network")
        ).start()
        self.model = patch.object(
            tranche, "ask", side_effect=AssertionError("unexpected model call")
        ).start()
        self.addCleanup(patch.stopall)

    def inputs(self, items):
        tranche.atomic_json(
            self.pages / "snapshot.json",
            {
                "version": 1,
                "repo": tranche.REPO,
                "items": items,
                "digest": tranche.digest(items),
                "observed_at": "2026-01-02T00:00:00Z",
            },
        )
        return tranche.load_prs()

    def judgments(self, prs, *, legacy=False, custom=None):
        records = [
            {"number": n, "answers": copy.deepcopy(custom or answers()), "usage": {}} for n in prs
        ]
        for record in records:
            if not legacy:
                record["binding"] = tranche.judgment_binding(prs[record["number"]])
        tranche.JUDGMENTS_PATH.write_text("".join(json.dumps(r) + "\n" for r in records))
        return tranche.current_judgments(prs, allow_unbound=legacy)

    def pairs(self, prs, relationships, *, legacy=False):
        records = []
        for a, b, verdict, probability in relationships:
            a, b = sorted((a, b))
            record = {
                "a": a,
                "b": b,
                "verdict": verdict,
                "probabilities": {"same_change": probability},
            }
            if not legacy:
                record["binding"] = tranche.pair_binding(prs, a, b)
            records.append(record)
        tranche.PAIRS_PATH.write_text("".join(json.dumps(r) + "\n" for r in records))

    def cluster(self, *, allow_unbound=False):
        tranche.cmd_cluster(argparse.Namespace(allow_unbound=allow_unbound))
        return json.loads((self.out / "summary.json").read_text()), json.loads(
            (self.out / "dupes.json").read_text()
        )

    def render(self):
        for name in ("tranche.py", "gen_page.py"):
            shutil.copy(Path(tranche.__file__).parent / name, self.root / name)
        return subprocess.run(
            [sys.executable, str(self.root / "gen_page.py")],
            cwd=self.root,
            text=True,
            capture_output=True,
            timeout=15,
        )

    def test_unknown_diffstat_is_distinct_from_true_zero(self):
        prs = self.inputs([pr(1), pr(2, changed_files=0, additions=0, deletions=0)])
        state = tranche.pr_state(prs[1])["pr"]
        self.assertFalse(state["diffstat_available"])
        self.assertIn("unknown", state["diffstat"])
        self.assertNotIn("0 files", state["diffstat"])
        self.assertEqual(tranche.pr_state(prs[2])["pr"]["diffstat"], "0 files changed, +0/-0")
        for count in (-1, True, "0", None):
            prs = self.inputs([pr(1, changed_files=count, additions=0, deletions=0)])
            self.assertFalse(tranche.pr_state(prs[1])["pr"]["diffstat_available"])

    def test_binding_tracks_full_source_even_outside_body_projection(self):
        original = pr(1, body="x" * 1500)
        prs = self.inputs([original])
        self.judgments(prs)
        self.assertTrue(prs[1]["body_truncated"])
        self.assertEqual(len(prs[1]["body"]), 1200)
        for change in (
            {"body": "x" * 1500 + "new text"},
            {"head": {"sha": "new"}},
            {"updated_at": "later"},
            {"labels": [{"name": "new"}]},
        ):
            with self.subTest(change=change):
                updated = dict(original, **change)
                self.assertEqual(tranche.current_judgments(self.inputs([updated])), {})
        prs = self.inputs([original])
        with patch.object(tranche, "MODEL", "different-model"):
            self.assertEqual(tranche.current_judgments(prs), {})
        questions = tranche.judge_questions()
        questions["risk"]["instructions"]["question"] += " New policy."
        with patch.object(tranche, "judge_questions", return_value=questions):
            self.assertEqual(tranche.current_judgments(prs), {})

    def test_resume_reuses_only_matching_records_and_saves_projection(self):
        prs = self.inputs([pr(1)])
        self.judgments(prs)
        args = argparse.Namespace(resume=True, limit=None)
        tranche.cmd_judge(args)  # No key read or model call.
        self.inputs([pr(1, head={"sha": "updated"})])
        self.key.side_effect = None
        self.key.return_value = "synthetic-key"
        self.model.side_effect = None
        self.model.return_value = {
            "answers": answers(),
            "model": "fixture-model",
            "request_id": "fixture",
        }
        tranche.cmd_judge(args)
        self.model.assert_called_once()
        record = tranche.load_done()[1]
        self.assertEqual(record["head_sha"], "updated")
        self.assertEqual(record["input"], tranche.pr_state(tranche.load_prs()[1]))
        self.assertEqual(record["resolved_model"], "fixture-model")
        self.assertIn("judged_at", record)
        self.assertEqual(len(tranche.current_judgments(tranche.load_prs())), 1)

    def test_legacy_judgment_is_not_resume_hit(self):
        prs = self.inputs([pr(1)])
        self.judgments(prs, legacy=True)
        self.key.side_effect = None
        self.key.return_value = "synthetic-key"
        self.model.side_effect = None
        self.model.return_value = {"answers": answers()}
        tranche.cmd_judge(argparse.Namespace(resume=True, limit=1))
        self.model.assert_called_once()
        self.assertIn("binding", tranche.load_done()[1])

    def test_enormous_json_integers_are_unknown_without_poisoning_caches(self):
        huge = 10**400
        for value in (huge, -huge):
            with self.subTest(value_sign=value > 0):
                self.assertIsNone(tranche.metric({"answers": {"risk": {"score": value}}}, "risk"))
                self.assertIsNone(tranche.p_same({"probabilities": {"same_change": value}}))
                pair = tranche.normalize_pair({"verdict": "same_change",
                    "probabilities": {"same_change": 0.9, "unrelated": value}})
                self.assertEqual(pair["probabilities"]["same_change"], 0.9)
                self.assertIsNone(pair["probabilities"]["unrelated"])
                tranche.JUDGMENTS_PATH.write_text(json.dumps({"number": 999,
                    "binding": "stale", "answers": {"risk": {"score": value}}}) + "\n")
                self.assertEqual(tranche.current_judgments({}), {})
        self.inputs([])
        summary, _ = self.cluster()
        self.assertEqual(summary["judged"], 0)

    def test_pair_reuse_is_bound_to_both_sources_questions_and_model(self):
        prs = self.inputs([pr(1), pr(2)])
        judgments = self.judgments(prs)
        self.pairs(prs, [(1, 2, "same_change", 0.9)])
        self.assertEqual(len(tranche.current_pairs(prs, judgments)), 1)
        tranche.cmd_dupes(argparse.Namespace(max_pairs=10))  # No key/model calls.
        changed = self.inputs([pr(1), pr(2, head={"sha": "new"})])
        new_judgments = self.judgments(changed)
        self.assertEqual(tranche.current_pairs(changed, new_judgments), [])
        with patch.object(tranche, "pair_questions", return_value={"new": "policy"}):
            self.assertEqual(tranche.current_pairs(prs, judgments), [])
        with patch.object(tranche, "MODEL", "new-model"):
            self.assertEqual(tranche.current_pairs(prs, judgments), [])
        self.key.side_effect = None
        self.key.return_value = "synthetic-key"
        self.model.side_effect = None
        self.model.return_value = {
            "answers": {
                "sameness": {"choice": "same_change", "probabilities": {"same_change": 0.9}}
            }
        }
        tranche.cmd_dupes(argparse.Namespace(max_pairs=10))
        self.model.assert_called_once()
        self.assertEqual(len(tranche.current_pairs(changed, new_judgments)), 1)

    def test_closed_members_do_not_reenter_pairs_or_reports(self):
        prs = self.inputs([pr(1), pr(2)])
        self.judgments(prs)
        self.pairs(prs, [(1, 2, "same_change", 0.9)])
        current = self.inputs([pr(1)])
        judgments = tranche.current_judgments(current)
        self.assertEqual(tranche.lexical_pairs(current, judgments), [])
        self.assertEqual(tranche.current_pairs(current, judgments), [])
        tranche.cmd_dupes(argparse.Namespace(max_pairs=10))
        summary, dupes = self.cluster()
        self.assertEqual(summary["judged"], 1)
        self.assertEqual(dupes["confirmed_groups"], [])
        self.assertEqual(summary["ready_prs"], 1)

    def test_connected_group_exposes_negative_uncertain_missing_relationships(self):
        prs = self.inputs([pr(1), pr(2), pr(3)])
        self.judgments(prs)
        edges = [(1, 2, "same_change", 0.9), (2, 3, "same_change", 0.9)]
        for extra, field in (
            ([(1, 3, "related_but_different", 0.04)], "conflicting_pairs"),
            ([(1, 3, "same_change", 0.59)], "uncertain_pairs"),
            ([], "missing_pairs"),
        ):
            with self.subTest(field=field):
                self.pairs(prs, edges + extra)
                summary, dupes = self.cluster()
                self.assertEqual(dupes["confirmed_groups"], [])
                self.assertEqual(dupes["review_groups"][0]["members"], [1, 2, 3])
                self.assertTrue(dupes["review_groups"][0][field])
                self.assertEqual(summary["ready_prs"], 0)
                self.assertIn(field, (self.out / "tranches.md").read_text())

    def test_contradictory_pair_is_visible_standalone_and_inside_groups(self):
        prs = self.inputs([pr(1), pr(2), pr(3)])
        self.judgments(prs)
        for verdict, probability, classification in (
            ("unrelated", 0.9, "contradictory"),
            ("related_but_different", 0.65, "contradictory"),
            ("same_change", 0.1, "contradictory"),
            ("same_change", 0.35, "uncertain"),
            ("unrelated", 0.64, "uncertain"),
            ("invalid", 0.9, "malformed"),
            ("same_change", None, "malformed"),
        ):
            with self.subTest(verdict=verdict, probability=probability):
                self.pairs(prs, [(1, 3, verdict, probability)])
                _, dupes = self.cluster()
                self.assertEqual(len(dupes["uncertain_pairs"]), 1)
                diagnostic = dupes["uncertain_pairs"][0]
                self.assertEqual(diagnostic["classification"], classification)
                self.assertEqual(diagnostic["p_same"], probability)
                self.assertIn(classification, (self.out / "tranches.md").read_text())
                result = self.render()
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(classification, (self.root / "docs" / "index.html").read_text())
                self.pairs(prs, [(1, 2, "same_change", 0.9),
                    (2, 3, "same_change", 0.9), (1, 3, verdict, probability)])
                _, dupes = self.cluster()
                self.assertEqual(dupes["confirmed_groups"], [])
                group = dupes["review_groups"][0]
                field = "conflicting_pairs" if classification == "contradictory" else "uncertain_pairs"
                self.assertEqual(group[field][0]["classification"], classification)
        self.pairs(prs, [(1, 2, "unrelated", 0.1)])
        _, dupes = self.cluster()
        self.assertEqual(dupes["uncertain_pairs"], [])
        self.assertEqual(dupes["review_groups"], [])

    def test_consistent_group_does_not_choose_oldest_survivor(self):
        prs = self.inputs([pr(1), pr(2), pr(3)])
        self.judgments(prs)
        self.pairs(
            prs,
            [(1, 2, "same_change", 0.9), (2, 3, "same_change", 0.9), (1, 3, "same_change", 0.9)],
        )
        summary, dupes = self.cluster()
        self.assertEqual(dupes["confirmed_groups"], [[1, 2, 3]])
        self.assertEqual(summary["superseded"], 0)
        items = json.loads((self.out / "clusters.json").read_text())["fix-misc"]["low"]
        self.assertTrue(all(item["superseded_by"] is None for item in items))
        self.assertEqual(summary["ready_prs"], 0)

    def test_published_conflict_shape_does_not_become_confirmed_equivalence(self):
        # Synthetic titles/bodies; numeric IDs preserve the observed public graph shape.
        prs = self.inputs([pr(n) for n in (7765, 8065, 12635, 12651)])
        self.judgments(prs)
        self.pairs(
            prs,
            [
                (7765, 8065, "related_but_different", 0.04),
                (8065, 12635, "same_change", 0.96),
                (7765, 12635, "same_change", 0.72),
                (8065, 12651, "same_change", 0.94),
            ],
        )
        _, dupes = self.cluster()
        self.assertEqual(dupes["confirmed_groups"], [])
        diagnostic = dupes["review_groups"][0]
        self.assertEqual(diagnostic["members"], [7765, 8065, 12635, 12651])
        self.assertEqual(diagnostic["conflicting_pairs"][0]["p_same"], 0.04)
        self.assertEqual(len(diagnostic["missing_pairs"]), 2)

    def test_unknown_or_invalid_model_fields_do_not_enter_review_candidates(self):
        prs = self.inputs([pr(1)])
        for field in ("risk", "security_flag", "finished_form", "is_fix", "review_effort"):
            for value in (
                None,
                {},
                {"score": True, "noul": True},
                {"score": -1, "noul": -1},
                {"score": 10, "noul": 10},
            ):
                with self.subTest(field=field, value=value):
                    data = answers()
                    data[field] = value
                    self.judgments(prs, custom=data)
                    summary, _ = self.cluster()
                    self.assertEqual(summary["ready_prs"], 0)
        for value in (float("nan"), float("inf"), "0", True):
            self.assertIsNone(tranche.metric({"answers": {"risk": {"score": value}}}, "risk"))
        self.assertIsNone(tranche.p_same({"probabilities": {"same_change": float("nan")}}))

    def test_model_judgments_normalize_before_save_and_retry_unknown_metrics(self):
        self.inputs([pr(1)])
        self.key.side_effect = None
        self.key.return_value = "synthetic-key"
        self.model.side_effect = None
        args = argparse.Namespace(resume=True, limit=None)
        for value, usage in ((float("nan"), None), (float("inf"), []),
                             (-float("inf"), {"input_tokens": True, "output_tokens": -1}),
                             ("1", {"input_tokens": 2.5, "output_tokens": "3"})):
            with self.subTest(value=value, usage=usage):
                data = answers()
                data["risk"]["score"] = value
                self.model.return_value = {"answers": data, "usage": usage}
                before = self.model.call_count
                tranche.cmd_judge(args)
                self.assertEqual(self.model.call_count, before + 1)
                record = tranche.load_done()[1]
                self.assertIsNone(record["answers"]["risk"]["score"])
                self.assertEqual(record["answers"]["finished_form"]["score"], 2)
                self.assertEqual(record["usage"], {"input_tokens": 0, "output_tokens": 0})
                self.assertTrue(record["normalization_errors"])
                json.dumps(record, allow_nan=False)
                self.assertEqual(self.cluster()[0]["ready_prs"], 0)
                result = self.render()
                self.assertEqual(result.returncode, 0, result.stderr)
        self.model.return_value = {"answers": answers(), "usage": {"input_tokens": 7}}
        tranche.cmd_judge(args)
        before = self.model.call_count
        tranche.cmd_judge(args)
        self.assertEqual(self.model.call_count, before)
        self.assertEqual(self.cluster()[0]["tokens"], {"input": 7, "output": 0})

    def test_pair_responses_and_poisoned_caches_recover_without_losing_evidence(self):
        prs = self.inputs([pr(1), pr(2)])
        self.judgments(prs)
        self.pairs(prs, [(1, 2, "same_change", float("nan"))])
        path = tranche.JUDGMENTS_PATH
        rows = [json.loads(line) for line in path.read_text().splitlines()]
        rows[0]["answers"]["risk"]["score"] = float("inf")
        rows[0]["usage"] = None
        junk = [None, [], 7, {}, {"number": []}, {"number": True}]
        path.write_text("broken\n" + "".join(json.dumps(r) + "\n" for r in junk + rows))
        tranche.PAIRS_PATH.write_text("broken\n" + "".join(json.dumps(r) + "\n" for r in
            [None, [], {}, {"a": [], "b": 2}, {"a": True, "b": 2}]) + tranche.PAIRS_PATH.read_text())
        before = path.read_bytes()
        self.assertEqual(self.cluster()[0]["ready_prs"], 1)
        self.assertEqual(self.render().returncode, 0)
        self.assertEqual(path.read_bytes(), before)  # Recovery is in memory, not binding retrofit.
        self.key.side_effect = None
        self.key.return_value = "synthetic-key"
        self.model.side_effect = None
        self.model.return_value = {"answers": answers()}
        tranche.cmd_judge(argparse.Namespace(resume=True, limit=None))
        self.model.assert_called_once()
        for response in (None, {"answers": []}, {"answers": {"sameness": []}},
                         {"answers": {"sameness": {"choice": [], "probabilities": []}}},
                         *[{"answers": {"sameness": {"choice": "same_change",
                            "probabilities": {"same_change": v}}}, "usage": "invalid"}
                           for v in (float("nan"), float("inf"), -float("inf"), True, 2)]):
            with self.subTest(response=response):
                self.model.return_value = response
                calls = self.model.call_count
                tranche.cmd_dupes(argparse.Namespace(max_pairs=10))
                self.assertEqual(self.model.call_count, calls + 1)
                records = tranche.current_pairs(prs, tranche.current_judgments(prs))
                self.assertEqual(len(records), 1)
                self.assertIsNone(tranche.p_same(records[0]))
                self.assertTrue(records[0]["normalization_errors"])
                for line in tranche.PAIRS_PATH.read_text().splitlines()[7:]:
                    json.loads(line, parse_constant=lambda token: self.fail(token))
                self.assertEqual(self.cluster()[1]["confirmed_groups"], [])
                self.assertEqual(self.render().returncode, 0)
        self.model.return_value = {"answers": {"sameness": {"choice": "same_change",
            "probabilities": {"same_change": 0.9}}}, "usage": {"input_tokens": 3}}
        tranche.cmd_dupes(argparse.Namespace(max_pairs=10))
        calls = self.model.call_count
        tranche.cmd_dupes(argparse.Namespace(max_pairs=10))
        self.assertEqual(self.model.call_count, calls)
        self.assertEqual(self.cluster()[1]["confirmed_groups"], [[1, 2]])
        self.assertEqual(self.render().returncode, 0)

    def test_invalid_category_and_answer_shapes_are_reportable_not_reusable(self):
        prs = self.inputs([pr(1)])
        self.key.side_effect = None
        self.key.return_value = "synthetic-key"
        self.model.side_effect = None
        args = argparse.Namespace(resume=True, limit=None)
        for shape in (dict(answers(), category={"choice": []}), None, [], "bad"):
            with self.subTest(shape=shape):
                tranche.JUDGMENTS_PATH.write_text(json.dumps({"number": 1,
                    "answers": shape, "binding": tranche.judgment_binding(prs[1])}) + "\n")
                self.assertEqual(self.cluster()[0]["ready_prs"], 0)
                self.assertEqual(self.render().returncode, 0)
                self.model.return_value = {"answers": shape}
                calls = self.model.call_count
                tranche.cmd_judge(args)
                tranche.cmd_judge(args)
                self.assertEqual(self.model.call_count, calls + 2)
                self.assertEqual(self.cluster()[0]["ready_prs"], 0)
        for response in (None, [], {}):
            self.model.return_value = response
            tranche.cmd_judge(args)
            self.assertEqual(self.cluster()[0]["ready_prs"], 0)

    def test_drafts_cannot_enter_review_candidates(self):
        prs = self.inputs([pr(1, draft=True)])
        self.judgments(prs)
        self.assertEqual(self.cluster()[0]["ready_prs"], 0)

    def test_security_meta_category_has_top_priority(self):
        prs = self.inputs([pr(n) for n in (1, 2, 3, 4)])
        records = {1: dict(answers(), security_flag={"noul": 0.9}),
                   2: dict(answers(), security_flag={"noul": 0.5}),
                   3: dict(answers(), security_flag={"noul": 0.49}),
                   4: dict(answers(), security_flag={"noul": None})}
        tranche.JUDGMENTS_PATH.write_text("".join(
            json.dumps({"number": n, "answers": records[n],
                        "binding": tranche.judgment_binding(prs[n])}) + "\n"
            for n in sorted(prs)))
        summary, _ = self.cluster()
        self.assertEqual(summary["security_priority"], 2)
        clusters = json.loads((self.out / "clusters.json").read_text())
        self.assertEqual([item["number"] for item in clusters["security-review"]], [1, 2])
        markdown = (self.out / "tranches.md").read_text()
        self.assertLess(markdown.index("Security review — top priority"),
                        markdown.index("## Review candidates:"))
        report = self.render()
        self.assertEqual(report.returncode, 0, report.stderr)

    def test_security_section_absent_when_nothing_flagged(self):
        prs = self.inputs([pr(1)])
        self.judgments(prs)
        summary, _ = self.cluster()
        self.assertEqual(summary["security_priority"], 0)
        clusters = json.loads((self.out / "clusters.json").read_text())
        self.assertEqual(clusters["security-review"], [])
        self.assertNotIn("Security review — top priority", (self.out / "tranches.md").read_text())

    def test_unbound_opt_in_is_inspection_not_freshness_or_readiness(self):
        prs = self.inputs([pr(1), pr(2)])
        self.judgments(prs, legacy=True)
        self.pairs(prs, [(1, 2, "same_change", 0.9)], legacy=True)
        self.assertEqual(self.cluster()[0]["judged"], 0)
        summary, dupes = self.cluster(allow_unbound=True)
        self.assertEqual(summary["unbound_judgments"], 2)
        self.assertEqual(summary["ready_prs"], 0)
        self.assertEqual(dupes["confirmed_groups"], [])
        self.assertTrue(dupes["review_groups"][0]["unbound_evidence"])
        self.judgments(prs)
        self.inputs([pr(1, body="changed"), pr(2, body="changed")])
        self.assertEqual(self.cluster(allow_unbound=True)[0]["judged"], 0)

    def test_empty_fetch_removes_legacy_tail_membership(self):
        (self.pages / "page_1.json").write_text(json.dumps([pr(99)]))
        self.network.side_effect = [io.BytesIO(b"[]")]
        tranche.cmd_fetch(argparse.Namespace(transport="urllib"))
        self.assertEqual(tranche.load_prs(), {})
        self.assertTrue((self.pages / "page_1.json").exists())  # Ignored legacy input.

    def test_exact_page_boundary_ends_with_empty_page_and_replaces_membership(self):
        self.inputs([pr(999)])
        items = [pr(n) for n in range(1, 101)]
        self.network.side_effect = [io.BytesIO(json.dumps(items).encode()), io.BytesIO(b"[]")]
        with patch.object(tranche.time, "sleep"):
            tranche.cmd_fetch(argparse.Namespace(transport="urllib"))
        self.assertEqual(set(tranche.load_prs()), set(range(1, 101)))
        self.assertEqual(self.network.call_count, 2)

    def test_failed_or_duplicate_pagination_retains_committed_snapshot(self):
        self.inputs([pr(999)])
        before = (self.pages / "snapshot.json").read_bytes()
        items = [pr(n) for n in range(1, 101)]
        for second in (
            urllib.error.URLError("offline fixture"),
            io.BytesIO(json.dumps([pr(1)]).encode()),
        ):
            self.network.side_effect = [io.BytesIO(json.dumps(items).encode()), second]
            with (
                patch.object(tranche.time, "sleep"),
                self.assertRaises((urllib.error.URLError, tranche.TrancheFatal)),
            ):
                tranche.cmd_fetch(argparse.Namespace(transport="urllib"))
            self.assertEqual((self.pages / "snapshot.json").read_bytes(), before)

    def test_malformed_fetch_does_not_replace_usable_snapshot(self):
        self.inputs([pr(999)])
        before = (self.pages / "snapshot.json").read_bytes()
        for item in ({"number": 1}, pr(1, body={"invalid": "type"}), pr(1, labels=None)):
            self.network.side_effect = [io.BytesIO(json.dumps([item]).encode())]
            with self.assertRaises(tranche.TrancheFatal):
                tranche.cmd_fetch(argparse.Namespace(transport="urllib"))
            self.assertEqual((self.pages / "snapshot.json").read_bytes(), before)

    def test_curl_transport_uses_same_atomic_membership_commit(self):
        self.inputs([pr(999)])
        result = subprocess.CompletedProcess([], 0, json.dumps([pr(1)]), "")
        with patch.object(tranche.subprocess, "run", return_value=result) as run:
            tranche.cmd_fetch(argparse.Namespace(transport="curl"))
        self.assertEqual(set(tranche.load_prs()), {1})
        self.assertIn("--max-time", run.call_args.args[0])
        before = (self.pages / "snapshot.json").read_bytes()
        with patch.object(
            tranche.subprocess,
            "run",
            return_value=subprocess.CompletedProcess([], 22, "", "fixture"),
        ):
            with self.assertRaises(tranche.TrancheFatal):
                tranche.cmd_fetch(argparse.Namespace(transport="curl"))
        self.assertEqual((self.pages / "snapshot.json").read_bytes(), before)

    def test_snapshot_repository_and_content_integrity_are_checked(self):
        items = [pr(1)]
        for field, replacement in (("repo", "other/repo"), ("items", [pr(2)]), ("version", 999)):
            self.inputs(items)
            path = self.pages / "snapshot.json"
            value = json.loads(path.read_text())
            value[field] = replacement
            path.write_text(json.dumps(value))
            with self.assertRaises(tranche.TrancheFatal):
                tranche.load_prs()

    def test_html_render_matches_cli_coverage_and_escapes_source_text(self):
        prs = self.inputs([pr(1, title="Fix <script>alert(1)</script>"), pr(2)])
        self.judgments({1: prs[1]})
        summary, _ = self.cluster()
        self.assertEqual(summary["ready_prs"], 1)
        result = self.render()
        self.assertEqual(result.returncode, 0, result.stderr)
        page = (self.root / "docs" / "index.html").read_text()
        import re
        payload = re.search(r'<script id="workbench-data" type="application/json">(.*?)</script>', page, re.S)
        self.assertIsNotNone(payload, "Workbench must include all captured PRs")
        rows = json.loads(payload.group(1))["prs"]
        self.assertEqual([row["number"] for row in rows], [1, 2])
        self.assertEqual(rows[0]["title"], "Fix <script>alert(1)</script>")
        self.assertNotIn("<script>alert(1)</script>", page)
        self.assertIn(r"\u003cscript\u003e", payload.group(1))
        self.assertTrue(rows[0]["candidate"])
        self.assertFalse(rows[1]["candidate"])
        self.assertIsNone(rows[1]["risk"])
        self.assertIsNone(rows[1]["security"])
        self.assertEqual(rows[1]["freshness"], "unjudged or stale")
        self.assertEqual(rows[1]["category"], "unknown")
        self.assertNotIn("reviewed &amp; QA'd", page)
        self.assertNotIn("security-clean", page)
        self.assertIn("AI-assisted priorities; review code and tests before merging.", page)

    def test_html_exposes_group_conflicts(self):
        prs = self.inputs([pr(1), pr(2), pr(3)])
        self.judgments(prs)
        self.pairs(
            prs, [(1, 2, "same_change", 0.9), (2, 3, "same_change", 0.9), (1, 3, "unrelated", 0.01)]
        )
        self.cluster()
        result = self.render()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("conflicting_pairs", (self.root / "docs" / "index.html").read_text())

    def test_html_refuses_stale_inputs_or_mixed_outputs_before_overwrite(self):
        prs = self.inputs([pr(1)])
        self.judgments(prs)
        self.cluster()
        self.assertEqual(self.render().returncode, 0)
        target = self.root / "docs" / "index.html"
        before = target.read_bytes()
        self.inputs([pr(1, head={"sha": "changed"})])
        self.assertNotEqual(self.render().returncode, 0)
        self.assertEqual(target.read_bytes(), before)
        self.inputs([pr(1)])
        (self.out / "dupes.json").write_text("{}")
        self.assertNotEqual(self.render().returncode, 0)
        self.assertEqual(target.read_bytes(), before)

    def test_workbench_has_native_controls_and_no_process_commentary(self):
        self.inputs([pr(1, body='Snippet </script><img src=x onerror=alert(1)> & text')])
        self.key.side_effect = None
        self.key.return_value = "synthetic-key"
        self.model.side_effect = None
        self.model.return_value = {"answers": dict(answers(), security_flag={"noul": 0.8})}
        tranche.cmd_judge(argparse.Namespace(resume=True, limit=None))
        self.cluster()
        self.assertEqual(self.render().returncode, 0)
        page = (self.root / "docs" / "index.html").read_text()
        for text in ('assets/workbench.css', 'assets/workbench.js', '<dialog',
                     'id="search"', 'id="sort"', 'id="category"', 'aria-live="polite"',
                     'data-queue="security"', 'Security first', 'Security probability',
                     'Review candidates', 'Senior review', 'Author follow-up', 'Related PRs',
                     'assets/tranche.gif', 'assets/tranche-title.png', 'assets/omarchy.gif',
                     'assets/omarchy-title.png', 'assets/tranche-mascot.png'):
            self.assertIn(text, page)
        self.assertLess(page.index('data-queue="security"'), page.index('data-queue="all"'))
        payload = json.loads(re.search(
            r'<script id="workbench-data" type="application/json">(.*?)</script>',
            page, re.S).group(1))
        self.assertTrue(payload["prs"][0]["security_priority"])
        for text in ('Observation:', 'requested jev', 'fresh runs:', '<blockquote>',
                     '<b>Method.</b>', 'fetch → judge', '<img src=x onerror=alert(1)>'):
            self.assertNotIn(text, page)
        self.assertIn(r'\u003c/script\u003e', page)
        self.assertIn(r'\u0026', page)

    def test_empty_corpus_renders_without_credentials(self):
        self.inputs([])
        self.cluster()
        result = self.render()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(
            "0 captured PRs", (self.root / "docs" / "index.html").read_text()
        )

    def test_all_supports_documented_resume_and_pair_budget(self):
        with (
            patch.object(
                sys, "argv", ["tranche.py", "all", "--resume", "--limit", "2", "--max-pairs", "0"]
            ),
            patch.object(tranche, "cmd_judge") as judge,
            patch.object(tranche, "cmd_dupes") as dupes,
            patch.object(tranche, "cmd_cluster") as cluster,
        ):
            tranche.main()
        self.assertTrue(judge.call_args.args[0].resume)
        self.assertEqual(dupes.call_args.args[0].max_pairs, 0)
        self.assertEqual(cluster.call_count, 1)


if __name__ == "__main__":
    unittest.main()
