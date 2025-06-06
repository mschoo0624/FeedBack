from fastapi import FastAPI
from transformers import pipeline

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Load model globally (simple version)
sentiment_model = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

@app.post("/analyze")
async def analyze_text(text: str):
    result = sentiment_model(text)[0]
    return {
        "sentiment": "like" if result["label"] == "POSITIVE" else "dislike",
        "confidence": result["score"]
    }