# 🛒 E-commerce Support Resolution Agent (RAG + Multi-Agent System)

## 📌 Overview
This project is an AI-powered **customer support assistant** that resolves e-commerce tickets using a **multi-agent Retrieval-Augmented Generation (RAG)** system.

It ensures:
- ✅ Policy-grounded responses
- ✅ Citation-backed reasoning
- ✅ Safe and compliant outputs
- ✅ No hallucination

---

## 🎯 Objective
Build a system that:
- Understands customer tickets
- Retrieves relevant policy documents
- Generates structured support resolutions
- Ensures correctness using a compliance agent

---

## 🧠 Architecture

### 🔹 Multi-Agent Pipeline

1. **Triage Agent**
   - Classifies issue type (refund/shipping/payment/etc.)
   - Detects missing information
   - Asks clarifying questions

2. **Policy Retriever Agent**
   - Queries FAISS vector DB
   - Returns relevant policy chunks
   - Includes citations (doc + section)

3. **Resolution Writer Agent**
   - Generates final structured response
   - Uses ONLY retrieved evidence
   - No hallucination allowed

4. **Compliance / Safety Agent**
   - Validates output
   - Ensures:
     - citations exist
     - no unsupported claims
     - no policy violations
   - Forces escalation if needed

---

## 🔄 RAG Pipeline Flow

1. Load policy documents
2. Chunk text (500 tokens, overlap 50)
3. Generate embeddings (HuggingFace)
4. Store in FAISS
5. Query processing:
   - Retrieve top-K chunks
   - Generate response
   - Validate with compliance agent

---

## 📊 Data Sources

Policy dataset includes:
- Returns & Refund policies
- Cancellation policies
- Shipping & delivery
- Promotions / coupons
- Disputes (damaged, missing items)

📌 Sources:
- Amazon Policies (public)
- Flipkart Policies
- Synthetic internal policy documents

🚀 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/Muthuraja18/ecommerce-support-agent.git

cd ecommerce-support-agent

2️⃣ Create Virtual Environment (Recommended)
python -m venv myenv
myenv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set API Key (Groq)
Windows (PowerShell):
setx GROQ_API_KEY "your_groq_api_key"
Temporary (current session):
$env:GROQ_API_KEY="your_groq_api_key"

5️⃣ Build Vector Database (FAISS)
python -m src.vector_store

👉 This will:

Load policy documents
Split into chunks
Create FAISS index
6️⃣ Run the Application
streamlit run app.py

👉 Open in browser:

http://localhost:8501
7️⃣ Run Evaluation
python src/evaluation.py

👉 Outputs:

Citation coverage
System performance


📂 Project Structure
ecommerce-support-agent/
│
├── data/
│   ├── policies/
│   └── test_cases.json
│
├── src/
│   ├── agents.py
│   ├── crew.py
│   ├── tasks.py
│   ├── tools.py
│   ├── ingestion.py
│   ├── vector_store.py
│   └── evaluation.py
│
├── app.py
├── requirements.txt
└── README.md

⚠️ Notes
Ensure policy documents exist in data/policies/
Do NOT commit API keys
If FAISS fails → reinstall dependencies
📅 Accessed: March 2026

---

```bash
pip install -r requirements.txt
