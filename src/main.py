from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
from os import environ
import json

app = Flask(__name__)

# pass headers and data to the function
@app.route('/')
def index():
  url = "https://localhost:3780/api/3/assets"
  app.config['user'] = environ.get('UNAME')  
  app.config['pass'] = environ.get('PASS') 

  res = requests.get(url,auth = HTTPBasicAuth(app.config['user'], app.config['pass'] ),verify=False)

  # json_data = json.loads(res.content)
  asset_data = res.json()

  return asset_data


if __name__ == '__main__':
   app.run(debug=True)	