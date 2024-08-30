# Sotaで言うところのRobotToolsの部分です
import datetime
import os
import openai
from entity import Webhook, WebhookInfo, WebhookBody
from api_query import ApiQuery
from auth import Auth
from typing import Callable, Dict, List, NoReturn, Optional, Tuple, Union
from collections import deque

class BoccoTools:
    _DEFAULT_ROOM_ID = ""
    
    def __init__(self) -> None:
        self.auth = Auth()
        self.api = ApiQuery()
        self.message = {}
        self._webhook_events_cb: Dict[str, Dict[str, Callable]] = {}
        self._request_id_deque: deque = deque([], 10)
        
    # 音声認識
    def get_speech(self) -> str:
        self.access_token, self.uuid = self.auth.check_expired()
        end_point = "/v1/rooms/"+self.uuid+"/messages"
        header = {
            'Authorization': 'Bearer ' + self.access_token
        }
        body = self.api.get(end_point=end_point, headers=header)
        
        if  "error" in body:
            return ""

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
    
    # 発話
    def send_speech(self, text:str) -> None:
        self.access_token, self.uuid = self.auth.check_expired()
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
        if "error" in body:
            return
        print(f"POSTED: {body}")
    
    # webhookの設定
    def set_webhook(self, webhook:Webhook) -> None:
        self.access_token, self.uuid = self.auth.check_expired()
        end_point = "/v1/webhook"
        header = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }
        data = {
            "description": webhook.description,
            "url": webhook.url
        }
        body = self.api.post(data=data, end_point=end_point, headers=header)
        
        if "error" in body:
            return WebhookInfo(**body)
    
    # event取得        
    def event(self, event: str, room_id_list: List[str] = []) -> Callable:
        def decorator(func):
            if event not in self._webhook_events_cb:
                self._webhook_events_cb[event] = {}

            for room_id in room_id_list:
                self._webhook_events_cb[event][room_id] = func

        return decorator
    
    def _register_webhook_event(self, events: List[str]) -> dict:
        self.access_token, self.uuid = self.auth.check_expired()
        end_point = "/v1/webhook/events"
        header = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }
        data = {
            "events": events
        }
        body = self.api.put(data=data, end_point=end_point, headers=header)
        
        if "error" in body:
            return {"error": body["error"]}
        return WebhookInfo(**body)
        
    def start_webhook_event(self) -> str:
        response = self._register_webhook_event(list(self._webhook_events_cb.keys()))
        return response.secret

    def get_cb_func(self, body: dict) -> Tuple[Callable, WebhookBody]:
        self.access_token, self.uuid = self.auth.check_expired()
        emo_webhook_body = WebhookBody(**body)
        print(emo_webhook_body, self._webhook_events_cb)
        if emo_webhook_body.request_id not in self._request_id_deque:
            try:
                event_cb = self._webhook_events_cb[emo_webhook_body.event]
            except KeyError as e:
                print(f"error:{e}")
            print(event_cb)
            room_id = emo_webhook_body.uuid
            if room_id in event_cb:
                cb_func = event_cb[room_id]
            elif self._DEFAULT_ROOM_ID in event_cb:
                cb_func = event_cb[self._DEFAULT_ROOM_ID]
            else:
                print(f"error: room error")
            self._request_id_deque.append(emo_webhook_body.request_id)
            return cb_func
        else:
            print("Webhook request id is duplicated")

    
    # 発話テキスト生成
    def gene_text(self, text:str, prompts:list) -> Tuple[str, list]:
        model = "gpt-4o-mini"
        if len(prompts) == 0:
            default_prompt = [
            {'role': 'system', 'content': 'あなたはユーザーの雑談相手です。'},
            {'role': 'system', 'content': '返事は短めに一文までにしてください。'}
            ]
            prompts = default_prompt
        prompts.append({'role': 'user', 'content': text})
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        response = openai.chat.completions.create(
            model=model,
            messages=prompts
        )
        message = response.choices[0].message.content
        prompts.append({'role':'assistant', 'content':message})
        return message, prompts
        
        