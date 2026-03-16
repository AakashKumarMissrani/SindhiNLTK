# 📚 SindhiNLTK: Comprehensive Usage Guide

This document outlines the API and usage of every module within the `sindhinltk` package. The toolkit is designed to be modular; you can use the unified pipeline or instantiate individual components for custom workflows.

## 1. The Master Pipeline (`SindhiNLP`)
The `SindhiNLP` class automatically chains the text processing tools in the optimal order: **Normalize ➔ Tokenize ➔ Remove Stopwords ➔ Stem ➔ Sentiment Analysis**.

```python
from sindhinltk import SindhiNLP

nlp = SindhiNLP()
text = "سنڌي ٻولي تمام مٺي ۽ خوبصورت آهي"
result = nlp.process(text)

print(result['tokens'])    # ['سنڌي', 'ٻولي', 'تمام', 'مٺي', '۽', 'خوبصورت', 'آهي']
print(result['stems'])     # ['سنڌي', 'ٻول', 'تمام', 'مٺ', 'خوبصورت', 'آه'] 
print(result['sentiment']) # {'label': 'Positive', 'confidence': '98.5%'}
