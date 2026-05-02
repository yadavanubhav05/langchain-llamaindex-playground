🚀 LangChain + LlamaIndex Playground

Hands-on demos covering core LLM application patterns using LangChain and LlamaIndex.

📦 Modules
1️⃣ Basic Chain (01_basic_chain)
Simple LLM call using Gemini
Prompt → Response flow
Foundation for all LLM apps
2️⃣ LlamaIndex RAG (02_llamaindex_rag)
Document ingestion
Embeddings + vector index
Query engine for summarization

👉 Shows how RAG works end-to-end

3️⃣ Weather Agent (03_weather_agent)
LangChain ReAct agent
External API integration (wttr.in)
Tool usage + reasoning

👉 Shows agent-based workflows

4️⃣ Observability Demo (04_observability_demo)
OpenTelemetry tracing
Latency tracking
Structured logging

👉 Shows production-level monitoring basics

🧠 Concepts Covered
LLM basics
Retrieval Augmented Generation (RAG)
Agents & tools
API integrations
Observability (tracing, logging, latency)
⚙️ Setup
git clone <your-repo-url>
cd <module-folder>
pip install -r requirements.txt
python main.py
🔑 Environment Setup

Create .env (or set env variable):

GOOGLE_API_KEY=your_api_key
📁 Project Structure
.
├── 01_basic_chain/
├── 02_llamaindex_rag/
├── 03_weather_agent/
├── 04_observability_demo/
🎯 Goal of this Repo

To demonstrate how:

LlamaIndex handles data ingestion & retrieval
LangChain handles orchestration & agents
LLM apps can be extended with tools, APIs, and observability
🧩 One-liner

Build → Retrieve → Act → Monitor

📌 Future Improvements
Add vector DB (Chroma / FAISS)
Streamlit UI
API deployment (FastAPI)
Advanced RAG (reranking, hybrid search)