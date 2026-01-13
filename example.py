import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

user_prompt = input("Enter your prompt: ")

system_message = {
    "role": "system", 
    "content": """
    in all messages use only 10 words maximum
    """
}

messages = [
    system_message,
    {"role": "user", "content": user_prompt}
]

response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=messages
)

print(response.choices[0].message.content)