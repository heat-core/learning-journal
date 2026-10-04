import unittest
from challenges.stage_1_backend import RateLimiter, SQLQueryOptimizer, HealthAggregator

class TestStage1Backend(unittest.TestCase):
    def test_rate_limiter_allows_and_blocks(self):
        limiter = RateLimiter(max_requests=3, window_seconds=1.0)
        client = "192.168.1.10"
        self.assertTrue(limiter.is_allowed(client))
        self.assertTrue(limiter.is_allowed(client))
        self.assertTrue(limiter.is_allowed(client))
        self.assertFalse(limiter.is_allowed(client))

    def test_sql_n_plus_one_detector(self):
        bad_queries = [
            "SELECT * FROM users;",
            "SELECT * FROM profiles WHERE id = 1;",
            "SELECT * FROM profiles WHERE id = 2;",
            "SELECT * FROM profiles WHERE id = 3;",
        ]
        self.assertTrue(SQLQueryOptimizer.detect_n_plus_one(bad_queries))

        good_batch = SQLQueryOptimizer.build_batch_query("profiles", [1, 2, 3])
        self.assertEqual(good_batch, "SELECT * FROM profiles WHERE id IN (1, 2, 3);")

    def test_health_aggregator(self):
        agg = HealthAggregator()
        agg.register_check("db", lambda: (True, "connected"))
        agg.register_check("cache", lambda: (True, "pong"))
        report = agg.check_health()
        self.assertEqual(report["status"], "UP")

        agg.register_check("storage", lambda: (False, "disk full"))
        failing_report = agg.check_health()
        self.assertEqual(failing_report["status"], "DOWN")

if __name__ == "__main__":
    unittest.main()
