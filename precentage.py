"""
בדיקת אחוזים של חיובי ושלילי כדי לדעת האם המנתח סנטימנט מדויק מספיק ביחס לנתונים
"""

import pandas as pd

# List of file paths
file_paths = [
    # r'C:\Users\User\PycharmProjects\pythonProject1\input_pn\cleaned_belif_polarity.xlsx',
    # r'C:\Users\User\PycharmProjects\pythonProject1\input_pn\cleaned_DRUNK_polarity.xlsx',
    # r'C:\Users\User\PycharmProjects\pythonProject1\input_pn\cleaned_laniege_polarity.xlsx',
     r'C:\Users\User\PycharmProjects\pythonProject1\input_pn\cleaned_origin_polarity.xlsx'
]

total_reviews = 0
total_positive_reviews = 0
total_negative_reviews = 0

# Iterate over each file
for file_path in file_paths:
    df = pd.read_excel(file_path)

    total_reviews += len(df)
    total_positive_reviews += len(df[df['polarity'] == 'P'])
    total_negative_reviews += len(df[df['polarity'] == 'N'])

# Calculate the percentage of positive and negative reviews
positive_percentage = (total_positive_reviews / total_reviews) * 100
negative_percentage = (total_negative_reviews / total_reviews) * 100


print(f"Positive Reviews: {positive_percentage:.2f}%")
print(f"Negative Reviews: {negative_percentage:.2f}%")
