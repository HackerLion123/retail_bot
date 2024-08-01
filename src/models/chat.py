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

    prompt = """
    You are a cloth styling assistant that provide clothing recommendation based on user query.

    You have access to DuckDuckGoSearchRun tool which you can use to search web on good trends and
    matching colors to use for style recommendation.
    
    You will have following 3 inputs:

    User's Past 4 purchases
    {user_history}

    User's Past 3 Search
    {user_search_history}

    User Query:
    {user_query}

    Now, follow these instrustions step by step and don't miss any step.

    1. Based on the user's purchase and search history determine user's gender.
    2. Based on the user's purchase, gender and search history determine user's style preference.
       eg: casual, business casual, vintage, street wear, punk, girly girl etc.
    3. Now use web to search for latest trends in user's style preference category.
    4. Now consider user's search query and find styles that matches with user search query.
    5. The recommendation you provide should be name of the clothing item, color material.

    
    """


def generate_response():
    pass


def parse_output():
    pass


def get_agent_response(agent, messages):
    pass
