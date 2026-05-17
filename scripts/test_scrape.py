from google_play_scraper import reviews, Sort

package = "prod.cbe.birr"
print(f"Testing: {package}")

try:
    result, token = reviews(
        package,
        lang='en',
        country='us',
        sort=Sort.NEWEST,
        count=100
    )
    print(f"Number of reviews collected: {len(result)}")
    if len(result) > 0:
        print(f"First review: {result[0]['content'][:100]}")
except Exception as e:
    print(f"Error: {e}")