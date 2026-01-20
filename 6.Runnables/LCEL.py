from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableBranch , RunnablePassthrough

model = ChatOllama(model = 'gemma3:4b')

template1 = PromptTemplate(
    template = 'Generate a report on {topic}',
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = 'Summarize the following text in less than 400 words /n {text}',
    input_variables =['text']
)

parser = StrOutputParser()

report_gen_chain = template1 | model | parser     #LCEL

branch_runnable = RunnableBranch(
    (lambda x : len(x.split()) > 400 , template2 | model | parser),   #LCEL
    RunnablePassthrough()
)

final_runnable = report_gen_chain | branch_runnable    #LCEL

result = final_runnable.invoke({'topic' : 'Virat Kohli'})

print(result)