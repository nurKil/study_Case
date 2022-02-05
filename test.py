import requests, json

city = 'ankara'
api_key = "8d476f8333ac7d602c10abc6c10f76f8"
metric ="&units=metric"
BASE = "http://api.openweathermap.org/data/2.5/weather?"
url = BASE + "appid=" + api_key + "&q=" + city + metric
r = requests.get(url).json()
temp = r["main"]["temp"]
print(temp)

