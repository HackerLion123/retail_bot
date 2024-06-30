import streamlit as st

from PIL import Image


def generate_page():
    """_summary_"""
    st.title("Style Bot")

    user_input = st.text_input("What would you like to ask?")

    if st.button("Submit"):
        if user_input:
            chatbot_response = "Bro..."
            st.write(f"Chatbot: {chatbot_response}")
        else:
            st.write("Please enter a question or message to get a response.")
