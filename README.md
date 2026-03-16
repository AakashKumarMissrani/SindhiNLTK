# 🛡️ SindhiNLTK: A Morphology-Aware NLP Toolkit

[![PyPI version](https://img.shields.io/pypi/v/sindhinltk.svg)](https://pypi.org/project/sindhinltk/)
[![Hugging Face Hub](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-SindhiNLTK-blue)](https://huggingface.co/aakashMeghwar01/SindhiNLTK)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**SindhiNLTK** is a high-performance Python library designed to address the "Linguistic Efficiency Gap" in Sindhi Language Processing. Standard multilingual models (like Llama-3 and mBERT) suffer from **Subword Shattering**, where unique Sindhi orthographic clusters are broken into semantically meaningless tokens. 

SindhiNLTK introduces a **V3 Linguistic Shield**—a hybrid Regex-BPE architecture—that protects the integrity of the 52-letter Sindhi alphabet, reducing the "Token Tax" significantly.

---

## 📊 Performance Benchmarks
Validated against a corpus of **43,784 SFT instruction samples**.

| Metric | Llama-3 (Meta) | SindhiNLTK (Ours) | Improvement |
| :--- | :--- | :--- | :--- |
| **Token Fertility Rate** | 4.15 | **1.06** | **291% More Efficient** |
| **Aspiration Integrity** | ~30% | **100% (Atomic)** | **Linguistic Accuracy** |
| **Context Window** | Baseline | **4x Larger** | **Memory Optimization** |

---

## 🚀 Key Features
* **Anti-Shatter Tokenizer**: Ensures aspirated digraphs (like گھ، جھ، کھ) remain as atomic units.
* **Neural Sentiment Engine**: Context-aware classification (Positive/Negative/Neutral).
* **Morphological Stemmer**: Advanced rule-based suffix stripping for Sindhi verb/noun forms.
* **Stopword Removal**: Curated list of high-frequency functional words.
* **NFKC Normalization**: Standardization for consistent Unicode processing.

---

## 💻 Installation & Quick Start

```bash
pip install sindhinltk
