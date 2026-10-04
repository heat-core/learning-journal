import unittest
from challenges.stage_6_production_pilot import ReliabilityMetricsCalculator

class TestStage6Reliability(unittest.TestCase):
    def test_latency_percentiles(self):
        latencies = [10.0, 12.0, 15.0, 18.0, 20.0, 25.0, 30.0, 50.0, 100.0, 200.0]
        calc = ReliabilityMetricsCalculator()
        p = calc.calculate_percentiles(latencies)
        self.assertTrue(p["p50"] <= p["p95"] <= p["p99"] <= p["max"])
        self.assertEqual(p["max"], 200.0)

    def test_availability_sli(self):
        calc = ReliabilityMetricsCalculator()
        sli = calc.calculate_availability_sli(1000, 5)  # 5 errors out of 1000
        self.assertEqual(sli, 99.5)

if __name__ == "__main__":
    unittest.main()
