import streamlit as st
from utils import format_docs

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

import re

st.title("⚖️ Resume vs Job Description")

if "retriever" not in st.session_state:
    st.warning("Upload resume first")
    st.stop()

retriever = st.session_state["retriever"]
llm = st.session_state["llm"]

jd = st.text_area("Paste Job Description")

prompt = PromptTemplate.from_template("""
Compare resume with job description.

Context:
{context}

Job Description:
{question}

Return:
- Matching Skills
- Missing Skills
- Suggestions
- Match Score (%) (ex:"70%")
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

if st.button("Analyze"):

    result = chain.invoke(jd)

    st.markdown("### 📄 Analysis")
    st.markdown(result)

    # Extract score
    match = re.search(r'\d+', result)
    if match:
        score = int(match.group())

        st.markdown("### 📊 Match Score")
        st.progress(score)
        st.metric("Score", f"{score}%")