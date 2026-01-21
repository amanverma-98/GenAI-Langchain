from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = 'llama3')

template = PromptTemplate(
    template = 'Write the summary about the {topic}',
    input_variables = ['topic']
)

loader = TextLoader("7.Document_Loaders/cricket.txt" , encoding = 'utf-8')

docs = loader.load()

# print(docs)

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

# print(type(docs[0]))

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({'topic' : docs[0]})

print(result)