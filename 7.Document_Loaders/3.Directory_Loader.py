from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path = '7.Document_Loaders/books',
    glob = '*.pdf' ,
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()


for document in docs:
    print(document.metadata)