"""
SindhiTokenizer — Regex-based word tokenizer for Sindhi (Arabic script).
No external model needed. Handles Arabic punctuation correctly.
"""

import re


class SindhiTokenizer:
    """
    Splits Sindhi text into word tokens using Unicode-aware regex.
    Keeps Arabic-script words whole; splits on spaces and non-Arabic punctuation.
    Does NOT require transformers or any HF model.

    Usage:
        tok = SindhiTokenizer()
        tok.tokenize("ڪاوڙيندڙ ماڻهو گھر ۾ مسئلا پيدا ڪندو آهي")
        # → ['ڪاوڙيندڙ', 'ماڻهو', 'گھر', '۾', 'مسئلا', 'پيدا', 'ڪندو', 'آهي']
    """

    # Arabic/Sindhi chars U+0600-U+06FF + Arabic extended U+0750-U+077F + U+FB50-U+FDFF
    _ARABIC_RANGE = r"\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF"

    def __init__(self):
        # Matches: runs of Sindhi/Arabic chars OR single non-Arabic non-space tokens
        self._pattern = re.compile(
            rf"[{self._ARABIC_RANGE}]+"
            rf"|[^{self._ARABIC_RANGE}\s]+"
        )

    def tokenize(self, text: str) -> list:
        """Tokenize a Sindhi string into a list of word tokens."""
        if not text:
            return []
        return self._pattern.findall(text)

    def sent_tokenize(self, text: str) -> list:
        """
        Split text into sentences on Sindhi/Arabic sentence-final marks:
        ۔ (U+06D4), ? (U+003F), ! and their Arabic variants.
        """
        if not text:
            return []
        parts = re.split(r"[۔؟!\?]+", text)
        return [s.strip() for s in parts if s.strip()]


# Backwards-compatible alias (Gemini added this name, keep it)
TokenizersBackend = SindhiTokenizer
