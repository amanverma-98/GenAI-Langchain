from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
model = ChatOllama(model = 'llama3')


template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}'
    , input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text . /n {text}',
    imput_variables = ['text']
)

parser = StrOutputParser()   # parser ek string only return krta addn details ko removwe kr deta hai

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic' : 'Blackhole'})

print(result)