import streamlit as st
import os
import google.generativeai as genai

# Set Google API key
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
os.getenv('GOOGLE_API_KEY')

st.title("Chat - Gemini Bot")

model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages = [
        {
            "role": "assistant",
            "content":"Ask me Anything"
        }
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process and store Query and Response
def llm_function(query):
    response = model.generate_content(query)

    # displaying assistant message
    with st.chat_message("assistant"):
        st.markdown(response.text)

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role":"user",
            "content": query
        }
    )

    # storing the user message
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response.text
        }
    )

# accept user input
query = st.chat_input("What is up?")

# Calling the Function when Input is Provided
if query:
    # Displaying the User Message
    with st.chat_message("user"):
        st.markdown(query)


    llm_function(query)