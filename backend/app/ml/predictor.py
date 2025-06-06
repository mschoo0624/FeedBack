from transformers import pipeline
from .preprocess import clean_text

class SentimentAnalyzer:
    def __init__(self):
        self.model = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            return_all_scores=True
        )
        
    def predict(self, text: str):
        cleaned = clean_text(text)  # Implement in preprocess.py
        results = self.model(cleaned)[0]
        # Convert to {label: score} format
        return {res["label"]: res["score"] for res in results}