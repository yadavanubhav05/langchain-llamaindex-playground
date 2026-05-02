# LlamaIndex RAG Demo (Gemini + Local Docs)

Simple demo showing how to:

* Load documents
* Build a vector index
* Query using Gemini (LLM)

---

## 📂 Project Structure

```
02_llamaindex_rag/
├── main.py
├── requirements.txt
├── docs/
│   └── sample.txt
```

---

## ⚙️ Setup

### 1. Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API key

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run

```bash
python main.py
```

---

## 🧠 What This Does

```text
Load documents → Create embeddings → Build index
→ Retrieve relevant chunks → Gemini generates answer
```

---

## 🔍 Example Query

```
Summarize the document in simple points
```

---

## 📌 Key Concepts

* **Documents** → Raw input files
* **Nodes** → Chunked text
* **Embeddings** → Vector representation
* **Index** → Enables semantic search
* **Query Engine** → Retrieves + answers

---

## ⚠️ Notes

* Uses **Gemini (gemini-2.5-flash)**
* Uses **HuggingFace embeddings (BGE small)**
* Keep documents inside `/docs` folder

---

## 🎯 Purpose

Basic RAG (Retrieval-Augmented Generation) demo using LlamaIndex.
