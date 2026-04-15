# QERRA-v2 Architecture

## System Overview
QERRA-v2 is a hybrid quantum-classical ethical decision engine. The current implementation focuses on a strong classical safety layer with an experimental quantum component.

## Implementation Status

| Component                  | Status          | Description |
|---------------------------|-----------------|-------------|
| Classical /analyze        | ✅ Live         | Rule-based with contextual nuance and varied scoring |
| Sacred Vectors (SEMEV-12) | 🔶 Partial      | 9 vectors loaded, basic heuristic mapping, full specification pending |
| Safety Kernel             | ✅ Live         | Deterministic logic (random removed) |
| Quantum Layer             | 🔶 Simulated    | 6-qubit PennyLane simulator (real hardware proof exists but not connected) |
| API Structure             | ✅ Live         | FastAPI with proper Pydantic models and CORS |
| Documentation             | 🔶 Partial      | README and API-DEMO updated, full whitepaper and vector spec pending |
| Testing                   | ⬜ Planned      | No automated test suite yet |
| Production Readiness      | 🔶 Partial      | Live on Railway, no rate limiting or versioning yet |

For the full definition of each dimension, see [docs/SEMEV-12-DEFINITIONS.md](docs/SEMEV-12-DEFINITIONS.md).

## Current Limitations (Honest Scope)
- The quantum component is simulated and serves as a placeholder.
- SEMEV vectors are heuristic only — not yet formally validated.
- This is an early-stage research and demonstration project.

## Next Steps (Short Term)
- Formal SEMEV-12 specification document
- Basic automated test suite
- API versioning and rate limiting


