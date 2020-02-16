# we import the Twilio client from the dependency we just installed
from twilio.rest import Client
from config import config

# the following line needs your Twilio Account SID and Auth Token
client = Client(config[0], config[1])

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+18656845102", from_="+19177461747", body="Hi Dad")
