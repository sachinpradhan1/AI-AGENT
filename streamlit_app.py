#!/usr/bin/env python3
"""
Streamlit Web Interface for AI Agent - Vercel Deployment
"""

import streamlit as st
import os
import sys
from typing import List, Dict

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import main module
from main import AIAgent

# Page configuration
st.set_page_config(
    page_title="AI Agent by Sachin",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0.5rem;
    }
    .user-message {
        background-color: #e3f2fd;
    }
    .assistant-message {
        background-color: #f3e5f5;
    }
    .sidebar .sidebar-content {
        background-color: #f5f5f5;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    try:
        st.session_state.agent = AIAgent()
        st.session_state.initialized = True
    except Exception as e:
        st.session_state.initialized = False
        st.session_state.error = str(e)

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("🤖 AI Agent")
    st.markdown("### Sachin")
    
    # Agent status
    if st.session_state.get('initialized', False):
        st.success("✅ Agent Ready")
    else:
        st.error("❌ Agent Error")
        if 'error' in st.session_state:
            st.error(f"Error: {st.session_state.error}")
    
    st.markdown("---")
    
    # Controls
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        if 'agent' in st.session_state:
            st.session_state.agent.clear_history()
        st.rerun()
    
    st.markdown("---")
    
    # Settings
    st.markdown("### Settings")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    
    st.markdown("---")
    
    # Information
    st.markdown("### About")
    st.markdown("""
    This AI agent is built with:
    - **LangChain** for orchestration
    - **Google Gemini** for intelligence
    - **Streamlit** for web interface
    - **UV** for dependency management
    
    **Created by Sachin**  
    [LinkedIn Profile](https://www.linkedin.com/in/sachin-pradhan-ba82a927a)
    """)

# Main interface
st.title("💬 Chat with AI Agent")

# Check if agent is initialized
if not st.session_state.get('initialized', False):
    st.error("❌ AI Agent failed to initialize. Please check your API key and try again.")
    st.stop()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.agent.get_response(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p>🤖 <strong>AI Agent</strong> - Powered by LangChain & Google Gemini</p>
        <p>Created by <strong>Sachin</strong> | 
        <a href='https://www.linkedin.com/in/sachin-pradhan-ba82a927a' target='_blank'>
        LinkedIn Profile</a></p>
    </div>
    """, 
    unsafe_allow_html=True
)