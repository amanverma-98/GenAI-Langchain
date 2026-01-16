from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser

model = ChatOllama(model = 'llama3')

parser = JsonOutputParser()

template1 = PromptTemplate(
    template = 'Give me the name , age and city of a fictional person /n {format_instructions}' , 
    input_variables = [],
    partial_variables = {'format_instructions' : parser.get_format_instructions()}
)

# prompt = template1.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)   # final output dictionary m ayega isse

chain = template1 | model | parser

result = chain.invoke({}) # agr koi input nhi to empty dictionary paas krni hogi

print(result['name'])