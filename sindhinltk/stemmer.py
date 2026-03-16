class SindhiStemmer:
    def stem(self, word):
        suffixes = ["ائيندڙ", "يندڙ", "يائين", "ائين", "يون", "ان", "ون", "ين", "ي", "و"]
        for s in suffixes:
            if word.endswith(s) and len(word) - len(s) >= 2: return word[:-len(s)]
        return word