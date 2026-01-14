from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
from langchain_ollama import ChatOllama
model = ChatOllama(model="llama3")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of India?")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)