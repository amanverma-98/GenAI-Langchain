from langchain_huggingface import HuggingFaceEmbeddings

model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

docs = ["What is the capital of France?"
        , "How to learn Langchain?"
        , "Explain the theory of relativity in simple terms."]
result = model.embed_documents(docs)

print(str(result))