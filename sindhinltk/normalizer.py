import unicodedata
import re
class SindhiNormalizer:
    def normalize(self, text):
        text = unicodedata.normalize("NFKC", text)
        return re.sub(r"[ \t]+", " ", text).strip()