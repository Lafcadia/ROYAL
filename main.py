import os

import openai

openai.api_base = 'https://api.aigcapi.io/v1'
openai.api_key = os.getenv("AIGCAPI_KEY")

messages = [
    {"role": "user", "content": "你好"}
]

res = openai.ChatCompletion.create(
    model="gpt-4",
    messages=messages,
    stream=False,
)

print(res['choices'][0]['message']['content'])