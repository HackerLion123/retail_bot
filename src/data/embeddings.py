from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
from langchain_chroma import Chroma
from src import config


def generate_embeddings(docs):

    print("Starting to generate embeddings...")

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    print("Embeddings model initialized.")

    # Create Emdeddings
    db = Chroma.from_documents(
        documents=docs, embedding=embeddings, persist_directory=config.EMBEDDING_PATH
    )

    # db = InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)

    # Load Embeddings
    db = Chroma(embedding_function=embeddings, persist_directory=config.EMBEDDING_PATH)
    print("Database created from documents.")

    # print(db.similarity_search("Black Shirt"))

    # db.persist()
    print("Database persisted.")

    return db
