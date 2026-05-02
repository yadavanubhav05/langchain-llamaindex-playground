import os
from dotenv import load_dotenv

# =========================
# Load ENV
# =========================
load_dotenv()

# =========================
# LLM (Gemini)
# =========================
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# =========================
# Tools
# =========================
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_core.tools import Tool   # <-- correct import

search = DuckDuckGoSearchResults()

tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description=(
            "Use this to find real-time information like stock prices. "
            "Returns text containing results."
        )
    ),
    Tool(
        name="Calculator",
        func=lambda x: str(eval(x)),
        description=(
            "Use this ONLY for numeric calculations. "
            "Input must be a valid math expression like '0.15 * 500'."
        )
    )
]

# =========================
# Agent
# =========================
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=6,   # increased
    handle_parsing_errors=True
)

# =========================
# Run
# =========================
if __name__ == "__main__":
    query = """
Find the current Meta (META) stock price.

Steps:
1. Use Web Search to find the latest price
2. Extract ONLY the number (example: 500)
3. Then calculate 15% using Calculator as: 0.15 * <number>

Return ONLY the final numeric result.
"""

    response = agent_executor.invoke({
        "input": query
    })

    print("\n=========== RESULT ===========\n")
    print(response["output"])