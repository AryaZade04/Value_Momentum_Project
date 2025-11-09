#older
import streamlit as st

def show_header():
    st.title("🚗 Auto Insurance Policy Assistant")
    st.subheader("Choose an option below:")

import streamlit as st

def show_header():
    # App Title
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1;'>🚗 Auto Insurance Policy Assistant</h1>
        """,
        unsafe_allow_html=True
    )

    # Subtitle
    st.markdown(
        """
        <p style='text-align: center; font-size: 18px; color: #5D6D7E;'>
        Upload, summarize, and compare auto insurance policies in clear bullet points.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Divider line for a clean layout
    st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)

    # Option selector
    st.subheader("🔍 Choose an option below:")
    st.write(
        """
        - **📄 Summarize Policy:** Upload a PDF and get a clean, 250-word summary in bullet points.
        - **⚖️ Compare Policies:** Compare two policy summaries side-by-side to see which offers better coverage.
        - **💬 Insights:** Get key highlights, coverage, and exclusions automatically extracted.
        """
    )
