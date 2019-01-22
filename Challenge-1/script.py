import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline


# Reading the data
texts = open('training.txt', 'r', encoding='utf-8').readlines()[1:]
targets = [t.split('\t')[1].strip() for t in texts]
texts = [t.split('\t')[0].strip() for t in texts]


# Remove punctuations and other symbols
def remove_punc(text):
    clean_text = re.sub(r'[?|!|\'|"|#|.|,|)|(|\|/]', r' ', text)
    clean_text = clean_text.replace('\n', ' ')
    return clean_text.strip()


# Remove non-alpha numeric words
def remove_nonalpha(text):
    pat = re.compile('[\W_]+')
    clean_text = ' '.join(pat.sub('', word) for word in text.split())
    return clean_text.strip()


def clean_up(text):
    text = remove_punc(text.lower())
    text = remove_nonalpha(text)
    text = ' '.join(text.split())
    return text


# Clean up
texts = np.array([clean_up(t) for t in texts])
targets = np.array(targets)

# ML Pipeline
pline = Pipeline([
    ('tffidf', TfidfVectorizer(strip_accents='unicode',
                               ngram_range=(1, 1), stop_words='english')),
    ('svc', SVC(C=0.8, kernel='linear', class_weight='balanced'))
])
# Training
pline.fit(texts, targets)


# Testing
test_texts = []
for i in range(int(input())):
    txt = input()
    test_texts.append(clean_up(txt))

test_preds = pline.predict(test_texts)
for pred in test_preds:
    print(pred)
