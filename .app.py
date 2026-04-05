import streamlit as st
import google.generativeai as genai

# הגדרות עמוד
st.set_page_config(page_title="Module G Writing Master", layout="wide")

st.title("🎓 Module G: Writing Master")
st.markdown("### From Basic to Brilliant | Improve Your Writing for 5 Points")

# Sidebar
with st.sidebar:
    st.header("Setup ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Make sure requirements.txt includes: google-generativeai>=0.5.0")

# שלב 1: נושא
topic = st.text_input("Step 1: Enter your essay topic:", placeholder="e.g., The advantages of physical textbooks")

if topic:
    st.divider()
    if not api_key:
        st.warning("Please enter your API Key in the sidebar.")
    else:
        try:
            # הגדרה מפורשת למניעת שגיאת 404
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name="gemini-1.5-flash")

            # שלב 2: בניית טיעונים (Basic to Brilliant)
            st.header("Step 2: Argument Builder & Vocabulary 💡")
            
            prompt = f"""
            The topic is: '{topic}'. 
            Create a markdown table with 3 main arguments (2 for, 1 against).
            Columns:
            1. 'Argument' (Short title)
            2. 'Basic Level' (Simple 3-unit sentence)
            3. 'Brilliant Level' (Module G level, using Band III vocabulary and connectors)
            4. 'Keywords' (Advanced words from the brilliant version + Hebrew translation)
            """
            
            with st.spinner("Generating brilliant arguments..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)

            st.divider()
            
            # שלב 3: כתיבה ומשוב לפי הקריטריונים של פרחי דיין
            st.header("Step 3: Write & Get Expert Feedback ✍️")
            col_a, col_b = st.columns(2)
            
            with col_a:
                user_essay = st.text_area("Write your essay here (120-140 words):", height=400)
                if st.button("Analyze My Essay 📊"):
                    if user_essay:
                        with st.spinner("Analyzing based on Module G rubric..."):
                            feedback_prompt = f"""
                            Analyze the following essay on '{topic}' based on Module G criteria (Content, Vocabulary, Language Use).
                            1. Estimated Score (out of 40).
                            2. Content: Is it well-developed?
                            3. Vocabulary: Identify 3 'Basic' sentences and show how to 'Upgrade' them to 'Brilliant' level.
                            4. List 5 Band III words they should consider adding.
                            Essay: {user_essay}
                            """
                            feedback = model.generate_content(feedback_prompt)
                            with col_b:
                                st.markdown("### 📋 Evaluation & Upgrades")
                                st.write(feedback.text)
                    else:
                        st.error("Please write your essay first!")

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("Developed to help students reach 'Brilliant' levels in English writing. 🌟")
