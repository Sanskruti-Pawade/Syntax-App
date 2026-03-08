import streamlit as st
import google.generativeai as genai

# --- 1. SETUP (The Secure Way) ---
# This line tells the app to look inside your 'secrets.toml' notepad file
API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=API_KEY, transport='rest')
model = genai.GenerativeModel('gemini-2.5-flash')

# --- 2. THE INTERFACE (Centered & Shifted Up) ---
st.set_page_config(
    page_title="Syntax", 
    page_icon="🎯", 
    layout="centered",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d041a 0%, #3d0a3d 50%, #800b4d 100%);
    }
    .main .block-container {
        padding-top: 0.1rem !important;
        margin-top: -30px !important; 
        text-align: center;
    }
    h1 { color: #ffffff !important; text-align: center; font-weight: 800; margin-bottom: -5px !important; }
    .tagline { 
        color: #d1d5db !important; 
        text-align: center; 
        font-size: 1.3em !important; 
        font-style: normal !important; 
        font-weight: 500;
        margin-bottom: 12px !important;
    }
    .stTextArea label p {
        color: #ffffff !important;
        font-weight: normal !important;
        font-size: 1.05rem !important; 
        text-align: center !important;
        display: block;
        width: 100%;
        margin-bottom: 5px !important;
    }
    .stTextArea textarea {
        background-color: #0d1117 !important;
        color: #ffffff !important; 
        border: 2px solid rgba(255,255,255,0.2) !important;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        padding: 15px;
    }
    .stButton>button {
        background: linear-gradient(to right, #b31217, #d6006e) !important;
        color: white !important;
        border: 2px solid #ffffff !important; 
        border-radius: 12px;
        width: 100%;
        font-weight: bold;
        padding: 12px;
        margin-top: 5px !important;
    }
    .stSpinner p {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.25rem !important;
        text-align: center;
    }
    .result-card {
        background-color: rgba(13, 17, 23, 0.95);
        color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1);
        margin-top: 15px;
        text-align: left;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. THE LAYOUT ---
st.title("🎯 Syntax")
st.markdown('<p class="tagline">Hitting the mark on every line of code.</p>', unsafe_allow_html=True)

user_code = st.text_area("Paste your code here:", height=350)

if st.button("Hit the Mark"):
    if user_code:
        with st.spinner("Syntax is aiming..."):
            try:
                prompt = "Identify language, fix errors, and give 3 practice questions for: " + user_code
                response = model.generate_content(prompt)
                st.divider()
                st.markdown(f'<div class="result-card">{response.text}</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Note: {e}")
    else:
        st.warning("Please paste your code first!")