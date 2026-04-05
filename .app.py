import streamlit as st
import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant")

# ניסיון משיכה מה-Secrets
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Missing API Key! Please add 'GEMINI_API_KEY' to your Streamlit Secrets.")
    st.stop()

# הגדרת המודל בצורה מפורשת
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# שימוש במודל flash-1.5 (הכי יציב כרגע)
model = genai.GenerativeModel('gemini-1.5-flash')

# שלב 1: נושא
topic = st.text_input("Step 1: What is the essay topic?", placeholder="e.g., AI in Education")

if topic:
    st.header("Step 2: Suggestions & Content 💡")
    
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
    
    try:
        with st.spinner("Generating content..."):
            response = model.generate_content(prompt)
            st.markdown(response.text)
    except Exception as e:
        st.error(f"Generation Error: {e}")
