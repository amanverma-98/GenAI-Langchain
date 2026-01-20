from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence , RunnableParallel
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = 'llama3')

template1 = PromptTemplate(
    template = 'Generate a tweet on {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Write a linkedin post on {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

parallel_runnable = RunnableParallel(
   {'tweet' : RunnableSequence(template1 , model , parser) ,
    'linkedin' : RunnableSequence(template2 , model , parser)
    })

result = parallel_runnable.invoke({'topic':'Virat Kohli'})

print(result)