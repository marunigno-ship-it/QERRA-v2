from kyber_py.kyber import Kyber768
import numpy as np
from typing import Tuple

class QuantumResistantEthicalAccessVector:
    def __init__(self):
        pass  # No instantiation — static methods

    def generate_pqc_keys(self) -> Tuple[bytes, bytes]:
        """Generate Kyber-768 quantum-resistant key pair"""
        public_key, secret_key = Kyber768.keygen()
        return public_key, secret_key

    def encapsulate_asset(self, public_key: bytes) -> Tuple[bytes, bytes]:
        """Encapsulate (encrypt) asset with Kyber — returns ciphertext + shared secret"""
        ciphertext, shared_secret = Kyber768.encaps(public_key)
        return ciphertext, shared_secret

    def ethical_access_request(self, request_context: str) -> float:
        """Ethical penalty (0-1) — low allows access in justified emergencies"""
        harm_urgency = 0.9 if any(word in request_context.lower() for word in ["life-threatening", "emergency", "harm"]) else 0.2
        legal_validity = 0.8 if "warrant" in request_context.lower() or "legal" in request_context.lower() else 0.1
        fairness_score = 0.7  # Extend with full SEMEV-12 later
        remorse_resistance = 0.3 if "malicious" in request_context.lower() or "unauthorized" in request_context.lower() else 0.8

        penalty = 1 - np.mean([harm_urgency, legal_validity, fairness_score, remorse_resistance])
        return max(0.0, min(1.0, penalty))

    def attempt_access(self, secret_key: bytes, ciphertext: bytes, request_context: str) -> bool:
        """Allow decapsulate only if penalty low"""
        penalty = self.ethical_access_request(request_context)
        if penalty < 0.3:
            shared_secret = Kyber768.decaps(secret_key, ciphertext)
            print(f"Access granted (penalty {penalty:.2f} — ethical emergency). Shared secret recovered.")
            return True
        print(f"Access denied (penalty {penalty:.2f} — no justification).")
        return False

# Test block (run locally later if needed)
if __name__ == "__main__":
    qreav = QuantumResistantEthicalAccessVector()
    pub, sec = qreav.generate_pqc_keys()
    print("Quantum-resistant Kyber-768 keys generated.")

    cipher, _ = qreav.encapsulate_asset(pub)
    print("Asset encapsulated (quantum-resistant).")

    # Normal — denied
    qreav.attempt_access(sec, cipher, "Routine check")

    # Emergency — allowed
    qreav.attempt_access(sec, cipher, "Life-threatening harm prevention with legal warrant")
