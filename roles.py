import ollama

messages=[
    {
        "role":"system",
        "content":"if you are my friend give me the best wish to get success in one line"
    },
    {
        "role":"user",
        "content":"what is ai"
    }
]

model_name="llama3.2:latest "
response=ollama.chat(model=model_name,messages=messages)

print(response.message)