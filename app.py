import streamlit as st
import csv
from datetime import datetime
from core import get_response

st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")
st.title("💇 Customer Support Chatbot")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# CSV Logging
LOG_FILE = "chat_logs.csv"
def log_chat(user_input, response):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), user_input, response])

# 🔁 Handle user input first
with st.form(key="chat_form", clear_on_submit=True):
    cols = st.columns([5, 1])
    user_input = cols[0].text_input("Type your message:", placeholder="Ask me anything...", label_visibility="collapsed")
    submitted = cols[1].form_submit_button("Send")

if submitted and user_input:
    response = get_response(user_input)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.chat_history.append({
        "timestamp": timestamp,
        "user": user_input,
        "bot": response
    })
    log_chat(user_input, response)

# ✅ Render Chat History (fixed size container)
st.markdown("### 💬 Chat History")

# CSS for styling scrollable chat box
st.markdown("""
<style>
.chat-container {
    height: 400px;
    overflow-y: auto;
    background-color: #f5f5f5;
    padding: 1rem;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-bottom: 1.5rem;
}
.chat-entry {
    margin-bottom: 1.2rem;
}
.chat-timestamp {
    font-size: 0.75rem;
    color: #888;
    margin-bottom: 0.2rem;
}
.chat-user {
    background-color: #DCF8C6;
    padding: 0.6rem;
    border-radius: 10px;
    margin-bottom: 0.3rem;
    white-space: pre-wrap;
}
.chat-bot {
    background-color: #E5E5EA;
    padding: 0.6rem;
    border-radius: 10px;
    white-space: pre-wrap;
}
</style>
<div class="chat-container">
""", unsafe_allow_html=True)

# Render each chat message in container
for entry in st.session_state.chat_history:
    st.markdown(f"""
    <div class='chat-entry'>
        <div class='chat-timestamp'>{entry['timestamp']}</div>
        <div class='chat-user'><strong>You:</strong> {entry['user']}</div>
        <div class='chat-bot'><strong>Bot:</strong> {entry['bot']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)