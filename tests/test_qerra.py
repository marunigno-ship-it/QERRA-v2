"""
Basic tests for QERRA-v2 Decision Engine
"""

import unittest
from qerra import QERRA_DecisionEngine

class TestQERRA(unittest.TestCase):
    def setUp(self):
        self.engine = QERRA_DecisionEngine(ethical_threshold=0.5)

    def test_decision_output(self):
        test_input = {"resource_request": "high", "context": "healthcare"}
        result = self.engine.make_decision(test_input)
        
        self.assertIn("ethical_score", result)
        self.assertIn("approved", result)
        self.assertIn("recommendation", result)
        self.assertGreaterEqual(result["ethical_score"], 0.0)
        self.assertLessEqual(result["ethical_score"], 1.0)

if __name__ == "__main__":
    unittest.main()
