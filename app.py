# app.py

import streamlit as st
import csv
from datetime import datetime
from core import get_response

# Set up Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("💇 Customer Support Chatbot")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Each entry: (user_input, response)

# Input from user
user_input = st.text_input("Ask me anything:")

# Log file path
LOG_FILE = "chat_logs.csv"

# Function to log chats to file
def log_chat(user_input, response):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), user_input, response])

# If input is given, get response + store in chat history + log it
if user_input:
    response = get_response(user_input)
    st.session_state.chat_history.append((user_input, response))
    log_chat(user_input, response)

# Display chat history
st.markdown("### 💬 Chat History")
for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Bot:** {bot_msg}")
    st.markdown("---")