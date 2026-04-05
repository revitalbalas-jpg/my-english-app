import streamlit as st
import google.generativeai as genai

# הגדרות תצוגה
st.set_page_config(page_title="Module G Writing Master", layout="wide", initial_sidebar_state="expanded")

# עיצוב כותרות
st.title("🎓 Module G: Writing Master")
st.subheader("From Basic to Brilliant | Inspired by 'Module G Writing' Guide")

# Sidebar - הגדרות ומפתחות
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.markdown("---")
    st.info("This app helps students upgrade their writing from 3-4 points level to a high 5-points level.")

# שלב 1: הזנת נושא
topic = st.text_input("Step 1: What is your essay topic?", placeholder="e.g., Should students have a four-day school week?")

if topic:
    st.divider()
    if not api_key:
        st.warning("Please enter your API Key in the sidebar to generate arguments.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')

            # יצירת טבלת טיעונים (Basic vs Brilliant)
            st.header("Step 2: Argument Builder & Vocabulary 💡")
            
            prompt = f"""
            The topic is: '{topic}'.
            Create a table for a Module G student with 3 arguments (2 pro, 1 con).
            Columns: 
            1. 'The Idea' (short name)
            2. 'Basic Level' (Simple 3-unit English)
            3. 'Brilliant Level' (High 5-unit English using Band III, connectors, and complex grammar)
            4. 'Keywords' (Advanced words with Hebrew translation)
            """
            
            with st.spinner("Building your brilliant arguments..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)

            st.divider()
            
            # שלב 3: כתיבה ובדיקה
            st.header("Step 3: Write & Get Feedback ✍️")
            col_a, col_b = st.columns([1, 1])
            
            with col_a:
                st.write("Draft your essay here (120-140 words):")
                user_essay = st.text_area("Your Essay:", height=400)
                analyze_button = st.button("Check My Essay 📊")

            with col_b:
                if analyze_button and user_essay:
                    with st.spinner("Analyzing according to Module G Rubric..."):
                        # פרוםט בדיקה מפורט לפי הקריטריונים של הבגרות
                        check_prompt = f"""
                        Analyze the following essay on the topic '{topic}' based on the official Module G rubric:
                        1. Content (Are the ideas relevant and well-developed?)
                        2. Vocabulary (Is there enough Band III and varied language?)
                        3. Language Use (Grammar, spelling, and punctuation).
                        
                        For each category:
                        - Give a brief comment.
                        - Identify 3 'Basic' sentences and show how to 'Upgrade' them to 'Brilliant' level.
                        - Give a total estimated score (out of 40).
                        
                        Essay: {user_essay}
                        """
                        feedback = model.generate_content(check_prompt)
                        st.markdown("### 📋 Expert Feedback")
                        st.write(feedback.text)
                elif analyze_button:
                    st.error("Please write something before clicking check!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

# עיצוב תחתון
st.markdown("---")
st.caption("Developed for English Teachers and Students | Aim for Excellence 🌟")
