from sklearn.metrics import confusion_matrix, accuracy_score, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, MaxPooling1D, GlobalMaxPooling1D, Dense, Dropout
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score



# פונקציה לעץ החלטה
def play_decision_tree(file_name):
    data = pd.read_excel(file_name)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['Cleaned Verbatim'])
    y = data['polarity']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)

    y_pred = dt.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred) * 100
    f1 = f1_score(y_test, y_pred, average='weighted')

    # מטריצת בלבול
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

    positive_predictions = tp
    negative_predictions = tn

    error_margin = 100 - accuracy

    return accuracy, f1, error_margin, positive_predictions, negative_predictions


# פונקציה ללמידה עמוקה
def play_deep_learning(file_name):
    data = pd.read_excel(file_name)
    data['polarity'] = data['polarity'].map({'P': 1, 'N': 0})

    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(data['Cleaned Verbatim'])
    X = tokenizer.texts_to_sequences(data['Cleaned Verbatim'])
    X = pad_sequences(X, maxlen=100)

    y = np.array(data['polarity'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = Sequential()
    model.add(Embedding(input_dim=5000, output_dim=128, input_length=100))
    model.add(Conv1D(filters=128, kernel_size=5, activation='relu'))
    model.add(MaxPooling1D(pool_size=5))
    model.add(Conv1D(filters=128, kernel_size=5, activation='relu'))
    model.add(GlobalMaxPooling1D())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, batch_size=32, epochs=5, validation_data=(X_test, y_test))

    loss, accuracy = model.evaluate(X_test, y_test)
    accuracy = accuracy * 100

    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5).astype(int)
    f1 = f1_score(y_test, y_pred)

    # מטריצת בלבול
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

    positive_predictions = tp
    negative_predictions = tn

    error_margin = 100 - accuracy

    return accuracy, f1, error_margin, positive_predictions, negative_predictions


def main():
    file_path = r'C:\Users\User\PycharmProjects\pythonProject1\input_pn\cleaned_belif_polarity.xlsx'  # דוגמה לנתיב קובץ

    # הרצת עץ החלטה
    dt_accuracy, dt_f1, dt_error_margin, dt_pos_pred, dt_neg_pred = play_decision_tree(file_path)

    # הרצת למידה עמוקה
    dl_accuracy, dl_f1, dl_error_margin, dl_pos_pred, dl_neg_pred = play_deep_learning(file_path)

    # הדפסת התוצאות עבור עץ החלטה
    print("Decision Tree Results:")
    print(f"Positive Predictions: {100*(dl_pos_pred/(dl_pos_pred+dl_neg_pred))}")
    print(f"Negative Predictions:  {100*(dl_neg_pred/(dl_pos_pred+dl_neg_pred))}")

    # הדפסת התוצאות עבור למידה עמוקה
    print("\nDeep Learning Results:")
    print(f"Positive Predictions: {100*(dl_pos_pred/(dl_pos_pred+dl_neg_pred))}")
    print(f"Negative Predictions: {100*(dl_neg_pred/(dl_pos_pred+dl_neg_pred))}")


if __name__ == "__main__":
    main()
