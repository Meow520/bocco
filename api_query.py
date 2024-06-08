import urllib.error
import certifi
import json
import ssl
import urllib
import urllib.request

class ApiQuery():
    def __init__(self) -> None:
        self.base_url = "https://platform-api.bocco.me"
        self.ctx = ssl.create_default_context(cafile=certifi.where())
        
    def request(self, end_point:str, headers: dict) -> dict:
        url = self.base_url + end_point
        req = urllib.request.Request(url=url, headers=headers)
        try:
            with urllib.request.urlopen(req, context=self.ctx) as res:
                body = json.loads(res.read())
                return body
        except urllib.error.URLError as e:
            print(e.reason)
            return {}
    
    def get(self, end_point:str, headers:dict) -> dict:
        url = self.base_url + end_point
        req = urllib.request.Request(url=url, headers=headers)
        try:
            with urllib.request.urlopen(req, context=self.ctx) as res:
                body = json.loads(res.read())
                return body
        except urllib.error.URLError as e:
            print(e.reason)
            return {}
    
    def post(self, data:dict, end_point:str, headers:dict) -> dict:
        url = self.base_url + end_point
        req = urllib.request.Request(url=url, headers=headers, data=data.encode(), method='POST')
        try:
            with urllib.request.urlopen(req, context=self.ctx) as res:
                body = json.loads(res.read())
                return body
        except urllib.error.URLError as e:
            print(e.reason)
            return {}