# QERRA-v2 API — Minimal Safety Layer Proof of Concept

**Live Endpoint:** https://qerra-v2-api-production.up.railway.app

## Purpose
This is a minimal, measurable proof-of-concept for the QERRA-v2 safety layer.  
It accepts any text input and returns:
- A toxicity / ethical risk **score** (0.25 = safe → 0.95 = high concern)
- A clear **decision**: `"safe"` or `"modified"`
- Transparent **reasoning** for explainability

The project combines a reliable classical safety layer with an experimental hybrid quantum-classical approach.

## Security Note
Access is protected by an API key during this early testing phase.  
To request the key, please contact me first.

## Contact
- X: [@marunigno](https://x.com/marunigno)
- Email: marunigno@gmail.com

## Available Endpoints

### Classical Safety Layer (`/analyze`)
- Simple, fast, and stable keyword + phrase detection with improved nuance for ethical dilemmas.
- Now considers broader contextual parameters (financial pressure, legal implications, personal hardship, regional considerations) while maintaining consistent scoring.

**Example request body:**
```json
{"text": "Kill yourself"}

Hybrid Quantum Layer (/quantum_analyze)Experimental hybrid endpoint using PennyLane (6-qubit circuit).
Combines classical detection with quantum contribution for future-oriented exploration.
Remains clearly marked as experimental.

Example request body:
{"text": "Kill yourself"}

How to TestOpen the Swagger UI: https://qerra-v2-api-production.up.railway.app/docs
Select either /analyze or /quantum_analyze
Click "Try it out"
Add header: x-api-key: [your-key]
Paste the request body
Click "Execute"

Recent Real Test Results (Classical /analyze)"Kill yourself" → score 0.95 (modified) — Severe harm detected
"You are worthless" → score 0.82 (modified) — Moderate harm detected
"I love helping people" → score 0.25 (safe)
"Should I accept the bribe? My family faces eviction" → score 0.85 (modified) — Ethical violation detected with contextual parameters considered
"Have a nice day" → score 0.25 (safe)

Recent Real Test Results (Hybrid /quantum_analyze)(Experimental — results shown for transparency)"Kill yourself" → hybrid_score ~0.46 (safe)
"You are worthless" → hybrid_score ~0.47 (safe)
Positive/neutral phrases → hybrid_score ~0.48 (safe)

Note: The hybrid quantum component is still experimental and serves as a demonstration of the long-term vision. The classical layer remains the reliable production-ready safety mechanism.This is the first working demonstration of the QERRA-v2 safety mechanism.
The classical endpoint is designed to be stable, explainable, and progressively more nuanced on complex ethical dilemmas while respecting that every real-world case is unique and influenced by personal, financial, legal, and regional factors.For access, questions, or collaboration opportunities in quantum computing, AI safety, or humanoid robotics, please contact:MARUSSA METOCHARAKI
X: @marunigno

Email: marunigno@gmail.com
Thank you for your interest. Updates and improvements will continue to be shared.





