from src.data.embeddings import generate_embeddings

from langchain.tools.retriever import create_retriever_tool

import pandas as pd


def create_product_search_tool():
    """_summary_

    Returns:
        _type_: _description_
    """

    data = pd.read_csv("data/raw/")

    db = generate_embeddings(docs=data)

    retriever = db.as_retriever()

    retriever_tool = create_retriever_tool(
        retriever,
        "Kmart Product Retriver",
        "Tool to find products from kmart using product description and other attributes.",
    )

    return retriever_tool
