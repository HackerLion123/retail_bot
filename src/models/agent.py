from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import Ollama
from langchain.agents import AgentExecutor, initialize_agent


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
        tools = [DuckDuckGoSearchRun()]
        self.agent = initialize_agent(
            agent="chat-conversational-react-description",
            tools=tools,
            llm=llm,
            verbose=True,
            early_stopping_method="generate",
            memory=self.memory,
            handle_parsing_errors=True,
        )
        self.agent_executor = AgentExecutor(
            agent=self.agent, tools=tools, verbose=True, handle_parsing_errors=True
        )

    def chat(self, question):
        return self.agent_executor.invoke(question)


if __name__ == "__main__":
    agent = ChatAgent()

    agent.build("You are a style bot you provide style suggestions")
    agent.chat([("human", "Tropical trend")])
