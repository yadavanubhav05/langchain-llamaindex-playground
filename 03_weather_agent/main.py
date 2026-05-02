import os
import requests
from dotenv import load_dotenv

from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import hub

# =========================
# Load ENV
# =========================
load_dotenv()

# =========================
# Weather Tool
# =========================
def get_weather(city: str) -> str:
    """Fetch current weather for a city"""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
        return response.text
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

# =========================
# LLM
# =========================
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# =========================
# Tools
# =========================
tools = [
    Tool(
        name="Weather API",
        func=get_weather,
        description="Get current weather conditions for any city"
    )
]

# =========================
# Agent
# =========================
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm,
    tools,
    prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

# =========================
# Run
# =========================
if __name__ == "__main__":
    query = "What's the weather in Paris? How should I dress?"

    try:
        response = agent_executor.invoke({
            "input": query
        })

        print("\n=========== RESULT ===========\n")
        print(response["output"])

    except Exception as e:
        print(f"Error: {str(e)}")