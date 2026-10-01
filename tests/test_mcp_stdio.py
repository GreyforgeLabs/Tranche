"""Opt-in real SDK/client test: TRANCHE_MCP_INTEGRATION=1 python -m unittest tests.test_mcp_stdio."""
import asyncio
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

import tranche


@unittest.skipUnless(os.environ.get("TRANCHE_MCP_INTEGRATION") == "1", "opt-in SDK integration")
class StdioTests(unittest.TestCase):
    def test_sdk_preserves_bounded_text_at_serialization_boundary(self):
        from unittest.mock import patch
        import mcp_server

        payload = {"items": [[0] for _ in range(120000)]}
        # Negative control: pretty-printing the payload breaches the cap.
        expanded = json.dumps(payload, indent=2)
        self.assertGreater(len(expanded.encode()), mcp_server.MAX_RESULT_BYTES)
        text = mcp_server.result_text(payload)
        request = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                   "params": {"name": "surface", "arguments": {}}}
        with patch.object(mcp_server.Reports, "surface", return_value=payload):
            response = mcp_server.dispatch(request)
        self.assertFalse(response["result"]["isError"])
        transmitted = response["result"]["content"][0]["text"]
        self.assertEqual(transmitted, text)
        self.assertLessEqual(len(transmitted.encode()), mcp_server.MAX_RESULT_BYTES)
        self.assertLessEqual(len(json.dumps(response).encode()),
                             mcp_server.MAX_RESULT_BYTES + 1024)
        with patch.object(mcp_server, "MAX_RESULT_BYTES", len(text.encode())):
            self.assertEqual(mcp_server.result_text(payload), text)
        with patch.object(mcp_server, "MAX_RESULT_BYTES", len(text.encode()) - 1):
            with self.assertRaises(mcp_server.ReportError):
                mcp_server.result_text(payload)

    def test_real_local_batch_discovery_prompt_and_stale_refusal(self):
        # Imports are deliberately inside the opt-in test, not the core suite.
        from mcp import ClientSession, StdioServerParameters
        from mcp.client.stdio import stdio_client

        # The MCP package is blocked in the server process.
        bootstrap = (
            "import builtins, runpy, sys\n"
            "blocked = 'mcp'\n"
            "original = builtins.__import__\n"
            "def guard(name, *args, **kwargs):\n"
            "    if name == blocked or name.startswith(blocked + '.'):\n"
            "        raise ModuleNotFoundError(name)\n"
            "    return original(name, *args, **kwargs)\n"
            "builtins.__import__ = guard\n"
            "sys.argv = [sys.argv[1], *sys.argv[2:]]\n"
            "runpy.run_path(sys.argv[0], run_name='__main__')\n")
        self.assertIsNotNone(importlib.util.find_spec("mcp"))

        root = Path(tranche.__file__).parent
        expected = json.loads((root / "out" / "batches.json").read_text())["batches"][0]
        # The actual local observation, unchanged.
        observed = root

        def params_for(target):
            return StdioServerParameters(
                command=sys.executable,
                args=["-c", bootstrap, str(root / "mcp_server.py"), "--root", str(target)])

        async def exercise():
            params = params_for(observed)
            async with stdio_client(params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    tools = (await session.list_tools()).tools
                    self.assertEqual({t.name for t in tools},
                                     {"surface", "query", "pick", "next_prompt", "related", "digests"})
                    schemas = {tool.name: tool.inputSchema for tool in tools}
                    for schema in schemas.values():
                        self.assertFalse(schema["additionalProperties"])
                    query_schema = schemas["query"]["properties"]
                    self.assertEqual(query_schema["limit"]["maximum"], 100)
                    self.assertEqual(query_schema["offset"]["minimum"], 0)
                    self.assertEqual(query_schema["text"]["maxLength"], 512)
                    self.assertIn("security", query_schema["queue"]["enum"])
                    self.assertEqual(schemas["pick"]["properties"]["batch_id"]["pattern"], r"^B[0-9]{3,6}$")
                    for tool in tools:
                        self.assertTrue(tool.annotations.readOnlyHint)
                        self.assertFalse(tool.annotations.openWorldHint)
                    picked = await session.call_tool("pick", {"batch_id": expected["id"]})
                    self.assertFalse(picked.isError, picked)
                    data = json.loads(picked.content[0].text)
                    self.assertEqual(data["batch"], expected)
                    import mcp_server
                    # SDK must transmit the exact bounded JSON, not pretty-print it.
                    self.assertEqual(picked.content[0].text, mcp_server.result_text(data))
                    self.assertLessEqual(len(picked.content[0].text.encode()), mcp_server.MAX_RESULT_BYTES)
                    prompt = await session.call_tool("next_prompt", {})
                    self.assertFalse(prompt.isError, prompt)
                    self.assertEqual(json.loads(prompt.content[0].text)["batch"]["review_prompt"].encode(),
                                     expected["review_prompt"].encode())
                    for arguments in ({"limit": 101}, {"limit": True}, {"limit": "1"},
                                      {"security": "true"}, {"unknown": 1}):
                        invalid = await session.call_tool("query", arguments)
                        self.assertTrue(invalid.isError, arguments)
            # A disposable copy; the real observation is never modified.
            with tempfile.TemporaryDirectory() as directory:
                copy = Path(directory)
                shutil.copytree(observed / "out", copy / "out", ignore=shutil.ignore_patterns("*.md"))
                (copy / "data" / "pages").mkdir(parents=True)
                shutil.copy(root / "data" / "pages" / "snapshot.json", copy / "data" / "pages")
                params = params_for(copy)
                async with stdio_client(params) as (read, write):
                    async with ClientSession(read, write) as session:
                        await session.initialize()
                        self.assertFalse((await session.call_tool("surface", {})).isError)
                        path = copy / "out" / "batches.json"
                        data = json.loads(path.read_text())
                        data["batches"][0]["review_prompt"] += " modified"
                        path.write_text(json.dumps(data))
                        for name, arguments in (("surface", {}), ("pick", {"batch_id": expected["id"]}),
                                                ("digests", {}), ("query", {}),
                                                ("next_prompt", {}), ("related", {"number": expected["members"][0]})):
                            result = await session.call_tool(name, arguments)
                            self.assertTrue(result.isError, name)
                            self.assertIn("stale or modified", result.content[0].text)
        asyncio.run(asyncio.wait_for(exercise(), timeout=180))


if __name__ == "__main__":
    unittest.main()
