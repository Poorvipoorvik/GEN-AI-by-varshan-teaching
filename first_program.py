import ollama 

model_name="llama3.2:latest "
prompt="explain how ai software work in one line"
response=ollama.generate(model=model_name,prompt=prompt)
print(response.response)