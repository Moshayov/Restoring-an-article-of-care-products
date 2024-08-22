import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, f1_score


def play(file_name):
    data = pd.read_excel(file_name)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['Cleaned Verbatim'])
    y = data['polarity']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    svm = SVC(kernel='linear')
    svm.fit(X_train, y_train)

    y_pred = svm.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred) * 100
    f1 = f1_score(y_test, y_pred, average='weighted')
    error_margin = 100 - accuracy

    return accuracy, f1, error_margin
