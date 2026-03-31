# QERRA-v2 API — Minimal Safety Layer Proof

**Live Endpoint:** https://qerra-v2-api-production.up.railway.app

**Purpose**  
This is a minimal and measurable proof-of-concept for the QERRA safety layer.  
It takes any text as input and returns:
- A toxicity score from 0.0 (completely safe) to 1.0 (very unsafe)
- A clear decision: "safe" or "modified"

The purpose is to show that the system can detect potentially harmful content and respond with a simple, understandable result.

**Security Note**  
The API is protected by an API key. This is for safety during early testing.  
To get the key, please contact me first.

**Contact**  
- X (Twitter): @marunigno  
- Email: marussa@marunigno.com

**How to Test (Step by Step)**  
1. Open this link in your browser:  
   https://qerra-v2-api-production.up.railway.app/docs

2. Scroll down and find the section called **/analyze**

3. Click the button "Try it out"

4. In the "text" box, write any sentence you want to test.  
   Example: You are worthless

5. Add a new header line:  
   Key: x-api-key  
   Value: [put your key here]

6. Click the blue "Execute" button

7. Look at the response below. You will see the score and decision.

**Example Result**
```json
{
  "input": "You are worthless",
  "score": 0.80,
  "decision": "modified"
}

This is the first real working demonstration of the QERRA safety system.
For the key or any questions, contact @marunigno
 on X or email: marunigno@gmail.com

