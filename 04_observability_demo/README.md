# LLM Observability Demo (LangChain + Gemini + OpenTelemetry)

Simple demo showing how to add observability (tracing + logging) to LLM calls.

---

## 🚀 What this does

- Calls Gemini LLM
- Wraps it inside OpenTelemetry tracing
- Logs:
  - question
  - response
  - latency
- Prints trace spans in console

---

## 🧠 Concepts Covered

- Observability in LLM apps
- Tracing (OpenTelemetry)
- Logging (JSON logs)
- Latency tracking

---

## 📦 Setup

```bash
pip install -r requirements.txt