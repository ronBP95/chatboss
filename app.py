# app.py

import streamlit as st
import csv
from datetime import datetime
from core import get_response

# Set up Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")
st.title("💇 Customer Support Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Each: {"timestamp", "user", "bot"}

# Input container
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:", placeholder="Ask me anything...")
    submit_button = st.form_submit_button("Send")

# Log file path
LOG_FILE = "chat_logs.csv"

# Logging function
def log_chat(user_input, response):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), user_input, response])

# Handle user input
if submit_button and user_input:
    response = get_response(user_input)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Store in session history
    st.session_state.chat_history.append({
        "timestamp": timestamp,
        "user": user_input,
        "bot": response
    })

    log_chat(user_input, response)

# 💬 Display chat history in a fixed scrollable container
st.markdown("### 💬 Chat History")

chat_container = """
<style>
.chat-box {
    height: 400px;
    overflow-y: scroll;
    padding: 1rem;
    border: 1px solid #DDD;
    background-color: #f9f9f9;
    border-radius: 10px;
}
.chat-entry {
    margin-bottom: 1rem;
}
.chat-user {
    background-color: #DCF8C6;
    padding: 0.5rem;
    border-radius: 10px;
    margin-bottom: 0.25rem;
}
.chat-bot {
    background-color: #E5E5EA;
    padding: 0.5rem;
    border-radius: 10px;
}
.chat-timestamp {
    font-size: 0.75rem;
    color: #888;
    margin-bottom: 0.25rem;
}
</style>
<div class="chat-box">
"""

for entry in st.session_state.chat_history:
    chat_container += f"""
    <div class="chat-entry">
        <div class="chat-timestamp">{entry['timestamp']}</div>
        <div class="chat-user"><strong>You:</strong> {entry['user']}</div>
        <div class="chat-bot"><strong>Bot:</strong> {entry['bot']}</div>
    </div>
    """

chat_container += "</div>"

st.markdown(chat_container, unsafe_allow_html=True)