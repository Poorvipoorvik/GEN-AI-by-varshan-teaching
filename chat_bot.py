import ollama  # import software to interact  with real time
messages =[{ "role":"system", "content":"you are a friendly assistant." }]
model_name="llama3.2:latest" # we declare modle_ name by using variable 

while True: # to continously accept user questions until the user enters bye

    user_prompt=input("you : ") # here we ask enter the promt by user

    if user_prompt=="bye": # here we use if in case user enter a prompt bye then it exit's the loop crack
        break

    user_role={"role":"user","content":user_prompt  } # initialise dictionary but we use user_prompt

    messages.append(user_role) # it add new messages to the convesrtion history

    response=ollama.chat(model=model_name,messages=messages) # to call ollama because sends the converstion msg to the selected ollama model and get a respose

    response=response.message.content # use content because it give content only not allow meta data 

    print("assistent :",response)
    assistent_role={"role":"assistant","content":"response"}
    messages.append(assistent_role) 