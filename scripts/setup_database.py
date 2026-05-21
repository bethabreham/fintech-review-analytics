import psycopg2
import pandas as pd

# Connection settings (change password to yours)
conn_params = {
    'host': 'localhost',
    'port': 5432,
    'user': 'postgres',
    'password': 'password123',  # CHANGE THIS to your password
    'database': 'postgres'
}

print("Step 1: Connecting to PostgreSQL...")
conn = psycopg2.connect(**conn_params)
conn.autocommit = True
cur = conn.cursor()

# Create database
print("Step 2: Creating database 'bank_reviews'...")
cur.execute("DROP DATABASE IF EXISTS bank_reviews")
cur.execute("CREATE DATABASE bank_reviews")

# Close connection
cur.close()
conn.close()

# Connect to new database
conn_params['database'] = 'bank_reviews'
conn = psycopg2.connect(**conn_params)
cur = conn.cursor()

# Create banks table
print("Step 3: Creating 'banks' table...")
cur.execute("""
    CREATE TABLE IF NOT EXISTS banks (
        bank_id SERIAL PRIMARY KEY,
        bank_name VARCHAR(100) UNIQUE NOT NULL,
        app_name VARCHAR(200)
    )
""")

# Create reviews table
print("Step 4: Creating 'reviews' table...")
cur.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        review_id SERIAL PRIMARY KEY,
        bank_id INTEGER REFERENCES banks(bank_id),
        review_text TEXT,
        rating INTEGER,
        review_date DATE,
        sentiment_label VARCHAR(10),
        sentiment_score FLOAT,
        source VARCHAR(50)
    )
""")
print("Tables created successfully!")

# Insert banks
print("Step 5: Inserting bank data...")
banks = [
    ("CBE", "Commercial Bank of Ethiopia Mobile"),
    ("BOA", "Bank of Abyssinia Mobile"),
    ("Dashen", "Dashen Bank Mobile")
]

for bank_name, app_name in banks:
    cur.execute("""
        INSERT INTO banks (bank_name, app_name) 
        VALUES (%s, %s) 
        ON CONFLICT (bank_name) DO NOTHING
    """, (bank_name, app_name))

conn.commit()
print("Banks inserted.")

# Load cleaned data
print("Step 6: Loading cleaned CSV...")
df = pd.read_csv('data/raw/bank_reviews_cleaned.csv')
print(f"Loaded {len(df)} reviews")

# Get bank_id mapping
cur.execute("SELECT bank_name, bank_id FROM banks")
bank_map = {name: id for name, id in cur.fetchall()}

# Insert reviews
print("Step 7: Inserting reviews into database...")
count = 0
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO reviews (bank_id, review_text, rating, review_date, source)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        bank_map[row['bank']],
        row['review_text'],
        row['rating'],
        row['review_date'],
        row['source']
    ))
    count += 1
    if count % 100 == 0:
        print(f"  Inserted {count} reviews...")

conn.commit()
print(f"Inserted {count} reviews successfully!")

# Verification queries
print("\n" + "="*50)
print("VERIFICATION QUERIES")
print("="*50)

# Count reviews per bank
cur.execute("""
    SELECT b.bank_name, COUNT(r.review_id) as review_count
    FROM reviews r
    JOIN banks b ON r.bank_id = b.bank_id
    GROUP BY b.bank_name
""")
print("\nReviews per bank:")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]}")

# Average rating per bank
cur.execute("""
    SELECT b.bank_name, AVG(r.rating) as avg_rating
    FROM reviews r
    JOIN banks b ON r.bank_id = b.bank_id
    GROUP BY b.bank_name
""")
print("\nAverage rating per bank:")
for row in cur.fetchall():
    print(f"  {row[0]}: {row[1]:.2f}")

# Check for nulls in key columns
cur.execute("""
    SELECT 
        COUNT(*) as total,
        SUM(CASE WHEN review_text IS NULL THEN 1 ELSE 0 END) as null_review_text,
        SUM(CASE WHEN rating IS NULL THEN 1 ELSE 0 END) as null_rating
    FROM reviews
""")
result = cur.fetchone()
print(f"\nData integrity:")
print(f"  Total reviews: {result[0]}")
print(f"  Null review_text: {result[1]}")
print(f"  Null rating: {result[2]}")

cur.close()
conn.close()
print("\n✅ Database setup complete!")