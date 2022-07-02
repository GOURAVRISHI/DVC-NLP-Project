# featurization stage

```python
from sklearn.feature_extraction.text import CountVectorizer


max_features= 100   # number of words we want to consider
ngrams = 2  # tri gram 

vectorizer = CountVectorizer(max_features= max_features, ngram_range= (1, ngrams))
X= vectorizer.fit_transform(corpus)
print(X.toarray())
print(vectorizer.get_feature_names_out())
```