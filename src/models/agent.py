from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.chat_models import ChatOllama
from langchain.agents import AgentExecutor, create_react_agent


from src import config


class ChatAgent:

    def __init__(self) -> None:
        self.messages = []
        self.rag_chain = None
        self.memory = ConversationBufferMemory(
            memory_key="history", return_messages=True
        )

    def build(self, prompt):
        self._define_model()

    def _create_prompt(self):
        self.prompt = """
        """

    def _define_model(self):
        llm = ChatOllama(**config.MODEL_CONFIG)

    def chat(self):
        pass
