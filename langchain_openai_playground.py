from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community import document_loaders

load_dotenv()

# todo use the newest model
llm = ChatOpenAI(model='gpt-3.5-turbo-0125')

# todo perhaps, we don't need a loader: just create a Document
data_path = Path(__file__).parent / 'data'
file_names = [
    'test_doc1.txt',
    'test_doc2.txt',
    'test_doc3.txt'
]
documents = []
for file_name in file_names:
    loads = document_loaders.TextLoader(data_path / file_name).load()
    documents.extend(loads)

# todo use a proper embedding (multilingual)
vectorstore = Chroma.from_documents(documents, embedding=OpenAIEmbeddings())

retriever = vectorstore.as_retriever(search_type='similarity')
retrieved_docs = retriever.invoke('What is my place of origin?')
print(retrieved_docs[0].page_content)

retrieved_docs = retriever.invoke('Who am I?')
print(retrieved_docs[0].page_content)

retrieved_docs = retriever.invoke('What age am I?')
print(retrieved_docs[0].page_content)
