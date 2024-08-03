# auth周り
import os
from os.path import dirname, join

from dotenv import load_dotenv
from api_query import ApiQuery

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

class Auth:
    def __init__(self) -> None:
        self.refresh_token = os.environ.get("REFRESH_TOKEN")
        self.access_token = ""
        self.uuid = ""
        self.api = ApiQuery()

    # アクセストークン取得
    def _get_access_token(self) -> str:
        if self.refresh_token == "":
            print("Failed, please set 'REFRESH_TOKEN' on the `.env` file")
            return 
        end_point = "/oauth/token/refresh"
        req_header = {
            'Content-Type': 'application/json',
        }
        req_data = {
        'refresh_token': self.refresh_token
        }
        body = self.api.post(data=req_data, end_point=end_point, headers=req_header)
        if body != {}:
            return body["access_token"]
            
    # uuid取得
    def _get_uuid(self) -> str:
        if self.access_token == "":
            self.access_token = self._get_access_token()
        end_point = "/v1/rooms"
        header = {
            'Authorization': 'Bearer ' + self.access_token
        }
        body = self.api.get(end_point=end_point, headers=header)
        if body != {}:
            return body["rooms"][0]["uuid"]
    
    # アクセストークンのアップデート
    def update_token(self):
        self.access_token = self._get_access_token()
        self.uuid = self._get_uuid()
            


