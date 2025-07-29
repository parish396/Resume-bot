# app.py
import streamlit as st
from langchain_resume_bot import extract_text_from_pdf, analyze_resume

st.title("📄 Resume Bot with LangChain + Streamlit")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_text_from_pdf("temp_resume.pdf")
    st.text_area("Extracted Resume Text", resume_text, height=250)

    question = st.text_input("Ask a question about your resume:")
    if st.button("Analyze") and question:
        with st.spinner("Thinking..."):
            response = analyze_resume(resume_text, question)
            st.markdown("### 🤖 Response")
            st.write(response)
