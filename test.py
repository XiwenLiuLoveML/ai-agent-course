from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=api_key
)

response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {"role": "user", "content": "Describe yourself in one sentence."}
    ]
)

print(response.choices[0].message.content)