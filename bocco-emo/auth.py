# auth周り
import os
import time
from os.path import dirname, join
from typing import Tuple

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
        self.update_timestamp = 0.0

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
            
    # 部屋のuuid取得
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
    def _update_token(self) -> Tuple[str, str]:
        new_access_token = self._get_access_token()
        self.access_token = new_access_token
        new_uuid = self._get_uuid()
        self.uuid = new_uuid
        self.update_timestamp = time.time()
        return new_access_token, new_uuid
    
    # トークンの期限を確認して必要であればアップデートする
    def check_expired(self) -> Tuple[str, str]:
        ut = time.time()
        if ut - self.update_timestamp >= 3600:
            new_access_token, new_uuid = self._update_token()
        else:
            new_access_token, new_uuid = self.access_token, self._get_uuid()
        return new_access_token, new_uuid
            


