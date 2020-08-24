from flask import Flask,jsonify
import json
import requests

app=Flask(__name__)

@app.route('/')
def index():
    return "Welcome to your local host"

@app.route("/weather/city/<int:city_id>", methods=['GET'])
def get_city(city_id):
    connectionString = "https://api.openweathermap.org//data/2.5/weather?id="+str(city_id)+"&units=metric&appid=244df0cbb2bcae2bca2fbe929ae3a613"
    return requests.get(connectionString).json()

    #http://localhost:5656

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5656)