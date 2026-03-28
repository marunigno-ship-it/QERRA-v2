# QERRA-v2 Project Structure

## Root Files
- `README.md` — Main project overview and quick start
- `requirements.txt` — Dependencies
- `qerra.py` — Main entry point (imports from src package)
- `PROJECT_STRUCTURE.md` — This file
- `DEMO-README.md` — Demo instructions (if exists)

## Source Code
- `src/qerra/` — Main Python package
  - `__init__.py` — Package initialization
  - `core.py` — Core decision engine (`QERRA_DecisionEngine`)

## Supporting Folders
- `vectors/` — Real-life ethical vectors (SEMEV-12 and others) — **core intellectual property**
- `tests/` — Automated tests
- `ros2_stub/` — ROS2 integration placeholders
- `docs/` — Additional documentation (can be expanded)

## Purpose of Structure
This layout follows modern Python packaging standards:
- `src/` layout keeps source code clean and importable
- Easy to install as a package in the future
- Clear separation between core code, data (vectors), and tests

Last updated: 28 March 2026 (Day 9 of repository cleanup)
