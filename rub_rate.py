import requests

def get_rub_rate():
    url = 'https://open.er-api.com/v6/latest/RUB'
    response = requests.get(url)
    data = response.json()
    
    rub_to_usd_rate = data['rates']['RUB']
    usd_to_cny_rate = data['rates']['CNY']
    
    rub_to_yuan_rate = rub_to_usd_rate / usd_to_cny_rate
    return round(rub_to_yuan_rate, 3)