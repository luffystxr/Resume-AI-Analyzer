import streamlit as st
from utils import format_docs

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

st.title("💬 Resume Chat Assistant")

if "retriever" not in st.session_state:
    st.warning("Upload resume from Home page")
    st.stop()

retriever = st.session_state["retriever"]
llm = st.session_state["llm"]

prompt = PromptTemplate.from_template("""
Answer based only on resume context.

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

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

query = st.chat_input("Ask about your resume...")

if query:
    st.session_state.messages.append(("user", query))

    response = chain.invoke(query)
    st.session_state.messages.append(("assistant", response))

# Display chat
for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)