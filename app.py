import streamlit as st
import os

# Page Config
st.set_page_config(
    page_title="MHZALY Claude-Style Omni Chat",
    page_icon="🔮",
    layout="centered"
)

# Purple Cyberpunk Theme
st.markdown("""
    <style>
    .stApp { background-color: #0b0210; color: #e2d9f3; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #130722; border-right: 1px solid #2a124a; }
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #170a29 !important; color: #ffffff !important; border: 1px solid #5a2295 !important; border-radius: 8px !important;
    }
    .stChatMessage { background-color: #130722; border: 1px solid #2a124a; border-radius: 12px; padding: 12px; margin-bottom: 12px; }
    h1, h2, h3 { color: #e0aaff !important; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

# Sidebar for API Key Setup
with st.sidebar:
    st.title("🔮 AI Configuration")
    st.markdown("---")
    api_key_input = st.text_input("Enter Free API Key (Groq / Gemini)", type="password", placeholder="gsk_... or AIza...")
    st.markdown("---")
    st.markdown("### 💡 Note")
    st.markdown("Claude/Groq jaisi real intelligence ke liye live API connection zaroori hota hai taake model har sawal ka natural aur dynamic jawab de sake.")
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.title("🔮 MHZALY Neural Assistant")
st.markdown("Claude & Groq jaisa fluid, real-time conversational chat experience.")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input Box
if prompt := st.chat_input("Apna sawal yahan likhein..."):
    if not api_key_input:
        st.error("Barah-e-karam sidebar mein apni API key enter karein taake chat engine start ho sake.")
    else:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Real AI Response
        with st.chat_message("assistant"):
            try:
                # Using Groq or OpenAI compatible client if key is provided
                from groq import Groq
                client = Groq(api_key=api_key_input)
                
                stream = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                    stream=True,
                )
                
                def response_generator():
                    for chunk in stream:
                        if chunk.choices[0].delta.content:
                            yield chunk.choices[0].delta.content

                response = st.write_stream(response_generator())
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"Connection Error: {e}. Barah-e-karam apni valid API key check karein.")
