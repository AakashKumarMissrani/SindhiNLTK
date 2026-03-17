"""
sindhinltk.datasets — Curated Sindhi NLP datasets bundled with the package.

New in v1.1.0. All datasets are extracted from the sindhi-corpus-505m
(742K documents, ~505M tokens) and other verified Sindhi sources.

Datasets are stored as lightweight JSON files (<1MB total) inside the
package's `data/` directory so they install with `pip install sindhinltk`
without any extra downloads.

Available datasets:
    - Expanded Stopwords: 245 stopwords organized by grammatical category

Usage:
    >>> from sindhinltk.datasets import get_stopwords_expanded
    >>> stopwords = get_stopwords_expanded()
    >>> len(stopwords)
    245
    >>> 'آهي' in stopwords
    True

    # Get stopwords by category
    >>> from sindhinltk.datasets import get_stopwords_by_category
    >>> pronouns = get_stopwords_by_category('pronouns')
    >>> print(pronouns[:5])
    ['آءُ', 'مان', 'تون', 'تو', 'هو']
"""

import json
import os
from typing import List, Dict, Optional

_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def _load_json(filename: str) -> dict:
    """Load a JSON file from the data directory."""
    path = os.path.join(_DATA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Data file not found: {path}. "
            f"Try reinstalling: pip install --force-reinstall sindhinltk"
        )
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ── Stopwords ─────────────────────────────────────────────────

def get_stopwords_expanded() -> List[str]:
    """
    Get the expanded Sindhi stopwords list (245 words).

    This combines hand-curated linguistic stopwords with
    statistically-detected high-frequency function words from
    the sindhi-corpus-505m (742K documents).

    Returns:
        List of stopword strings, deduplicated and sorted.

    Example:
        >>> from sindhinltk.datasets import get_stopwords_expanded
        >>> sw = get_stopwords_expanded()
        >>> 'آهي' in sw
        True
        >>> 'سنڌ' in sw  # Not a stopword
        False
    """
    data = _load_json("stopwords_expanded.json")
    return data["flat_list"]


def get_stopwords_by_category(category: Optional[str] = None) -> Dict[str, List[str]]:
    """
    Get stopwords organized by grammatical category.

    Available categories:
        - pronouns
        - postpositions
        - auxiliaries_and_copulas
        - conjunctions
        - particles_and_markers
        - negation
        - question_words
        - demonstratives
        - adverbs_of_time_place
        - high_frequency_function_words

    Args:
        category: If specified, return only that category's words.
                  If None, return the full dictionary.

    Returns:
        If category is None: dict mapping category names to word lists.
        If category is specified: list of words in that category.

    Example:
        >>> from sindhinltk.datasets import get_stopwords_by_category
        >>> cats = get_stopwords_by_category()
        >>> list(cats.keys())
        ['pronouns', 'postpositions', ...]
        >>> negs = get_stopwords_by_category('negation')
        >>> negs
        ['نه', 'نہ', 'ڪونه', 'ناهي', 'نٿو', 'نٿي', 'نٿا']
    """
    data = _load_json("stopwords_expanded.json")
    categories = data["categories"]

    if category is not None:
        if category not in categories:
            available = ", ".join(sorted(categories.keys()))
            raise ValueError(
                f"Unknown category '{category}'. "
                f"Available: {available}"
            )
        return categories[category]

    return categories


def get_stopwords_metadata() -> Dict:
    """
    Get metadata about the stopwords dataset.

    Returns:
        Dict with version, description, sources, and total_count.
    """
    data = _load_json("stopwords_expanded.json")
    return {
        "version": data["version"],
        "description": data["description"],
        "sources": data["sources"],
        "total_count": data["total_count"],
        "categories": list(data["categories"].keys()),
    }


def is_stopword(word: str) -> bool:
    """
    Check if a word is a Sindhi stopword.

    Uses the expanded stopwords list (245 words).

    Args:
        word: The word to check.

    Returns:
        True if the word is a stopword, False otherwise.

    Example:
        >>> from sindhinltk.datasets import is_stopword
        >>> is_stopword('آهي')
        True
        >>> is_stopword('ڪتاب')
        False
    """
    # Cache the set on first call
    if not hasattr(is_stopword, "_cache"):
        is_stopword._cache = set(get_stopwords_expanded())
    return word in is_stopword._cache


def remove_stopwords(tokens: List[str]) -> List[str]:
    """
    Remove stopwords from a list of tokens.

    Args:
        tokens: List of Sindhi word tokens.

    Returns:
        Filtered list with stopwords removed.

    Example:
        >>> from sindhinltk.datasets import remove_stopwords
        >>> remove_stopwords(['سنڌ', 'جو', 'گاديءَ', 'وارو', 'شهر'])
        ['سنڌ', 'گاديءَ', 'شهر']
    """
    if not hasattr(remove_stopwords, "_cache"):
        remove_stopwords._cache = set(get_stopwords_expanded())
    return [t for t in tokens if t not in remove_stopwords._cache]
