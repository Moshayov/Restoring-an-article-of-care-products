# בדיקה של מסווגים שונים כדי לדעת איזה מהם הוא הכי טוב עבורנו


import pandas as pd
from flair.models import TextClassifier
from flair.data import Sentence

# קריאת הקובץ
file_path = 'cleaned/cleaned_laniege.xlsx'
df = pd.read_excel(file_path)

# טעינת מסווג הסנטימנט
classifier = TextClassifier.load('en-sentiment')

# פונקציה לניתוח סנטימנט
def get_sentiment(text):
    if isinstance(text, str):
        sentence = Sentence(text)
        classifier.predict(sentence)
        label = sentence.labels[0].value
        return 'Positive' if label == 'POSITIVE' else 'Negative'
    else:
        return 'Negative'

# המרת כל הערכים למחרוזות
df['Cleaned Verbatim'] = df['Cleaned Verbatim'].astype(str)

# הוספת עמודת סנטימנט
df['Sentiment'] = df['Cleaned Verbatim'].apply(get_sentiment)

# הצגת התוצאות
print(df)

# שמירת התוצאות לקובץ אקסל חדש
output_path = 'sentiment_analysis_results_flair.xlsx'
df.to_excel(output_path, index=False)
