import streamlit as st
from PIL import Image
import time
import datetime

# Page Configuration
st.set_page_config(
    page_title="MHZALY Omni-AI Universal Core",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# ADVANCED PURPLE CYBERPUNK THEME & CSS
# ----------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0210;
        color: #e2d9f3;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: #130722;
        border-right: 1px solid #2a124a;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #170a29 !important;
        color: #ffffff !important;
        border: 1px solid #5a2295 !important;
        border-radius: 8px !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #7b2cbf 0%, #b5179e 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #9d4edd 100%, #f72585 100%);
        box-shadow: 0 0 20px rgba(181, 23, 158, 0.6);
    }
    .stChatMessage {
        background-color: #130722;
        border: 1px solid #2a124a;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
    }
    h1, h2, h3 {
        color: #e0aaff !important;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# SIDEBAR - OMNI AI CONTROL CENTER
# ----------------------------------------------------
with st.sidebar:
    st.title("🌌 MHZALY OMNI CORE")
    st.markdown("---")
    
    ai_personality = st.selectbox(
        "🧠 AI Architecture / Persona",
        ["Omni Universal Assistant (Groq/GPT Style)", "Deep Reasoning Engine (DeepSeek-R1 Style)", "Cybersecurity & Code Expert"]
    )
    
    target_language = st.selectbox(
        "💻 Target Programming Language",
        ["Python", "JavaScript", "C++", "Rust", "Go", "Bash", "Solidity", "SQL"]
    )
    
    enable_reasoning = st.checkbox("🔍 Enable Deep Chain-of-Thought (CoT)", value=True)
    creativity_level = st.slider("✨ Creativity / Temperature", 0.0, 1.0, 0.7)
    
    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("<p style='text-align: center; color: #7f52a0; font-size: 12px;'>Autonomous Security & AI Engine v5.0</p>", unsafe_allow_html=True)

# ----------------------------------------------------
# MAIN CHAT INTERFACE
# ----------------------------------------------------
st.title("🌌 MHZALY Omni-AI Assistant")
st.markdown("Duniya ke तमाम advanced AI features (Reasoning, Multi-language Coding, Visual Parsing, aur Ultra-fast Streaming) ka complete local hub.")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Message History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image" in message and message["image"]:
            st.image(message["image"], width=300)

# Simulated Response Generator with All Advanced Features
def omni_response_generator(query, persona, lang, reasoning):
    # 1. Chain-of-Thought Reasoning simulation (DeepSeek / OpenAI o1 style)
    if reasoning:
        yield "🔍 **Thinking Process & Chain of Thought:**\n"
        yield f"- Analyzing user intent for query: *'{query}'*\n"
        yield f"- Evaluating against architecture parameters ({persona})\n"
        yield f"- Optimizing script structure for target language: **{lang}**\n\n---\n\n"
        time.sleep(0.3)

    # 2. Core Response / Code Generation
    if "code" in query.lower() or "likho" in query.lower() or "script" in query.lower():
        code_text = f"💻 **Advanced Generated Script ({lang}):**\n\n"
        code_text += f"```{lang.lower()}\n"
        code_text += f"# MHZALY Omni-Engine Automated Production Script\n"
        code_text += f"# Target Task: {query}\n"
        code_text += f"import sys\nimport os\n\n"
        code_text += f"def main():\n"
        code_text += f"    print('[+] Initializing secure execution module...')\n"
        code_text += f"    # Executing operational logic\n"
        code_text += f"    return True\n\n"
        code_text += f"if __name__ == '__main__':\n"
        code_text += f"    main()\n"
        code_text += f"```\n\nTask successfully compiled with zero external latency!"
        for word in code_text.split(" "):
            yield word + " "
            time.sleep(0.015)
    else:
        general_text = f"⚡ **Omni Intelligence Response:**\nAapka task (*'{query}'*) successfully process ho gaya hai. Yeh system duniya ki kisi bhi programming language mein code likhne, complex logic ko step-by-step solve karne, aur visual data ko parse karne ki mukammal salahiyat rakhta hai."
        for word in general_text.split(" "):
            yield word + " "
            time.sleep(0.015)

# Input Layout (Text + Image Upload)
col1, col2 = st.columns([6, 1])
with col1:
    user_prompt = st.text_input("Apna task, sawal, ya code requirement yahan likhein...", placeholder="e.g., Python mein Port Scanner likho ya logic samjhao...")
with col2:
    uploaded_image = st.file_uploader("Upload", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if st.button("Send Request 🚀", use_container_width=True) or user_prompt:
    if user_prompt or uploaded_image:
        user_message_content = user_prompt if user_prompt else "[Visual Asset Uploaded]"
        st.session_state.messages.append({"role": "user", "content": user_message_content, "image": uploaded_image})
        
        with st.chat_message("user"):
            st.markdown(user_message_content)
            if uploaded_image:
                st.image(uploaded_image, width=300)

        with st.chat_message("assistant"):
            if uploaded_image:
                st.markdown("📸 **Visual Intelligence:** Image layout and visual data parsed successfully.")
            
            # Stream response word-by-word
            response = st.write_stream(omni_response_generator(
                user_prompt if user_prompt else "Analyze uploaded image", 
                ai_personality, 
                target_language, 
                enable_reasoning
            ))
            
        st.session_state.messages.append({"role": "assistant", "content": response})
