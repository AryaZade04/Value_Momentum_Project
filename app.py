# older


import streamlit as st
from utils import show_header
from pdf_reader import extract_text_from_pdf
from summarizer import summarize_policy
from comparator import compare_policies

show_header()

option = st.radio("Select Mode:", ["Summarize Policy", "Compare Quotes"])

if option == "Summarize Policy":
    file = st.file_uploader("Upload Auto Insurance Policy PDF", type=["pdf"])
    if file:
        text = extract_text_from_pdf(file)
        with st.spinner("Summarizing..."):
            summary = summarize_policy(text)
        st.subheader("🧾 Summary:")
        st.write(summary)

elif option == "Compare Quotes":
    files = st.file_uploader("Upload 2 or more Policy PDFs", type=["pdf"], accept_multiple_files=True)
    if len(files) >= 2:
        texts = [extract_text_from_pdf(f) for f in files]
        result = compare_policies(texts)
        st.subheader("📊 Comparison:")
        st.write(result)
    else:
        st.info("Please upload at least 2 policy PDFs.")
