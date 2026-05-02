# 🚀 LangChain Agent Demo (Gemini + Tools)

This demo shows how to build a **LangChain agent** that can:

* 🔍 Search real-time data (via DuckDuckGo)
* 🧮 Perform calculations (via Calculator tool)
* 🤖 Use an LLM (Gemini) to decide which tool to use

---

## 📂 Project Structure

```
LangChain/
└── 01_basic_chain/
    ├── main.py
    ├── requirements.txt
    └── README.md
```

---

## ⚙️ Setup

### 1. Create virtual environment (optional but recommended)

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Mac/Linux
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add API key

Create a `.env` file in the same folder:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Demo

```bash
python main.py
```

---

## 🧠 What This Demo Does

The agent is asked to:

1. Search Meta (META) stock price
2. Extract the numeric value
3. Calculate 15% using a calculator tool
4. Return final result

---

## 🔄 How It Works (Simple View)

```
User Query
   ↓
Agent (ReAct reasoning)
   ↓
Chooses Tool
   ├── Web Search
   └── Calculator
   ↓
LLM (Gemini processes result)
   ↓
Final Answer
```

---

## 🧪 Example Output

```
Action: Web Search
Action Input: Meta stock price

Action: Calculator
Action Input: 0.15 * 500

Final Answer: 75
```

---

## ⚠️ Important Notes

* This is an **agent-based system**, not a fixed pipeline
* Tool usage is **decided dynamically by the LLM**
* Sometimes the agent may:

  * Skip a tool
  * Stop early
  * Misinterpret outputs

👉 This is expected behavior

---

## 🎯 Key Learning

This demo helps you understand:

* How agents decide which tool to use
* How tools integrate with LLMs
* Limitations of agent-based workflows

---

## 🚧 Limitations

* ❌ Not deterministic (no guaranteed step execution)
* ❌ Depends on LLM reasoning quality
* ❌ Web search returns unstructured text

---

## 🔥 Next Step

To make this **reliable and production-ready**, move to:

👉 **LCEL (LangChain Expression Language)**

With LCEL you can:

* Guarantee execution order
* Force tool usage
* Build deterministic pipelines

---

## 👨‍💻 Author

Built as part of hands-on learning for:

* LangChain
* Agents vs Chains
* Tool integration with LLMs

---