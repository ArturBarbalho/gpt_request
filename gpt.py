from keys import key
import requests
import json

link = 'https://api.openai.com/v1/chat/completions'
headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
msg_body = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "show me the bitcoin cotation in dollar"}]
}
msg_body = json.dumps(msg_body)

request = requests.post(link, headers=headers, data=msg_body)

print(request.text)