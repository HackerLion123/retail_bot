from langchain.memory import ChatMessageHistory, ConversationBufferMemory
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.llms import Ollama
from langchain.agents import AgentExecutor, create_react_agent

from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain.tools.render import render_text_description
from langchain.globals import set_llm_cache
from langchain.cache import SQLiteCache

from src import config

set_llm_cache(SQLiteCache(database_path=config.LLM_CACHE_PATH))


class ChatAgent:

    def __init__(self) -> None:
        self.messages = []
        self.rag_chain = None
        self.memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True, output_key="output"
        )

    def build(self, prompt):
        self._create_agent(prompt=prompt)

    def _create_agent(self, prompt):
        llm = Ollama(**config.MODEL_CONFIG)

        # setting search region to aus.
        wrapper = DuckDuckGoSearchAPIWrapper(region="au-en", time="y", max_results=5)
        tools = [DuckDuckGoSearchRun(api_wrapper=wrapper)]
        self.tools_desc = render_text_description(tools)

        agent = create_react_agent(llm, tools=tools)
        self.agent = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=config.DEBUG_FLAG,
            early_stopping_method="generate",
            memory=self.memory,
            handle_parsing_errors=True,
        )

    def chat(self, input):
        return self.agent.invoke(input)


if __name__ == "__main__":
    agent = ChatAgent()

    agent.build("You are a style bot you provide style suggestions")
    agent.chat({"input": "Tropical trend", "chat_history": []})
