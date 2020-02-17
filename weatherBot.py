# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
from config import *
import requests
import json
import os

url = "https://community-open-weather-map.p.rapidapi.com/weather"
querystring = {"lat":"35.9606","lon":"83.9207","units":"%22imperial%22","q":"knoxville"}

headers = {
    'x-rapidapi-host': os.environ.get("hiddenWeather"),
    'x-rapidapi-key': os.environ.get("hiddenWeatherSecret")
    }

responseJson = requests.request("GET", url, headers=headers, params=querystring)
response = json.loads(responseJson.text)

print(response)
#response["main"] = "Drizzle"
if (response["main"] in ["Drizzle", "Rain", "Snow", "Thunderstorm"]):

	# the following line needs your Twilio Account SID and Auth Token
	client = Client(os.environ.get("hiddenText"), os.environ.get("hiddenTextSecret"))

	# change the "from_" number to your Twilio number and the "to" number
	# to the phone number you signed up for Twilio with, or upgrade your
	# account to send SMS to any phone number
	client.messages.create(to=os.environ.get("phoneTo"), from_=os.environ.get("phoneFrom"), body=response["weather"][0]["description"])
	print(response)
	print(response["weather"][0]["description"])



