# QERRA-v2 Project Structure

To preserve the ethical mission while enabling future sustainability and institutional adoption, the project is divided into two clear layers:
Core Layer (Fully Open-Source – AGPL-3.0)




- Ethical vectors (SEMEV-12, PEMEV-11, SEEV-12, etc.)
- Research algorithms & simulations (quantum entanglement, randomness seeding, toxicity detection)
- Basic classical/hybrid demos and documentation
- Governance logic and philosophical foundation

This layer remains free forever for anyone to use, modify, or fork.

## Edge Layer (Potential Future Licensable / Commercial)
- Deployment adapters (e.g., hardened ROS2 integrations, real-time control bridges)
- High-reliability modules (error mitigation, fail-safe recovery)
- Security, compliance, and audit tooling
- Certified enterprise distributions (QERRA Certified builds)
- Institutional support & SLAs

This layer enables monetisation through reliability, validation, and integration — while the core ethical philosophy stays open.

Deterministic Safety Architecture
- Sensor Input → AI Inference (probabilistic LLM/quantum layer) → Safety Kernel (deterministic overrides) → Actuation.
- Kernel Features: 
  - Independent hard constraints (e.g., force/torque thresholds, emergency stops).
  - Fail-safe under latency/noise (default to safe state).
  - Override unsafe AI outputs (e.g., PEMEV ethical checks).
- Implementation Plan: Code separation in Python (core open, edge protected).

### Simple Diagram (Text-based)


### Monetisation Note
The ethical core and research layer stay fully open and free.  
Monetisation happens only at the edge layer: enterprise support contracts, certified deployment packages, dual licensing for regulated/high-stakes environments, and optional paid integrations.  
This preserves accessibility and mission integrity while allowing sustainability as the project scales.

For more on contribution, see HOW_TO_CONTRIBUTE.md.
For trademark, see README.md.
