# pip install langchain langchain-google-genai google-generativeai python-dotenv
import os
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="Streaming Bot", page_icon="🤖")

st.title("Streaming Bot")

# Conversation
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

user_query = st.chat_input("Your message")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(user_query))
    
    with st.chat_message("human"):
        st.markdown(user_query)
        
    with st.chat_message("AI"):
        ai_response = "I don't know"
        st.markdown(ai_response)
        
    st.session_state.chat_history.append(AIMessage(ai_response))







