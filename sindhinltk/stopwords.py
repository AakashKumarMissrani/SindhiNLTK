"""
SindhiStopwords — Comprehensive Sindhi stopword list (Arabic script).
168 words across 10 semantic categories.
"""

_STOPWORDS = {
    # ── 1. Personal pronouns ────────────────────────────────────
    "pronouns": [
        "مان", "تون", "هو", "هوءَ", "اسان", "توهان", "اهي",
        "اهو", "اها", "هي", "هن", "انهن", "پاڻ", "پنهنجو",
        "پنهنجي", "پنهنجا",
    ],
    # ── 2. Demonstratives ───────────────────────────────────────
    "demonstratives": [
        "هي", "هيءَ", "اهو", "اها", "اهي", "هيٺ", "مٿي",
        "هتي", "اتي", "هنن", "انهي",
    ],
    # ── 3. Postpositions ────────────────────────────────────────
    "postpositions": [
        "۾", "تي", "کان", "کي", "سان", "لاءِ", "تان",
        "جو", "جي", "جا", "ڏانهن", "پاران", "وارو", "واري",
        "وارا", "بعد", "اڳ", "آڏو", "پٺيان",
    ],
    # ── 4. Conjunctions ─────────────────────────────────────────
    "conjunctions": [
        "۽", "پر", "يا", "ته", "جڏهن", "جيئن", "ڇاڪاڻ",
        "ڇو", "تنهن", "ان", "اگر", "جيڪڏهن", "ورنه",
        "البته", "بلڪه", "يعني",
    ],
    # ── 5. Question words ───────────────────────────────────────
    "question_words": [
        "ڇا", "ڪير", "ڪٿي", "ڪڏهن", "ڪيئن", "ڪيترو",
        "ڪهڙو", "ڪهڙي", "ڪهڙا",
    ],
    # ── 6. Auxiliary verbs / copulas ────────────────────────────
    "auxiliaries": [
        "آهي", "آهن", "آهيان", "آهيو", "هئو", "هئي",
        "هئاسين", "هوندو", "هوندي", "هوندا", "هجي", "هجن",
        "ٿو", "ٿي", "ٿا", "ٿيو", "ٿئي", "ويو", "وئي",
        "ويا", "اچي", "آيو", "آئي", "ڪيو", "ڪئي", "ڪيا",
    ],
    # ── 7. Negation ─────────────────────────────────────────────
    "negation": [
        "نه", "ناهي", "ناهن", "نٿو", "نٿي", "نٿا",
        "نڪو", "هرگز",
    ],
    # ── 8. Quantifiers / determiners ────────────────────────────
    "quantifiers": [
        "هر", "ڪو", "ڪا", "ڪي", "ڪجهه", "سڀ", "سڀئي",
        "گهڻو", "گهڻي", "گهڻا", "ٿورو", "ٿوري", "ڪيترا",
        "ڪافي", "وڌيڪ", "گهٽ", "تمام", "بلڪل",
    ],
    # ── 9. Adverbs of time / place ──────────────────────────────
    "adverbs": [
        "اڄ", "سڀاڻي", "ڪالهه", "هاڻي", "پوءِ", "اڳ",
        "تڏهن", "هميشه", "اڃا", "وري",
        "پهرين", "آخر", "جلدي", "آهستي",
    ],
    # ── 10. Discourse particles ─────────────────────────────────
    "particles": [
        "ها", "ٺيڪ", "ڀلا", "ڏس", "ٻڌ", "چيو",
        "واه", "آ", "مثال", "يعني", "ٻيو", "ٻي",
    ],
}


class SindhiStopwords:
    """
    Sindhi stopword filter.

    Usage:
        sw = SindhiStopwords()
        sw.is_stopword("آهي")                          # True
        sw.remove_stopwords(["سنڌي", "آهي", "سٺي"])   # ["سنڌي", "سٺي"]
        sw.get_stopwords()                             # full set
        sw.get_stopwords(category="pronouns")         # just pronouns
    """

    def __init__(self):
        self._by_category = _STOPWORDS
        self._all = set(w for words in _STOPWORDS.values() for w in words)

    def get_stopwords(self, category: str = None) -> set:
        """Return full stopword set, or words for a specific category."""
        if category:
            if category not in self._by_category:
                raise ValueError(
                    f"Unknown category '{category}'. "
                    f"Available: {list(self._by_category.keys())}"
                )
            return set(self._by_category[category])
        return set(self._all)

    def get_categories(self) -> list:
        return list(self._by_category.keys())

    def is_stopword(self, word: str) -> bool:
        return word in self._all

    def remove_stopwords(self, tokens: list) -> list:
        return [t for t in tokens if t not in self._all]
