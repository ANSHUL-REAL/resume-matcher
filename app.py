
import streamlit as st

st.title("📝 Resume Matcher")
st.write("Paste your resume and job description below:")

resume = st.text_area("Resume Text")
job = st.text_area("Job Description")

if st.button("Check Match"):
    st.success("✅ Feature coming soon!")
