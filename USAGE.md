# 📚 SindhiNLTK: Comprehensive Usage Guide

This document outlines the API and usage of every module within the `sindhinltk` package. The toolkit is designed to be modular; you can use the unified pipeline or instantiate individual components for custom workflows.

## 1. The Master Pipeline (`SindhiNLP`)
The `SindhiNLP` class automatically chains the text processing tools in the optimal order: **Normalize ➔ Tokenize ➔ Remove Stopwords ➔ Stem ➔ Sentiment Analysis**.

```python
# test_all functions

from sindhinltk import SindhiNLP
from sindhinltk import (
    SindhiNLP, 
    SindhiTokenizer, 
    SindhiNormalizer, 
    SindhiStemmer, 
    SindhiStopwords, 
    SindhiSentiment
)

print("🚀 Starting SindhiNLTK Diagnostic Test...\n")

# 1. Test Normalizer
print("--- 1. Normalizer ---")
norm = SindhiNormalizer()
raw_text = "سنڌي      ٻولي\tآهي"
print(f"Raw:   {repr(raw_text)}")
print(f"Clean: {repr(norm.normalize(raw_text))}\n")

# 2. Test Tokenizer (The Shield)
print("--- 2. Tokenizer (V3 Shield) ---")
tok = SindhiTokenizer()
text = "گھوڙو ڊوڙي ٿو"
print(f"Input:  {text}")
print(f"Tokens: {tok.tokenize(text)}\n")

# 3. Test Stemmer
print("--- 3. Stemmer ---")
stemmer = SindhiStemmer()
word = "ڇوڪريون"
print(f"Word: {word} -> Root: {stemmer.stem(word)}\n")

# 4. Test Stopwords
print("--- 4. Stopwords ---")
sw = SindhiStopwords()
tokens = ["علي", "۽", "احمد", "۾", "آهن"]
print(f"Original: {tokens}")
print(f"Filtered: {sw.remove_stopwords(tokens)}\n")

# 5. Test Sentiment
print("--- 5. Sentiment Engine ---")
sent = SindhiSentiment()
good_text = "سنڌي ٻولي تمام مٺي آهي"
print(f"Text: {good_text}")
print(f"Result: {sent.analyze(good_text)}\n")

# 6. Test Full Pipeline
print("--- 6. Master Pipeline (SindhiNLP) ---")
nlp = SindhiNLP()
complex_text = "شاگردن کي ڪتابن مان گهڻو ڪجهه سکڻ گهرجي."
res = nlp.process(complex_text)
print(f"Original:  {res['original']}")
print(f"Tokens:    {res['tokens']}")
print(f"Stems:     {res['stems']}")
print(f"Sentiment: {res['sentiment']}\n")

print("✅ All modules executed successfully!")


nlp = SindhiNLP()
text = "سنڌي ٻولي تمام مٺي ۽ خوبصورت آهي"
result = nlp.process(text)

print(result['tokens'])    # ['سنڌي', 'ٻولي', 'تمام', 'مٺي', '۽', 'خوبصورت', 'آهي']
print(result['stems'])     # ['سنڌي', 'ٻول', 'تمام', 'مٺ', 'خوبصورت', 'آه'] 
print(result['sentiment']) # {'label': 'Positive', 'confidence': '98.5%'}
