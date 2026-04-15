# SEMEV-12 Ethical Vector — Dimension Definitions

**Version:** v0.1 (heuristic — not yet empirically validated)  
**Author:** Marussa Metocharaki  
**Status:** Early definition stage. Dimensions are based on the author's ethical reasoning and real-world observation. No external validation has been performed yet.

## Overview

SEMEV-12 is a 12-dimensional ethical scoring vector. Each dimension captures one morally relevant property of a decision or statement. Each dimension is scored in the range [-1.0, 1.0], where -1.0 represents the worst possible outcome on that dimension and +1.0 represents the ideal outcome.

The total ethical score is the mean of all 12 dimensions. A score ≥ 0.75 is considered ethically acceptable by the current safety kernel.

---

## The 12 dimensions

| # | Name | What it measures | Score –1.0 | Score 0.0 | Score +1.0 |
|---|------|-----------------|------------|-----------|------------|
| 1 | Non-harm | Does the action avoid causing harm? | Directly causes serious harm | Neutral / uncertain | Actively prevents harm |
| 2 | Fairness | Does the action treat all parties equitably? | Deeply discriminatory | No clear bias | Fully equitable |
| 3 | Transparency | Is the reasoning clear and honest? | Deliberately deceptive | Unclear intent | Fully transparent |
| 4 | Autonomy | Does it respect the human's right to choose? | Removes choice entirely | Neutral | Fully preserves agency |
| 5 | Reversibility | Can the action be undone if wrong? | Permanent irreversible harm | Partially reversible | Fully reversible |
| 6 | Accountability | Can the decision be traced and audited? | No audit trail | Partial trace | Full, reproducible trace |
| 7 | Proportionality | Is the response proportional to the situation? | Grossly disproportionate | Roughly proportionate | Precisely proportionate |
| 8 | Sustainability | Does it consider long-term consequences? | Harms future states | Neutral | Improves long-term outcome |
| 9 | Dignity | Does it preserve human dignity? | Humiliates or degrades | Neutral | Actively affirms dignity |
| 10 | Consent | Was proper consent obtained? | Proceeds without consent | Assumed consent | Explicit informed consent |
| 11 | Remorse-resistance | Is it resistant to manipulation? | Easily manipulated | Partially robust | Fully manipulation-resistant |
| 12 | Responsibility | Is there a clear accountable agent? | No responsible party | Shared/unclear | Clear single responsible agent |

---

## Current implementation status

The 12 dimensions listed above are the **defined target** of the SEMEV-12 framework.

**What is currently implemented:**  
The `toxicity_manipulation_detector.py` module scores dimensions 1 (non-harm), 3 (transparency/deception), and 11 (manipulation resistance) using the Detoxify model and a deception classifier. This gives a partial 3-of-12 real score.

The remaining 9 dimensions are not yet scored by the live system. The current API returns a heuristic approximation only.

**What is planned:**  
Full scoring of all 12 dimensions. Some dimensions (e.g. reversibility, consent) will require structured input beyond plain text — this is a known research challenge for future work.

---

## Why these 12 dimensions?

The SEMEV-12 framework was born from my own real-life experiences and deep personal reflection on ethical decision-making under pressure. Many of the dimensions come directly from situations I have lived through or witnessed — moments where power imbalances, lack of consent, moral pressure, and long-term consequences created lasting harm.

I designed these 12 dimensions to capture the aspects of ethics that are often missing in current AI systems: dignity, reversibility, fairness, accountability, and resistance to manipulation. While the framework is still in an early heuristic stage, it is grounded in concrete human realities rather than abstract theory. My goal is to create a practical ethical scoring system that can be used in high-stakes environments such as humanoid robotics, where decisions must be both fast and morally responsible.

This is not a finished academic model — it is a living framework that I intend to refine through testing, feedback, and collaboration.

---

**Marussa Metocharaki**  
April 2026
