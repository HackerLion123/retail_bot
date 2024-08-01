from langchain_community.tools import StructuredTool

from src.data.embeddings import generate_embeddings


class ProductSearch:

    def __init__(self, product_desc) -> None:
        vector_db = generate_embeddings(docs=product_desc)

    def search(self):
        pass
