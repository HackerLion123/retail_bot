from langchain_community.embeddings import OllamaEmbeddings


embeddings = OllamaEmbeddings(model="nomic-embed-text", show_progress=False)
