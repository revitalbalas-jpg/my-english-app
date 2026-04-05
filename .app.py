import streamlit as st
import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

# כותרות מעוצבות
st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant | Inspired by 'Module G Writing' Guide")

# Sidebar להגדרות
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.markdown("---")
    st.info("Tip: Use Band III vocabulary to reach the 'Brilliant' level!")

# שלב 1: הזנת נושא
topic = st.text_input("Step 1: What is your essay topic?", placeholder="e.g., Should schools emphasize academic subjects or life skills?")

if topic:
    st.divider()
    if not api_key:
        st.warning("Please enter your API Key in the sidebar to start.")
    else:
        try:
            # הגדרת ה-API
            genai.configure(api_key=api_key)
            # שימוש במודל יציב
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")

            # שלב 2: בניית טיעונים ואוצר מילים
            st.header("Step 2: Argument Builder & Vocabulary 💡")
            
            prompt = f"""
            The essay topic is: '{topic}'.
            Provide a table for a high-school student (Module G level).
            Include 3 arguments (2 pro, 1 con).
            Table columns: 
            - Argument (Short name)
            - Basic Level (3-unit English)
            - Brilliant Level (Module G - using Band III and complex structures)
            - Vocabulary (List advanced words from the brilliant version with Hebrew translations)
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
                st.write("Draft your essay here (120-140 words):")
                user_essay = st.text_area("Your Draft:", height=350)
                check_button = st.button("Check My Essay 📊")

            with col2:
                if check_button and user_essay:
                    with st.spinner("Analyzing your writing..."):
                        check_prompt = f"""
                        Evaluate this essay on the topic '{topic}' based on Module G criteria (Content, Vocabulary, Language).
                        1. Give a score estimate (out of 40).
                        2. Identify 3 'Basic' sentences from the student's text.
                        3. For each, show how to 'Upgrade' it to a 'Brilliant' level (Module G).
                        4. Provide a short list of 5 Band III words they should add to improve.
                        
                        Essay: {user_essay}
                        """
                        feedback = model.generate_content(check_prompt)
                        st.markdown("### 📋 Evaluation & Upgrades")
                        st.write(feedback.text)
                elif check_button:
                    st.error("Please write your essay first!")

        except Exception as e:
            st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Developed to help students excel in the G-Module writing task. 🌟")
