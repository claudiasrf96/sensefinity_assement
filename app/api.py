import json
import os
import requests

connectionString = None
resultJson = None

def init() :
    global connectionString
    global resultJson
    print("\napi - init\n")

    cityId = input("Please insert the city ID you'd like to get weather for: ") 

    # Build connectiong string
    #default city id: 2267057
    connectionString = "https://api.openweathermap.org//data/2.5/weather?id="+cityId+"&units=metric&appid=244df0cbb2bcae2bca2fbe929ae3a613"
    r = requests.get(connectionString)
    resultJson = r.json()

def getInfo() :
    print("Temperature now in " + resultJson['name'] + " is " + str(resultJson['main']['temp']) + " Celsius")
    print("and if you look to the sky you see " + resultJson['weather'][0]['description'] )