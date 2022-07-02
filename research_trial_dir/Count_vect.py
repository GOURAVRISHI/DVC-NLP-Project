from sklearn.feature_extraction.text import CountVectorizer

# corpus = [
#     "zebra apple ball cat cat",
#     "ball cat dog elephant",
#     "very very unique"
# ]

corpus = [
    "apple ball cat",
    "ball cat dog elephant",
]

# below outcome is when n_gram = 3
# ['apple' 
# 'apple ball' 
# 'apple ball cat' 
# 'ball' 
# 'ball cat' 
# 'ball cat dog'    
# 'cat' 
# 'cat dog' 
# 'dog']

vectorizer = CountVectorizer()
X= vectorizer.fit_transform(corpus)
# print(X.toarray())
# print(vectorizer.get_feature_names_out())

max_features= 100   # number of words we want to consider
ngrams = 2  # tri gram 

vectorizer = CountVectorizer(max_features= max_features, ngram_range= (1, ngrams))
X= vectorizer.fit_transform(corpus)
print(X.toarray())
print(vectorizer.get_feature_names_out())