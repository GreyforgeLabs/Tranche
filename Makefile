# Omarchy PR Triage Makefile v1.0
# Jev-powered triage pipeline with colorized output

# ============== Colors & Symbols ==============
GREEN := \033[92m
EMERALD := \033[38;2;16;185;129m
CYAN := \033[96m
YELLOW := \033[93m
MAGENTA := \033[95m
RED := \033[91m
GRAY := \033[90m
BOLD := \033[1m
RESET := \033[0m

CHECK := ✓
CROSS := ✗
ARROW := ▸
PROGRESS := →
PEOPLE := 👥
SCALE := ⚖️

# ============== Project Metadata ==============
REPO := blackopsrepl/omarchy-pr-jev-triage
LIVE_URL := https://vdistefano.studio/omarchy-pr-jev-triage/
JUDGED := $(shell test -f out/judgments.jsonl && wc -l < out/judgments.jsonl || echo 0)
PAIRED := $(shell test -f out/pair_verdicts.jsonl && wc -l < out/pair_verdicts.jsonl || echo 0)

# ============== Phony Targets ==============
.PHONY: banner help fetch judge judge-full dupes cluster page gif all publish verify info clean-judgments

# ============== Default Target ==============
.DEFAULT_GOAL := help

# ============== Banner ==============
banner:
	@printf "$(EMERALD)$(BOLD)  ___  ___  _   _ _   _  _  _  _____ _   _ _   _  _____ _   _ __   __\n"
	@printf " / _ \\ / _ \\| | | | | | |( \\/ )( _   ) ( ) ( ) ( ) (_   _) ( ) ( )\\ \\ / /\n"
	@printf "( (_) ) (_) ) |_| | |_| | \\  /  ) ( ) | |\\ V V V V V | |  | |_| |\\ V V /\n"
	@printf " \\___/ \\___/ \\___/ \\___/  (__)  (_) (_)_)  \\_/\\_/\\_/\\_/  (_)  (_____) \\_/  $(RESET)"
	@printf "$(GRAY)  x Jev$(RESET)\n"
	@printf "  $(GRAY)judged: $(CYAN)$(JUDGED)$(GRAY) PRs, $(CYAN)$(PAIRED)$(GRAY) pair verdicts$(RESET)\n"
	@printf "  $(GRAY)$(LIVE_URL)$(RESET)\n\n"

# ============== Data ==============

fetch: banner
	@printf "$(CYAN)$(BOLD)╔══════════════════════════════════════╗$(RESET)\n"
	@printf "$(CYAN)$(BOLD)║        Fetching Open PRs             ║$(RESET)\n"
	@printf "$(CYAN)$(BOLD)╚══════════════════════════════════════╝$(RESET)\n\n"
	@printf "$(ARROW) $(BOLD)Paging omacom/omarchy pulls API (curl; python urllib is IPv6-broken here)...$(RESET)\n"
	@mkdir -p data/pages && rm -f data/pages/page_*.json && \
		ok=1; for i in $$(seq 1 30); do \
			curl -sf "https://api.github.com/repos/omacom/omarchy/pulls?state=open&per_page=100&page=$$i" > data/pages/page_$$i.json || { ok=0; break; }; \
			n=$$(python3 -c "import json;print(len(json.load(open('data/pages/page_$$i.json'))))" 2>/dev/null || echo 0); \
			printf "$(PROGRESS) page $$i: $$n PRs\n"; \
			[ "$$n" = "0" ] && break; sleep 0.3; done; \
		[ $$ok -eq 1 ] && printf "$(GREEN)$(CHECK) Fetch complete$(RESET)\n\n" || \
		(printf "$(RED)$(CROSS) Fetch failed$(RESET)\n\n" && exit 1)

# ============== Jev Pipeline ==============

judge: banner
	@printf "$(CYAN)$(BOLD)╔══════════════════════════════════════╗$(RESET)\n"
	@printf "$(CYAN)$(BOLD)║        Jev Judgment Pass             ║$(RESET)\n"
	@printf "$(CYAN)$(BOLD)╚══════════════════════════════════════╝$(RESET)\n\n"
	@printf "$(ARROW) $(BOLD)Judging PRs (7 typed questions, one batched call each)...$(RESET)\n"
	@python3 triage.py judge --resume && \
		printf "$(GREEN)$(CHECK) Judgments saved to out/judgments.jsonl$(RESET)\n\n" || \
		(printf "$(RED)$(CROSS) Judge pass failed$(RESET)\n\n" && exit 1)

judge-full: banner
	@printf "$(RED)$(BOLD)WARNING: fresh pass over all PRs — ~5M input tokens on Jev$(RESET)\n"
	@printf "$(YELLOW)Press Ctrl+C to abort, or Enter to continue...$(RESET)\n"
	@read dummy
	@python3 triage.py judge

dupes: banner
	@printf "$(ARROW) $(BOLD)Confirming duplicate pairs with Jev sameness judgments...$(RESET)\n"
	@python3 triage.py dupes && \
		printf "$(GREEN)$(CHECK) Pair verdicts in out/pair_verdicts.jsonl$(RESET)\n\n" || \
		(printf "$(RED)$(CROSS) Dupe pass failed$(RESET)\n\n" && exit 1)

cluster: banner
	@printf "$(ARROW) $(BOLD)Clustering tranches, dupes, escalation lists...$(RESET)\n"
	@python3 triage.py cluster

# ============== Output ==============

page: banner
	@printf "$(ARROW) $(BOLD)Rendering GitHub Pages report from out/ data...$(RESET)\n"
	@python3 gen_page.py && \
		printf "$(GREEN)$(CHECK) docs/index.html written$(RESET)\n\n" || \
		(printf "$(RED)$(CROSS) Page generation failed$(RESET)\n\n" && exit 1)

gif: banner
	@printf "$(ARROW) $(BOLD)Rendering title GIF with glyphfx (capture → rasterize)...$(RESET)\n"
	@python3 tools/make_title_gif.py && \
		printf "$(GREEN)$(CHECK) docs/assets/omarchy-triage.gif written$(RESET)\n\n" || \
		(printf "$(RED)$(CROSS) GIF generation failed$(RESET)\n\n" && exit 1)

# ============== Composite Targets ==============

all: fetch judge dupes cluster page
	@printf "$(GREEN)$(BOLD)╔══════════════════════════════════════╗$(RESET)\n"
	@printf "$(GREEN)$(BOLD)║        $(CHECK) PIPELINE COMPLETE              ║$(RESET)\n"
	@printf "$(GREEN)$(BOLD)╚══════════════════════════════════════╝$(RESET)\n"
	@printf "$(GRAY)Run 'make publish' to ship it.$(RESET)\n\n"

publish: banner
	@printf "$(CYAN)$(BOLD)╔══════════════════════════════════════╗$(RESET)\n"
	@printf "$(CYAN)$(BOLD)║        Publishing to Pages           ║$(RESET)\n"
	@printf "$(CYAN)$(BOLD)╚══════════════════════════════════════╝$(RESET)\n\n"
	@git add -A docs/ && \
		git diff --cached --quiet && \
			printf "$(YELLOW)Nothing new to publish$(RESET)\n\n" || \
		( git commit -qm "chore: refresh triage report" && git push -q origin main && \
		  printf "$(GREEN)$(CHECK) Pushed — Pages rebuilds at $(CYAN)$(LIVE_URL)$(RESET)\n" && \
		  printf "$(GRAY)Watch: gh api repos/$(REPO)/pages --jq .status$(RESET)\n\n" )

verify: banner
	@printf "$(ARROW) $(BOLD)Proving the release is live...$(RESET)\n"
	@gh api repos/$(REPO)/pages --jq '"  status: " + .status + "  (https enforced: " + (.https_enforced|tostring) + ")"'
	@code=$$(curl -s -o /tmp/verify.html -w "%{http_code}" -L "$(LIVE_URL)") ; \
		[ "$$code" = "200" ] && grep -q "OMARCHY TRIAGE" /tmp/verify.html && \
		printf "$(GREEN)$(CHECK) 200 + content at $(LIVE_URL)$(RESET)\n\n" || \
		(printf "$(RED)$(CROSS) Live check failed (HTTP $$code)$(RESET)\n\n" && exit 1)

info: banner
	@python3 -c "import json; s=json.load(open('out/summary.json')); [print(f'  $(CYAN){k:>22}$(RESET)  {v}') for k,v in s.items()]"
	@printf "\n"

# ============== Danger Zone ==============

clean-judgments: banner
	@printf "$(RED)$(BOLD)WARNING: deletes all Jev judgments (~5M tokens to redo)$(RESET)\n"
	@printf "$(YELLOW)Press Ctrl+C to abort, or Enter to continue...$(RESET)\n"
	@read dummy
	@rm -fv out/judgments.jsonl out/pair_verdicts.jsonl && \
		printf "$(GREEN)$(CHECK) Judgment cache cleared$(RESET)\n\n"

# ============== Help ==============

help: banner
	@/bin/echo -e "$(CYAN)$(BOLD)Pipeline:$(RESET)"
	@/bin/echo -e "  $(GREEN)make fetch$(RESET)         - Refresh open-PR snapshot (curl-paged REST)"
	@/bin/echo -e "  $(GREEN)make judge$(RESET)         - Jev pass over unjudged PRs (resume-safe)"
	@/bin/echo -e "  $(GREEN)make dupes$(RESET)         - Confirm duplicate pairs with Jev"
	@/bin/echo -e "  $(GREEN)make cluster$(RESET)       - Build tranches, dupe groups, escalation lists"
	@/bin/echo -e ""
	@/bin/echo -e "$(CYAN)$(BOLD)Output:$(RESET)"
	@/bin/echo -e "  $(GREEN)make page$(RESET)          - Render docs/index.html from out/ data"
	@/bin/echo -e "  $(GREEN)make gif$(RESET)           - Re-render the glyphfx title GIF"
	@/bin/echo -e ""
	@/bin/echo -e "$(CYAN)$(BOLD)Composite:$(RESET)"
	@/bin/echo -e "  $(GREEN)make all$(RESET)           - $(YELLOW)$(BOLD)fetch → judge → dupes → cluster → page$(RESET)"
	@/bin/echo -e "  $(GREEN)make publish$(RESET)       - Commit docs/ + push (Pages rebuilds)"
	@/bin/echo -e "  $(GREEN)make verify$(RESET)        - Prove the live page serves"
	@/bin/echo -e ""
	@/bin/echo -e "$(CYAN)$(BOLD)Other:$(RESET)"
	@/bin/echo -e "  $(GREEN)make info$(RESET)          - Show summary.json numbers"
	@/bin/echo -e "  $(GREEN)make judge-full$(RESET)    - $(RED)Fresh judgment pass (burns ~5M tokens)$(RESET)"
	@/bin/echo -e "  $(GREEN)make clean-judgments$(RESET) - $(RED)Delete the judgment cache$(RESET)"
	@/bin/echo -e "  $(GREEN)make help$(RESET)          - Show this help message"
	@/bin/echo -e ""
	@/bin/echo -e "$(GRAY)API key: ~/Documents/jevapi.txt  ·  Model: jev-latest (jev-1.13.x)$(RESET)"
	@/bin/echo -e ""
