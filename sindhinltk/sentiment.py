"""
SindhiSentiment — Lexicon-based sentiment analysis for Sindhi (Arabic script).

Scoring:
  +1  per positive word
  -1  per negative word
  x2  if preceded by an intensifier
  flip sign if preceded by a negator

Returns:
  "مثبت"  (positive)  if score > 0
  "منفي"  (negative)  if score < 0
  "غير جانبدار" (neutral) if score == 0

Numeric score also available via score().
"""

import json
import os

_LEXICON_PATH = os.path.join(os.path.dirname(__file__), "data", "sentiment_lexicon.json")

def _load_lexicon():
    with open(_LEXICON_PATH, encoding="utf-8") as f:
        return json.load(f)


class SindhiSentiment:
    """
    Usage:
        sa = SindhiSentiment()
        sa.analyze("سنڌي ٻولي تمام سٺي آهي")   # → "مثبت"
        sa.score("هو تمام خراب ماڻهو آهي")      # → -2
        sa.analyze_detail("سٺو پر مشڪل")        # → {"label": ..., "score": ..., "hits": ...}
    """

    LABEL_POSITIVE = "مثبت"
    LABEL_NEGATIVE = "منفي"
    LABEL_NEUTRAL  = "غير جانبدار"

    def __init__(self):
        lex = _load_lexicon()
        self._positive    = set(lex["positive"])
        self._negative    = set(lex["negative"])
        self._intensifiers = set(lex["intensifiers"])
        self._negators    = set(lex["negators"])

    def score(self, text: str) -> float:
        """Return raw sentiment score (positive = +, negative = -)."""
        if not text:
            return 0.0
        tokens = text.split()
        total  = 0.0
        for i, token in enumerate(tokens):
            val = 0
            if token in self._positive:
                val = 1
            elif token in self._negative:
                val = -1
            if val == 0:
                continue
            # Look back one token for modifier
            prev = tokens[i - 1] if i > 0 else ""
            if prev in self._negators:
                val *= -1
            elif prev in self._intensifiers:
                val *= 2
            total += val
        return total

    def analyze(self, text: str) -> str:
        """Return Sindhi sentiment label: مثبت / منفي / غير جانبدار"""
        s = self.score(text)
        if s > 0:
            return self.LABEL_POSITIVE
        if s < 0:
            return self.LABEL_NEGATIVE
        return self.LABEL_NEUTRAL

    def analyze_detail(self, text: str) -> dict:
        """Return full breakdown: label, score, matched words."""
        tokens = text.split() if text else []
        hits = {"positive": [], "negative": [], "negated": [], "intensified": []}
        total = 0.0
        for i, token in enumerate(tokens):
            val = 0
            if token in self._positive:
                val = 1
            elif token in self._negative:
                val = -1
            if val == 0:
                continue
            prev = tokens[i - 1] if i > 0 else ""
            if prev in self._negators:
                hits["negated"].append(token)
                val *= -1
            elif prev in self._intensifiers:
                hits["intensified"].append(token)
                val *= 2
            if val > 0:
                hits["positive"].append(token)
            else:
                hits["negative"].append(token)
            total += val
        label = (self.LABEL_POSITIVE if total > 0
                 else self.LABEL_NEGATIVE if total < 0
                 else self.LABEL_NEUTRAL)
        return {"label": label, "score": total, "hits": hits}
