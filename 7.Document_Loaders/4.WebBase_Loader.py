from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = 'llama3')

template = PromptTemplate(
    template = 'Answer the following question /n {question} from the given text /n {text}',
    input_variables = ['question' , 'text']
)

url = "https://www.akgec.ac.in/courses-offered/"

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

parser = StrOutputParser()

chain = template | model | parser

result = chain.invoke({'question' : 'What are the courses available' , 'text' : docs[0].page_content})

print(result)