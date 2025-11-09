# 🛡️ Intelligent Insurance Assistant System (AIPA + Renewal Prediction)

This project integrates **Generative AI** and **Machine Learning** to assist in auto insurance decision-making through:
1. **Policy Summarization**
2. **Quote Comparison**
3. **Insurance Policy Renewal Prediction**

The solution helps users **quickly understand policies**, compare multiple insurance plans, and **predict whether a customer is likely to renew** their insurance based on behavioral and financial indicators.

---

## 🌟 Key Functional Modules

| Module | Description | Technology Used |
|--------|-------------|----------------|
| **Policy Summarization** | Converts lengthy policy documents into short, clear summaries. | FLAN-T5, Transformers, PyMuPDF |
| **Quote Comparison** | Compares 2+ policy PDFs and highlights key differences. | LangChain, Custom Comparator |
| **Renewal Prediction Model** | Predicts probability of customer renewing their insurance policy. | Random Forest / Logistic Regression, Pandas, Scikit-Learn |

---

## 🎯 Problem Solved
Insurance documents are **long, repetitive, and legally complex**.  
Customers often **do not understand** what they are paying for and what is covered.  
Additionally, insurance providers need models to **predict customer churn/renewal**.

This project provides:
- Easy-to-read policy summaries
- Clear comparison between quotes
- Data-driven renewal decision prediction

---

## 🧠 System Architecture

                           ┌───────────────────────────┐
                           │     Streamlit Web UI      │
                           └─────────────┬─────────────┘
                                         │
                              User Uploads Policy PDFs
                                         │
                           ┌─────────────▼─────────────┐
                           │        PDF Reader         │
                           │     (PyMuPDF / OCR)       │
                           └─────────────┬─────────────┘
                                         │ Extracted Text
                                         ▼
                         ┌─────────────────────────────────┐
                         │        Text Preprocessing        │
                         │ (Cleaning, Normalization, Split) │
                         └─────────────────┬───────────────┘
                                           │
                                           ▼
                           ┌────────────────────────────┐
                           │     FLAN-T5 Summarizer     │
                           └─────────────┬──────────────┘
                                         │ Summarized Policy Output
                                         ▼
                         ┌──────────────────────────────────┐
                         │        Quote Comparison Engine    │
                         │ (Rule-Based + Semantic Matching)  │
                         └──────────────────────────────────┘

                         ┌──────────────────────────────────┐
                         │     Renewal Prediction Model      │
                         │ (Logistic Regression / RandomForest) │
                         └──────────────────────────────────┘

---

## 🧰 Technology Stack

| Layer | Technology Used |
|------|----------------|
| Programming | Python |
| Summarization Model | FLAN-T5 |
| Comparison Logic | LangChain + Rule Based |
| ML Model for Renewal | Logistic Regression / Random Forest |
| Data Processing | Pandas, NumPy |
| Visualization | Streamlit UI |
| Deployment | Cloudflared / Ngrok Tunnel |
| PDF Text Extraction | PyMuPDF |

---

