from langchain_core.prompts import ChatPromptTemplate

#hm yha pr humanmessage / systemmessage ka use ni kr rhe h kyuki isse jb output ayega to hmne jo input diya wo nhi dikhega bs same string jo di thi whi dikh jayegi bss

template = ChatPromptTemplate(
    [('system' , "You are a {domain} expert"),
    ('human' , "Explain the concept of {topic}")
])

prompt = template.invoke({
    'domain': "mathematics",
    'topic': "Fourier Transform"
})

print(prompt)