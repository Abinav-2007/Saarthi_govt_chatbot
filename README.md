# Saarthi_govt_chatbot
A virtual helpdesk chatbot for Indian government processes using Groq’s LLaMA3-70B and Streamlit UI.
FILES:
- index.py          : Backend logic (API connection, chatbot persona, response handling)
- ui.py             : Streamlit frontend UI (ChatGPT-style layout, input, file/voice upload)
- readme.txt        : This file

API USED:
- Groq API (https://console.groq.com/)
- Model: LLaMA 3 (llama3-70b-8192)

DEPENDENCIES (RECOMMENDED VERSIONS):
- streamlit==1.35.0
- requests==2.31.0

HOW TO RUN:
1. Install dependencies:
   pip install streamlit==1.35.0 requests==2.31.0

2. Start the chatbot:
   streamlit run ui.py
