import streamlit as st
from PIL import Image
from engine import MHZALYCoreEngine

# Page Layout Setup
st.set_page_config(
    page_title="MHZALY Heavy-Duty Omni Core",
    page_icon="⚡",
    layout="wide"
)

# Initialize Engine Instance
engine = MHZALYCoreEngine()

# Custom Purple Cyberpunk Styling
st.markdown("""
    <style>
    .stApp { background-color: #0b0210; color: #e2d9f3; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #130722; border-right: 1px solid #2a124a; }
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #170a29 !important; color: #ffffff !important; border: 1px solid #5a2295 !important; border-radius: 8px !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #7b2cbf 0%, #b5179e 100%); color: white; border: none; border-radius: 8px; padding: 0.6rem 1.2rem; font-weight: 600;
    }
    .stButton button:hover { background: linear-gradient(135deg, #9d4edd 100%, #f72585 100%); }
    .stChatMessage { background-color: #130722; border: 1px solid #2a124a; border-radius: 12px; padding: 12px; margin-bottom: 12px; }
    h1, h2, h3 { color: #e0aaff !important; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.title("⚡ MHZALY CORE ENGINE")
    st.markdown("---")
    selected_lang = st.selectbox("Select Target Language", engine.supported_languages)
    st.markdown("---")
    if st.button("Clear Memory Cache", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown(f"<p style='text-align: center; color: #7f52a0;'>Engine Version: {engine.version}</p>", unsafe_allow_html=True)

# Main UI Interface
st.title("⚡ MHZALY Autonomous Heavy-Duty Engine")
st.markdown("Real programmatic logic engine—no fake simulations, direct code generation and task execution.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Render Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("image"):
            st.image(message["image"], width=300)

# Input Box & File Uploader
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input("Apna task ya query yahan enter karein...", placeholder="e.g., Python mein Port Scanner script likho...")
with col2:
    uploaded_image = st.file_uploader("Image", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if st.button("Execute Process 🚀", use_container_width=True) or user_input:
    if user_input or uploaded_image:
        query_text = user_input if user_input else "Analyze uploaded image structure"
        
        # Save User Message
        user_msg = {"role": "user", "content": query_text, "image": uploaded_image}
        st.session_state.messages.append(user_msg)
        
        with st.chat_message("user"):
            st.markdown(query_text)
            if uploaded_image:
                st.image(uploaded_image, width=300)

        # Generate Real Response from Engine
        with st.chat_message("assistant"):
            with st.spinner("Executing core logic modules..."):
                if uploaded_image:
                    img = Image.open(uploaded_image)
                    analysis_result = f"📸 **Image Processed Successfully:**\n- Dimensions: {img.size}\n- Format: {img.format}\n- Mode: {img.mode}"
                else:
                    analysis_result = engine.analyze_system_query(query_text, selected_lang)
                
                st.markdown(analysis_result)
                
        # Save Assistant Message
        st.session_state.messages.append({"role": "assistant", "content": analysis_result})
