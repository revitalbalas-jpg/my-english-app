import streamlit as st

# עיצוב בסיסי של האתר
st.set_page_config(page_title="Bagrut 5-Points Essay Helper", layout="centered")

st.title("📝 Bagrut 5-Points Essay Master")
st.subheader("Learn, Practice, and Ace your English Examination")

# שלב 1: הזנת נושא
topic = st.text_input("Step 1: Enter your essay topic here:", placeholder="e.g., Should students wear uniforms?")

if topic:
    st.divider()
    
    # שלב 2: אוצר מילים
    st.header("Step 2: Vocabulary & Phrases 📚")
    st.info("Based on your topic, here are some Band III words to include:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Connectors:**\n* Furthermore\n* Nevertheless\n* Consequently")
    with col2:
        st.markdown("**Topic Specific:**\n* Academic achievement\n* Controversial issue\n* Substantial impact")

    st.divider()

    # שלב 3: תבנית
    st.header("Step 3: Use the Template 🖼️")
    with st.expander("Click to see the 5-point structure"):
        st.write("""
        1. **Intro:** Background + Opinion.
        2. **Body I:** Main argument + Example.
        3. **Body II:** Opposing view + Rebuttal.
        4. **Conclusion:** Summarize your position.
        """)

    st.divider()

    # שלב 4: כתיבת החיבור
    st.header("Step 4: Type Your Essay ✍️")
    essay_text = st.text_area("Write your essay here (120-140 words):", height=300)

    # שלב 5: בדיקה
    if st.button("Check My Essay 📊"):
        st.success("Analysis Complete!")
        st.write("### Your Score Profile:")
        
        # ציונים לדוגמה (יוחלפו בבדיקה אמיתית בהמשך)
        st.write("**Content (40%):**")
        st.progress(0.85) # ירוק
        
        st.write("**Vocabulary (25%):**")
        st.progress(0.60) # צהוב
        
        st.write("**Language (25%):**")
        st.progress(0.40) # אדום
        
        st.write("**Mechanics (10%):**")
        st.progress(0.90) # ירוק
        
        st.metric(label="Estimated Final Score", value="78/100")
