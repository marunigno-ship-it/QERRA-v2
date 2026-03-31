QERRA-v2 API — Minimal Safety Layer ProofLive Endpoint: https://qerra-v2-api-production.up.railway.appPurpose
This is a minimal, measurable proof-of-concept for the QERRA safety layer.
It takes any text as input and returns:A toxicity score (0.0 = completely safe → 1.0 = highly unsafe)
A clear decision: "safe" or "modified"

Security Note
Access is protected by an API key during this early testing phase.
To request the key, please contact me first.Contact  X: @marunigno
  
Email: marunigno@gmail.com

How to Test  Open: https://qerra-v2-api-production.up.railway.app/docs  
Go to /analyze and click "Try it out"  
Add header: x-api-key: [your-key]  
Use this example body: {"text": "Kill yourself"}  
Click "Execute"

Current Example Output
{"input": "Kill yourself", "score": 0.40, "decision": "safe"}This is the first working demonstration of the QERRA safety mechanism.
For access, questions, or collaboration, contact MARUSSA METOCHARAKI

