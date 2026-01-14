from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder

template = ChatPromptTemplate(
    [('system' , "You are a virtual assistant"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human' , "{query}")
])

# create chat history
chat_history = []

with open("2.Prompts/chat_history.txt") as f:
    chat_history.extend(f.readlines())

print("Chat History: ", chat_history)

#create prompt
prompt = template.invoke({
    'chat_history': chat_history,
    'query': "Where is my refund?"
})

print(prompt)