import streamlit as st
import os

# ניסיון לייבוא הספרייה, ואם היא חסרה - התקנה שקטה
try:
    import google.generativeai as genai
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant | Improve Your Writing")

# Sidebar
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Tip: If you get a 404 error, wait a minute for the server to update.")

# שלב 1: נושא
topic = st.text_input("Step 1: What is your essay topic?", placeholder="e.g., Should students study art in school?")

if topic:
    st.divider()
    if not api_key:
        st.warning("Please enter your API Key in the sidebar.")
    else:
        try:
            # הגדרת ה-API
            genai.configure(api_key=api_key)
            
            # הגדרת המודל - שימוש בגרסה יציבה
            model = genai.GenerativeModel('gemini-1.5-flash')

            # שלב 2: בניית טיעונים
            st.header("Step 2: Argument Builder & Vocabulary 💡")
            
            prompt = f"Topic: {topic}. Create a table for Module G high school level. 3 arguments. Columns: Argument, Basic Sentence, Brilliant Sentence (Band III), Hebrew Vocabulary."
            
            with st.spinner("Generating ideas..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)

            st.divider()
            
            # שלב 3: כתיבה ומשוב
            st.header("Step 3: Essay Feedback ✍️")
            user_essay = st.text_area("Write your essay (120-140 words):", height=300)
            
            if st.button("Get Feedback 📊"):
                if user_essay:
                    with st.spinner("Analyzing..."):
                        check_prompt = f"Evaluate this essay on {topic} for Module G. Score, 3 sentence upgrades, and 5 Band III words to add. Essay: {user_essay}"
                        feedback = model.generate_content(check_prompt)
                        st.markdown("### 📋 Evaluation")
                        st.write(feedback.text)
                else:
                    st.error("Please write your essay first!")

        except Exception as e:
            # הודעת שגיאה ידידותית יותר
            if "404" in str(e):
                st.error("The model is still updating on the server. Please wait 1-2 minutes and refresh the page.")
            else:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Success in Module G starts here! 🌟")
