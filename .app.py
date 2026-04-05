import streamlit as st
import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant | Inspired by 'Module G Writing' Guide")

# Sidebar
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Ensure your requirements.txt is updated!")

# שלב 1: נושא
topic = st.text_input("Step 1: What is the essay topic?", placeholder="e.g., The role of schools in the 21st century")

if topic:
    st.divider()
    if not api_key:
        st.warning("Please enter your API Key in the sidebar.")
    else:
        try:
            # הגדרה ספציפית למניעת שגיאת 404
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-flash')

            # שלב 2: בניית טיעונים (Basic to Brilliant)
            st.header("Step 2: Argument Builder & Vocabulary 💡")
            
            prompt = f"""
            The topic is: '{topic}'. Create a table with 3 arguments (2 pro, 1 con).
            Columns:
            1. 'The Idea'
            2. 'Basic Level' (3-unit sentence)
            3. 'Brilliant Level' (Module G level, Band III, complex grammar)
            4. 'Keywords' (Advanced words with Hebrew translation)
            """
            
            with st.spinner("Generating brilliant ideas..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)

            st.divider()
            
            # שלב 3: כתיבה ובדיקה
            st.header("Step 3: Write & Get Expert Feedback ✍️")
            col_a, col_b = st.columns(2)
            
            with col_a:
                user_essay = st.text_area("Write your essay (120-140 words):", height=400)
                if st.button("Check My Essay 📊"):
                    if user_essay:
                        with st.spinner("Analyzing..."):
                            check_prompt = f"Evaluate this essay on '{topic}' based on Module G criteria. 1. Score estimate (out of 40). 2. Show 3 'Basic' sentences and their 'Brilliant' upgrades. 3. List 5 Band III words to add. Essay: {user_essay}"
                            feedback = model.generate_content(check_prompt)
                            with col_b:
                                st.markdown("### 📋 Evaluation")
                                st.write(feedback.text)
                    else:
                        st.error("Please write something first!")

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("Developed for Excellence in English Writing 🌟")
