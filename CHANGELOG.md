# Changelog

## [1.1.0] — 2026-03-17

### Added
- **`sindhinltk.datasets` module** — New module providing programmatic access to bundled Sindhi linguistic datasets.
- **Expanded stopwords** — 245 stopwords organized by 10 grammatical categories (pronouns, postpositions, auxiliaries, conjunctions, particles, negation, question words, demonstratives, adverbs, high-frequency function words).
- **Utility functions** — `is_stopword()`, `remove_stopwords()`, `get_stopwords_by_category()`, `get_stopwords_metadata()`.
- **Bundled JSON data** — Stopwords data ships with the package (<50KB), no external downloads needed.
- **Python 3.8–3.12 support** declared in classifiers.
- **Optional dependencies** — `pip install sindhinltk[sentiment]` for the neural sentiment engine.

### Changed
- **`pyproject.toml`** — Modernized packaging with proper metadata, URLs, keywords, and `[tool.setuptools.package-data]` for JSON files.
- **README.md** — Expanded with v1.1 features, data source citations, and related projects.

### Data Sources
Stopwords derived from statistical analysis of:
- `aakashMeghwar01/sindhi-corpus-505m` (HuggingFace, 742K docs)
- `owaisraza009/sindhi-stopwords` (Kaggle)
- Hand-curated linguistic review

## [1.0.4] — 2026-03-16

- V3 Linguistic Shield release
- Anti-Shatter Tokenizer with 1.06 fertility rate
- 100% aspiration integrity for Sindhi digraphs
- Neural Sentiment Engine
- Morphological Stemmer
- Published on PyPI

## [1.0.0] — Initial Release

- Basic stemmer, stopwords, normalizer
- Published on PyPI as `sindhinltk`
