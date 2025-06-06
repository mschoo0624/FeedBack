from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class SarcasmDetector:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter")

    def predict(self, text: str):
        inputs = self.tokenizer(f"tweet: {text} </s>", return_tensors="pt")
        outputs = self.model.generate(**inputs)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)