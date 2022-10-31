import requests
from requests_oauthlib import OAuth1
import pprint
from dotenv import load_dotenv
import os

pp = pprint.PrettyPrinter(indent=2, depth=2)

load_dotenv()

auth = OAuth1(os.environ['apikey'], os.environ['secretkey'])
endpoint = "http://api.thenounproject.com/icon/1"

response = requests.get(endpoint, auth=auth)
responseJSON = response.json()
pp.pprint(responseJSON)