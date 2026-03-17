"""
SindhiStemmer — Rule-based suffix stripping for Sindhi (Arabic script).
Strips common verb, noun, and adjective suffixes in longest-first order.
"""

class SindhiStemmer:
    """
    Strips inflectional suffixes from Sindhi words.

    Usage:
        stm = SindhiStemmer()
        stm.stem("ڪاوڙيندڙ")   # → "ڪاوڙ"
        stm.stem("ڪندو")        # → "ڪ"
        stm.stem("وڃندا")       # → "وڃ"
    """

    # Ordered longest-first so greedy matching picks the most specific rule
    SUFFIXES = [
        # ── Verb / participial ──────────────────────────────────
        "يندڙ",   # ڪاوڙيندڙ → ڪاوڙ  (present participle, agent)
        "يندي",   # هلندي
        "يندو",   # هلندو
        "يندا",   # هلندا
        "ندڙ",    # ڪندڙ → ڪ
        "ندو",    # ڪندو → ڪ
        "ندي",    # ڪندي → ڪ
        "ندا",    # ڪندا → ڪ
        "ندي",    # ڪندي
        "ندو",    # ڪندو
        "ندا",    # ڪندا
        "يائين",  # ڪيائين → ڪ
        "ائين",   # ويائين
        "ئين",    # ڏئين
        "وٿو",    # وٺوٿو
        "وٿي",
        "ايو",    # اچايو
        "ئيو",
        "يو",     # ويو → و (keep min length check)
        "ئي",     # ڏيئي
        "وي",
        # ── Noun / adjective ────────────────────────────────────
        "پڻ",    # سچپڻ → سچ
        "اڻ",    # سهاڻ → سه
        "وڻ",    # پاڻ-وڻ
        "ون",    # ڪتابون → ڪتاب
        "ين",    # ماڻهين → ماڻهو (approx)
        "ڻو",    # ننڍڻو
        "ڻي",
        "ڻا",
        "اً",    # tanwin
    ]

    MIN_STEM = 1   # don't strip if result would be shorter

    def stem(self, word: str) -> str:
        """Return the stem of a single Sindhi word."""
        if not word:
            return word
        for suffix in self.SUFFIXES:
            if word.endswith(suffix):
                candidate = word[: len(word) - len(suffix)]
                if len(candidate) >= self.MIN_STEM:
                    return candidate
        return word

    def stem_tokens(self, tokens: list) -> list:
        """Stem a list of word tokens."""
        return [self.stem(t) for t in tokens]
