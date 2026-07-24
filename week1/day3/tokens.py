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

# 3 prompts
prompt1="hi"
prompt2="what will be the trend it market which job will be boom in 2 years detail 100 words"
prompt3="write a 1000 word of essay on Machine learning"

prompts=[prompt1,prompt2,prompt3]

for prompt in prompts:
  message={
  "role":role,
  "content": prompt
  }

  messages=[message]
  response=client.chat.completions.create(model=model, messages=messages,max_tokens=500)
  usage=response.usage
  answer=response.choices[0].message.content
  print(answer)
  print(f"prompt: {prompt} --> your token: {usage.prompt_tokens} completion tokens: {usage.completion_tokens} Finish Token: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")


# prompt="Do you know Virat Kohli"
# message={
#   "role":role,
#   "content": prompt
# }
# messages=[message]
# response=client.chat.completions.create(model=model, messages=messages)
# # print(response)
# answer=response.choices[0].message.content
# print(answer)