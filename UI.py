# UI.py

import streamlit as st
from index import query_saarthi, SAARTHI_PERSONA

st.set_page_config(page_title="Saarthi — Government Helpdesk Chatbot", page_icon="🧭")

# 💅 Style & Upload Button CSS
st.markdown(
    """
    <style>
    body {
        background-color: #111;
        color: #f1f1f1;
    }
    .stTextInput>div>div>input {
        background-color: #2c2c2c;
        color: white;
        border-radius: 8px;
    }
    .file-upload-btn {
        position: fixed;
        bottom: 2.5rem;
        right: 2.5rem;
        height: 40px;
        width: 40px;
        border-radius: 50%;
        background-color: white;
        color: black;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        line-height: 35px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        z-index: 9999;
    }
    .file-upload-btn:hover {
        background-color: #e0e0e0;
    }
    section[data-testid="stFileUploader"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧭 Saarthi — Government Helpdesk Chatbot")

# 🗂️ Hidden uploader (controlled by "+" button)
uploaded_files = st.file_uploader("Upload", accept_multiple_files=True, label_visibility="collapsed")

# 👍 Show only if uploaded
if uploaded_files:
    for file in uploaded_files:
        st.success(f"Uploaded: {file.name}")

# ➕ Plus button (triggers file uploader)
st.markdown("""
    <label class="file-upload-btn" onclick="document.querySelector('input[type=file]').click()">+</label>
    """, unsafe_allow_html=True)

# 🧠 Chat history init
if "history" not in st.session_state:
    st.session_state.history = [
        {"role": "system", "content": SAARTHI_PERSONA}
    ]

# 💬 Display past messages
for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**Saarthi:** {msg['content']}")

# 🗨️ Chat input
user_input = st.chat_input("Ask about government process…")
if user_input:
    reply = query_saarthi(user_input, st.session_state.history)
    st.rerun()
