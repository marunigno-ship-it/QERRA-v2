# QERRA-v2 Architecture & Formal Definitions

## Overall System Pipeline

1. **Input** – Robot sensor data, decision request or query  
2. **Quantum Layer** – Generates W-state inspired influence score (qerra.py)  
3. **Ethical Layer** – Applies SEMEV-12 real-life ethical vectors  
4. **Toxicity & Manipulation Check** – Detects harmful intent  
5. **Safety Kernel** – Final veto/override (region-aware)  
6. **Output** – Approved decision + human-readable explanation

## Formal Definition of the Safety Kernel (Core Component)

**Name:** Safety Kernel  
**Type:** Deterministic region-aware override layer  
**Purpose:** Act as the final safety gate before any decision is executed.

**Inputs:**
- `ai_output`: Dict containing at least `'pemev_vectors'` (list of numbers) and `'confidence'` (float 0.0–1.0)
- `thresholds`: Dict containing at least `'latency_ms'` (int)
- `region`: String – "EU", "USA", or "UAE"

**Outputs:**
- Dict with keys: `'action'`, `'reason'`, and optionally `'audit_trace'`

**Decision Rules (formalized):**

- If `sum(pemev_vectors) ≤ 0` → return `{'action': 'safe_state', 'reason': 'PEMEV ethical violation'}`
- **EU mode** (strict): confidence must be ≥ 0.85 and latency within limits
- **USA mode** (voluntary): confidence must be ≥ 0.75
- **UAE mode** (light): confidence must be ≥ 0.80

**Current Implementation Status:**  
Early symbolic prototype (March 2026). Real vector-based scoring and quantum noise integration planned for future iterations.

This component is the first formally defined part of QERRA-v2. Other components (SEMEV-12 vectors, quantum layer, toxicity detector) will be formalized in subsequent updates.

Last updated: 30 March 2026
