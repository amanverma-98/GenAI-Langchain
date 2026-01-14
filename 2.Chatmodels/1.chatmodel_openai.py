from openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4" , temperature=1.4 , max_completion_tokens=1024) 
# temperature ko creativity ko handle krne k liye use kiya hai
# max_completion_tokens response ki length ko control krta hai

response = chat_model.invoke("Tell me a joke about programming.")
print(response)