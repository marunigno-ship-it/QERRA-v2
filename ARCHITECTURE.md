# QERRA-v2 Architecture & Formal Definitions

## License
**AGPL-3.0** — see [LICENSE](LICENSE) file.

## 1. Formal Definition of the Safety Kernel

**Name:** Safety Kernel  
**Type:** Deterministic region-aware override layer  
**Purpose:** Final safety gate that evaluates and can veto or modify any proposed decision before execution.

**Inputs:**
- `ai_output`: dict  
  - `pemev_vectors`: list[float] (ethical vector scores from SEMEV-12)  
  - `confidence`: float ∈ [0.0, 1.0]  
- `thresholds`: dict (contains at least `latency_ms`: int)  
- `region`: str ∈ {"EU", "USA", "UAE"}

**Outputs:**
- dict with keys:  
  - `action`: str ∈ {"APPROVED", "REJECTED_WITH_SAFETY", "safe_state", "override", "halt"}  
  - `reason`: str (human-readable explanation)  
  - `audit_trace`: str (optional, for debugging)

**Mathematical Decision Rules:**

- If ∑(pemev_vectors) ≤ 0 → return `{'action': 'safe_state', 'reason': 'PEMEV ethical violation'}`
- **EU mode** (strict): if confidence < 0.85 or latency > threshold → halt
- **USA mode** (voluntary): if confidence < 0.75 → override
- **UAE mode** (light): if confidence < 0.80 → halt

**Current Status:** Early symbolic prototype (March 2026). Real quantum noise integration and full vector-based scoring planned for future iterations.

## 2. Overall System Pipeline

1. Input (sensor data / decision query)  
2. Quantum Layer (W-state simulation)  
3. Ethical Layer (SEMEV-12 real-life vectors)  
4. Toxicity & Manipulation Detector  
5. Safety Kernel (final override)  
6. Output (approved decision + explanation)

Last updated: 30 March 2026
