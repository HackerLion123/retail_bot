import streamlit as st

from PIL import Image

import requests
from io import BytesIO

import json


from src.models.search import ProductSearch

from src.models.chat import generate_response


def generate_page():
    """_summary_"""

    st.set_page_config(page_title="Kmart", page_icon=":books:")
    st.title("Style Bot")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    with st.chat_message("assistant"):
        st.markdown("Hello, How can I help you today?")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        print(prompt)

        response = generate_response(input=prompt, user_id="default")

        with st.chat_message("assistant"):
            parse_output(response["output"])

        st.session_state.messages.append({"role": "assistant", "content": response})


def parse_output(output):

    output = json.loads(output)
    search = ProductSearch()

    for product in output["recommendations"]:

        recommendations = search.search(str(product))

        for keycode in recommendations:
            print(keycode["img"])

            # image = Image.open(keycode["img"])

            response = requests.get(keycode["img"])
            image = Image.open(BytesIO(response.content))

            st.image(image, caption=keycode["name"])
