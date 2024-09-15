from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from src import config


def generate_embeddings(docs):

    print("Starting to generate embeddings...")

    embeddings = OllamaEmbeddings(model="nomic-embed-text", show_progress=False)
    print("Embeddings model initialized.")

    db = Chroma.from_documents(
        documents=docs, embedding=embeddings, persist_directory=config.EMBEDDING_PATH
    )
    print("Database created from documents.")

    db.persist()
    print("Database persisted.")

    return db
