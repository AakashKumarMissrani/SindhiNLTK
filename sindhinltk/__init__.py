from .normalizer import SindhiNormalizer
from .tokenizer import SindhiTokenizer
from .stemmer import SindhiStemmer
from .stopwords import SindhiStopwords
from .sentiment import SindhiSentiment
class SindhiNLP:
    def __init__(self):
        self.norm = SindhiNormalizer()
        self.tok = SindhiTokenizer()
        self.stemmer = SindhiStemmer()
        self.sw = SindhiStopwords()
        self.sent = SindhiSentiment()
    def process(self, text):
        clean = self.norm.normalize(text)
        tokens = self.tok.tokenize(clean)
        no_sw = self.sw.remove_stopwords(tokens)
        stems = [self.stemmer.stem(t) for t in no_sw]
        sentiment = self.sent.analyze(clean)
        return {"tokens": tokens, "stems": stems, "sentiment": sentiment}