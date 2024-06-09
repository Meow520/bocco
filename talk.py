from api_query import ApiQuery
from typing import Tuple
import openai
import datetime

class Talk:
    def __init__(self, uuid:str, access_token:str, openai_key:str) -> None:
        self.uuid = uuid
        self.access_token = access_token
        self.openai_key = openai_key
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
            
            
    def gene_text(self, text:str, prompts:list) -> Tuple[str, list]:
        model = "gpt-4-turbo"
        if len(prompts) == 0:
            default_prompt = [
            {'role': 'system', 'content': 'あなたはユーザーの雑談相手です。'},
            {'role': 'system', 'content': '返事は短めに一文までにしてください。'}
            ]
            prompts = default_prompt
        prompts.append({'role': 'user', 'content': text})
        openai.api_key = self.openai_key
        response = openai.chat.completions.create(
            model=model,
            messages=prompts
        )
        message = response.choices[0].message.content
        prompts.append({'role':'assistant', 'content':message})
        return message, prompts
        