from google_play_scraper import reviews, Sort
import pandas as pd
import time

apps = {
    "CBE": "prod.cbe.birr",
    "BOA": "com.boa.apollo",
    "Dashen": "com.cr2.amolelight"
}

all_reviews = []

for bank, package_name in apps.items():
    print(f"Scraping {bank} ({package_name})...")
    try:
        result, token = reviews(
            package_name,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=500
        )
        
        print(f"  Collected {len(result)} raw reviews")
        
        for review in result:
            all_reviews.append({
                'bank': bank,
                'review_text': review['content'],
                'rating': review['score'],
                'review_date': review['at'].date(),
                'source': 'Google Play'
            })
        
        print(f"  Added {len(result)} reviews for {bank}")
        time.sleep(2)
        
    except Exception as e:
        print(f"  Error scraping {bank}: {e}")

if len(all_reviews) == 0:
    print("No reviews collected. Check package names or internet connection.")
else:
    df = pd.DataFrame(all_reviews)
    df = df.drop_duplicates(subset=['review_text', 'bank'])
    df.to_csv('data/raw/bank_reviews.csv', index=False)
    print(f"\nTotal reviews saved: {len(df)}")
    print(df['bank'].value_counts())