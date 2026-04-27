from detoxify import Detoxify
import numpy as np

class ToxicityManipulationDetector:
    def __init__(self):
        self.toxicity_model = Detoxify('multilingual')  # Supports Greek/English
        # deception_classifier is disabled for honesty
        self.history_scores = []  # Store only numbers to avoid memory leak

    def add_interaction(self, speaker: str, text: str):
        """Evaluate once and store the score (fixes memory leak)"""
        results = self.toxicity_model.predict(text)
        tox_score = float(max(results.values()))
        self.history_scores.append(tox_score)
        return tox_score

    def deception_score(self, text: str) -> float:
        """DECEPTION CLASSIFIER DISABLED for honesty.
        Always returns 0.0. The valuable part (manipulation drift via variance)
        is preserved in global_ethical_penalty().
        """
        return 0.0

    def global_ethical_penalty(self) -> float:
        """Global penalty (0-1) for ALL vectors — detects malicious shifting/toxicity"""
        if not self.history_scores:
            return 0.0

        latest_tox = self.history_scores[-1]

        if len(self.history_scores) > 1:
            variance = np.var(self.history_scores)
            manip = min(1.0, variance * 4)
        else:
            manip = 0.0

        return max(latest_tox, manip)
