Sure! Here’s the full updated README with that clearer phrasing:

---

 📊 Crypto Top Gainers & Losers API

A simple project to **fetch, store, and serve** Top Crypto Gainers & Losers from CoinGecko’s market data.
Built with **FastAPI** and **SQLite** for personal use, dashboards, or learning purposes.

---

 ⚡ Features

* Fetches **all market coins** from CoinGecko every 12 hours
* Stores historical market data in SQLite
* Provides a simple **REST API** to get:

  * ✅ Top gainers or losers in **Top 500 coins**
  * ✅ Top gainers or losers in **entire market**
  * ✅ Filter results by timeframe: `24h`, `7d`, `30d`, `1y`

---

 🗂 Project Structure

```
.
├── getdata.py           Data fetcher — fetches & stores market data snapshots
├── api.py               FastAPI server — serves gainers/losers endpoints
├── coins_snapshots.db   SQLite database (auto-generated)
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

* ✅ **Top 500 Gainers**
  `GET /top500/gainers?timeframe=24h&limit=10`

* ✅ **Global Losers (Entire Market)**
  `GET /global/losers?timeframe=7d&limit=5`

---

 ⏰ Automate Data Fetch with Cron

Edit your crontab:

```bash
crontab -e
```

Add this line to fetch every **12 hours**:

```bash
0 */12 * * * /usr/bin/python3 /path/to/getdata.py >> /path/to/cron.log 2>&1
```

> Replace `/path/to/` with your actual full path.

---

 📜 Disclaimer

This project uses **CoinGecko's free public API**, respecting their fair use policy.
It is intended for **personal, educational, or internal use only**.

> 🚫 If you plan to use this API **for commercial, production, or high-traffic purposes**,
> consider subscribing to **[CoinGecko Pro API](https://www.coingecko.com/en/api)** and reviewing their [API Terms of Service](https://www.coingecko.com/en/api_terms).

I am **not affiliated with CoinGecko**. Use at your own responsibility.



 ⭐ If you find this useful, please star the repo!

