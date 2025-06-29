
import streamlit as st

st.title("📝 Resume Matcher")
st.write("Paste your resume and job description below:")

resume = st.text_area("Resume Text")
job = st.text_area("Job Description")

if st.button("Check Match"):
    from matcher import get_match_score_and_missing

if st.button("Check Match"):
    score, missing = get_match_score_and_missing(resume, job)
    st.markdown(f"### ✅ Match Score: {score:.2f}%")
    st.markdown("### ❌ Missing Skills:")
    if missing:
        for skill in missing:
            st.write(f"- {skill}")
    else:
        st.write("All skills matched! 🎉")
