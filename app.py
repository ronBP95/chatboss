# app.py

import streamlit as st
import csv
from datetime import datetime
from core import get_response

# Set up Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("💇 Customer Support Chatbot")

# Input from user
user_input = st.text_input("Ask me anything:")

# Log file path
LOG_FILE = "chat_logs.csv"

# Function to log chats
def log_chat(user_input, response):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), user_input, response])

# Handle user input
if user_input:
    response = get_response(user_input)
    st.write(f"**Bot:** {response}")
    log_chat(user_input, response)  # 🟢 Don't forget to log the chat!