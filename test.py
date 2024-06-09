from auth import Auth as A
from talk import Talk as T
a = A()
a.update_token()
t = T(a.uuid, a.access_token, a.open_ai_key)
text = t.get_speech()
print(type(text), text)
message = str(text)
res, prompts = t.gene_text(text="こんにちは", prompts=[])
print(res)