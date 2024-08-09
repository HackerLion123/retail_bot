from langchain.output_parsers import StructuredOutputParser


from src.models.agent import ChatAgent

from src.models.prompt import create_agent_prompt

from PIL import Image

import streamlit as st


def generate_response(input):
    agent = ChatAgent()
    prompt = create_agent_prompt()
    agent.build()


    return 


def get_agent_response(agent):
    
