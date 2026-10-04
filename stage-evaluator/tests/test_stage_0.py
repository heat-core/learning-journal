import unittest
from challenges.stage_0_python import retry_with_backoff, TypedBatchPipeline, ImmutableDataModel

class TestStage0Python(unittest.TestCase):
    def test_retry_decorator_succeeds_on_transient_failure(self):
        calls = 0
        @retry_with_backoff(max_retries=3, base_delay=0.01)
        def flaky_api():
            nonlocal calls
            calls += 1
            if calls < 3:
                raise ConnectionError("Temporary timeout")
            return "SUCCESS"

        self.assertEqual(flaky_api(), "SUCCESS")
        self.assertEqual(calls, 3)

    def test_retry_decorator_raises_after_max_retries(self):
        @retry_with_backoff(max_retries=2, base_delay=0.01, exceptions=(ValueError,))
        def always_fails():
            raise ValueError("Invalid schema")

        with self.assertRaises(ValueError):
            always_fails()

    def test_batch_pipeline_chunks_correctly(self):
        def stream():
            for i in range(7):
                yield i

        with TypedBatchPipeline(max_batch_size=3) as pipeline:
            batches = list(pipeline.batch(stream()))

        self.assertEqual(batches, [[0, 1, 2], [3, 4, 5], [6]])

    def test_immutable_model_validation_and_frozen(self):
        model = ImmutableDataModel(id=101, name="Farbod", score=98.5)
        self.assertEqual(model.id, 101)
        self.assertEqual(model.name, "Farbod")
        self.assertEqual(model.score, 98.5)
        self.assertEqual(model.to_dict(), {"id": 101, "name": "Farbod", "score": 98.5})

        with self.assertRaises(AttributeError):
            model.score = 100.0

        with self.assertRaises(ValueError):
            ImmutableDataModel(id=-1, name="Test", score=50.0)

if __name__ == "__main__":
    unittest.main()
