"""
Streamlit chat example using MCPAgent with built-in conversation memory and Web Search.

"""

import asyncio
import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

# Load environment variables for API keys
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Config file path - change this to your config file
config_file = "config.json"

# Initialize MCP client and agent with memory enabled
client = MCPClient.from_config_file(config_file)
llm = ChatGroq(model="gemma2-9b-it", api_key=groq_api_key)
agent = MCPAgent(
    llm=llm,
    client=client,
    max_steps=15,
    memory_enabled=True,  # Enable built-in conversation memory
)

# Helper function to run async agent.run in sync context
def run_agent(user_input):
    return asyncio.run(agent.run(user_input))

st.title("Interactive MCP Chat (Streamlit)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def clear_history():
    agent.clear_conversation_history()
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

col1, col2 = st.columns(2)
with col1:
    if st.button("Send") and user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        try:
            response = run_agent(user_input)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
        except Exception as e:
            st.session_state.chat_history.append({"role": "assistant", "content": f"Error: {e}"})
        st.experimental_rerun()

with col2:
    if st.button("Clear"):
        clear_history()
        st.experimental_rerun()

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Assistant:** {chat['content']}")
