from openai import OpenAI
#Do we need to pass the key in?
def set_message(system_message="", user_message=""):

  client = OpenAI()
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": str(system_message)},
      {"role": "user", "content": str(user_message)}]
  )
  return completion.choices[0].message.content

import sys
set_message(sys.argv[1], sys.argv[2])