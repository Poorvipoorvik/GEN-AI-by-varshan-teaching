# prompt = " it is given instrunction or input to given ai model"
# prompt engineering = " it is process of designing or optimising instruction given to LLM to obtain accurate,relevent and usefull output"

# there are 5 most important rules

import ollama # to connect python to ollama 

# 1). role
system_role_content = "you are a wild life travel writer for a south India travel blog."

#2). task
user_role_content_v1= "write an introduction to Karnataka's wildlife for first time visitors."

#3). constrains
user_role_content_v2= """write an introduction to Karnataka's wildlife for first time visitors.
150 words,audienc: who never seen safari,exactly three parks """

#4). format
user_role_content_v3="""write an introduction to Karnataka's wildlife for first time visitors.
150 words,audienc: who never seen safari,exactly three parks
format: three bullet(park,signature animal,best month)"""

#5). example or context
user_role_content_v4="""write an introduction to Karnataka's wildlife for first time visitors.
150 words,audienc: who never seen safari,exactly three parks
format: three bullet(park,signature animal,best month)
context:nagarahole tiger reserve best month to witness"""

messages=[
    {
        "role":"system",
        "content":system_role_content
    },
    {
        "role":"user",
        "content":user_role_content_v1 + user_role_content_v2 + user_role_content_v3 + user_role_content_v4
    }
]

model_name="llama3.2:latest"

response= ollama.chat(model= model_name,messages = messages)

print(response.message.content)
