import openai 

openai.api_key = ''
message_history = []
user_msg = ''


message_history.append({
        "role":"user",
        "content":user_msg
        })

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history
)

reply_content = completion.choices[0].message.content

message_history.append({
        "role":"assistant",
        "content":reply_content
        })