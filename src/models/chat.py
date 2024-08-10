from langchain.output_parsers import StructuredOutputParser


from src.models.agent import ChatAgent

from src.models.prompt import create_agent_prompt

from PIL import Image

import streamlit as st


def fetch_user_search_history(user_id="default"):

    return "\n".join(
        ["Blue men's jeans", "Formal shoes", "Plain shirt", "green Tshirts"]
    )


def generate_response(input, user_id):
    agent = ChatAgent()
    tools_desc = agent.tools_desc
    prompt = create_agent_prompt(tools_desc=tools_desc)
    agent.build(prompt=prompt)

    user_history = fetch_user_search_history(user_id)

    chat_input = f"""
    user search history:

    {user_history}


    user question: {input}
    """

    return agent.chat(input=chat_input)


if __name__ == "__main__":
    output = generate_response(
        "I am going to costrica I want dress for that", "default"
    )
