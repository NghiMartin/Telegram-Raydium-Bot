import requests

def handle_baseURL(pool_Type, page_Size, page_Index):
    return f'https://api-v3.raydium.io/pools/info/list?poolType={pool_Type}&poolSortField=default&sortType=desc&pageSize={page_Size}&page={page_Index}'

def get_pool_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching pool data: {e}")
        return None

def format_number(value, decimals=0):
    if decimals == 0:
        return f"{round(value):,}"
    else:
        return f"{value:,.{decimals}f}"

def extract_pool_details(pool_data, title):
    pools = pool_data['data']['data']
    pool_details = [title]

    for pool in pools:
        mintA_symbol = pool['mintA']['symbol']
        mintB_symbol = pool['mintB']['symbol']
  
        pool_id = pool.get("id")

        tvl = pool['tvl']
        volume = pool['day']['volume']
        volume_fee = pool['day']['volumeFee']
        apr = pool['day']['apr']

        details = f"""🔄 {mintA_symbol} ↔️ {mintB_symbol}
        🌊 Liquidity: ${format_number(tvl)} 💰
        📈 24h Volume: ${format_number(volume)} 💰
        💵 24h Fee: ${format_number(volume_fee)}
        📅 24h APR: {format_number(apr, 2)}%
        🔗 [Add liquidity to this pool](https://raydium.io/liquidity/increase/?mode=add&pool_id={pool_id})
        """
        pool_details.append(details)
    return pool_details
