import streamlit as st
from utils import format_docs

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

import json

st.title("🧠 Interview Prep + MCQ Quiz")

if "retriever" not in st.session_state:
    st.warning("Upload resume first")
    st.stop()

retriever = st.session_state["retriever"]
llm = st.session_state["llm"]

mode = st.radio("Mode", ["Resume Based", "JD Based"])

jd = ""
if mode == "JD Based":
    jd = st.text_area("Paste Job Description")

prompt = PromptTemplate.from_template("""
Generate 5 MCQs in STRICT JSON.

Format:

[
  {{
    "question": "...",
    "options": ["A","B","C","D"],
    "answer": "A"
  }}
]

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

if st.button("Generate MCQs"):

    query = "skills projects" if mode == "Resume Based" else jd

    raw = chain.invoke(query)

    try:
        mcqs = json.loads(raw)
    except:
        st.error("Failed to parse MCQs")
        st.code(raw)
        st.stop()

    st.markdown("## 📝 Quiz")

    answers = {}

    for i, q in enumerate(mcqs):
        st.markdown(f"### Q{i+1}: {q['question']}")

        answers[i] = st.radio(
            "Choose:",
            q["options"],
            key=f"q{i}"
        )

    if st.button("Submit Quiz"):

        score = sum(
            1 for i, q in enumerate(mcqs)
            if answers[i] == q["answer"]
        )

        st.success(f"🎯 Score: {score}/{len(mcqs)}")

        st.markdown("### ✅ Correct Answers")
        for i, q in enumerate(mcqs):
            st.write(f"Q{i+1}: {q['answer']}")