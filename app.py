import streamlit as st
import datetime
import re

st.set_page_config(
    page_title="MHZALY Pure Python Omni Assistant",
    page_icon="⚡",
    layout="wide"
)

# ----------------------------------------------------
# ADVANCED PURE PYTHON PROCEDURAL ENGINE
# ----------------------------------------------------
class PurePythonAssistant:
    def __init__(self):
        self.version = "15.1-OFFLINE"
        self.supported_langs = ["Python", "JavaScript", "C++", "Rust", "Go", "Bash", "Java", "SQL"]

    def evaluate_query(self, query: str, target_lang: str, chat_history: list) -> str:
        q = query.lower().strip()
        
        if any(w in q for w in ['hi', 'hello', 'salam', 'hey', 'assalam']):
            return "Walaikum Assalam! Main aapka 100% offline, independent Python assistant hoon. Bataiye, aaj konsa task ya code likhwana hai?"
        
        elif any(w in q for w in ['kaise ho', 'how are you']):
            return "Main bilkul theek hoon! Systems fully operational hain aur bina kisi API ke local logic par run ho rahe ہیں۔"

        elif any(w in q for w in ['code', 'script', 'program', 'likho', 'banao', 'generate', 'function']):
            return self._generate_dynamic_code(query, target_lang)

        elif any(w in q for w in ['log', 'scan', 'ip', 'threat', 'security', 'analyze', 'parse']):
            return self._perform_regex_triage(query)

        elif any(w in q for w in ['time', 'date', 'status', 'waqt']):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"⚡ **System Status:** Timestamp: `{now}` | Mode: 100% Offline Python Logic."

        else:
            return self._generate_conversational_fallback(query, target_lang)

    def _generate_dynamic_code(self, task: str, lang: str) -> str:
        templates = {
            "Python": (
                f"# Autonomous Python Script\n"
                f"# Objective: {task}\n"
                "import sys\nimport os\nimport datetime\n\n"
                "def main_process():\n"
                f"    print(f'[*] Initializing execution for: {task}')\n"
                "    try:\n"
                "        print('[+] Task completed successfully.')\n"
                "    except Exception as e:\n"
                "        print(f'[-] Error: {{e}}')\n\n"
                "if __name__ == '__main__':\n"
                "    main_process()"
            ),
            "JavaScript": (
                f"// Autonomous Node.js Script\n"
                f"// Objective: {task}\n"
                "const fs = require('fs');\n\n"
                "function executeTask() {\n"
                f"    console.log('[*] Running Node execution for: {task}');\n"
                "}\n\n"
                "executeTask();"
            ),
            "C++": (
                f"// Autonomous C++ Binary Source\n"
                f"// Objective: {task}\n"
                "#include <iostream>\n"
                "#include <string>\n\n"
                "using namespace std;\n\n"
                "int main() {\n"
                f"    cout << \"[*] Executing C++ module for: {task}\" << endl;\n"
                "    return 0;\n"
                "}"
            ),
            "Rust": (
                f"// Autonomous Rust Program\n"
                f"// Objective: {task}\n"
                "fn main() {{\n"
                f"    println!(\"[*] Running Rust routine for: {{}}\", \"{task}\");\n"
                "}}"
            ),
            "Go": (
                f"// Autonomous Go Routine\n"
                f"// Objective: {task}\n"
                "package main\nimport \"fmt\"\n\n"
                "func main() {\n"
                f"    fmt.Println(\"[*] Executing Go service for: {task}\")\n"
                "}"
            )
        }
        
        default_code = f"// Language: {lang}\n// Task: {task}\n// Status: Procedurally compiled via local engine."
        code_body = templates.get(lang, default_code)
        
        return f"💻 **Generated Code ({lang}):**\n```{lang.lower()}\n{code_body}\n```\n\nAap is code mein mazeed modifications ya functions add karwa sakte hain."

    def _perform_regex_triage(self, data: str) -> str:
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        url_pattern = r'https?://[^\s]+'
        
        ips = re.findall(ip_pattern, data)
        urls = re.findall(url_pattern, data)
        
        return (
            f"🛡️ **Local Regex & Text Analysis Report:**\n"
            f"- Extracted IP Addresses: `{list(set(ips)) if ips else 'None found'}`\n"
            f"- Extracted URLs: `{list(set(urls)) if urls else 'None found'}`\n"
            f"- Input String Length: {len(data)} characters\n"
            f"- Analysis Method: Native Python Regex Engine (Zero API)."
        )

    def _generate_conversational_fallback(self, query: str, lang: str) -> str:
        return (
            f"💬 **MHZALY Conversational Core:**\n"
            f"Aapne jo sawal ya task diya hai (*'{query}'*), use mainay local logic ke tehet analyze kar liya hai. "
            f"Kyunki yeh system 100% independent aur offline hai, yeh predefined linguistic patterns aur dynamic code templates par execute hota hai.\n\n"
            f"Agar aapko isay kisi specific programming language (**{lang}**) mein convert karwana hai ya koi automation script banwani hai, toh bas bataiye!"
        )

assistant = PurePythonAssistant()

# ----------------------------------------------------
# UI STYLING (Purple Theme)
# ----------------------------------------------------
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

with st.sidebar:
    st.title("⚡ OFFLINE ASSISTANT")
    st.markdown("---")
    selected_language = st.selectbox("Target Programming Language", assistant.supported_langs)
    st.markdown("---")
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.markdown(f"<p style='text-align: center; color: #7f52a0;'>Engine: v{assistant.version}</p>", unsafe_allow_html=True)

st.title("⚡ MHZALY Independent Chat Assistant")
st.markdown("100% Offline, Pure Python Logic, Zero APIs, Zero Heavy Dependencies.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Apna sawal ya task yahan type karein..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Processing locally..."):
            response_text = assistant.evaluate_query(user_input, selected_language, st.session_state.messages)
            st.markdown(response_text)
            
    st.session_state.messages.append({"role": "assistant", "content": response_text})
