import streamlit as st
import csv
from datetime import datetime
from core import get_response

st.set_page_config(page_title="Chatbot", page_icon="💬", layout="centered")
st.title("💇 Customer Support Chatbot")

# Initialize history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Logging setup
LOG_FILE = "chat_logs.csv"
def log_chat(user_input, response):
    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), user_input, response])

# 📥 Input section FIRST to allow chat history to react to updated state
with st.form(key="chat_form", clear_on_submit=True):
    cols = st.columns([5, 1])
    user_input = cols[0].text_input("Type your message:", placeholder="Ask me anything...", label_visibility="collapsed")
    submitted = cols[1].form_submit_button("Send")

# 🧠 Process user input
if submitted and user_input:
    response = get_response(user_input)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.session_state.chat_history.append({
        "timestamp": timestamp,
        "user": user_input,
        "bot": response
    })

    log_chat(user_input, response)

# ✅ Show chat history AFTER input is processed
st.markdown("### 💬 Chat History")
with st.container():
    for entry in st.session_state.chat_history:
        st.text(f"{entry['timestamp']}")
        st.text(f"→ You: {entry['user']}")
        st.text(f"→ Bot: {entry['bot']}")
        st.markdown("---")