from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

docs = [
     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Who is the aggrsive Indian cricketer?"

doc_embeddings = model.embed_documents(docs)
query_embeddings = model.embed_query(query)
# cosine_similarity for semantic search
similarities = cosine_similarity([query_embeddings], doc_embeddings)[0]  # cosine similarity m hmesa 2d list m input bhejenge but hme 1d list chahiye
# print("Similarity scores:", similarities)
# most_similar_doc_index = np.argmax(similarities)

# print("Most similar document to the query:")
# print(docs[most_similar_doc_index])
# print("Similarity score:", similarities[0][most_similar_doc_index])

print(similarities)
# hm hr number ko uske index k sath ek tuple m convert krdenge fir us tuple ko similarity score k hisab se sort krdenge
# hisse index loose nhi hoga
index , similarity = sorted(list(enumerate(similarities)) , key = lambda x:x[1])[-1] # (index , similarity score) of the most similar document

print(docs[index])