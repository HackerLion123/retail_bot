from src.models.agent import ChatAgent

from src.models.prompt import create_agent_prompt

from PIL import Image

import streamlit as st


def fetch_user_search_history(user_id="default"):
    return "\n".join(["light Blue jeans", "White sneakers", "casual tops"])


def generate_response(input, user_id):
    agent = ChatAgent()
    prompt = create_agent_prompt()
    agent.build(prompt=prompt)

    user_history = fetch_user_search_history(user_id)

    chat_input = f"""
    user search history:

    {user_history}


    user question:

    {input}
    """

    return agent.chat(input=chat_input)


if __name__ == "__main__":
    output = generate_response("suggest me outfit for beach party", "default")
    print(output)
