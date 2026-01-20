from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableLambda

model = ChatOllama(model = 'llama3')

template1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

def count_words(joke):
    return len(joke.split())

parser = StrOutputParser()

joke_gen_runnable = RunnableSequence(template1 , model , parser)

lambda_runnable = RunnableParallel(
    {'joke': RunnablePassthrough() ,
     'count_words' : RunnableLambda(count_words)
})

final_runnable = RunnableSequence(joke_gen_runnable , lambda_runnable)

result = final_runnable.invoke({'topic':'virat kohli'})

print(result)