import unittest
from challenges.stage_2_machine_learning import SafeStandardScaler, ClassificationMetrics

class TestStage2ML(unittest.TestCase):
    def test_safe_scaler_fit_transform(self):
        train = [10.0, 20.0, 30.0]
        scaler = SafeStandardScaler().fit(train)
        self.assertAlmostEqual(scaler.mean_, 20.0)
        scaled_train = scaler.transform(train)
        self.assertAlmostEqual(scaled_train[1], 0.0)

        test = [20.0, 40.0]
        scaled_test = scaler.transform(test)
        self.assertAlmostEqual(scaled_test[0], 0.0)

    def test_classification_metrics(self):
        y_true = [1, 1, 0, 1, 0, 0, 1, 0]
        y_pred = [1, 0, 0, 1, 0, 1, 1, 0]
        metrics = ClassificationMetrics.compute(y_true, y_pred)
        self.assertEqual(metrics["tp"], 3)
        self.assertEqual(metrics["fp"], 1)
        self.assertEqual(metrics["fn"], 1)
        self.assertEqual(metrics["tn"], 3)
        self.assertEqual(metrics["precision"], 0.75)
        self.assertEqual(metrics["recall"], 0.75)
        self.assertEqual(metrics["f1"], 0.75)

if __name__ == "__main__":
    unittest.main()
