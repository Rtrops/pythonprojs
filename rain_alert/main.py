import requests

api_key = "0d936d79de6a910bd30a1518ec444966"
URL_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

# MY_LAT = 35.9606
# MY_LONG = -83.9207

weather_params = {
    "lat": 35.9606, # sahara 25.284266
    "lon": -83.9207,  #sahara 14.438434,
    "appid": api_key,
    "exclude": "current,daily,minutely"
}

r = requests.get(url=URL_ENDPOINT, params=weather_params)
r.raise_for_status
data = r.json()

hourly = [{"hour": item["dt"], "weather": item["weather"][0]["id"]} for item in data['hourly']]

# print(hourly)

for hour in hourly:
    if hour["weather"] < 700:
        print("Bring an umbrella")
        break
    
