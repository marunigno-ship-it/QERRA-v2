"""
Simple test to check if the new src/qerra package structure works
Run this from the root of the repository
"""

try:
    from src.qerra.core import QERRA_DecisionEngine
    print("✅ Successfully imported QERRA_DecisionEngine from src.qerra.core")
    
    engine = QERRA_DecisionEngine(ethical_threshold=0.5)
    test_input = {"resource_request": "high", "context": "healthcare"}
    result = engine.make_decision(test_input)
    print("✅ QERRA Decision test successful:")
    print(result)
    
except Exception as e:
    print("❌ Import or execution failed:")
    print(e)
