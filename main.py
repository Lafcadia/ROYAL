import os

import openai
from openai import OpenAI

client = OpenAI(api_key=os.getenv("AIGCAPI_KEY"), base_url='https://api.aigcapi.io/v1')

messages = [
    {"role": "user", "content": "宇宙万法的源头，它是什么？（给出一份相对详尽的回答）"}
]

res = client.chat.completions.create(model="gpt-4",
                                     messages=messages,
                                     stream=False)

print(res.choices[0].message.content)
