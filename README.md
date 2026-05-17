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