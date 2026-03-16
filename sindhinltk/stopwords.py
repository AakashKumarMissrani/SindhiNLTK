class SindhiStopwords:
    def __init__(self):
        self.sw = {"۽", "يا", "پر", "ڪرڻ", "ته", "کي", "جو", "جي", "جا", "تي", "تان", "کان", "۾", "سان"}
    def remove_stopwords(self, tokens):
        return [t for t in tokens if t not in self.sw]