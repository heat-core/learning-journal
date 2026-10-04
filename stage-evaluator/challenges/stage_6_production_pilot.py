"""
Stage 6 Challenge: Real-World Pilot, Observability & Reliability
Gate 5 Focus: Latency Percentiles (P50, P95, P99) & Error Budget Burn (Project P5)
"""
from typing import List, Dict

class ReliabilityMetricsCalculator:
    """
    Computes latency percentiles and Service Level Indicator (SLI) compliance.
    """
    @staticmethod
    def calculate_percentiles(latencies_ms: List[float]) -> Dict[str, float]:
        if not latencies_ms:
            raise ValueError("Latencies list cannot be empty")
        sorted_vals = sorted(latencies_ms)
        n = len(sorted_vals)

        def get_p(p: float):
            idx = int(math_ceil(p * n)) - 1
            idx = max(0, min(idx, n - 1))
            return sorted_vals[idx]

        def math_ceil(val):
            import math
            return math.ceil(val)

        return {
            "p50": round(get_p(0.50), 2),
            "p95": round(get_p(0.95), 2),
            "p99": round(get_p(0.99), 2),
            "max": round(sorted_vals[-1], 2),
        }

    @staticmethod
    def calculate_availability_sli(total_requests: int, failed_requests: int) -> float:
        if total_requests <= 0:
            return 100.0
        success = total_requests - failed_requests
        return round((success / total_requests) * 100.0, 3)
