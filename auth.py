import json
import certifi
import os
import ssl
import urllib
import urllib.error
import urllib.request
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

class Auth():
    def __init__(self) -> None:
        self.refresh_token = os.environ.get("REFRESH_TOKEN")
        self.access_token = ""
        self.uuid = ""

    def _get_access_token(self):
        if self.refresh_token == "":
            print("Failed, please set 'REFRESH_TOKEN' on the `.env` file")
            return
        
        context = ssl.create_default_context(cafile=certifi.where())
        access_url = "https://platform-api.bocco.me/oauth/token/refresh"
        req_header = {
            'Content-Type': 'application/json',
        }
        req_data = json.dumps({
        'refresh_token': self.refresh_token
        })
        req = urllib.request.Request(url=access_url, data=req_data.encode(), method='POST', headers=req_header)
        try:
            with urllib.request.urlopen(req, context=context) as response:
                body = json.loads(response.read())
                print("--- Got Access Token ---")
                return body["access_token"]

        except urllib.error.URLError as error:
            print(error.reason)
            
    def _get_uuid(self):
        if self.access_token == "":
            self.access_token = self._get_access_token()
        context = ssl.create_default_context(cafile=certifi.where())
        uuid_url = "https://platform-api.bocco.me/v1/rooms"
        header = {
            'Authorization': 'Bearer ' + self.access_token
        }
        req = urllib.request.Request(url=uuid_url, headers=header)
        try:
            with urllib.request.urlopen(req, context=context) as response:
                body = json.loads(response.read())
                print("--- Got Room UUID ---")
                return body["rooms"][0]["uuid"]
        except urllib.error.URLError as error:
            print(error.reason)
            
    def update_token(self):
        self.access_token = self._get_access_token()
        self.uuid = self._get_uuid()
            


