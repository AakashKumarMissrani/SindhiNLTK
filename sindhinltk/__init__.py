"""
SindhiNLTK — A Morphology-Aware, Neural-Hybrid NLP Toolkit for Sindhi.

Features:
    - Anti-Shatter Tokenizer (V3 Linguistic Shield)
    - Morphological Stemmer (rule-based suffix stripping)
    - Stopword Removal (expanded corpus-derived list)
    - NFKC Normalization (Sindhi-specific Unicode handling)
    - Neural Sentiment Engine (optional, requires transformers)
    - Curated Datasets (stopwords, benchmarks) — NEW in v1.1

Install:
    pip install sindhinltk

Usage:
    >>> from sindhinltk import stemmer, stopwords, normalizer
    >>> from sindhinltk.datasets import get_stopwords_expanded

Links:
    PyPI:       https://pypi.org/project/sindhinltk/
    GitHub:     https://github.com/AakashKumarMissrani/SindhiNLTK
    HuggingFace: https://huggingface.co/aakashMeghwar01
"""

__version__ = "1.1.0"
__author__ = "Aakash Meghwar"

from sindhinltk import stemmer
from sindhinltk import stopwords
from sindhinltk import normalizer

# New in v1.1
from sindhinltk import datasets
