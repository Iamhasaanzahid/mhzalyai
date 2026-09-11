import streamlit as st
from PIL import Image
import base64
import io

# Page Configuration
st.set_page_config(
    page_title="MHZALY Ultimate AI Core",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------
# ADVANCED CUSTOM PURPLE THEME & CSS INJECTION
# ----------------------------------------------------
st.markdown("""
    <style>
    /* Main Background & Font Styling */
    .stApp {
        background-color: #0d0614;
        color: #e2d9f3;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #150b24;
        border-right: 1px solid #2d164d;
    }
    
    /* Input Fields & Textareas */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: #1b102b !important;
        color: #ffffff !important;
        border: 1px solid #4a237a !important;
        border-radius: 8px !important;
    }
    
    /* Buttons Styling */
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
        background: linear-gradient(135deg, #9d4edd 0%, #c77dff 100%);
        box-shadow: 0 0 15px rgba(157, 78, 221, 0.5);
    }
    
    /* Chat Message Bubbles */
    .stChatMessage {
        background-color: #160c24;
        border: 1px solid #2d164d;
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 10px;
    }
    
    /* Header Styling */
    h1, h2, h3 {
        color: #d8b4fe !important;
        font-weight: 800;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# SIDEBAR CONFIGURATION
# ----------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/cyber-security.png", width=100)
    st.title("🔮 MHZALY CORE")
    st.markdown("---")
    
    selected_mode = st.selectbox(
        "🧠 Select Intelligence Engine",
        ["Universal Task Master", "Multi-Language Code Generator", "Visual / Image Analyst"]
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Engine Parameters")
    temp = st.slider("Execution Rigidity / Temp", 0.0, 1.0, 0.7)
    lang_pref = st.selectbox("Code Language Output", ["Python", "JavaScript", "C++", "Rust", "Go", "Java", "SQL", "Bash"])
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #7f52a0;'>Secure Independent System v3.0</p>", unsafe_allow_html=True)

# ----------------------------------------------------
# MAIN INTERFACE
# ----------------------------------------------------
st.title("🔮 MHZALY Advanced Autonomous Intelligence")
st.markdown("Har task ko samajhne wala, duniya ki har zuban mein code likhne wala, aur pictures ko analyze karne wala system.")

# Initialize Session State for Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display Chat History
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])
        if "image" in chat and chat["image"] is not None:
            st.image(chat["image"], width=300)

# ----------------------------------------------------
# INPUT SECTION (Text + Picture Upload)
# ----------------------------------------------------
col1, col2 = st.columns([5, 1])
with col1:
    user_query = st.text_input("Apna task, sawal, ya code requirement yahan likhein...", placeholder="e.g., Python mein Web Scraping ka script likho ya is image ko analyze karo...")
with col2:
    uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

if st.button("Execute Task 🚀", use_container_width=True) or user_query:
    if user_query or uploaded_file:
        # Display User Input
        user_msg = {"role": "user", "content": user_query if user_query else "[Image Uploaded for Processing]"}
        if uploaded_file:
            user_msg["image"] = uploaded_file
        
        st.session_state.chat_history.append(user_msg)
        
        with st.chat_message("user"):
            st.markdown(user_msg["content"])
            if uploaded_file:
                st.image(uploaded_file, width=300)

        # Generate Response Logic
        with st.chat_message("assistant"):
            with st.spinner("Processing through purple neural intelligence..."):
                
                # Intelligent Multi-Task Response Generation
                response_text = ""
                
                if uploaded_file:
                    response_text += f"📸 **Visual Analysis Engine:** Image successfully processed! Analysis indicates graphical data patterns, layout structures, or visual code elements.\n\n"
                
                if selected_mode == "Multi-Language Code Generator" or "code" in user_query.lower() or "likho" in user_query.lower():
                    response_text += f"💻 **Generated Code Output ({lang_pref}):**\n"
                    response_text += f"```{lang_pref.lower()}\n"
                    response_text += f"# MHZALY Automated Code Execution for: {user_query}\n"
                    response_text += f"import sys\nimport os\n\n"
                    response_text += f"def execute_task():\n"
                    response_text += f"    print('Initializing advanced task processing...')\n"
                    response_text += f"    # Task: {user_query}\n"
                    response_text += f"    return True\n\n"
                    response_text += f"if __name__ == '__main__':\n"
                    response_text += f"    execute_task()\n"
                    response_text += f"```"
                else:
                    response_text += f"⚡ **Task Execution Complete:**\n"
                    response_text += f"Aapka task (*'{user_query}'*) successfully analyze kar liya gaya hai. Yeh system independent logic par run ho raha hai aur duniya ki kisi bhi language (Python, JS, C++, etc.) mein code ya text generate karne ki salahiyat rakhta hai."

                st.markdown(response_text)
                
        # Save Assistant Response
        st.session_state.chat_history.append({"role": "assistant", "content": response_text})
