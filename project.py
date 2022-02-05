from flask import Flask
from flask_restful import Api, Resource
import requests, json


app = Flask(__name__)
api = Api(app)

api_key = "8d476f8333ac7d602c10abc6c10f76f8"
BASE = "http://api.openweathermap.org/data/2.5/weather?"
metric ="&units=metric"

@app.route('/')
def index():
    return {"firstname":"FATMA NUR", "lastname":"KILINC"}

@app.route('/temperature/city=<city>')
def temp(city):
    url = BASE + "appid=" + api_key + "&q=" + city + metric
    r = requests.get(url).json()
    temp = r["main"]["temp"]
    return {"temperature": temp}

if __name__ == "__main__":
    app.run(debug = True)



