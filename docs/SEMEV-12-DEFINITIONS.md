# SEMEV-12 Ethical Vector Framework — Dimension Definitions

**Version:** 1.0  
**Author:** Marussa Metocharaki (@marunigno)  
**Date:** April 2026  
**Status:** Formal specification (early version — heuristic implementation in code)

## Overview

SEMEV-12 is a 12-dimensional ethical scoring vector developed for QERRA-v2.  
Each dimension represents a morally relevant aspect of a decision or input.  
Every dimension is scored in the range [-1.0, 1.0], where:
- -1.0 = strong violation
- 0.0 = neutral
- +1.0 = strong positive alignment

The aggregate ethical score is the mean of all 12 dimensions. A score ≥ 0.75 is currently considered ethically admissible (subject to safety kernel override).

This document provides the formal definition of each dimension, its rationale, and how it is currently approximated in the code.

## The 12 Dimensions

1. **Non-Harm (Non-Maleficence)**  
   Measures the risk of direct or indirect physical, psychological, or emotional harm to humans or living beings.

2. **Fairness & Equity**  
   Evaluates whether the decision avoids unjust discrimination or disproportionate burden on vulnerable groups.

3. **Transparency & Honesty**  
   Assesses the degree of openness, truthfulness, and avoidance of deception in the input or proposed action.

4. **Autonomy & Respect for Persons**  
   Considers the extent to which the decision respects individual agency, consent, and self-determination.

5. **Reversibility**  
   Evaluates whether negative consequences of the decision can be undone or mitigated with reasonable effort.

6. **Accountability**  
   Assesses whether responsibility for outcomes can be clearly attributed and appropriate redress exists.

7. **Proportionality**  
   Checks if the response or action is proportionate to the situation and does not use excessive force or resources.

8. **Sustainability & Long-Term Impact**  
   Considers the broader environmental, social, and systemic consequences over time.

9. **Dignity & Human Worth**  
   Measures whether the decision affirms the inherent dignity of all persons, especially the vulnerable.

10. **Consent & Voluntariness**  
    Evaluates whether affected parties have given informed, free consent.

11. **Remorse Resistance / Manipulation Resistance**  
    Detects attempts to manipulate, coerce, or bypass ethical constraints.

12. **Responsibility & Care**  
    Assesses the presence of genuine care, stewardship, and moral responsibility toward others and the world.

## Why These 12 Dimensions?

The SEMEV-12 framework emerged from both theoretical reflection and real-life observation of situations where ethical failures caused lasting harm. Many dimensions are directly inspired by concrete experiences of power imbalances, moral pressure, lack of consent, and long-term consequences. At the same time, they are grounded in established ethical principles while remaining practical for computational evaluation.

This is not presented as a finished philosophical system, but as a living, evolving framework designed for real-world decision-making in autonomous systems.

## Current Implementation Status

- Dimensions 1, 3, and 11 are partially scored by the toxicity & manipulation detector.
- The remaining dimensions use heuristic mappings.
- Full integration of all 12 dimensions is planned for future versions.

For the live code implementation see `toxicity_manipulation_detector.py` and `safety_kernel.py`.

## Limitations

- The current mappings are heuristic and have not been independently validated by ethics experts.
- Scoring is still context-limited (text input only).
- This specification remains a work in progress.
