"""
Stage 4 Challenge: Agentic AI & Model Context Protocol (MCP)
Gate 4 Focus: ReAct Parsing, Tool Registry & Human-In-The-Loop (Project P3)
"""
from typing import Dict, Callable, Any

class MCPToolRegistry:
    """
    Simulates a Model Context Protocol tool dispatcher with schema and execution validation.
    """
    def __init__(self):
        self._tools: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, description: str, handler: Callable, requires_human_approval: bool = False):
        self._tools[name] = {
            "name": name,
            "description": description,
            "handler": handler,
            "requires_human_approval": requires_human_approval,
        }

    def execute(self, tool_name: str, args: Dict[str, Any], approved_by_human: bool = False) -> Dict[str, Any]:
        if tool_name not in self._tools:
            return {"error": f"Tool '{tool_name}' not found", "success": False}
        tool = self._tools[tool_name]
        if tool["requires_human_approval"] and not approved_by_human:
            return {"error": "Action blocked: Human approval required", "success": False, "blocked": True}

        try:
            res = tool["handler"](**args)
            return {"result": res, "success": True}
        except Exception as e:
            return {"error": str(e), "success": False}
