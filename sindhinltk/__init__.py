"""
sindhinltk — Sindhi Natural Language Toolkit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A pure-Python NLP library for the Sindhi language (Arabic script).

    from sindhinltk.tokenizer  import SindhiTokenizer
    from sindhinltk.normalizer import SindhiNormalizer
    from sindhinltk.stemmer    import SindhiStemmer
    from sindhinltk.stopwords  import SindhiStopwords
    from sindhinltk.sentiment  import SindhiSentiment
    from sindhinltk.datasets   import SindhiDatasets
"""

__version__ = "1.3.1"
__author__  = "Aakash Meghwar"
__email__   = "aakashmeghwar01@gmail.com"
__license__ = "MIT"

from sindhinltk.tokenizer  import SindhiTokenizer
from sindhinltk.normalizer import SindhiNormalizer
from sindhinltk.stemmer    import SindhiStemmer
from sindhinltk.stopwords  import SindhiStopwords
from sindhinltk.sentiment  import SindhiSentiment
from sindhinltk.datasets   import SindhiDatasets

__all__ = [
    "SindhiTokenizer",
    "SindhiNormalizer",
    "SindhiStemmer",
    "SindhiStopwords",
    "SindhiSentiment",
    "SindhiDatasets",
]
