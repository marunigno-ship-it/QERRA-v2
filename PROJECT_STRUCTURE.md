# QERRA-v2 Project Structure

## Overview
QERRA-v2 is a hybrid quantum-classical ethical decision engine designed for safe, interpretable decision-making in humanoid robots and high-stakes AI systems.

## Core Files
- `qerra.py` → Main Decision Engine (QERRA_DecisionEngine class)
- `qreav_vector.py` → Quantum-resistant ethical access vector
- `safety_kernel.py` → Final safety override layer
- `toxicity_manipulation_detector.py` → Real-time toxicity and manipulation detection
- `requirements.txt` → All dependencies

## Folders
- `vectors/` → Real-life based ethical vectors (SEMEV-12 and others)
- `tests/` → Automated tests
- `docs/` → Documentation
- `src/` → Future modular source (placeholder)

## Quick Start
```bash
pip install -r requirements.txt
python qerra.py
