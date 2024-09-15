from src.data.embeddings import generate_embeddings

from langchain.tools.retriever import create_retriever_tool
from langchain_core.documents import Document


import pandas as pd


def create_product_search_tool():
    """_summary_

    Returns:
        _type_: _description_
    """

    data = pd.read_csv("data/raw/train.csv")
    docs = (
        data[["name", "description", "p_attributes"]]
        .apply(
            lambda row: Document(
                page_content=" ".join(map(str, row)), metadata={"name": row["name"]}
            ),
            axis=1,
        )
        .tolist()
    )

    db = generate_embeddings(docs=docs)

    retriever = db.as_retriever()

    retriever_tool = create_retriever_tool(
        retriever,
        "Kmart Product Retriver",
        "Tool to find products from kmart using product description and other attributes.",
    )

    return retriever_tool


if __name__ == "__main__":
    pass
