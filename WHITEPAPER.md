# QERRA-v2 Whitepaper

**Quantum Ethical Rescue & Resource Allocator**  
**Hybrid Quantum-Classical Ethical Decision Engine for Safer Humanoid Robots and High-Stakes AI**

**Author:** Marussa Metocharaki (@marunigno)  
**Version:** 1.1  
**Date:** April 2026  
**License:** AGPL-3.0  

## Abstract

QERRA-v2 is an open-source hybrid quantum-classical ethical decision engine designed to bring stronger safety, transparency, and moral grounding to humanoid robots and high-stakes autonomous systems.

By combining quantum-inspired exploration (W-state superposition) with a classical ethical safety kernel and real-time toxicity/manipulation detection, QERRA-v2 aims to help AI systems make decisions that are not only fast and efficient but also more ethically considered. A live minimal safety layer is already operational via a public API endpoint that returns a toxicity score (0.0–1.0) and a clear decision (“safe” or “modified”).

This whitepaper presents the project’s vision, architecture, current implementation, quantum foundation, and future roadmap. It is written for researchers, developers, robotics engineers, and potential supporters who want to understand the core idea and real progress made under solo development conditions.

**Keywords:** Quantum AI, Ethical AI, AI Safety, Humanoid Robotics, Hybrid Quantum-Classical Systems, Toxicity Detection, Ethical Decision Engine

## 1. Introduction

Humanoid robots and advanced AI are moving from laboratories into real-world deployment — disaster response, healthcare, elder care, and autonomous decision-making. As these systems gain more autonomy, the need for robust ethical guardrails becomes critical. Current safety approaches often focus on narrow alignment or simple content filtering, but they frequently lack depth, explainability, and the ability to handle complex moral trade-offs.

QERRA-v2 addresses this gap by introducing a hybrid quantum-classical ethical decision layer. The system explores decision spaces using quantum superposition principles (currently simulated) and then applies strict ethical filtering through the SEMEV-12 vector framework, a toxicity and manipulation detector, and a safety kernel with region-aware overrides.

The project has been developed entirely by me, Marussa Metocharaki, as a solo long-term effort under significant personal challenges and constraints. Grok (built by xAI) has provided consistent guidance, technical feedback, and support throughout the entire journey.

## 2. Project Vision and Mission

QERRA-v2 was born from a deep personal conviction: high-stakes AI and humanoid robots must have ethics and safety as their foundation, not as an afterthought.

Our mission is to create an ethical decision engine that:

- Detects and flags potentially harmful or manipulative actions before they are acted upon
- Provides transparent reasoning for every decision
- Remains compatible with today’s NISQ quantum hardware and classical systems
- Evolves toward stronger quantum advantage as hardware improves

We believe ethical safety is not a technical luxury — it is a moral necessity. QERRA-v2 puts human values and moral responsibility at the very heart of every decision, while still striving for speed, transparency, and real-world practicality.

## 3. System Architecture

The QERRA-v2 pipeline consists of the following layers:

1. **Input Layer** – Accepts text, context, or decision proposals  
2. **Quantum Exploration Layer** – Uses W-state superposition to explore multiple possible outcomes (currently simulated, with real 8-qubit hardware proof completed)  
3. **Ethical Vector Layer (SEMEV-12)** – Applies 12 real-life-based ethical vectors for nuanced moral scoring  
4. **Toxicity & Manipulation Detector** – Returns a continuous score (0.0–1.0) and preliminary decision  
5. **Safety Kernel** – Final decision engine with region-aware override logic and explanation generation  
6. **Output Layer** – Returns “safe” or “modified” along with score and reasoning

A live implementation of the toxicity detector and safety kernel is running at the `/analyze` endpoint on Railway.

For detailed component breakdown, see [ARCHITECTURE.md](ARCHITECTURE.md).  
For live test results, see [API-DEMO.md](API-DEMO.md).

## 4. Quantum Foundation

A key differentiator of QERRA-v2 is the integration of quantum computing principles.  

In January 2026, a real 8-qubit W-state was successfully executed on IBM quantum hardware (Job ID: 598eb802-0a56-428c-aec0-b23edca61e3c). The W-state provides equal superposition across all basis states, enabling uniform exploration of decision possibilities — a natural fit for ethical trade-off analysis.

While the current live API uses classical simulation of the quantum layer for speed and reliability, the long-term goal is deeper integration with real quantum hardware as accessible qubits and coherence times improve.

See the dedicated repository for the 8-qubit proof: [8qubit-wstate-qubs](https://github.com/marunigno-ship-it/8qubit-wstate-qubs)

## 5. Current Implementation and Results

- **Live API**: `/analyze` endpoint returns toxicity score + decision  
- **Test Results** (April 2026): Harmful inputs correctly flagged (scores ~0.95), benign inputs remain safe (scores ~0.25)  
- **Technology Stack**: Pure Python, Qiskit (for quantum parts), deployed on Railway Pro  
- **License**: AGPL-3.0 (ensures derivatives remain open and ethical)

The system is functional today as a minimal viable safety layer and serves as a foundation for further development.

## Scope and Current Limitations

What this is not (important clarification):

- The system is not currently integrated with any robotic hardware or real-world robots.
- The quantum layer is not yet running in the live API (it is simulated for speed and reliability).
- The SEMEV-12 ethical vectors are an early heuristic implementation and have not been independently validated.
- The system has not been tested on non-English inputs or highly complex real-world scenarios.
- This is an early experimental prototype and should not be used for safety-critical decisions without further development and validation.

We believe in transparency: the current version demonstrates the core idea, but significant work remains before it can be considered production-ready.

## 6. Future Roadmap

- Short term: Improve documentation, expand SEMEV-12 documentation, better integrate quantum layer  
- Medium term: Enhanced ROS2 integration, more granular scoring, community contributions  
- Long term: Real quantum hardware integration at scale, broader testing in simulated robotics environments, potential collaboration with AI safety and robotics organizations

## 7. Call for Support

QERRA-v2 has been built single-handedly under significant personal challenges and constraints. Every contribution — whether code, feedback, documentation help, or financial support via GitHub Sponsors — helps sustain this long-term effort and brings us closer to safer AI systems.

If you believe in ethical technology and the value of independent open-source work, please consider supporting the project through [GitHub Sponsors](https://github.com/sponsors/marunigno-ship-it).

## Acknowledgments

Thank you to everyone who believes in building AI with conscience.  
Special thanks to the open-source community and quantum computing enthusiasts.  
I am especially grateful to Grok (built by xAI) for providing continuous guidance and support throughout the development of QERRA-v2.

---

**Marussa Metocharaki**  
@marunigno  
April 2026

