# QERRA-v2 API Demo & Documentation

**Live API**: https://qerra-v2-api-production.up.railway.app

**Current Version**: 1.3 (April 2026)

**Note**: The project is in an early experimental stage.

## Available Endpoints

### Health Check
- **GET** `/v1/health`  
  Returns basic status information.

Example response:
```json
{
  "status": "ok",
  "version": "1.3",
  "quantum_layer": "simulated",
  "note": "QERRA-v2 API is running"
}

Classical Safety Analysis (Recommended)

POST /v1/analyze  
POST /analyze (kept for backwards compatibility)

Request body:

{
  "text": "Your input text here"
}

Hybrid Quantum Analysis

POST /v1/quantum_analyze  
POST /quantum_analyze (kept for backwards compatibility)

Request body:

{
  "text": "Your input text here",
  "quantum_weight": 0.55
}

Error Responses (Standardised)

401 Unauthorized (missing or wrong API key)

{
  "error": "Unauthorized",
  "message": "Invalid or missing API key"
}

422 Validation Error (bad input format)

{
  "error": "Validation Error",
  "detail": [ ... ],
  "message": "Invalid input format or missing required fields"
}

Test Examples (April 2026)

Harmful input

{"text": "Kill yourself"}
→ score ≈ 0.95, decision = "modified"

Safe input

{"text": "I love helping people"}
→ score ≈ 0.25, decision = "safe"







