import sqlite3
import requests
import time
from datetime import datetime

conn = sqlite3.connect('coins_snapshots.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS snapshots (
    id TEXT,
    symbol TEXT,
    name TEXT,
    market_cap REAL,
    price REAL,
    change_24h REAL,
    change_7d REAL,
    change_30d REAL,
    change_1y REAL,
    snapshot_time TEXT
)''')

def fetch_all_coins():
    # Delete all previous snapshots to keep only the latest data
    c.execute("DELETE FROM snapshots")
    conn.commit()

    page = 1
    snapshot_time = datetime.utcnow().isoformat()

    while True:
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 250,
            "page": page,
            "price_change_percentage": "7d,30d,1y"
        }

        try:
            response = requests.get("https://api.coingecko.com/api/v3/coins/markets", params=params)
            if response.status_code == 429:
                print("Rate limit hit. Waiting 60s...")
                time.sleep(60)
                continue
            response.raise_for_status()

            data = response.json()
            if not data:
                print("No more data. Finished.")
                break

            for coin in data:
                c.execute('''INSERT INTO snapshots VALUES (?,?,?,?,?,?,?,?,?,?)''', (
                    coin['id'],
                    coin['symbol'],
                    coin['name'],
                    coin.get('market_cap') or 0,
                    coin.get('current_price') or 0,
                    coin.get('price_change_percentage_24h') or 0,
                    coin.get('price_change_percentage_7d_in_currency') or 0,
                    coin.get('price_change_percentage_30d_in_currency') or 0,
                    coin.get('price_change_percentage_1y_in_currency') or 0,
                    snapshot_time
                ))

            print(f"Saved page {page} with {len(data)} coins.")
            page += 1
            time.sleep(1.5)  # Respect rate limit

        except Exception as e:
            print(f"Error on page {page}: {e}")
            time.sleep(10)  # Wait before retry

    conn.commit()

fetch_all_coins()
conn.close()

