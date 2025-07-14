# app.py

import streamlit as st
from core import get_response

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("💇 Customer Support Chatbot")

user_input = st.text_input("Ask me anything:", "")

if user_input:
    response = get_response(user_input)
    st.write(f"**Bot:** {response}")