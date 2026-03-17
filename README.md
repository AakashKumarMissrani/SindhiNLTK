# sindhinltk

**Sindhi Natural Language Toolkit** — the first open-source Python NLP library for the Sindhi language (Arabic script).

[![PyPI version](https://img.shields.io/pypi/v/sindhinltk.svg)](https://pypi.org/project/sindhinltk/)
[![Python](https://img.shields.io/pypi/pyversions/sindhinltk.svg)](https://pypi.org/project/sindhinltk/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Installation

```bash
pip install sindhinltk
```

Zero dependencies — pure Python, works out of the box.

---

## Quick Start

```python
from sindhinltk.tokenizer  import SindhiTokenizer
from sindhinltk.normalizer import SindhiNormalizer
from sindhinltk.stemmer    import SindhiStemmer
from sindhinltk.stopwords  import SindhiStopwords
from sindhinltk.sentiment  import SindhiSentiment
from sindhinltk.datasets   import SindhiDatasets

text = "سنڌي ٻولي تمام سٺي ۽ قديم آهي"

tok     = SindhiTokenizer()
tokens  = tok.tokenize(text)
# → ['سنڌي', 'ٻولي', 'تمام', 'سٺي', '۽', 'قديم', 'آهي']

sw      = SindhiStopwords()
clean   = sw.remove_stopwords(tokens)
# → ['سنڌي', 'ٻولي', 'سٺي', 'قديم']

sa      = SindhiSentiment()
label   = sa.analyze(text)
# → 'مثبت'  (positive)
```

---

## Modules

### 1. Tokenizer — `SindhiTokenizer`

Regex-based word and sentence tokenizer. No internet or model download required.

```python
from sindhinltk.tokenizer import SindhiTokenizer

tok = SindhiTokenizer()

# Word tokenization
tokens = tok.tokenize("ڪاوڙيندڙ ماڻهو گھر ۾ مسئلا پيدا ڪندو آهي")
# → ['ڪاوڙيندڙ', 'ماڻهو', 'گھر', '۾', 'مسئلا', 'پيدا', 'ڪندو', 'آهي']

# Sentence tokenization
sentences = tok.sent_tokenize("هو گھر ۾ آهي۔ سنڌي ٻولي سٺي آهي۔")
# → ['هو گھر ۾ آهي', 'سنڌي ٻولي سٺي آهي']

# Empty input is safe
tok.tokenize("")       # → []
tok.sent_tokenize("")  # → []
```

---

### 2. Normalizer — `SindhiNormalizer`

Unicode NFC normalization, whitespace cleanup, and optional diacritic removal.

```python
from sindhinltk.normalizer import SindhiNormalizer

norm = SindhiNormalizer()

# Basic normalization (NFC + strip + collapse spaces)
norm.normalize("  سنڌي   ٻولي  ")
# → 'سنڌي ٻولي'

# Remove Arabic diacritics / harakat (zabar, zer, pesh, etc.)
norm.normalize("ھوُ ھر روزَ اِسڪول وَڃي ٿو", remove_diacritics=True)
# → 'ھو ھر روز اسڪول وڃي ٿو'

# Keep diacritics (default)
norm.normalize("ھوُ ھر روزَ اِسڪول وَڃي ٿو", remove_diacritics=False)
# → 'ھوُ ھر روزَ اِسڪول وَڃي ٿو'
```

---

### 3. Stemmer — `SindhiStemmer`

Rule-based suffix stripper for Sindhi verbs, nouns, and adjectives. Uses longest-match suffix rules.

```python
from sindhinltk.stemmer import SindhiStemmer

stm = SindhiStemmer()

# Single word stemming
stm.stem("ڪاوڙيندڙ")  # → 'ڪاوڙ'   (present participle)
stm.stem("هلندي")      # → 'هل'     (verb inflection)
stm.stem("وڃندا")      # → 'وڃ'     (plural verb)
stm.stem("ڪندو")       # → 'ڪ'      (verb form)
stm.stem("سنڌي")       # → 'سنڌي'   (no suffix, unchanged)

# Batch stemming
tokens = ['ڪاوڙيندڙ', 'ماڻهو', 'هلندي']
stm.stem_tokens(tokens)
# → ['ڪاوڙ', 'ماڻهو', 'هل']
```

---

### 4. Stopwords — `SindhiStopwords`

143 Sindhi stopwords across 10 semantic categories: pronouns, postpositions, conjunctions, auxiliaries, negation, quantifiers, adverbs, demonstratives, question words, and discourse particles.

```python
from sindhinltk.stopwords import SindhiStopwords

sw = SindhiStopwords()

# Remove stopwords from token list
tokens = ['سنڌي', 'ٻولي', 'آهي', 'تمام', 'سٺي']
sw.remove_stopwords(tokens)
# → ['سنڌي', 'ٻولي', 'سٺي']

# Check a single word
sw.is_stopword("آهي")    # → True
sw.is_stopword("سنڌي")  # → False

# Get all stopwords
all_sw = sw.get_stopwords()          # → set of 143 words

# Get stopwords by category
pronouns = sw.get_stopwords(category="pronouns")
# → {'مان', 'تون', 'هو', 'هوءَ', 'اسان', ...}

# List available categories
sw.get_categories()
# → ['pronouns', 'demonstratives', 'postpositions', 'conjunctions',
#    'question_words', 'auxiliaries', 'negation', 'quantifiers',
#    'adverbs', 'particles']
```

---

### 5. Sentiment — `SindhiSentiment`

Lexicon-based sentiment analysis. Handles intensifiers (`تمام`, `ڏاڍو`) and negators (`نه`, `ناهي`). Returns labels in Sindhi.

```python
from sindhinltk.sentiment import SindhiSentiment

sa = SindhiSentiment()

# Sentiment label (Sindhi)
sa.analyze("سنڌي ٻولي تمام سٺي آهي")   # → 'مثبت'        (positive)
sa.analyze("هو تمام خراب ماڻهو آهي")    # → 'منفي'         (negative)
sa.analyze("هو گھر ۾ آهي")              # → 'غير جانبدار'  (neutral)

# Numeric score (+positive / -negative)
sa.score("سنڌي ٻولي تمام سٺي آهي")    # → 2.0
sa.score("هو تمام خراب ماڻهو آهي")     # → -2.0

# Intensifiers multiply score
sa.score("سٺو")        # → 1.0
sa.score("تمام سٺو")   # → 2.0

# Negators flip sentiment
sa.score("سٺو")        # → 1.0
sa.score("نه سٺو")     # → -1.0

# Detailed breakdown
sa.analyze_detail("تمام سٺي ٻولي")
# → {
#     'label': 'مثبت',
#     'score': 2.0,
#     'hits': {
#         'positive': ['سٺي'],
#         'negative': [],
#         'negated': [],
#         'intensified': ['سٺي']
#     }
#   }
```

**Sentiment labels:**

| Label | Meaning |
|-------|---------|
| `مثبت` | Positive |
| `منفي` | Negative |
| `غير جانبدار` | Neutral |

---

### 6. Datasets — `SindhiDatasets`

Load bundled data assets included with the package.

```python
from sindhinltk.datasets import SindhiDatasets

ds = SindhiDatasets()

# See what's available
ds.list()
# → ['stopwords', 'sentiment_lexicon']

# Load stopwords by category dict
sw_data = ds.load("stopwords")
sw_data["pronouns"]   # → list of Sindhi pronouns
sw_data["auxiliaries"] # → list of auxiliary verbs

# Load sentiment lexicon
lex = ds.load("sentiment_lexicon")
lex["positive"]      # → list of positive words
lex["negative"]      # → list of negative words
lex["intensifiers"]  # → list of intensifier words
lex["negators"]      # → list of negator words

# Shortcuts
ds.load_stopwords()          # same as ds.load("stopwords")
ds.load_sentiment_lexicon()  # same as ds.load("sentiment_lexicon")
```

---

## Full Pipeline Example

```python
from sindhinltk.tokenizer  import SindhiTokenizer
from sindhinltk.normalizer import SindhiNormalizer
from sindhinltk.stemmer    import SindhiStemmer
from sindhinltk.stopwords  import SindhiStopwords
from sindhinltk.sentiment  import SindhiSentiment

def analyze(text):
    # Step 1: Normalize
    norm   = SindhiNormalizer()
    clean  = norm.normalize(text, remove_diacritics=True)

    # Step 2: Tokenize
    tok    = SindhiTokenizer()
    tokens = tok.tokenize(clean)

    # Step 3: Remove stopwords
    sw     = SindhiStopwords()
    tokens = sw.remove_stopwords(tokens)

    # Step 4: Stem
    stm    = SindhiStemmer()
    stems  = stm.stem_tokens(tokens)

    # Step 5: Sentiment
    sa     = SindhiSentiment()
    label  = sa.analyze(text)
    score  = sa.score(text)

    return {
        "original":  text,
        "tokens":    tokens,
        "stems":     stems,
        "sentiment": label,
        "score":     score,
    }

result = analyze("سنڌي ٻولي تمام سٺي ۽ قديم آهي")
print(result)
# {
#   'original':  'سنڌي ٻولي تمام سٺي ۽ قديم آهي',
#   'tokens':    ['سنڌي', 'ٻولي', 'سٺي', 'قديم'],
#   'stems':     ['سنڌي', 'ٻولي', 'سٺي', 'قديم'],
#   'sentiment': 'مثبت',
#   'score':     2.0
# }
```

---

## Related Resources

| Resource | Link |
|----------|------|
| **Sindhi Corpus 505M** | [huggingface.co/datasets/aakashMeghwar01/sindhi-corpus-505m](https://huggingface.co/datasets/aakashMeghwar01/sindhi-corpus-505m) |
| **SindhiLM Tokenizer v1** | [huggingface.co/aakashMeghwar01/SindhiLM-Tokenizer-v1](https://huggingface.co/aakashMeghwar01/SindhiLM-Tokenizer-v1) |
| **GitHub** | [github.com/AakashKumarMissrani/SindhiNLTK](https://github.com/AakashKumarMissrani/SindhiNLTK) |

---

## Author

**Aakash Meghwar**
[GitHub](https://github.com/AakashKumarMissrani) · [HuggingFace](https://huggingface.co/aakashMeghwar01)

---

## License

MIT — free to use, modify, and distribute.