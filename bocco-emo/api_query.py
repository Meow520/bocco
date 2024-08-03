# APIのやり取り
import urllib.error
import certifi
import json
import ssl
import urllib
import urllib.request

class ApiQuery:
    def __init__(self) -> None:
        self.base_url = "https://platform-api.bocco.me"
        self.ctx = ssl.create_default_context(cafile=certifi.where())
    
    # GET
    def get(self, end_point:str, headers:dict) -> dict:
        url = self.base_url + end_point
        req = urllib.request.Request(url=url, headers=headers, method="GET")
        try:
            with urllib.request.urlopen(req, context=self.ctx) as res:
                body = json.loads(res.read())
                return body
        except urllib.error.HTTPError as e:
            print(e.code)
            return {}
        except urllib.error.URLError as e:
            print(e.reason)
            return {}
    
    # POST
    def post(self, data:dict, end_point:str, headers:dict) -> dict:
        url = self.base_url + end_point
        req_data = json.dumps(data)
        req = urllib.request.Request(url=url, headers=headers, data=req_data.encode(), method="POST")
        try:
            with urllib.request.urlopen(req, context=self.ctx) as res:
                body = json.loads(res.read())
                return body
        except urllib.error.HTTPError as e:
            print(e.code)
            return {}
        except urllib.error.URLError as e:
            print(e.reason)
            return {}
    
    #　PUT 
    def put(self, data:dict, end_point:str, headers:dict) -> dict:
        url = self.base_url + end_point
        req_data = json.dumps(data)
        req = urllib.request.Request(url=url, headers=headers, data = req_data.encode(), method="PUT")
        try:
            with urllib.request.urlopen(req, context=self.ctx) as res:
                body = json.loads(res.read())
                return body
        except urllib.error.HTTPError as e:
            print(e.code)
            return {}
        except urllib.error.URLError as e:
            print(e.reason)
            return {}
