from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community import document_loaders

from smart_notes.memory_storage import MemoryStorage

load_dotenv()

# todo use the newest model
llm = ChatOpenAI(model='gpt-3.5-turbo-0125')

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

memory_storage = MemoryStorage()
# for document in documents:
#     memory_storage.store(document.page_content)

retrieved_content = memory_storage.withdraw('What is my place of origin?')
print(retrieved_content)

retrieved_content = memory_storage.withdraw('Who am I?')
print(retrieved_content)

retrieved_content = memory_storage.withdraw('What age am I?')
print(retrieved_content)

retrieved_content = memory_storage.withdraw('What do I like?')
print(retrieved_content)
