from flask import Flask
from flask_restful import Resource, Api
import json
  

f = open('airport.json')
app = Flask("VAPI")
api = Api(app)
data = json.load(f)
class AirIATA(Resource):

    def get(self, city, country=None):
        for i in data:
            if i['city']==city and (country is None or i['country'] == country):
                return i['IATA']
        return "check the city and country name"
api.add_resource(AirIATA, '/IATA/<city>','/IATA/<city>/<country>')


if __name__ == "__main__":
    app.run()