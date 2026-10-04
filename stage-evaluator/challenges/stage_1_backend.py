"""
Stage 1 Challenge: Production Backend, SQL & Docker Readiness
Gate 1 Focus: Rate Limiting, N+1 Query Detection & Health Checking (Project P0)
"""
import time
from collections import defaultdict
from typing import Dict, Any, List

class RateLimiter:
    """
    Sliding window rate limiter tracking requests per client IP.
    """
    def __init__(self, max_requests: int = 5, window_seconds: float = 1.0):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(list)

    def is_allowed(self, client_id: str) -> bool:
        now = time.time()
        timestamps = self.requests[client_id]
        # Remove timestamps outside the sliding window
        valid = [t for t in timestamps if now - t < self.window_seconds]
        self.requests[client_id] = valid

        if len(valid) < self.max_requests:
            self.requests[client_id].append(now)
            return True
        return False


class SQLQueryOptimizer:
    """
    Detects N+1 patterns and provides parameterized batch queries for relational tables.
    """
    @staticmethod
    def detect_n_plus_one(query_log: List[str]) -> bool:
        # If a single query repeats with different individual IDs, flag N+1
        select_count = defaultdict(int)
        for q in query_log:
            cleaned = q.strip().upper()
            if cleaned.startswith("SELECT") and "WHERE ID =" in cleaned:
                prefix = cleaned.split("WHERE ID =")[0].strip()
                select_count[prefix] += 1
                if select_count[prefix] >= 3:
                    return True
        return False

    @staticmethod
    def build_batch_query(table: str, ids: List[int]) -> str:
        if not ids:
            raise ValueError("IDs cannot be empty")
        placeholders = ", ".join(str(int(i)) for i in sorted(set(ids)))
        return f"SELECT * FROM {table} WHERE id IN ({placeholders});"


class HealthAggregator:
    """
    Aggregates health checks from Database, Cache, and Model Inference.
    """
    def __init__(self):
        self.checks = {}

    def register_check(self, service: str, check_fn):
        self.checks[service] = check_fn

    def check_health(self) -> Dict[str, Any]:
        results = {}
        all_healthy = True
        for name, fn in self.checks.items():
            try:
                ok, msg = fn()
                results[name] = {"status": "UP" if ok else "DOWN", "detail": msg}
                if not ok:
                    all_healthy = False
            except Exception as e:
                results[name] = {"status": "DOWN", "detail": str(e)}
                all_healthy = False
        return {
            "status": "UP" if all_healthy else "DOWN",
            "services": results
        }
