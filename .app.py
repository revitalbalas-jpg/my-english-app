import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Module G Writing Master", layout="wide")
st.title("🎓 Module G: Writing Master")

# בדיקת מפתח
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Missing API Key in Secrets!")
    st.stop()

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# פונקציה למציאת המודל הנכון בשרת
def get_available_model():
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # מעדיף את flash אם קיים, אם לא - לוקח את הראשון שזמין
                if 'gemini-1.5-flash' in m.name:
                    return m.name
                if 'gemini-pro' in m.name:
                    return m.name
        return None
    except:
        return "models/gemini-pro" # ברירת מחדל בטוחה

model_name = get_available_model()

if model_name:
    model = genai.GenerativeModel(model_name)
    
    topic = st.text_input("Step 1: What is the essay topic?")

    if topic:
        st.header("Step 2: Suggestions 💡")
        prompt = f"Create a table for Module G level on the topic: {topic}. Include arguments and Band III vocabulary with Hebrew translations."
        
        try:
            with st.spinner(f"Using {model_name}..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Generation Error: {e}")
else:
    st.error("No compatible Google models found on this server.")
