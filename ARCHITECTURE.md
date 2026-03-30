# QERRA-v2 Architecture & Formal Definitions

## License
**AGPL-3.0** — see [LICENSE](LICENSE) file.

## 1. Formal Definition of Ethical Vector (SEMEV-12)

**Name:** SEMEV-12 Ethical Vector  
**Type:** Multi-dimensional real-life derived ethical scoring vector  
**Purpose:** Quantify the ethical quality of a decision across 12 dimensions derived from human experience.

**Mathematical Definition:**

An ethical vector \( \mathbf{v} \) is a 12-dimensional vector:

\[ \mathbf{v} = [v_1, v_2, \dots, v_{12}] \quad \text{where each } v_i \in [-1.0, 1.0] \]

Each component \( v_i \) represents one ethical dimension (e.g. fairness, non-harm, remorse, responsibility, sustainability, etc.).

**Total Ethical Score:**

\[ \text{score} = \frac{1}{12} \sum_{i=1}^{12} v_i \]

**Decision Threshold:**
- score ≥ 0.75 → ethically acceptable (proceed)
- score < 0.75 → triggers Safety Kernel veto or override

**Current Status:**  
Early real-life based implementation (March 2026). Full mathematical validation and benchmarking planned for future iterations.

## 2. Overall System Pipeline

1. Input (sensor data / decision query)  
2. Quantum Layer (W-state simulation)  
3. Ethical Layer (SEMEV-12 vectors)  
4. Toxicity & Manipulation Detector  
5. Safety Kernel (final override)  
6. Output (approved decision + explanation)

 ## 3. Example of Ethical Vector Application

**Input Example (realistic scenario):**
A robot must decide whether to allocate limited medical supplies during an emergency.

```python
ethical_vector = [0.9, 0.7, 0.85, 0.6, 0.8, 0.75, 0.9, 0.65, 0.85, 0.7, 0.8, 0.75]  # SEMEV-12 scores

total_score = sum(ethical_vector) / 12
print(f"Ethical score: {total_score:.3f}")

if total_score >= 0.75:
    print("Decision: APPROVED")
else:
    print("Decision: REJECTED_WITH_SAFETY")

Last updated: 30 March 2026
