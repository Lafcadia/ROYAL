import os

import openai
from openai import OpenAI

client = OpenAI(api_key=os.getenv("AIGCAPI_KEY"))

# TODO: The 'openai.api_base' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(base_url='https://api.aigcapi.io/v1')'
# openai.api_base = 'https://api.aigcapi.io/v1'

messages = [
    {"role": "user", "content": "你好"}
]

res = client.chat.completions.create(model="gpt-4",
messages=messages,
stream=False)

print(res.choices[0].message.content)