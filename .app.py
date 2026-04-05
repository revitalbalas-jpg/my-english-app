import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Bagrut 5-Points Master", layout="centered")

# כותרת האתר
st.title("📝 Bagrut 5-Points Essay Master")
st.markdown("### Learn, Practice, and Ace your English Examination")

# אזור הגדרת המפתח (API Key) בצד
with st.sidebar:
    st.header("Settings ⚙️")
    api_key = st.text_input("Enter your Gemini API Key:", type="password")
    st.info("Get your key from [Google AI Studio](https://aistudio.google.com/)")

# שלב 1: הזנת נושא
topic = st.text_input("Step 1: Enter your essay topic:", placeholder="e.g., The impact of social media on youth")

if topic:
    st.divider()
    
    # שלב 2: אוצר מילים קבוע (Band III)
    st.header("Step 2: Essential Vocabulary (Band III) 📚")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Connectors")
        st.write("* Furthermore / Moreover\n* Consequently / As a result\n* On the other hand\n* Notwithstanding")
    with col2:
        st.subheader("Academic Phrases")
        st.write("* A controversial issue\n* Substantial evidence\n* Proponents argue...\n* In light of the above")

    # ניסיון להפיק מילים ספציפיות אם יש מפתח
    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            prompt = f"Provide 5 high-level Band III vocabulary words related to the topic: '{topic}'. For each word, provide a Hebrew translation and an example sentence."
            response = model.generate_content(prompt)
            st.success(f"Custom Vocabulary for: {topic} ✨")
            st.write(response.text)
        except Exception as e:
            st.warning("Could not load custom vocabulary. Check your API key.")

    st.divider()

    # שלב 3: כתיבת החיבור
    st.header("Step 3: Write Your Essay ✍️")
    essay_text = st.text_area("Write here (120-140 words):", height=300)

    if st.button("Check My Essay 📊"):
        if not api_key:
            st.error("Please enter your API Key in the sidebar to get a detailed check!")
        else:
            with st.spinner("Analyzing based on 5-point rubric..."):
                try:
                    check_prompt = f"Analyze this essay on the topic '{topic}' according to the Israeli 5-point Bagrut rubric: Content (40), Vocabulary (25), Language (25), Mechanics (10). Essay: {essay_text}"
                    check_response = model.generate_content(check_prompt)
                    st.markdown("### Professional Feedback:")
                    st.write(check_response.text)
                except:
                    st.error("Something went wrong with the check.")
