from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, MaxPooling1D, GlobalMaxPooling1D, Dense, Dropout
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import f1_score


def play(file_name):
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

    error_margin = 100 - accuracy

    return accuracy, f1, error_margin

# try