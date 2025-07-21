import streamlit as st
from index import query_saarthi, SAARTHI_PERSONA

st.set_page_config(page_title="Saarthi — Government Helpdesk Chatbot", page_icon="🧭")

# 💅 Style CSS
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
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧭 Saarthi — Government Helpdesk Chatbot")

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
