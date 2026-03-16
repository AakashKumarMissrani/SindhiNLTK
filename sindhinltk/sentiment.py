from transformers import pipeline
class SindhiSentiment:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis", model="tabularisai/multilingual-sentiment-analysis")
    def analyze(self, text):
        res = self.classifier(text)[0]
        m = {"LABEL_1": "Positive", "LABEL_0": "Negative", "LABEL_2": "Neutral"}
        return {"label": m.get(res["label"], res["label"]), "confidence": f"{round(res['score']*100, 2)}%"}