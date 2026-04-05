import streamlit as st
import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant")

# משיכת המפתח מה-Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Please set your API Key in the Streamlit Secrets!")
    st.stop()

# שלב 1: נושא
topic = st.text_input("Step 1: What is the essay topic?", placeholder="e.g., AI in Education")

if topic:
    st.header("Step 2: Suggestions & Content 💡")
    
    # הנחיה לבינה המלאכותית להשתמש באוצר המילים של "האמצע"
    prompt = f"""
    Topic: {topic}. 
    Create a table for Israeli high school students (Module G).
    Include 3 arguments.
    Columns: 
    1. 'Argument'
    2. 'Basic (3 Units)'
    3. 'Module G (5 Units)' -> Use words like 'Transform', 'Efficiency', 'Opportunity'.
    4. 'Key Vocabulary' -> Band III words with Hebrew translation.
    """
    
    with st.spinner("Generating high-quality content..."):
        response = model.generate_content(prompt)
        st.markdown(response.text)
