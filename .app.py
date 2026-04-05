import os
import subprocess
import sys
import streamlit as st

# מנגנון להבטחת גרסה מעודכנת של הספרייה
try:
    import google.generativeai as genai
    # בדיקה אם הגרסה תומכת ב-1.5 (לפחות 0.5.0)
    import pkg_resources
    version = pkg_resources.get_distribution("google-generativeai").version
    if version < "0.5.0":
        raise ImportError("Version too old")
except (ImportError, pkg_resources.DistributionNotFound):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "google-generativeai>=0.5.0"])
    import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant | Step-by-Step Essay Helper")

# Sidebar להגדרות
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("The app is now forcing a library update to avoid 404 errors.")

# שלב 1: הזנת נושא
topic = st.text_input("Step 1: What is the essay topic?", placeholder="e.g., Should students use AI in schools?")

if topic:
    st.divider()
    if not api_key:
        st.warning("Please enter your API Key in the sidebar to start.")
    else:
        try:
            # הגדרת ה-API
            genai.configure(api_key=api_key)
            
            # שימוש במודל - שימי לב לשם המדויק
            model = genai.GenerativeModel('gemini-1.5-flash')

            # שלב 2: בניית טיעונים ואוצר מילים
            st.header("Step 2: Argument Builder & Vocabulary 💡")
            
            prompt = f"""
            The essay topic is: '{topic}'.
            Provide a table for a high-school student (Module G level).
            Include 3 arguments (2 pro, 1 con).
            Table columns: 
            - Argument (Short name)
            - Basic Level (Simple English)
            - Brilliant Level (Module G - using Band III and complex structures)
            - Vocabulary (Advanced words from the brilliant version with Hebrew translations)
            Format as a Markdown table.
            """
            
            with st.spinner("Generating brilliant ideas..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)

            st.divider()
            
            # שלב 3: כתיבה ומשוב
            st.header("Step 3: Write & Upgrade Your Essay ✍️")
            col1, col2 = st.columns(2)
            
            with col1:
                user_essay = st.text_area("Draft your essay here (120-140 words):", height=350)
                check_button = st.button("Check My Essay 📊")

            with col2:
                if check_button and user_essay:
                    with st.spinner("Analyzing your writing..."):
                        check_prompt = f"""
                        Evaluate this essay on the topic '{topic}' based on Module G criteria.
                        1. Give a score estimate (out of 40).
                        2. Identify 3 'Basic' sentences and show how to 'Upgrade' them to 'Brilliant' level.
                        3. Provide 5 Band III words to add.
                        
                        Essay: {user_essay}
                        """
                        feedback = model.generate_content(check_prompt)
                        st.markdown("### 📋 Evaluation & Upgrades")
                        st.write(feedback.text)

        except Exception as e:
            st.error(f"Error details: {e}")
            st.info("If you see '404', wait 1 minute and refresh the page.")

st.markdown("---")
st.caption("Success in Module G starts with the right vocabulary! 🌟")
