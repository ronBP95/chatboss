# app.py

import streamlit as st
import csv
from datetime import datetime
from core import get_response
import html

# Set up Streamlit UI
st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")
st.title("💇 Customer Support Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Each: {"timestamp", "user", "bot"}

# 💬 Display chat history FIRST
st.markdown("### 💬 Chat History")

# CSS for layout and styling
chat_container = """
<style>
.chat-box {
    height: 400px;
    overflow-y: scroll;
    padding: 1rem;
    border: 1px solid #DDD;
    background-color: #f9f9f9;
    border-radius: 10px;
    margin-bottom: 1rem;
}
.chat-entry {
    margin-bottom: 1rem;
}
.chat-user {
    background-color: #DCF8C6;
    padding: 0.5rem;
    border-radius: 10px;
    margin-bottom: 0.25rem;
    white-space: pre-wrap;
}
.chat-bot {
    background-color: #E5E5EA;
    padding: 0.5rem;
    border-radius: 10px;
    white-space: pre-wrap;
}
.chat-timestamp {
    font-size: 0.75rem;
    color: #888;
    margin-bottom: 0.25rem;
}
.input-row {
    display: flex;
    gap: 0.5rem;
}
.input-row input {
    flex: 1;
}
</style>
<div class="chat-box">
"""

# Render the chat history
for entry in st.session_state.chat_history:
    chat_container += f"""
    <div class="chat-entry">
        <div class="chat-timestamp">{entry['timestamp']}</div>
        <div class="chat-user"><strong>You:</strong> {html.escape(entry['user'])}</div>
        <div class="chat-bot"><strong>Bot:</strong> {html.escape(entry['bot'])}</div>
    </div>
    """

chat_container += "</div>"
st.markdown(chat_container, unsafe_allow_html=True)

# 📥 Input form BELOW the chat history
with st.form(key="chat_form", clear_on_submit=True):
    # Use columns for horizontal layout
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input("Type your message:", label_visibility="collapsed", placeholder="Ask me anything...")
    with col2:
        submitted = st.form_submit_button("Send")

# 🗂️ Log file path
LOG_FILE = "chat_logs.csv"

# Logging function
def log_chat(user_input, response):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), user_input, response])

# Process input after send button is clicked
if submitted and user_input:
    response = get_response(user_input)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.chat_history.append({
        "timestamp": timestamp,
        "user": user_input,
        "bot": response
    })
    log_chat(user_input, response)