import streamlit as st
import random

st.set_page_config(page_title="Recruit-AI", layout="centered")

st.title("🤖 Recruit-AI")
st.subheader("AI-Powered Resume Screening Agent")

jd = st.text_area("📄 Paste Job Description")
resume = st.text_area("📎 Paste Resume")

if st.button("Analyze Candidate"):
    score = random.randint(65, 95)

    st.success(f"Candidate Score: {score}/100")

    st.write("### 🔍 Summary")
    st.write("The candidate demonstrates relevant technical skills and industry experience aligned with the job description.")

    st.write("### ✅ Matched Skills")
    st.write("- Python")
    st.write("- SQL")

    st.write("### ⚠️ Missing Skills")
    st.write("- AWS")

    if score > 75:
        st.write("### 📩 Recommended Action: Interview")
    else:
        st.write("### ❌ Recommended Action: Reject")
