import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
  raise ValueError("API Not Found")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="suggest me new clothing brand name"

message_system={
  "role": "system",
  "content": "you are a brand manager who suggest name for my company. name should be in one word. suggest only one name"
}

message={
  "role":role,
  "content": prompt
}

messages=[message_system,message]

response=client.chat.completions.create(model=model, messages=messages,temperature=2)
# print(response)

answer=response.choices[0].message.content
print(answer)