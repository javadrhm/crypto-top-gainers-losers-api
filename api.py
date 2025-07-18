from fastapi import FastAPI, Query, HTTPException
import sqlite3

app = FastAPI()

MAX_LIMIT = 1000
DEFAULT_TOP_LIMIT = 500
DEFAULT_RESULT_LIMIT = 10
ALLOWED_TIMEFRAMES = {'24h', '7d', '30d', '1y'}

def query_db(query, params=()):
    conn = sqlite3.connect('coins_snapshots.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(query, params)
    results = [dict(row) for row in c.fetchall()]
    conn.close()
    return results

def get_change_field(timeframe: str):
    return {
        '24h': 'change_24h',
        '7d': 'change_7d',
        '30d': 'change_30d',
        '1y': 'change_1y'
    }.get(timeframe, 'change_24h')

def validate_timeframe(timeframe: str):
    if timeframe not in ALLOWED_TIMEFRAMES:
        raise HTTPException(status_code=400, detail=f"Invalid timeframe '{timeframe}'. Allowed: {ALLOWED_TIMEFRAMES}")

def validate_limit(limit: int):
    if limit < 1 or limit > MAX_LIMIT:
        raise HTTPException(status_code=400, detail=f"Limit must be between 1 and {MAX_LIMIT}")

@app.get("/topcoins/{action}")
def topcoins(
    action: str,
    timeframe: str = Query('24h'),
    top: int = Query(DEFAULT_TOP_LIMIT, description="Number of top coins by market cap to consider"),
    limit: int = Query(DEFAULT_RESULT_LIMIT, description="Number of results to return")
):
    # Validate inputs
    if action not in {'gainers', 'losers'}:
        raise HTTPException(status_code=400, detail="Action must be 'gainers' or 'losers'")
    validate_timeframe(timeframe)
    validate_limit(top)
    validate_limit(limit)

    change_field = get_change_field(timeframe)
    order = 'DESC' if action == 'gainers' else 'ASC'

    query = f"""
    WITH top_coins AS (
        SELECT *
        FROM snapshots
        WHERE snapshot_time = (SELECT MAX(snapshot_time) FROM snapshots)
        ORDER BY market_cap DESC
        LIMIT ?
    )
    SELECT id, symbol, name, price, {change_field} as change
    FROM top_coins
    ORDER BY change {order}
    LIMIT ?
    """

    return query_db(query, (top, limit))

@app.get("/global/{action}")
def global_top(
    action: str,
    timeframe: str = Query('24h'),
    limit: int = Query(DEFAULT_RESULT_LIMIT, description="Number of results to return")
):
    # Validate inputs
    if action not in {'gainers', 'losers'}:
        raise HTTPException(status_code=400, detail="Action must be 'gainers' or 'losers'")
    validate_timeframe(timeframe)
    validate_limit(limit)

    change_field = get_change_field(timeframe)
    order = 'DESC' if action == 'gainers' else 'ASC'

    query = f"""
    SELECT id, symbol, name, price, {change_field} as change
    FROM snapshots
    WHERE snapshot_time = (SELECT MAX(snapshot_time) FROM snapshots)
    ORDER BY change {order}
    LIMIT ?
    """

    return query_db(query, (limit,))

