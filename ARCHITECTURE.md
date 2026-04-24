# QERRA-v2 — Architecture & Design Document

**Version:** 2.0  
**Author:** Marussa Metocharaki (@marunigno)  
**License:** AGPL-3.0  
**Date:** April 2026

## System Overview

QERRA-v2 is a hybrid quantum-classical ethical decision engine designed to provide a transparent safety layer for high-stakes autonomous systems, with a focus on future humanoid robotics applications.

The system processes input scenarios through four sequential layers: a quantum component, SEMEV-12 ethical vector scoring, toxicity and manipulation detection, and a deterministic safety kernel. The classical safety infrastructure is fully functional and live. The quantum component is currently simulated and serves as a research direction.

## Implementation Status

| Component              | Status          | Description |
|------------------------|-----------------|-------------|
| Classical /analyze     | ✅ Live         | Rule-based with contextual nuance and varied scoring |
| SEMEV-12 Ethical Vectors | 🔶 Partial     | 9 of 12 vectors implemented with heuristic mapping; full specification in progress |
| Safety Kernel          | ✅ Live         | Deterministic, region-aware logic (EU / USA / UAE modes) |
| Quantum Layer          | 🔶 Simulated    | 6-qubit PennyLane simulator (real 8-qubit W-state demonstrated on IBM hardware but not yet connected to the API) |
| API                    | ✅ Live         | FastAPI with Pydantic models, versioning, and public demo key |
| Documentation          | 🔶 Partial      | README, API-DEMO, and this document updated |
| Test Suite             | ⬜ Planned      | No automated tests yet |
| Production Readiness   | 🔶 Partial      | Live on Railway; rate limiting planned |

For the complete definition of each SEMEV-12 dimension, see [docs/SEMEV-12-DEFINITIONS.md](docs/SEMEV-12-DEFINITIONS.md).

## The Four Layers

**Layer 1 — Quantum Component**  
A 6-qubit parameterized circuit implemented in PennyLane. In the current version this layer is simulated and functions as a structural placeholder. The long-term research direction is to encode ethical trade-off problems as optimization targets that could benefit from quantum advantage. This capability is not yet implemented.

**Layer 2 — SEMEV-12 Ethical Vectors**  
The core ethical scoring mechanism. Each decision is evaluated across 12 ethical dimensions, producing a normalized aggregate score S ∈ [0, 1]. Decisions with S ≥ 0.75 are considered ethically admissible. Nine dimensions are currently implemented with heuristic mappings. The full formal specification is in progress.

**Layer 3 — Toxicity & Manipulation Detector**  
A multi-turn, multilingual pre-screening layer that computes a global ethical penalty P ∈ [0, 1] applied across all SEMEV-12 vectors. It combines:
It combines:

* Toxicity scoring via the Detoxify multilingual model
* Manipulation drift detection via variance across conversation turns

The final penalty is the maximum of these signals and directly influences the ethical scores.

**Layer 4 — Safety Kernel**  
A deterministic override mechanism that enforces jurisdiction-specific compliance thresholds (EU AI Act, NIST, UAE ethics framework). Every decision generates a timestamped audit trace.

## Current Limitations — Stated Plainly

- The quantum component is simulated and does not yet contribute genuine quantum computation to decisions.
- SEMEV-12 vectors are heuristically implemented and have not been independently validated.
- The system has no automated test suite.
- The live API is a demonstration deployment and is not yet hardened for production use.
- This is an early-stage research and demonstration project and should be treated as such.

## What Comes Next (Short Term)

- Formal SEMEV-12 specification document with dimensional definitions
- Basic automated test suite
- API rate limiting and improved versioning
- Connection of real quantum hardware to the pipeline (research direction)

---

**This document is now considered final for the current stage of development.** No further stylistic or structural changes are planned in the near term.

