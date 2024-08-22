import pandas as pd
from textblob import TextBlob
# המסווג שהוחלט בסוף שנשתמש בו

# Load the Excel file
file_path = 'cleaned_laniege.xlsx'
df = pd.read_excel(file_path)

# Function to determine sentiment polarity
def get_polarity(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'P'  # Positive
    else:
        return 'N'  # Negative or Neutral

# Remove rows with non-string values in 'Cleaned Verbatim'
df = df[df['Cleaned Verbatim'].apply(lambda x: isinstance(x, str))]

# Apply the function to the 'Cleaned Verbatim' column
df['polarity'] = df['Cleaned Verbatim'].apply(get_polarity)

# Save the updated dataframe to a new Excel file
output_path = 'cleaned_laniege_polarity.xlsx'
df.to_excel(output_path, index=False)
