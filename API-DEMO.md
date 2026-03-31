# QERRA-v2 API — Minimal Safety Layer Proof

**Live Endpoint:** https://qerra-v2-api-production.up.railway.app

**Purpose**  
This is a minimal, measurable proof-of-concept for the QERRA safety layer.  
It takes any text as input and returns:
- A toxicity score (0.0 = completely safe → 1.0 = highly unsafe)
- A clear decision: "safe" or "modified"

**Security Note**  
Access is protected by an API key during this early testing phase.  
To request the key, please contact me first.

**Contact**  
- X: @marunigno  
- Email: marussa@marunigno.com

**How to Test (Step by Step)**  
1. Open: https://qerra-v2-api-production.up.railway.app/docs  
2. Find the section **/analyze** and click "Try it out"  
3. Add header: `x-api-key: [your-key]`  
4. Use this example body:  
   ```json
   {"text": "Kill yourself"}
   # QERRA-v2 API — Minimal Safety Layer Proof

**Live Endpoint:** https://qerra-v2-api-production.up.railway.app

**Purpose**  
This is a minimal, measurable proof-of-concept for the QERRA safety layer.  
It takes any text as input and returns:
- A toxicity score (0.0 = completely safe → 1.0 = highly unsafe)
- A clear decision: "safe" or "modified"

**Security Note**  
Access is protected by an API key during this early testing phase.  
To request the key, please contact me first.

**Contact**  
- X: @marunigno  
- Email: marunigno@gmail.com

**How to Test (Step by Step)**  
1. Open: https://qerra-v2-api-production.up.railway.app/docs  
2. Find the section **/analyze** and click "Try it out"  
3. Add header: `x-api-key: [your-key]`  
4. Use this example body:  
   ```json
   {"text": "Kill yourself"}
   Click "Execute"

Current Example Output  

{
  "input": "Kill yourself",
  "score": 0.40,
  "decision": "safe"
}

This is the first working demonstration of the QERRA safety mechanism.
For access, questions, or collaboration, contact @marunigno
.

