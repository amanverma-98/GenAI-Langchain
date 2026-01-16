from typing import Optional , Literal
from langchain_ollama import ChatOllama
from pydantic import BaseModel , Field , EmailStr
model = ChatOllama(model="llama3")



#define data
class Review(BaseModel):
    key_themes : list[str] = Field(description = "Write all the key themes discussed in review")
    summary : str = Field(description = "Summary of the review")  #field ko additional info provide krne k liye yha pe rkhe hai
    sentiment : Literal["pos" , "neg"] = Field(description = "Sentiment of the review, either Positive, Negative or Neutral") # literal flexibility provide krta h kya output chahiye ab ya to pos ayega neg
    pros : Optional[list[str]] = Field(description ="Write all the pros present in review")    #Optional help krta h ki agr data present tbhi output m show hoga wrna nhi
    cons : Optional[list[str]] = Field(description = "Write all the cons present in review")
    name : Optional[str] = Field(description = "Write the name of the reviewer")
    email : Optional[EmailStr] = Field(description = "Write the email of reviewer")


structured_model = model.with_structured_output(Review)   #with_structure_output ek prompt generate krta h jo btata h ki output hme iss format/structure me chahiye



result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Aman Verma
""")




print("Structured Output: ", result)