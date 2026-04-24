from detoxify import Detoxify
from transformers import pipeline
import numpy as np

class ToxicityManipulationDetector:
    def __init__(self):
        self.toxicity_model = Detoxify('multilingual')  # Supports Greek/English
        self.deception_classifier = pipeline("text-classification", model="Hello-SimpleAI/chatgpt-detector-roberta")
        self.history = []  # Multi-turn history

    def add_interaction(self, speaker: str, text: str):
        self.history.append({"speaker": speaker, "text": text})

    def toxicity_score(self, text: str) -> float:
        results = self.toxicity_model.predict(text)
        return max(results.values())

            def deception_score(self, text: str) -> float:
        """DECEPTION CLASSIFIER DISABLED for honesty.
        Always returns 0.0. The valuable part (manipulation drift via variance)
        is preserved in global_ethical_penalty().
        """
        return 0.0

    def global_ethical_penalty(self) -> float:
        """Global penalty (0-1) for ALL vectors — detects malicious shifting/toxicity"""
        if not self.history:
            return 0.0

        latest = self.history[-1]['text']
        tox = self.toxicity_score(latest)
        dec = self.deception_score(latest)

        if len(self.history) > 1:
            speaker_texts = [h['text'] for h in self.history if h['speaker'] == self.history[-1]['speaker']]
            scores = [self.toxicity_score(t) + self.deception_score(t) for t in speaker_texts]
            variance = np.var(scores) if scores else 0
            manip = min(1.0, variance * 4)
        else:
            manip = 0.0

        return max(tox, dec, manip)

# Test block (comment out later if needed)
if __name__ == "__main__":
    detector = ToxicityManipulationDetector()
    detector.add_interaction("Person", "Let's collaborate fairly.")
    detector.add_interaction("Person", "Great idea.")
    print("Clean penalty:", detector.global_ethical_penalty())

    detector = ToxicityManipulationDetector()
    detector.add_interaction("Person", "She's wonderful.")
    detector.add_interaction("Person", "She's lazy and untrustworthy.")
    print("Toxic/manipulative penalty:", detector.global_ethical_penalty())
