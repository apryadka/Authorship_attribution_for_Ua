import pandas as pd
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from scripts.util.dir_path import DATA_CSV
from sklearn import pipeline
from sklearn.linear_model import LogisticRegression
from sklearn import metrics


data = pd.read_csv(f'{DATA_CSV}/preprocessed_data.csv')
print('Дані для векторизації')
print(data.head())

X = data.iloc[:, 0].values.astype('U')
Y = data.iloc[:, 1]

# SPLITTING THE TRAINING DATASET INTO TRAIN AND TEST
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, shuffle=True)

bow_vectorizer = CountVectorizer(ngram_range=(1, 2))
bow_train = bow_vectorizer.fit(X_train)
bow_train_vec = bow_vectorizer.fit_transform(X_train)
bow_test_vec = bow_vectorizer.fit_transform(X_test)
print(bow_test_vec)

tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf_train_vec = tfidf_vectorizer.fit_transform(X_train)
tfidf_test_vec = tfidf_vectorizer.fit_transform(X_test)
print(tfidf_test_vec)

pipe = pipeline.Pipeline(
    [('vec', tfidf_vectorizer), ('model', LogisticRegression())])
pipe.fit(X_train, y_train)
predict_val = pipe.predict(X_test)

print(metrics.accuracy_score(y_test, predict_val))
print(metrics.confusion_matrix(y_test, predict_val))

pipe1 = pipeline.Pipeline(
    [('vec', tfidf_vectorizer), ('model1', MultinomialNB())])
pipe1.fit(X_train, y_train)
predict_val1 = pipe1.predict(X_test)

print(metrics.accuracy_score(y_test, predict_val1))
print(metrics.confusion_matrix(y_test, predict_val1))

pipe2 = pipeline.Pipeline(
    [('vec', tfidf_vectorizer), ('model2', SVC())])
pipe2.fit(X_train, y_train)
predict_val2 = pipe2.predict(X_test)

print(metrics.accuracy_score(y_test, predict_val2))
print(metrics.confusion_matrix(y_test, predict_val2))