import unittest
from challenges.stage_4_agentic_mcp import MCPToolRegistry

class TestStage4Agentic(unittest.TestCase):
    def test_tool_execution_and_hitl(self):
        registry = MCPToolRegistry()
        registry.register("calc", "Math calculator", lambda x, y: x + y)
        registry.register("delete_file", "Delete file", lambda path: f"Deleted {path}", requires_human_approval=True)

        # Normal tool works
        res = registry.execute("calc", {"x": 10, "y": 20})
        self.assertTrue(res["success"])
        self.assertEqual(res["result"], 30)

        # Dangerous tool blocked without approval
        blocked = registry.execute("delete_file", {"path": "/etc/config"})
        self.assertFalse(blocked["success"])
        self.assertTrue(blocked.get("blocked"))

        # Dangerous tool succeeds with approval
        approved = registry.execute("delete_file", {"path": "/etc/config"}, approved_by_human=True)
        self.assertTrue(approved["success"])
        self.assertEqual(approved["result"], "Deleted /etc/config")

if __name__ == "__main__":
    unittest.main()
