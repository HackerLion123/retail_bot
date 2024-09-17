from langchain_ollama import OllamaEmbeddings
from langchain.tools import BaseTool
from langchain_chroma import Chroma


from src import config


class ProductSearch(BaseTool):
    name: str = "Kmart Product Retriever"
    description: str = (
        "Tool to search kmart products similar to the query. Returns Name and img."
    )

    def search(self, query: str) -> str:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        print("Embeddings model initialized.")

        # Load Embeddings
        db = Chroma(
            embedding_function=embeddings, persist_directory=config.EMBEDDING_PATH
        )
        retriever = db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 2},
        )
        docs = retriever.invoke(query)
        return [doc.metadata for doc in docs]

    def _run(self, query: str) -> str:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        print("Embeddings model initialized.")

        # Load Embeddings
        db = Chroma(
            embedding_function=embeddings, persist_directory=config.EMBEDDING_PATH
        )
        retriever = db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3},
        )
        docs = retriever.invoke(query)
        return str([doc.metadata for doc in docs])
