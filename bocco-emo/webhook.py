import http.server
import json
from auth import Auth
from bocco_tools import BoccoTools
from emo_platform import Client, EmoPlatformError, WebHook, Tokens

auth = Auth()
auth.check_expired()
tools = BoccoTools()

client = Client(tokens=Tokens(refresh_token=auth.refresh_token,access_token=auth.access_token))
# Please replace "YOUR WEBHOOK URL" with the URL forwarded to http://localhost:8000
client.create_webhook_setting(WebHook("https://5124-240b-250-2500-a500-3806-2c84-365f-55a3.ngrok-free.app"))


@client.event("recording.finished")
def message_callback(data):
    tools.send_speech("こんにちは")
    print("recording finished")
    # print(data)

@client.event("message.received")
def message_callback(data):
    tools.send_speech("こんにちは")
    print("message received")
    print(data)

secret_key = client.start_webhook_event()

# localserver
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
            cb_func, emo_webhook_body = client.get_cb_func(request_body)
        except EmoPlatformError:
            self._send_status(501)
            return

        cb_func(emo_webhook_body)

        self._send_status(200)


with http.server.HTTPServer(("", 8080), Handler) as httpd:
    httpd.serve_forever()
