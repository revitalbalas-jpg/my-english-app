import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="G-Module Master", layout="wide")

# כותרת האתר
st.title("📝 Bagrut 5-Points: Writing Master")
st.markdown("### From Basic to Brilliant - Writing Guide")

# Sidebar להגדרות
with st.sidebar:
    st.header("Settings ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Get your key from [Google AI Studio](https://aistudio.google.com/)")

# שלב 1: נושא החיבור
topic = st.text_input("Step 1: What is the essay topic?", placeholder="e.g., Should schools start at 10:00 AM?")

if topic:
    st.divider()
    st.header("Step 2: The Essay Blueprint 🗺️")
    st.info(f"Topic: {topic}")

    # טבלת תבניות - בסיסי מול מתקדם
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Writing 😕")
        st.write("**Intro:** I think that...")
        st.write("**Body 1:** First, I want to say...")
        st.write("**Contrast:** But some people think...")
        st.write("**Conclusion:** To sum up, I believe...")

    with col2:
        st.subheader("Brilliant Writing (Band III) ✨")
        st.write("**Intro:** The question of whether... has sparked a *heated debate*.")
        st.write("**Body 1:** *To begin with*, it is *widely acknowledged* that...")
        st.write("**Contrast:** *On the other hand*, *proponents* of the opposing view argue...")
        st.write("**Conclusion:** *In light of the above*, it is *evident* that...")

    # חיבור ל-AI ליצירת תוכן ספציפי
    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Topic: {topic}. Give 3 specific arguments (2 pro, 1 con) using Band III vocabulary. Provide Hebrew translations for difficult words."
            response = model.generate_content(prompt)
            st.success("Custom Ideas for your Topic 💡")
            st.write(response.text)
        except:
            st.warning("Enter a valid API key to get custom ideas.")

    st.divider()
    st.header("Step 3: Draft Your Essay ✍️")
    essay_text = st.text_area("Write your 120-140 words essay here:", height=300)

    if st.button("Analyze My Writing 📊"):
        if api_key:
            with st.spinner("Checking..."):
                check_prompt = f"Evaluate this essay on '{topic}' based on Module G rubric. Focus on Band III usage. Essay: {essay_text}"
                res = model.generate_content(check_prompt)
                st.markdown("### Feedback:")
                st.write(res.text)
        else:
            st.error("Please enter your API Key to get feedback.")
