from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from src import config


def generate_embeddings(docs):

    embeddings = OllamaEmbeddings(model="nomic-embed-text", show_progress=False)
    db = Chroma.from_documents(
        documents=docs, embedding=embeddings, persist_directory=config.EMBEDDING_PATH
    )
    db.persist()
    return db
