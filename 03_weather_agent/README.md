# 🌦️ Weather Agent using LangChain + Gemini

## Overview
This project demonstrates how to use a LangChain agent with an external API tool (Weather API) powered by Google Gemini.

The agent:
- Decides when to call the weather API
- Fetches real-time weather data
- Combines it with reasoning to suggest clothing

---

## How It Works

1. User asks a question
2. Agent analyzes the query
3. Agent decides to call Weather API
4. API returns weather data
5. LLM combines data + reasoning
6. Final answer is generated

---

## Tech Stack

- LangChain (Agent + Tools)
- Google Gemini (`gemini-2.5-flash`)
- wttr.in (Weather API)
- Python

---

## Setup

### 1. Clone repo
```bash
git clone <your-repo>
cd demo_03_weather_agent