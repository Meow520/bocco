import time
import os
import openai
from typing import Tuple
from auth import Auth
from bocco_tools import BoccoTools

def gene_text(text:str, prompts:list) -> Tuple[str, list]:
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

def main():
    # 初期設定（トークンの取得）
    auth = Auth()
    auth.update_token()
    tools = BoccoTools(uuid=auth.uuid, access_token=auth.access_token)
    
    # 会話
    prompts = []
    prev_text = ""
    while True:
        text = tools.get_speech()
        if text == "" or text == prev_text:
            print("please talk to emo")
            time.sleep(8)
            continue
        if text != prev_text:
            res, prompts = gene_text(text=text, prompts=prompts)
            tools.send_speech(res)
            prev_text = text
        time.sleep(8)
    
if __name__ == "__main__":
    main()