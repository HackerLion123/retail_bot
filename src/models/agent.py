from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import Ollama
from langchain.agents import AgentExecutor, initialize_agent

from langchain_community.utilities import DuckDuckGoSearchAPIWrapper


from src import config


class ChatAgent:

    def __init__(self) -> None:
        self.messages = []
        self.rag_chain = None
        self.memory = ConversationBufferMemory(
            memory_key="history", return_messages=True, output_key="output"
        )

    def build(self, prompt):
        self._create_agent(prompt=prompt)

    def _create_agent(self, prompt):
        llm = Ollama(**config.MODEL_CONFIG)

        # setting search region to aus.
        wrapper = DuckDuckGoSearchAPIWrapper(region="au-en", time="y", max_results=5)
        tools = [DuckDuckGoSearchRun(api_wrapper=wrapper)]
        self.agent = initialize_agent(
            agent="chat-conversational-react-description",
            tools=tools,
            llm=llm,
            verbose=config.DEBUG_FLAG,
            early_stopping_method="generate",
            memory=self.memory,
            handle_parsing_errors=True,
        )

    def chat(self, question):
        return self.agent.run(question)


if __name__ == "__main__":
    agent = ChatAgent()

    agent.build("You are a style bot you provide style suggestions")
    agent.chat({"input": "Tropical trend", "chat_history": []})
