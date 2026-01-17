from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = 'llama3')

prompt = PromptTemplate(
    template = 'Give me 5 line summary about {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic' : 'Virat Kohli'})

print(result)

# for visulaisation 

chain.get_graph().print_ascii()