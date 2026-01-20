from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

model = ChatOllama(model = 'llama3')

template1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Write a detailed explanation on {joke}',
    input_variables = ['joke']
)
parser = StrOutputParser()

runnable_sequence = RunnableSequence(template1 , model , parser , template2 , model , parser)

result = runnable_sequence.invoke({'topic':'virat kohli'})

print(result)