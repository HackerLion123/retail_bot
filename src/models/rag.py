from src.data.embeddings import generate_embeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_core.documents import Document
from langchain_core.tools import tool


import pandas as pd


def split_text(documents: list[Document]):
    """
    Split the text content of the given list of Document objects into smaller chunks.
    Args:
      documents (list[Document]): List of Document objects containing text content to split.
    Returns:
      list[Document]: List of Document objects representing the split text chunks.
    """
    # Initialize text splitter with specified parameters
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # Size of each chunk in characters
        chunk_overlap=100,  # Overlap between consecutive chunks
        length_function=len,  # Function to compute the length of the text
        add_start_index=True,  # Flag to add start index to each chunk
    )

    # Split documents into smaller chunks using text splitter
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # Print example of page content and metadata for a chunk
    document = chunks[0]
    print(document.page_content)
    print(document.metadata)

    return chunks


def create_document_embbedding():
    """_summary_

    Returns:
        _type_: _description_
    """

    data = pd.read_csv("data/raw/train.csv")
    docs = data.apply(
        lambda row: Document(
            page_content=" ".join(map(str, row[["name", "description"]])),
            metadata={"name": row["name"], "img": row["img"]},
        ),
        axis=1,
    ).tolist()

    docs = split_text(docs)

    generate_embeddings(docs=docs)


if __name__ == "__main__":

    data = pd.read_csv("data/raw/train.csv")
    docs = data.apply(
        lambda row: Document(
            page_content=" ".join(map(str, row[["name", "description"]])),
            metadata={"name": row["name"], "img": row["img"]},
        ),
        axis=1,
    ).tolist()

    docs = split_text(docs)

    generate_embeddings(docs=docs)
