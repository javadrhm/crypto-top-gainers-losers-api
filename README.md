📊 Crypto Top Gainers & Losers API

A simple project to **fetch, store, and serve** Top Crypto Gainers & Losers from CoinGecko’s market data.
Built with **FastAPI** and **SQLite** for personal use, dashboards, or learning purposes.

---

 ⚡ Features

* Fetches **all market coins** from CoinGecko every 12 hours
* Stores historical market data snapshots in SQLite
* Provides a simple **REST API** to get:

  * ✅ Top gainers or losers in a configurable number of **Top N coins by market cap** (default 500)
  * ✅ Top gainers or losers in the **entire market**
  * ✅ Filter results by timeframe:

    * `24h` (24 hours)
    * `7d` (7 days)
    * `30d` (30 days)
    * `1y` (1 year)

---

 🗂 Project Structure

```
.
├── getdata.py            Data fetcher — fetches & stores market data snapshots
├── api.py                FastAPI server — serves gainers/losers endpoints
├── coins_snapshots.db    SQLite database (auto-generated)
├── requirements.txt
├── README.md
```

---

 🛠 Setup

```bash
git clone https://github.com/yourusername/crypto-top-gainers-losers-api.git
cd crypto-top-gainers-losers-api

pip install -r requirements.txt
```

---

 🚀 Usage

 1️⃣ Fetch Data Manually

```bash
python3 getdata.py
```

 2️⃣ Run API Server

```bash
uvicorn api:app --reload --port 8000
```

---

 📝 Example API Calls

 Top N coins by market cap gainers/losers:

```http
GET /topcoins/gainers?top=500&limit=10&timeframe=7d
```

* `top` = how many top coins by market cap to consider (max 1000, default 500)
* `limit` = how many results to return (default 10)
* `timeframe` = one of `24h`, `7d`, `30d`, `1y`

 Global (entire market) gainers/losers:

```http
GET /global/losers?limit=20&timeframe=30d
```

* `limit` = how many results to return (default 10)
* `timeframe` = one of `24h`, `7d`, `30d`, `1y`

---

 ⏰ Automate Data Fetch with Cron

Edit your crontab:

```bash
crontab -e
```

Add this line to fetch every **12 hours**:

```bash
0 */12 * * * /usr/bin/python3 /full/path/to/getdata.py >> /full/path/to/cron.log 2>&1
```

> Replace `/full/path/to/` with your actual full paths.

---

 📜 Disclaimer

This project uses **CoinGecko's free public API**, respecting their fair use policy.
It is intended for **personal, educational, or internal use only**.

> 🚫 If you plan to use this API **for commercial, production, or high-traffic purposes**,
> consider subscribing to **[CoinGecko Pro API](https://www.coingecko.com/en/api)** and reviewing their [API Terms of Service](https://www.coingecko.com/en/api_terms).

I am **not affiliated with CoinGecko**. Use at your own responsibility.

---

⭐ If you find this useful, please star the repo!

