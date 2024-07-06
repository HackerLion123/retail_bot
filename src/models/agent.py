from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.chat_models import ChatOllama
from langchain.agents import AgentType


class ChatAgent:

    def __init__(self) -> None:
        self.messages = []

    def build(self, prompt):
        self._define_model()

    def _define_model(self):

        llm1 = ChatOllama()

        llm2 = ChatOllama()

    def chat(self):
        pass
