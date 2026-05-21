# Fintech Review Analytics

## Project Overview
Analysis of Google Play Store reviews for three Ethiopian banks: CBE, BOA, and Dashen. Scrapes reviews, performs sentiment analysis, extracts themes, and stores data in PostgreSQL.

## Scraping Methodology
- Library: google-play-scraper
- Target: 400+ reviews per bank
- Date range: May 2026
- Package names used:
  - CBE: prod.cbe.birr
  - BOA: com.boa.apollo
  - Dashen: com.cr2.amolelight

## Data Quality
- Total reviews collected: 1,215
- CBE: 380 reviews (20 short of 400 target)
- BOA: 430 reviews
- Dashen: 405 reviews
- Missing data: 0%
- Duplicates removed: 200+

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/bethabreham/fintech-review-analytics.git
   cd fintech-review-analytics

2. Create and activate virtual environment:
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run scraper:
   python scripts/scrape_reviews.py

5. Run preprocessing:
   python scripts/preprocess_reviews.py

6. Run sentiment analysis:
   python scripts/sentiment_analysis.py

## PostgreSQL Database

### Setup
1. Install PostgreSQL from https://www.postgresql.org/download/
2. Create database: CREATE DATABASE bank_reviews;
3. Run schema: python scripts/init_schema.py
4. Insert data: python scripts/setup_database.py

### Schema Design

banks table:
- bank_id: SERIAL PRIMARY KEY
- bank_name: VARCHAR(100) UNIQUE NOT NULL
- app_name: VARCHAR(200)

reviews table:
- review_id: SERIAL PRIMARY KEY
- bank_id: INTEGER FOREIGN KEY (references banks)
- review_text: TEXT
- rating: INTEGER
- review_date: DATE
- source: VARCHAR(50)

### Verification Queries

-- Count reviews per bank

SELECT b.bank_name, COUNT(r.review_id) as review_count

FROM reviews r JOIN banks b ON r.bank_id = b.bank_id 

GROUP BY b.bank_name;

-- Average rating per bank

SELECT b.bank_name, AVG(r.rating) as avg_rating

FROM reviews r JOIN banks b ON r.bank_id = b.bank_id 

GROUP BY b.bank_name;

## Key Findings

### Sentiment by Bank
| Bank | Positive | Neutral | Negative |
|------|----------|---------|----------|
| CBE | 42% | 28% | 30% |
| BOA | 38% | 32% | 30% |
| Dashen | 45% | 25% | 30% |

### Themes per Bank
| Bank | Primary Theme | Top Keywords |
|------|---------------|--------------|
| CBE | Login & Performance Issues | login, password, slow, error |
| BOA | Transaction Problems | failed, OTP, verification, pending |
| Dashen | Features & Stability | fingerprint, fast, crash, freeze |

## Recommendations

### CBE
- Optimize login flow (reduce steps, add biometric option)
- Improve app loading speed

### BOA
- Fix OTP delivery system
- Add retry mechanism for failed transactions

### Dashen
- Prioritize stability fixes (crash bugs)
- Promote fingerprint login feature

## Project Structure

fintech-review-analytics/

├── .github/workflows/

│   └── unittests.yml

├── .vscode/

│   └── settings.json

├── data/

│   └── raw/

├── notebooks/

├── scripts/

├── src/

├── tests/

├── .gitignore

├── requirements.txt

└── README.md

## CI/CD
GitHub Actions runs tests on every push to main branch.

## Dependencies
- pandas, numpy, matplotlib, seaborn
- google-play-scraper
- textblob, transformers
- psycopg2-binary, sqlalchemy
- pytest

## Limitations
- CBE had only 380 reviews (20 short of 400 target)
- Reviews in mixed languages (English and Amharic)
- Sentiment scores not yet added to PostgreSQL

## Author
Beth Abraham - 10 Academy KAIM 9 Cohort

## License
This project is for educational purposes as part of the 10 Academy training program.
