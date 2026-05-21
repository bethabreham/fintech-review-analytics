# Fintech Review Analytics

## Project Overview
Analysis of Google Play Store reviews for three Ethiopian banks: CBE, BOA, and Dashen.

## Setup Instructions

1. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
## Scraping Methodology

- **Library**: `google-play-scraper`
- **Target**: 400+ reviews per bank
- **Date range**: [INSERT DATE RANGE]
- **Package names used**:
  - CBE: `prod.cbe.birr`
  - BOA: `com.boa.apollo`
  - Dashen: `com.cr2.amolelight`

## Data Quality

- **Total reviews collected**: 1,215
- **CBE**: 380 reviews (20 short of 400 target)
- **BOA**: 430 reviews
- **Dashen**: 405 reviews

### Limitations
- CBE app has fewer available reviews (only 380)
- BOA required alternative package `com.boa.apollo` instead of primary
- All reviews are in mixed languages (English, Amharic)
## PostgreSQL Database Setup

1. Install PostgreSQL from https://www.postgresql.org/download/
2. Create database:
   ```sql
   CREATE DATABASE bank_reviews;
## PostgreSQL Database

### Setup
1. Install PostgreSQL
2. Create database: `CREATE DATABASE bank_reviews;`
3. Run schema: `python scripts/init_schema.py`
4. Insert data: `python scripts/setup_database.py`

### Verification Queries
```sql
-- Reviews per bank
SELECT b.bank_name, COUNT(r.review_id) 
FROM reviews r JOIN banks b ON r.bank_id = b.bank_id 
GROUP BY b.bank_name;

-- Average rating per bank
SELECT b.bank_name, AVG(r.rating) 
FROM reviews r JOIN banks b ON r.bank_id = b.bank_id 
GROUP BY b.bank_name;