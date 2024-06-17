from api_query import ApiQuery

import datetime

class BoccoTools:
    def __init__(self, uuid:str, access_token:str) -> None:
        self.uuid = uuid
        self.access_token = access_token
        self.api = ApiQuery()
        self.message = {}
        
    def get_speech(self) -> str:
        end_point = "/v1/rooms/"+self.uuid+"/messages"
        header = {
            'Authorization': 'Bearer ' + self.access_token
        }
        body = self.api.get(end_point=end_point, headers=header)
        if body == {}:
            return
        
        dt_now = datetime.datetime.now(datetime.timezone.utc)
        date = int(dt_now.strftime('%Y%m%d%H%M%S')+"000") - 200000
        for item in body["messages"]:
            # print(item, date)
            if item["user"]["user_type"] == "emo":
                if item["sequence"] < date:
                    print("No new message")
                    break
                self.message =item
                print("Got a new message")
                return item["message"]["ja"]
        return ""
    
    def send_speech(self, text:str) -> None:
        end_point = "/v1/rooms/"+self.uuid+"/messages/text"
        header = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }
        data = {
            "text": text,
            "immediate": True
        }
        body = self.api.post(data=data, end_point=end_point, headers=header)
        if body != {}:
            print(body)
            
        
    def start_rec(self) -> None:
        end_point = "/v1/webhook/events"
        data = {
            "event": [
                "recording.started"
                ]
            }
        header = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }
        body = self.api.put(data=data, end_point=end_point, headers=header)
        if body != {}:
            print(body)
            
    def stop_rec(self) -> None:
        end_point = "/v1/webhook/events"
        data = {
            "event": [
                "recording.finished"
                ]
            }
        header = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }
        body = self.api.put(data=data, end_point=end_point, headers=header)
        if body != {}:
            print(body)
        
        