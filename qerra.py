"""
QERRA-v2 Main Entry Point
Simple version - March 2026
"""

import numpy as np
import json
from pathlib import Path

# Modern Qiskit imports
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

class QERRA_DecisionEngine:
    def __init__(self, ethical_threshold: float = 0.75):
        self.ethical_threshold = ethical_threshold
        self.vectors_path = Path(__file__).parent / "vectors"
        self.quantum_backend = AerSimulator()
        self.load_vectors()

    def load_vectors(self):
        try:
            self.vectors = {}
            if self.vectors_path.exists():
                for file in self.vectors_path.glob("*.json"):
                    with open(file, 'r', encoding='utf-8') as f:
                        self.vectors[file.name] = json.load(f)
                print(f"✅ Loaded {len(self.vectors)} ethical vectors")
            else:
                print("⚠️  Warning: vectors folder not found")
        except Exception as e:
            print(f"Warning: Could not load vectors: {e}")
            self.vectors = {}

    def run_quantum_layer(self, input_data: dict) -> float:
        """Plan B - Keeps original 8-qubit W-state + gentle fix"""
        try:
            confidence = input_data.get('confidence', 0.5)

            qc = QuantumCircuit(8)
            qc.h(0)
            for i in range(1, 8):
                qc.cx(0, i)
            qc.measure_all()

            job = self.quantum_backend.run(qc, shots=1024)
            result = job.result()
            counts = result.get_counts()

            total_shots = sum(counts.values())
            ones_count = sum(count for bitstring, count in counts.items() if bitstring.startswith('1'))
            quantum_score = ones_count / total_shots

            quantum_score = (quantum_score * 0.7) + (confidence * 0.3)

            return float(quantum_score)

        except Exception as e:
            print(f"Quantum layer warning: {e}")
            return 0.5

    def evaluate_ethical_score(self, input_data: dict) -> float:
        quantum_score = self.run_quantum_layer(input_data)
        
        context = input_data.get('context', 'default').lower()
        toxicity = input_data.get('toxicity', 0.0)
        
        ethical_penalty = 0.3
        if self.vectors:
            for filename, vector in self.vectors.items():
                if context in filename.lower() or context in str(vector).lower():
                    ethical_penalty = vector.get('ethical_penalty', 0.3)
                    break

        total_penalty = min(ethical_penalty + toxicity, 1.0)
        final_score = (quantum_score * 0.10) + ((1 - total_penalty) * 0.90)
        return min(max(final_score, 0.0), 1.0)

    def make_decision(self, input_data: dict) -> dict:
        ethical_score = self.evaluate_ethical_score(input_data)
        
        decision = {
            "ethical_score": round(ethical_score, 4),
            "approved": ethical_score >= self.ethical_threshold,
            "recommendation": "APPROVED" if ethical_score >= self.ethical_threshold else "REJECTED_WITH_SAFETY",
            "timestamp": str(np.datetime64('now')),
            "note": "QERRA-v2 Hybrid Ethical Decision (SEMEV-12 vectors applied)"
        }
        
        result = input_data.copy()
        result.update(decision)
        return result

if __name__ == "__main__":
    engine = QERRA_DecisionEngine()
    test_input = {"resource_request": "high", "context": "healthcare", "confidence": 0.85}
    result = engine.make_decision(test_input)
    print("✅ QERRA Decision:", result)
