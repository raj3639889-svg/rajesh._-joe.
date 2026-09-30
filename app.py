import streamlit as st

st.title("⚖️ LegalEase AI")
st.write("Simple Legal Document Generator")

name = st.text_input("Enter your name")
document = st.selectbox(
    "Choose document",
    ["Rental Agreement", "Legal Notice", "Employment Agreement"]
)
details = st.text_area("Enter your details")

if st.button("Generate"):

    if name and details:

        result = f"""
        {document}

        Name: {name}

        Details:
        {details}

        Terms and Conditions:
        1. Both parties should follow the agreed terms.
        2. The information provided should be correct.
        3. Any changes should be agreed by both parties.

        Signature: __________________
        Date: _______________________

        Note: This is a simple AI project demonstration
        and not professional legal advice.
        """

        st.subheader("📄 Generated Legal Document")
        st.write(result)

        st.download_button(
            "⬇️ Download",
            result,
            "legal_document.txt"
        )

    else:
        st.warning("Please enter all details.")