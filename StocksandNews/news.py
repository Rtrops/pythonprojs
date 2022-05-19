import requests


params = {
    "q": "accenture",
    "domains": "reuters.com",
    "apiKey": "c92fd66afd534d74bb7f173522d588f7"    
}
r = requests.get(url="https://newsapi.org/v2/everything", params=params)
r.raise_for_status()

data = r.json()


print(data)
