# 🚀 AI Resume Analyzer (RAG-Based GenAI Application)

An intelligent, multi-page **AI Resume Analyzer** built using **LangChain (LCEL) + RAG + Streamlit**, capable of analyzing resumes, comparing them with job descriptions, and generating interview questions with interactive MCQ evaluation.

---

## 🎯 Key Features

### 📄 Resume Analysis
- Extracts:
  - Skills
  - Projects
  - Experience Summary
- Uses **Retrieval-Augmented Generation (RAG)** for accurate, context-aware insights

---

### 💬 Resume Chat Assistant
- ChatGPT-style interface
- Ask questions like:
  - “What are my skills?”
  - “What backend technologies do I know?”
- Maintains chat history

---

### ⚖️ Resume vs Job Description
- Compares resume with job requirements
- Outputs:
  - ✅ Matching Skills  
  - ❌ Missing Skills  
  - 💡 Suggestions  
  - 📊 Match Score (%)  

---

### 🧠 Interview + MCQ Generator
- Generates interview questions based on:
  - Resume
  - Job Description
- Converts them into MCQs
- Interactive quiz with scoring

---

## 🧠 Tech Stack

| Component | Technology |
|----------|-----------|
| Frontend | Streamlit |
| LLM Runtime | Ollama (Local) |
| Model Used | `llama3.2` |
| Embeddings | HuggingFace (`all-MiniLM-L6-v2`) |
| Vector Database | FAISS |
| Framework | LangChain (LCEL) |

---

## ⚙️ Architecture (RAG Pipeline)
   PDF Resume
      ↓
Text Extraction (PyPDFLoader)
      ↓
Chunking (RecursiveCharacterTextSplitter)
      ↓
Embeddings (HuggingFace)
      ↓
Vector Store (FAISS)
      ↓
  Retriever
      ↓
Prompt + LLM (Ollama - llama3.2)
      ↓
Final Response


---

## 🔗 LCEL Chain (Core Logic)

python
rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)


🖥️ Installation Guide
1️⃣ Clone the Repository
git clone <your-repo-url>
cd resume-analyzer
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install Ollama & Model

Download Ollama:
👉 https://ollama.com

Pull the model:

ollama pull llama3.2

5️⃣ Run the Application
streamlit run app.py


📁 Project Structure
resume-analyzer/
│
├── app.py                  # Home (Resume Upload + Analysis)
├── utils.py                # RAG pipeline logic
│
├── pages/
│   ├── 2_Resume_QA.py
│   ├── 3_Resume_vs_JD.py
│   ├── 4_Interview_MCQs.py
│
├── requirements.txt
└── README.md


⚠️ Important Notes
Ollama must be running locally
Works best with Python 3.10 / 3.11
Local LLM (Ollama) cannot be deployed on Streamlit Cloud
For deployment, use:
Groq API
Gemini API
🚀 Future Enhancements
🔄 Switch to Groq (ultra-fast inference)
🔐 Add user authentication
📊 Improve scoring algorithm
🧠 Add memory-based conversations
⏱️ MCQ timer & analytics dashboard
📦 Use structured output parser (Pydantic)
💡 Resume-Ready Description

Built a multi-page AI Resume Analyzer using RAG architecture with LangChain (LCEL), enabling resume analysis, job matching, and interactive MCQ-based interview preparation.

👨‍💻 Author

Sridharan S

⭐ If you like this project

Give it a ⭐ on GitHub and share it!


---

# 📦 Also include this `requirements.txt`

txt
streamlit

langchain
langchain-core
langchain-community
langchain-huggingface
langchain-ollama

faiss-cpu
sentence-transformers

pypdf

transformers
torch
torchvision
🚀 You now have

✔ Professional README
✔ Clean project documentation
✔ Interview-ready explanation








