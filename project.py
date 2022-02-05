from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Temperature(Resource):
    def get(self,city):
       return {city: "temperature"}

class Main(Resource):
    def get(self):
        return {"firstname": "FATMA NUR", "lastname": "KILINC"}

api.add_resource(Main,"/")
api.add_resource(Temperature,"/temperature/<string:city>")

if __name__ == "__main__":
    app.run(debug = True)


