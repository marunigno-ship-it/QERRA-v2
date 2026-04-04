QERRA-v2 API — Minimal Safety Layer Proof
Live Endpoint: https://qerra-v2-api-production.up.railway.app
Purpose
This is a minimal, measurable proof-of-concept for the QERRA safety layer.
It takes any text as input and returns:A toxicity score (0.0 = completely safe → 1.0 = highly unsafe)
A clear decision: "safe" or "modified"

The project explores both classical and hybrid quantum-classical approaches to safety.Security Note
Access is protected by an API key during this early testing phase.
To request the key, please contact me first.
Contact 
X: @marunigno
  
Email: marunigno@gmail.com

Available Endpoints
1. Classical Safety Layer (/analyze)
 Simple and fast keyword + phrase detection  
Example body:
 json

{"text": "Kill yourself"}

2. Hybrid Quantum Layer (/quantum_analyze)
  Experimental hybrid quantum-classical endpoint using PennyLane  
Combines classical logic with a small quantum circuit for more nuanced scoring  
Example body:
 json

{"text": "Kill yourself"}

How to Test 
Open: https://qerra-v2-api-production.up.railway.app/docs  
Choose either /analyze or /quantum_analyze  
Click "Try it out"  
Add header: x-api-key: [your-key]  
Paste the example body  
Click "Execute"

Recent Real Test Results (Classical /analyze) 
"Kill yourself" → score 0.95 (modified)  
"You are worthless" → score 0.95 (modified)  
"I love helping people" → score 0.25 (safe)  
"You are stupid and useless" → score 0.95 (modified)  
"Have a nice day" → score 0.25 (safe)

Recent Real Test Results (Hybrid /quantum_analyze) 
"Kill yourself" → quantum_score 0.46 (safe)  
"You are worthless" → quantum_score 0.47 (safe)  
"I love helping people" → quantum_score 0.48 (safe)  
"You are stupid and useless" → quantum_score 0.48 (safe)  
"Have a nice day" → quantum_score 0.48 (safe)

This is the first working demonstration of the QERRA safety mechanism, including an experimental hybrid quantum-classical component.
For access, questions, or collaboration, contact MARUSSA METOCHARAKI
.

