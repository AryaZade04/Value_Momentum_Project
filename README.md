# 🚗 Auto Insurance Policy Assistant (AIPA)

AIPA is an **AI-powered insurance assistant** designed to simplify understanding and comparison of auto insurance policy documents. The system uses **Generative AI (FLAN-T5)** to summarize lengthy insurance policies into easy-to-understand text and provides **side-by-side policy comparison** to help users make informed decisions quickly and confidently.

---

## 🌟 Key Features

| Feature | Description |
|--------|-------------|
| **Policy Summarization** | Upload any auto insurance policy PDF and get a short, clear summary of main coverage, exclusions, and claim conditions. |
| **Quote Comparison** | Upload 2 or more policy PDFs and see a structured comparison of differences in coverage, add-ons, and important terms. |
| **Interactive Web UI** | Built using Streamlit for a clean, modern, and user-friendly interface. |

---

## 🧠 Project Motivation

Insurance policy documents are often long, complex, and filled with legal language.  
Many customers skip reading or misunderstand the terms — leading to poor financial decisions.

**AIPA solves this by:**
- Translating complex legal text into simple language
- Highlighting differences across multiple insurance policies
- Saving time and improving clarity

---

## 🧰 Technology Stack

| Layer | Technology Used | Purpose |
|------|-----------------|---------|
| Programming Language | Python | Core backend + logic |
| Summarization Model | **FLAN-T5 (HuggingFace)** | Generates short policy summaries |
| NLP Pipeline | LangChain | Enables structured reasoning and workflow | 
| PDF Processing | PyMuPDF | Extracts clean text from PDFs |
| UI Framework | Streamlit | User-friendly web application |
| Deployment | Cloudflared / Ngrok | Public access without server hosting |

---

## 🏗️ System Architecture

