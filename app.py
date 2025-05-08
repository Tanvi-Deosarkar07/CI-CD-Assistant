
import streamlit as st
import google.generativeai as genai
from retriever import retrieve

st.set_page_config(page_title="CI/CD RAG Assistant", layout="centered")
st.title("🚀 CI/CD RAG Assistant")
st.write("Ask anything about your CI/CD documentation.")

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

query = st.text_input("What’s your CI/CD question?")

if st.button("Ask") and query:
    chunks, sources = retrieve(query)
    context = "\n\n".join(chunks)
    prompt = f"""Answer this question using only the documentation below:\n\n{context}\n\nQ: {query}"""
    response = model.generate_content(prompt)

    st.subheader("💡 Answer")
    st.write(response.text)

    st.subheader("📁 Source Docs")
    for src in set(sources):
        st.markdown(f"- {src}")
