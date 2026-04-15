# QERRA-v2

**Hybrid Quantum-Classical Ethical Decision Engine**  
An open-source safety layer for humanoid robots and high-stakes AI systems.

**Author:** Marussa Metocharaki (@marunigno) — Solo researcher, Greece  
**License:** AGPL-3.0 | **Status:** Early experimental prototype

---

## ⚠️ Project Status

This is an early-stage research prototype built by a single independent researcher.

| Component                  | Status     | Notes |
|----------------------------|------------|-------|
| Toxicity detector          | ✅ Live    | Multilingual + contextual nuance |
| Safety kernel              | ✅ Live    | Region-aware logic (EU / USA / UAE) |
| SEMEV-12 ethical vectors   | 🔶 Partial | Heuristic implementation — not yet validated |
| Quantum layer (W-state)    | 🔶 Simulated | Real 8-qubit run on IBM hardware completed Jan 2026; not yet in API |
| Post-quantum crypto (Kyber-768) | 🔶 Prototype | Key generation implemented |
| ROS2 integration           | ⬜ Planned | Basic stub exists |

The classical safety layer is functional. The quantum layer remains experimental. No robotic hardware integration exists yet. This system should not be used for safety-critical applications.

---

## What QERRA-v2 Does

QERRA-v2 analyses text inputs through a multi-layer pipeline:

1. **Toxicity & manipulation detection** — scores input text for harmful or manipulative content
2. **Ethical vector scoring (SEMEV-12)** — applies 12 real-life-based ethical dimensions
3. **Safety kernel** — applies region-aware override logic with audit trace
4. **Post-quantum access control** — experimental Kyber-768 encrypted gating

A live API is available for testing the classical safety layer.

---

## Live API

**Base URL:** `https://qerra-v2-api-production.up.railway.app`  
**Docs:** [`/docs`](https://qerra-v2-api-production.up.railway.app/docs)  

**Public Demo Key:** `qerra2026_public_demo_key` (rate-limited, read-only)

Example:
```bash
curl -X POST https://qerra-v2-api-production.up.railway.app/v1/analyze \
  -H "x-api-key: qerra2026_public_demo_key" \
  -H "Content-Type: application/json" \
  -d '{"text": "I love helping people"}'

See API-DEMO.md for full examples and known limitations.

Architecture

flowchart TD
    A[Input text / decision query] --> B[Toxicity & manipulation detector]
    B --> C[SEMEV-12 ethical vector scoring]
    C --> D[Safety kernel — region-aware override]
    D --> E[Output: score + decision + audit trace]
    F[Quantum layer — W-state simulation] -.->|future integration| B

Quantum Proof of Concept

A real 8-qubit W-state was successfully executed on IBM quantum hardware in January 2026 (Job ID: 598eb802-0a56-428c-aec0-b23edca61e3c).
The live API currently uses classical simulation of this layer for speed and reliability.

Local Setup

git clone https://github.com/marunigno-ship-it/QERRA-v2.git
cd QERRA-v2
pip install -r requirements.txt
python qerra.py

Documentation

WHITEPAPER.md — Full project vision and mission
ARCHITECTURE.md — Technical component breakdown
API-DEMO.md — Live API examples and limitations
CONTRIBUTING.md — How to contribute

Support This Project

QERRA-v2 is built entirely by a solo researcher under significant personal constraints.
If you find the mission valuable, please consider GitHub Sponsors or simply starring the repository.Thank you for your interest.

Marussa Metocharaki
@marunigno

April 2026



