from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
model = ChatOllama(model="llama3")

# chat_history = []
# while True:
#     user_input = input("Aman: ")
#     chat_history.append(user_input)
#     if user_input == "exit":
#         break

#     result = model.invoke(chat_history)
#     print("Llama3: ", result.content)
#     chat_history.append(result.content)

# print(chat_history)

#above is okay but here the messages of user and AI model can't differentiate so we have to store messages using name of user and AI with help of dictionary

chat_history = [
    SystemMessage(content="You are a doctor AI assistant. Answer as concisely as possible.")
]

while True:
    user_input = input("Aman: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("Llama3: ", result.content)

print(chat_history)