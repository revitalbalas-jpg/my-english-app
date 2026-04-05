import streamlit as st
import os
import subprocess
import sys

# מנגנון להבטחת ספרייה מעודכנת ומניעת שגיאות 404
try:
    import google.generativeai as genai
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai>=0.5.0"])
    import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant | Adapted for 5-Unit Students")

# Sidebar
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("The app is optimized for clear, high-level high school English.")

# שלב 1: נושא
topic = st.text_input("Step 1: What is the essay topic?", placeholder="e.g., The impact of AI on education")

if topic:
    st.divider()
    if not api_key:
        st.warning("Please enter your API Key in the sidebar.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')

            # שלב 2: בניית טיעונים מותאמים
            st.header("Step 2: Argument Builder & Vocabulary 💡")
            
            # הנחיה ל-AI לייצר רמת "אמצע" מתאימה
            prompt = f"""
            Topic: {topic}. 
            Create a table for Israeli high school students (Module G, 5 units).
            Language should be high-level but accessible (not academic/PhD level).
            Include 3 arguments.
            Columns: 
            1. 'Argument' (Short title)
            2. 'Basic Level' (Simple 3-unit sentence)
            3. 'Module G Level' (Using clear connectors like 'Furthermore', 'However' and phrases like 'Take advantage of')
            4. 'Keywords' (5-unit vocabulary words with Hebrew translation)
            """
            
            with st.spinner("Generating ideas for your students..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)

            st.divider()
            
            # שלב 3: כתיבה ומשוב
            st.header("Step 3: Write & Get Feedback ✍️")
            user_essay = st.text_area("Write your essay (120-140 words):", height=300)
            
            if st.button("Check My Essay 📊"):
                if user_essay:
                    with st.spinner("Analyzing..."):
                        # הנחיה למשוב מאוזן
                        check_prompt = f"""
                        Evaluate this essay on '{topic}' for Module G.
                        1. Estimated Score (out of 40).
                        2. Content & Language: Give 3 tips to make the English sound more natural for a 5-unit student.
                        3. Show 3 sentences from the essay and suggest a 'Module G' upgrade for each.
                        Essay: {user_essay}
                        """
                        feedback = model.generate_content(check_prompt)
                        st.markdown("### 📋 Evaluation & Tips")
                        st.write(feedback.text)
                else:
                    st.error("Please write your essay first!")

        except Exception as e:
            if "404" in str(e):
                st.error("Server is updating. Please refresh in 1 minute.")
            else:
                st.error(f"Error: {e}")

st.markdown("---")
st.caption("Helping students reach their potential in English. 🌟")
