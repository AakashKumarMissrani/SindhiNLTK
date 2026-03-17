# Upgrade Guide: SindhiNLTK v1.0.4 → v1.1.0

## What Changed

```
v1.0.4 (your current)          v1.1.0 (this package)
├── sindhinltk/                 ├── sindhinltk/
│   ├── __init__.py             │   ├── __init__.py          ← UPDATED (new version + datasets import)
│   ├── stemmer.py              │   ├── stemmer.py           ← STUB — copy your v1.0.4 code
│   ├── stopwords.py            │   ├── stopwords.py         ← STUB — copy your v1.0.4 code
│   ├── normalizer.py           │   ├── normalizer.py        ← STUB — copy your v1.0.4 code
│   └── (sentiment etc.)        │   ├── datasets.py          ← NEW — expanded stopwords API
│                               │   └── data/
│                               │       ├── __init__.py       ← NEW
│                               │       └── stopwords_expanded.json  ← NEW (245 stopwords)
├── pyproject.toml              ├── pyproject.toml            ← UPDATED (v1.1.0, new metadata)
├── README.md                   ├── README.md                 ← UPDATED (v1.1 features + data sources)
└── ...                         ├── CHANGELOG.md              ← NEW
                                └── UPGRADE_GUIDE.md          ← NEW (this file)
```

## Step-by-Step Merge

### 1. Copy your existing module code into the stubs

The `stemmer.py`, `stopwords.py`, and `normalizer.py` files in this package
are **stubs** with placeholder implementations. Replace them with your
actual v1.0.4 code:

```bash
# From your v1.0.4 repo:
cp v1.0.4/sindhinltk/stemmer.py    v1.1.0/sindhinltk/stemmer.py
cp v1.0.4/sindhinltk/stopwords.py  v1.1.0/sindhinltk/stopwords.py
cp v1.0.4/sindhinltk/normalizer.py v1.1.0/sindhinltk/normalizer.py
```

Also copy any other modules you have (sentiment engine, etc.):
```bash
cp v1.0.4/sindhinltk/sentiment.py  v1.1.0/sindhinltk/sentiment.py  # if exists
```

### 2. Keep these NEW files as-is

These are new in v1.1 and don't need modification:
- `sindhinltk/datasets.py` — the new datasets API
- `sindhinltk/data/stopwords_expanded.json` — 245 expanded stopwords
- `sindhinltk/data/__init__.py` — makes `data/` a package for file loading
- `CHANGELOG.md` — version history

### 3. Update __init__.py if you have extra modules

If your v1.0.4 has modules beyond stemmer/stopwords/normalizer
(like a sentiment module), add them to `__init__.py`:

```python
# In sindhinltk/__init__.py, add:
from sindhinltk import sentiment  # if you have this
```

### 4. Build and test locally

```bash
cd SindhiNLTK-v1.1/

# Install in dev mode
pip install -e .

# Test existing features still work
python -c "from sindhinltk import stemmer; print(stemmer.stem('ڪتابون'))"

# Test new features
python -c "from sindhinltk.datasets import get_stopwords_expanded; print(len(get_stopwords_expanded()))"

# Test category filtering
python -c "from sindhinltk.datasets import get_stopwords_by_category; print(get_stopwords_by_category('negation'))"
```

### 5. Build and publish to PyPI

```bash
# Build
pip install build twine
python -m build

# Check the package
twine check dist/*

# Upload to PyPI
twine upload dist/*
```

## Backward Compatibility

v1.1.0 is **fully backward compatible** with v1.0.4:
- `from sindhinltk import stemmer, stopwords, normalizer` — still works
- `stopwords.get_stopwords()` — returns the same original list
- All existing function signatures are preserved
- The new `datasets` module is additive only
