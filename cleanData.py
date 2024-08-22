import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords

# הורדת מילות עצירה
nltk.download('stopwords')

# רשימת מילות עצירה באנגלית
stop_words = set(stopwords.words('english'))

# פונקציה להסרת תווים שאינם אנגלית ואימוג'ים
def remove_non_english_and_emojis(text):
    # הסרת תווים שאינם באנגלית ואימוג'ים
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    return text

# פונקציה לניקוי הטקסט
def clean_text(text):
    if not isinstance(text, str):
        return ''
    # הסרת תווים שאינם באנגלית ואימוג'ים
    text = remove_non_english_and_emojis(text)
    # הסרת סימני פיסוק
    text = text.translate(str.maketrans('', '', string.punctuation))
    # המרת הטקסט לאותיות קטנות
    text = text.lower()
    # הסרת מילות עצירה
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]
    # חיבור המילים מחדש לטקסט נקי
    cleaned_text = ' '.join(cleaned_words)
    return cleaned_text

# קריאת קובץ האקסל
file_path = 'laniege database.xlsx'
df = pd.read_excel(file_path)

# ניקוי העמודה "Verbatim"
df['Cleaned Verbatim'] = df['Verbatim'].apply(clean_text)

# יצירת DataFrame חדש עם העמודה הנקייה בלבד
cleaned_df = df[['Cleaned Verbatim']]

# שמירת הנתונים הנקיים לקובץ אקסל חדש
cleaned_file_path = 'cleaned_laniege.xlsx'
cleaned_df.to_excel(cleaned_file_path, index=False)

print("ניקוי הנתונים הושלם ונשמר לקובץ החדש בהצלחה!")
