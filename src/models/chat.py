from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain.tools.render import render_text_description
from langchain.output_parsers import StructuredOutputParser
from langchain_core.prompts import ChatPromptTemplate


from src.models.agent import ChatAgent
from src.models.rag import RAGSearch


class StyleAgentPrompt:

    bos = "<|begin_of_text|>"
    header_start = "<|start_header_id|>"
    header_end = "<|end_header_id|>"
    eos = "<|eot_id|>"

    prompt = f"""
    {bos}{header_start} system {header_end}

    You are a cloth styling assistant that provide clothing recommendation based on user query.

    

    
    """


def generate_response():
    pass


def parse_output():
    pass


def get_agent_response(agent, messages):
    pass
