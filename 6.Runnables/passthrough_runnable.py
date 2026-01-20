from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough

model = ChatOllama(model = 'llama3')

template1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Give an explanation of the {joke}',
    input_variables = ['topic']
)

parser = StrOutputParser()

joke_gen_runnable = RunnableSequence(template1 , model , parser)

pass_through_runnable = RunnableParallel(
    {'joke': RunnablePassthrough() ,
     'explanation' : RunnableSequence(template2 , model , parser)    
})

parser2 = JsonOutputParser()

final_runnable = RunnableSequence(joke_gen_runnable , pass_through_runnable)

result = final_runnable.invoke({'topic':'virat kohli'})

print(result)