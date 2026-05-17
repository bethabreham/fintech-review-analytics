from google_play_scraper import search

banks = ["Commercial Bank of Ethiopia", "Bank of Abyssinia", "Dashen Bank"]

for bank in banks:
    print(f"\nSearching for: {bank}")
    try:
        results = search(bank, n_hits=3)
        for app in results:
            print(f"  Name: {app['title']}")
            print(f"  Package: {app['appId']}")
            print(f"  Rating: {app['score']}")
    except Exception as e:
        print(f"  Error: {e}")