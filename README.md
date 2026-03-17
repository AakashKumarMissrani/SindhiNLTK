# SindhiNLTK: A Morphology-Aware NLP Toolkit for Sindhi

[![PyPI version](https://img.shields.io/pypi/v/sindhinltk.svg)](https://pypi.org/project/sindhinltk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**SindhiNLTK** is a high-performance Python library for Sindhi natural language processing. It addresses the "Linguistic Efficiency Gap" where standard multilingual models break Sindhi's unique orthographic clusters into meaningless tokens.

## What's New in v1.1.0

- **Expanded Stopwords** — 245 stopwords (up from ~30) organized by grammatical category (pronouns, postpositions, auxiliaries, conjunctions, etc.), extracted from the [sindhi-corpus-505m](https://huggingface.co/datasets/aakashMeghwar01/sindhi-corpus-505m).
- **Datasets Module** — `sindhinltk.datasets` provides programmatic access to bundled linguistic data with category filtering and utility functions.
- **Improved Packaging** — Proper `pyproject.toml` with `[project.optional-dependencies]`, bundled JSON data files, Python 3.8–3.12 support.

## Performance

Validated against a corpus of 43,784 SFT instruction samples:

| Metric | Llama-3 (Meta) | SindhiNLTK (Ours) | Improvement |
|--------|---------------|-------------------|-------------|
| Token Fertility Rate | 4.15 | **1.06** | 291% more efficient |
| Aspiration Integrity | ~30% | **100% (Atomic)** | Full linguistic accuracy |
| Context Window | Baseline | **4x Larger** | Memory optimization |

## Installation

```bash
pip install sindhinltk
```

For sentiment analysis (requires PyTorch):
```bash
pip install sindhinltk[sentiment]
```

## Quick Start

```python
from sindhinltk import stemmer, normalizer, stopwords

# Normalize text
text = normalizer.normalize("  سنڌ   جي   ثقافت  ")
# → "سنڌ جي ثقافت"

# Stem words
stemmer.stem("ڪتابون")   # → "ڪتاب"
stemmer.stem("پڙهائيندڙ")  # → "پڙه"

# Get stopwords
sw = stopwords.get_stopwords()
```

### New in v1.1: Expanded Stopwords & Datasets

```python
from sindhinltk.datasets import (
    get_stopwords_expanded,
    get_stopwords_by_category,
    is_stopword,
    remove_stopwords,
)

# 245 stopwords (vs ~30 in v1.0)
all_sw = get_stopwords_expanded()
print(len(all_sw))  # 245

# Filter by grammatical category
pronouns = get_stopwords_by_category("pronouns")
negation = get_stopwords_by_category("negation")
postpositions = get_stopwords_by_category("postpositions")

# Quick check
is_stopword("آهي")    # True
is_stopword("ڪتاب")   # False

# Filter a token list
tokens = ["سنڌ", "جو", "گاديءَ", "وارو", "شهر"]
clean = remove_stopwords(tokens)
# → ["سنڌ", "گاديءَ", "شهر"]
```

**Available categories:** `pronouns`, `postpositions`, `auxiliaries_and_copulas`, `conjunctions`, `particles_and_markers`, `negation`, `question_words`, `demonstratives`, `adverbs_of_time_place`, `high_frequency_function_words`

## Data Sources

The expanded stopwords and SindhiNLTK's development are informed by these Sindhi datasets:

| Source | Type | Size |
|--------|------|------|
| [sindhi-corpus-505m](https://huggingface.co/datasets/aakashMeghwar01/sindhi-corpus-505m) | Web + news + lit | 505M tokens |
| [AMBILE Sindhi Mega Corpus](https://kaggle.com/datasets/ambile/sindhi-mega-corpus-118-million-tokens) | Mixed | 118M tokens |
| [Daily Kawish Articles](https://kaggle.com/datasets/owaisraza009/sindhi-articles-dataset-from-daily-kawish) | News | Articles |
| [CC100-Sindhi](https://metatext.io/datasets/cc100-sindhi) | Web crawl | Large |
| [Sindhi Legal Dataset](https://kaggle.com/datasets/danishmahdi/sindhi-legal-dataset) | Legal | Documents |
| [Sindhi Stopwords](https://kaggle.com/datasets/owaisraza009/sindhi-stopwords) | Linguistic | Word list |
| [Encyclopedia Sindhiana](https://kaggle.com/datasets/danishmahdi/encyclopedia-sindhiana-text-corpus) | Encyclopedia | Articles |
| [Awami Awaz News](https://kaggle.com/datasets/danishmahdi/sindhi-news-corpus-awami-awaz) | News | Articles |
| [Sindh Express News](https://kaggle.com/datasets/danishmahdi/sindhi-news-corpus-sindh-express) | News | Articles |
| [Sindhi Religious Data](https://kaggle.com/datasets/nairsaanvi/sindhi-religious-data) | Religious | Texts |
| [Sindhi Language Corpus](https://kaggle.com/datasets/majidshah123/sindhi-language-corpus) | Mixed | Corpus |

## Related Projects

- **[SindhiLM](https://huggingface.co/aakashMeghwar01/SindhiLM)** — GPT-2 model for Sindhi (37.8M params)
- **[SindhiLM-Qwen-0.5B-v2](https://huggingface.co/aakashMeghwar01/SindhiLM-Qwen-0.5B-v2)** — Qwen2.5-0.5B fine-tuned for Sindhi
- **[SindhiLM-Tokenizer-v2](https://huggingface.co/aakashMeghwar01)** — Morpheme-boundary-aware BPE tokenizer
- **[Sindhi-Intelligence-Core-SFT-v2](https://huggingface.co/datasets/aakashMeghwar01/Sindhi-Intelligence-Core-SFT-v2)** — 46K instruction-tuning samples

## Author

**Aakash Meghwar** — Computational Linguist

- HuggingFace: [aakashMeghwar01](https://huggingface.co/aakashMeghwar01)
- GitHub: [AakashKumarMissrani](https://github.com/AakashKumarMissrani)

## License

MIT
