import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Inputs
N = int(input())
train = [input() for _ in range(N)]

# Traning
clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', SVC())
])
clf.fit(train, np.arange(N))

# Predictions
input()
test = [input() for _ in range(N)]
preds = clf.predict(test)

for i in preds:
    print(i + 1)
