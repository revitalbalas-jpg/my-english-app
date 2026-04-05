import streamlit as st
import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant")

# Sidebar
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")

# שלב 1: נושא
topic = st.text_input("Step 1: What is the essay topic?")

if topic:
    if not api_key:
        st.warning("Please enter your API Key in the sidebar.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            st.header("Step 2: Suggestions 💡")
            prompt = f"Provide a table for Module G level on the topic: {topic}. Include arguments and Band III vocabulary with Hebrew translations."
            
            with st.spinner("Generating..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
