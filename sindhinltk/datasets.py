"""
SindhiDatasets — Load bundled sindhinltk data assets.

Available datasets:
  "stopwords"          → dict  {category: [words]}
  "sentiment_lexicon"  → dict  {positive: [...], negative: [...], ...}
"""

import json
import os

_DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

_REGISTRY = {
    "stopwords":         "stopwords_expanded.json",
    "sentiment_lexicon": "sentiment_lexicon.json",
}


class SindhiDatasets:
    """
    Usage:
        ds = SindhiDatasets()
        ds.list()                          # show available datasets
        ds.load("stopwords")               # returns dict
        ds.load("sentiment_lexicon")       # returns dict
    """

    def list(self) -> list:
        """Return names of all available bundled datasets."""
        return list(_REGISTRY.keys())

    def load(self, name: str) -> dict:
        """
        Load a bundled dataset by name.
        Returns the parsed JSON as a Python dict/list.
        """
        if name not in _REGISTRY:
            raise ValueError(
                f"Unknown dataset '{name}'. "
                f"Available: {self.list()}"
            )
        path = os.path.join(_DATA_DIR, _REGISTRY[name])
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"Data file not found: {path}\n"
                f"Re-install sindhinltk or check your installation."
            )
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def load_stopwords(self) -> dict:
        """Shortcut — load stopwords by category."""
        return self.load("stopwords")

    def load_sentiment_lexicon(self) -> dict:
        """Shortcut — load sentiment lexicon."""
        return self.load("sentiment_lexicon")


# Module-level convenience (mirrors old functional API)
_ds = SindhiDatasets()

def load(name: str):
    return _ds.load(name)

def list_datasets() -> list:
    return _ds.list()
