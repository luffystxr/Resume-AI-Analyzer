import streamlit as st
from utils import build_rag, format_docs

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")

# Upload once
uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    if "retriever" not in st.session_state:
        with st.spinner("Processing resume..."):
            retriever, llm = build_rag("temp.pdf")
            st.session_state["retriever"] = retriever
            st.session_state["llm"] = llm

    st.success("✅ Resume ready!")

# Resume Analysis
if "retriever" in st.session_state:

    retriever = st.session_state["retriever"]
    llm = st.session_state["llm"]

    prompt = PromptTemplate.from_template("""
Extract:
- Skills
- Projects
- Experience summary

Context:
{context}

Question:
{question}
""")

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Analyzing..."):
            result = chain.invoke("Analyze resume")

        st.markdown("### 📊 Analysis Result")
        st.markdown(result)

else:
    st.info("📌 Upload your resume to begin")