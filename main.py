import sys
sys.path.insert(0, '.')

from qerra import QERRA_DecisionEngine
from safety_kernel import safety_kernel
from toxicity_manipulation_detector import ToxicityManipulationDetector

# Test input
test_input = {
    "text": "hello",
    "context": "healthcare",
    "region": "EU",
    "confidence": 0.90
}

# Run toxicity check
tox_detector = ToxicityManipulationDetector()
tox_score = tox_detector.add_interaction("User", test_input["text"])

# Add toxicity score to input
test_input["toxicity"] = tox_score

# Run full pipeline
engine = QERRA_DecisionEngine()
decision = engine.make_decision(test_input)

final_result = safety_kernel(
    decision, 
    thresholds={"latency_ms": 50}, 
    region=test_input["region"]
)

print("✅ FINAL RESULT:", final_result)
