import os

MODEL_CONFIG = {
    "base_url": "http://localhost:11434",
    "model": "mistral",  # "llama3.1",  # "mistral",  # "mistral-nemo",
    "temperature": 0.3,
    "keep_alive": 8000,
    "num_gpu": -1,
}


EMBEDDING_PATH = "data/processed/"

DEBUG_FLAG = True


LLM_CACHE_PATH = "data/cache/"
