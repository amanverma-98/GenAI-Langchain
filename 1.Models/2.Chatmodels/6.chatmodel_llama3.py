from langchain_ollama import ChatOllama

model = ChatOllama(model = "llama3" , temperature=1.4 , max_tokens=1024)

response = model.invoke("What is the meaning of life?")
print(response.content)