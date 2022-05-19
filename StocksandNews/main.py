import requests
from datetime import datetime, date, timedelta
from metadata import acn
import time




API_KEY = "MUKAOF2LM1HGQ5QS"
api_url = 'https://www.alphavantage.co/query'


parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "ACN",
    "apikey": API_KEY
}

# stock = acn["Time Series (Daily)"]
# first_two = list(stock.items())[:2]

## first_two variable will fail if i go over the API limit. This block will try 5 times 
tries = 5
while tries > 0:
    r = requests.get(url=api_url, params=parameters)
    data = r.json()
    try:
        first_two = list(data["Time Series (Daily)"].items())[:2]
    except KeyError:
        print("...API failure. Retrying in 60 secs.")
        time.sleep(60)
        tries -= 1
    else:
        print("API Call Success.")
        break


last_businessday = float(first_two[0][1]["4. close"])
before_last = float(first_two[1][1]["4. close"])

diff = round(last_businessday - before_last, 3)
diff_percent = round((diff / last_businessday) * 100, 3)
if last_businessday > before_last:
    print(f"ACN is up by {diff}({diff_percent}%) from the previous stock price of {before_last}. Last Business Day is {last_businessday}")
else:
    print(f"ACN is down by {diff}({diff_percent}%) from the previous stock price of {before_last}")
