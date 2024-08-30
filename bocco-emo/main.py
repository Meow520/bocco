import http.server
import json
from bocco_tools import BoccoTools
from entity import Webhook

tools = BoccoTools()
prompt: list = []

# Webhookの受け取り先を指定する（WebhookURLにngrokでのサーバー立ち上げ時に出るFowardingの欄の矢印の元のURLを貼り付ける）
tools.set_webhook(Webhook("WebhookURL"))

# メッセージを受け取った時（アプリの部屋で何らかのメッセージが投稿された時）に下のmessage_callbackが発火
@tools.event("message.received")
def message_callback(data):
    global prompt
    # メッセージの送信者のuser_typeで判別（send_speechもメッセージの投稿となるが、emoで受け取った時とはuser_typeが異なるため）
    if data.data.message.user.user_type == "emo":
        # ユーザーの発話データ取得
        user_speech = data.data.message.message.ja
        # 返答生成
        response, prompt = tools.gene_text(text=user_speech, prompts=prompt)
        tools.send_speech(response)
    else:
        # print("plain message received")
        pass

# セキュリティ上の問題が起きないためにsecret_keyを作成
secret_key = tools.start_webhook_event()

# localserverを立ち上げる
class Handler(http.server.BaseHTTPRequestHandler):
    def _send_status(self, status):
        self.send_response(status)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()

    def do_POST(self):
        # check secret_key
        if not secret_key == self.headers["X-Platform-Api-Secret"]:
            self._send_status(401)
            return

        content_len = int(self.headers["content-length"])
        request_body = json.loads(self.rfile.read(content_len).decode("utf-8"))

        try:
            # ここでイベント発火時のCallback関数を受け取る
            cb_func, emo_webhook_body = tools.get_cb_func(request_body)
        except Exception:
            self._send_status(501)
            return

        cb_func(emo_webhook_body)

        self._send_status(200)

# サーバー立ち上げ（ポート番号はngrokのサーバー立ち上げ時のポートと同一にする）
with http.server.HTTPServer(("", 8080), Handler) as httpd:
    httpd.serve_forever()
