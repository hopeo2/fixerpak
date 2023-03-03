import requests
import json

base_path = "https://api.apilayer.com/fixer/latest?base=usd&apikey="


def get_rates(api_key):
    response = requests.get(base_path + api_key)

    if response.status_code == 200:
        return json.loads(response.text)
    return None
