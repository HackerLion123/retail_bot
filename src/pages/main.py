import streamlit as st

from PIL import Image

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

        response = f"Echo: {prompt}"

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
