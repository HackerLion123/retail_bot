from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.chat_models import ChatOllama
from langchain_community.llms import Ollama
from langchain.agents import AgentType


class ChatAgent:

    def __init__(self) -> None:

        self.messages = []

    def build(self, prompt):
        pass

    def chat(self):
        pass
