import pandas as pd
import re

df = pd.read_csv('data/raw/bank_reviews.csv')
print(f"Original rows: {len(df)}")

df = df.dropna(subset=['review_text', 'rating'])
print(f"After dropping missing: {len(df)}")

df = df.drop_duplicates(subset=['review_text', 'bank'])
print(f"After removing duplicates: {len(df)}")

df['review_date'] = pd.to_datetime(df['review_date']).dt.strftime('%Y-%m-%d')
df['review_text'] = df['review_text'].str.strip()

df.to_csv('data/raw/bank_reviews_cleaned.csv', index=False)

print(f"\nCleaned data saved to data/raw/bank_reviews_cleaned.csv")
print(df['bank'].value_counts())