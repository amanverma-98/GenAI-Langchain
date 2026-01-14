from langchain_huggingface import ChatHuggingFace , HuggingFacePipeline

# Pipeline is imported here for local models

llm = HuggingFacePipeline.from_model_id(model_id = "HuggingFaceH4/zephyr-7b-beta" , task = "text-generation"
                                     , pipeline_kwargs = {"max_new_tokens":1024 , "temperature":1.4})
model = ChatHuggingFace(llm = llm)

result = model.invoke("Tell me one joke about programming.")    
print(result.content)