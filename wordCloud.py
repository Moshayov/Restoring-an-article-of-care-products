import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# קריאת קובץ האקסל עם הנתונים הנקיים
cleaned_file_path = 'cleaned/cleaned_bleif.xlsx'
df = pd.read_excel(cleaned_file_path)

# החלפת ערכי NaN במחרוזות ריקות
df['Cleaned Verbatim'] = df['Cleaned Verbatim'].fillna('')

# איחוד כל השורות בעמודה "Cleaned Verbatim" לטקסט אחד
text = ' '.join(df['Cleaned Verbatim'].astype(str))

# יצירת ה-WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Greens').generate(text)

# הצגת ה-WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
