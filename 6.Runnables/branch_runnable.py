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
    template = 'Summarize the following text /n {text}',
    input_variables =['text']
)

parser = StrOutputParser()

report_gen_chain = RunnableSequence(template1 , model , parser)

branch_runnable = RunnableBranch(
    (lambda x : len(x.split()) > 500 , RunnableSequence(template2,model , parser)),
    RunnablePassthrough()
)

final_runnable = RunnableSequence(report_gen_chain , branch_runnable)

result = final_runnable.invoke({'topic' : 'Virat Kohli'})

print(result)