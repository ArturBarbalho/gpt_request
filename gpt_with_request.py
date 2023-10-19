from keys import key
import requests
import json

class Chat_request():
    def __init__(self, msg):    
        link = 'https://api.openai.com/v1/chat/completions'
        headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        msg_body = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{msg}"}]
        }
        msg_body = json.dumps(msg_body)

        request = requests.post(link, headers=headers, data=msg_body)

        return request.text

