from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('7.Document_Loaders/dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].metadata)

print(docs[0].page_content)