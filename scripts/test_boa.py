from google_play_scraper import reviews, Sort

package = "com.bankofabyssinia.abyssiniraemit"
print(f"Testing BOA package: {package}")

try:
    result, token = reviews(
        package,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=100
    )
    print(f"Reviews found: {len(result)}")
    if len(result) > 0:
        print(f"Sample: {result[0]['content'][:100]}")
except Exception as e:
    print(f"Error: {e}")