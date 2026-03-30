# QERRA-v2

**Hybrid Quantum-Classical Ethical Decision Engine** for safer humanoid robots and high-stakes AI.

## License
**AGPL-3.0**  
See the [LICENSE](LICENSE) file for full details.

## How to Use (Real Example)

```python
from qerra import QERRA_DecisionEngine

engine = QERRA_DecisionEngine(ethical_threshold=0.75)

input_data = {
    "resource_request": "high",
    "context": "healthcare",
    "pemev_vectors": [1, 2, 3],
    "confidence": 0.82
}

result = engine.make_decision(input_data)
print(result)

flowchart TD
    A[Input: Robot sensor data / Query] --> B[Quantum Layer<br>W-state simulation]
    B --> C[Ethical Vectors<br>SEMEV-12 real-life based]
    C --> D[Toxicity & Manipulation Detector]
    D --> E[Safety Kernel<br>Region-aware override]
    E --> F[Final Decision + Explanation]
    F --> G[Output: Robot action / Safe state]
