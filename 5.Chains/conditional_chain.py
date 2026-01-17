from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch , RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import Literal

model = ChatOllama(model = 'gemma3:4b')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positive' , 'negative'] = Field(description = 'Generate the sentiment from the text')

parser2 = PydanticOutputParser(pydantic_object = Feedback)


prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative /n {feedback} /n {format_instructions}',
    input_variables = ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions}
)

classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback':'This is a terribe smartphone'}).sentiment

prompt2 = PromptTemplate(
    template = 'Write an appropriate response to this positive feedback /n {feedback}' , 
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to this negative feedback /n {feedback}' , 
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    #(cond , chain)
    (lambda x : x.sentiment == 'positive' , prompt2 | model | parser),
    (lambda x : x.sentiment == 'negative' , prompt3 | model | parser),
    RunnableLambda(lambda x : "could not find sentiment") # default chain  # RunnableLambda lambda ko chain m convert kr deta h
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback' : 'This is a terrible phone'})

print(result)

chain.get_graph().print_ascii()