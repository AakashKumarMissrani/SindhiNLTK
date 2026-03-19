# SindhiNLTK User Guide  
**Natural Language Toolkit for Sindhi Language**  
**Version:** 1.3.1 (latest stable – March 2025)  
**Author:** Aakash Meghwar  
**License:** MIT  
**PyPI:** https://pypi.org/project/sindhinltk/  
**GitHub:** https://github.com/AakashKumarMissrani/SindhiNLTK  

## 1. Installation

```bash
pip install sindhinltk
```
 ## 2. Quick Start – All Modules in 30 seconds
```
 from sindhinltk import *

text = "سنڌ جي حڪومت ڪاوڙيندڙ ٻارن کي مدد ڪندي."

# Tokenization
tokens = SindhiTokenizer().tokenize(text)
sents  = SindhiTokenizer().sent_tokenize(text + " ٻيو جملو۔")

# Normalization
clean  = SindhiNormalizer().normalize(text, remove_diacritics=True)

# Stemming
root   = SindhiStemmer().stem("ڪاوڙيندڙ")
stemmed_list = SindhiStemmer().stem_tokens(tokens)

# Stopwords
filtered = SindhiStopwords().remove_stopwords(tokens)
is_stop  = SindhiStopwords().is_stopword("کي")

# Sentiment (lexicon-based)
score    = SindhiSentiment().analyze(text)   # مثبت / منفی / غير جانبدار

print(tokens, sents, clean, root, score)
```
## 3. Module Overview & Main Methods
```
Module,Class,Main Methods,Purpose

```
## 4.Fertility Check (Tokenizer Quality)

```
text = """[paste long Sindhi text here – 200+ words recommended]"""
tokens = SindhiTokenizer().tokenize(text)
words = text.split()
fertility = len(tokens) / max(1, len(words))
print(f"Fertility: {fertility:.2f}")   # Target: 1.30–1.45 on real text

```
## 5. Full Pipeline Example
```
from sindhinltk import *

text = "سنڌ جي خوبصورت زمين سنڌو درياھ جي وهڪري سبب آباد آهي۔"

tok = SindhiTokenizer()
norm = SindhiNormalizer()
stm = SindhiStemmer()
sw = SindhiStopwords()
sa = SindhiSentiment()

clean_text = norm.normalize(text, remove_diacritics=True)
tokens = tok.tokenize(clean_text)
filtered = sw.remove_stopwords(tokens)
stemmed = stm.stem_tokens(filtered)
sentiment = sa.analyze(text)

print("Clean:", clean_text)
print("Tokens:", tokens)
print("Filtered:", filtered)
print("Stemmed:", stemmed)
print("Sentiment:", sentiment)
```
## 6. Best Practices
```
Normalize before stemming/sentiment
Use remove_diacritics=True for web/social text
Test fertility on real varied Sindhi content (news, Wikipedia, books)
Sentiment is basic lexicon method — not contextual
```
