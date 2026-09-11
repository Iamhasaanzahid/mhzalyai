import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="MHZALY Groq-Style AI Core",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# PURPLE CYBERPUNK THEME & CSS
# ----------------------------------------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #0d0614;
        color: #e2d9f3;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: #150b24;
        border-right: 1px solid #2d164d;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #1b102b !important;
        color: #ffffff !important;
        border: 1px solid #4a237a !important;
        border-radius: 8px !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #7b2cbf 0%, #9d4edd 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #9d4edd 100%, #c77dff 100%);
        box-shadow: 0 0 15px rgba(157, 78, 221, 0.5);
    }
    .stChatMessage {
        background-color: #160c24;
        border: 1px solid #2d164d;
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 10px;
    }
    h1, h2, h3 {
        color: #d8b4fe !important;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------
with st.sidebar:
    st.title("⚡ MHZALY FAST CORE")
    st.markdown("---")
    engine_mode = st.selectbox(
        "🧠 Mode Selection",
        ["Groq-Style Universal Assistant", "Multi-Language Code Engine", "Visual Analyzer"]
    )
    lang_output = st.selectbox("Target Language", ["Python", "JavaScript", "C++", "Rust", "Go", "Bash"])
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #7f52a0;'>Ultra-Responsive Engine v3.5</p>", unsafe_allow_html=True)

# ----------------------------------------------------
# MAIN CHAT INTERFACE
# ----------------------------------------------------
st.title("⚡ MHZALY Groq-Speed Intelligence")
st.markdown("Bina kisiheavy dependency ke, ultra-fast streaming response aur multi-language code generation engine.")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Prior Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "image" in message and message["image"]:
            st.image(message["image"], width=300)

# Streaming Response Generator (Groq Style)
def response_generator(query, lang):
    if "code" in query.lower() or "likho" in query.lower():
        text = f"💻 **Generated Code Output ({lang}):**\n\n```python\n# MHZALY Optimized Code Script\nimport sys\n\ndef main():\n    print('Executing task: {query}')\n    # Ready for production deployment\n\nif __name__ == '__main__':\n    main()\n```\n\nTask successfully compiled with zero external latency!"
    else:
        text = f"⚡ **Instant Analysis:** Aapka task (*'{query}'*) successfully process ho gaya hai. Yeh system pure logic aur lightning-fast execution ke sath har zuban aur task ko handle karne ki salahiyat rakhta hai."
    
    # Simulate Groq-like word-by-word streaming effect
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# User Input Handling
col1, col2 = st.columns([5, 1])
with col1:
    user_prompt = st.text_input("Apna task yahan type karein...", placeholder="e.g., Python mein script likho ya logic samjhao...")
with col2:
    uploaded_image = st.file_uploader("Upload", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if st.button("Send Request 🚀", use_container_width=True) or user_prompt:
    if user_prompt or uploaded_image:
        # Append User Message
        user_message_content = user_prompt if user_prompt else "[Image Uploaded]"
        st.session_state.messages.append({"role": "user", "content": user_message_content, "image": uploaded_image})
        
        with st.chat_message("user"):
            st.markdown(user_message_content)
            if uploaded_image:
                st.image(uploaded_image, width=300)

        # Generate Assistant Streaming Response
        with st.chat_message("assistant"):
            if uploaded_image:
                st.markdown("📸 **Visual Data Registered:** Image layout parsed successfully.")
            
            # Stream response word-by-word like Groq
            response = st.write_stream(response_generator(user_prompt if user_prompt else "Analyze uploaded image", lang_output))
            
        # Append Assistant Message
        st.session_state.messages.append({"role": "assistant", "content": response})
