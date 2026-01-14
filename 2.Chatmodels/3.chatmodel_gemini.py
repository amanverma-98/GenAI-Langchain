from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model="gemini-1.5-turbo" , temperature=1.4 , max_output_tokens=1024)

result = model.invoke("Tell me a joke about programming.")
print(result)