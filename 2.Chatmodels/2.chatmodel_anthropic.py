from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-2" , temperature=1.4 , max_tokens_to_sample=1024)

result = model.invoke("Tell me a joke about programming.")
print(result)