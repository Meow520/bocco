import time

from auth import Auth
from talk import Talk

def main():
    # 初期設定（トークンの取得）
    auth = Auth()
    auth.update_token()
    talk = Talk(uuid=auth.uuid, access_token=auth.access_token, openai_key=auth.open_ai_key)
    prompts = []
    prev_text = ""
    while True:
        text = talk.get_speech()
        if text == "" or text == prev_text:
            print("please talk to emo")
            time.sleep(5)
            continue
        if text != prev_text:
            res, prompts = talk.gene_text(text=text, prompts=prompts)
            talk.send_speech(res)
            prev_text = text
    
if __name__ == "__main__":
    main()