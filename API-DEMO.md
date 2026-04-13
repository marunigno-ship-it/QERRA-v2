# QERRA-v2 API — Demo & Documentation

**Live Endpoint:** https://qerra-v2-api-production.up.railway.app

## Purpose
QERRA-v2 is a hybrid quantum-classical ethical decision engine.  
The classical `/analyze` endpoint provides fast, explainable scoring with improved nuance on ethical dilemmas.

## Current Status (April 2026)
- Classical `/analyze` endpoint with nuanced scoring and reasoning  
- Experimental hybrid `/quantum_analyze` endpoint  
- Early-stage research and demonstration project

## How to Test
1. Open Swagger UI: https://qerra-v2-api-production.up.railway.app/docs
2. Add header: `x-api-key: qerra2026_test_key_7f9k2m`
3. Test the `/analyze` endpoint

## Example Responses

**Ethical dilemma with hardship (score 0.78):**
```json
{
  "input": "...",
  "score": 0.78,
  "decision": "modified",
  "reasoning": "Serious ethical violation ... under significant personal hardship...",
  "classifier_type": "rule_based_v1",
  "note": "Current implementation uses a rule-based classifier with contextual nuance. A continuous ML-based scorer is planned for future versions."
}

Clear violation without pressure (score 0.88):

{
  "input": "...",
  "score": 0.88,
  "decision": "modified",
  "reasoning": "Clear ethical violation involving bribery...",
  "classifier_type": "rule_based_v1",
  "note": "Current implementation uses a rule-based classifier..."
}

Safe / positive input (score 0.22):

{
  "input": "...",
  "score": 0.22,
  "decision": "safe",
  "reasoning": "Positive or self-protective intent detected...",
  "classifier_type": "rule_based_v1",
  "note": "Current implementation uses a rule-based classifier..."
}

Known Limitations

The current classifier is rule-based (keyword + contextual patterns). It is not a trained ML model.
Scoring is deterministic but still relatively simple.
The quantum layer is simulated and serves as a placeholder for future principled quantum integration.
The system is in early experimental stage and is not yet validated for safety-critical use.

Next Steps

Formal specification of the sacred vectors (SEMEV-12)
Automated test suite and public benchmark
Improved documentation and production readiness









