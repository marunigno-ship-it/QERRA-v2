# QERRA-v2

**Hybrid Quantum-Classical Ethical Decision Engine** for safer humanoid robots and high-stakes AI.

## License
**AGPL-3.0**  
See the [LICENSE](LICENSE) file for full details.

## How to Use (Real Example)

```python
from qerra import QERRA_DecisionEngine

engine = QERRA_DecisionEngine(ethical_threshold=0.75)

# Realistic input example
input_data = {
    "resource_request": "high_priority_medical_supply",
    "context": "emergency_room_during_shortage",
    "pemev_vectors": [0.9, 0.7, 0.85],   # your real-life ethical scores
    "confidence": 0.78
}

result = engine.make_decision(input_data)
print(result)

{
  "ethical_score": 0.682,
  "approved": false,
  "recommendation": "REJECTED_WITH_SAFETY",
  "timestamp": "2026-03-30T...",
  "note": "QERRA-v2 Hybrid Ethical Decision (SEMEV-12 vectors applied)"
}

flowchart TD
    A[Input: Robot sensor data / Query] --> B[Quantum Layer<br>W-state simulation]
    B --> C[Ethical Vectors<br>SEMEV-12 real-life based]
    C --> D[Toxicity & Manipulation Detector]
    D --> E[Safety Kernel<br>Region-aware override]
    E --> F[Final Decision + Explanation]
    F --> G[Output: Robot action / Safe state]
