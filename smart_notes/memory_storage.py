from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings


DEFAULT_VECTOR_STORE_PATH = str(Path(__file__).parents[1] / 'data' / 'embeddings')


class MemoryStorage:
    # todo should I use async when storing and retrieving?
    def __init__(self, vector_store_path: str = DEFAULT_VECTOR_STORE_PATH):
        # todo use a proper embedding (multilingual)
        self._vectorstore = Chroma(embedding_function=OpenAIEmbeddings(),
                                   persist_directory=vector_store_path)
        # todo don't know how to change the default number of retrieved number (which is 4)
        self._retriever = self._vectorstore.as_retriever(search_type='similarity')

    def store(self, memory: str):
        document = Document(memory)
        self._vectorstore.add_documents([document])

    def withdraw(self, request: str) -> str:
        retrieved_docs = self._retriever.invoke(request)
        return retrieved_docs[0].page_content
