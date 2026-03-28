"""
QERRA-v2 Main Entry Point
This file allows running the engine directly from the root
"""

from src.qerra.core import QERRA_DecisionEngine

if __name__ == "__main__":
    engine = QERRA_DecisionEngine()
    test_input = {"resource_request": "high", "context": "healthcare"}
    result = engine.make_decision(test_input)
    print("✅ QERRA Decision:", result)
