import os
import json
import asyncio
from textwrap import dedent
from datetime import datetime
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from uqlm import LLMPanel
from langchain_openai import ChatOpenAI # LangChain wrapper for OpenAI
import dotenv
dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Hallucination

# ---------- TOOLS ----------
def get_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------- AGNO AGENT ----------
agent = Agent(
    name="Helpful Assistant",
    model=OpenAIChat(id="gpt-4o-mini", api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are a helpful assistant.
        - If the user explicitly asks for the current date or time, call 'get_date_time'.
        - If the user asks for up-to-date information (e.g., stock prices, news), call the 'google_search' tool.
        - Always include the tool's result in your final answer.
        - Do not call 'get_date_time' unless the query is specifically about the date or time.
    """),
    tools=[GoogleSearchTools(), get_date_time],
)

# ---------- RUN AGENT ----------
prompt = "what are the current trends in artificial intelligence and machine learning?"
response = agent.run(prompt)
agent_output = response.content
print("Agent response:\n", agent_output)

# ---------- HALLUCINATION CHECK ----------
# Create a LangChain OpenAI model for judging
judge_llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.environ["OPENAI_API_KEY"],
)

# Panel with a single judge
panel = LLMPanel(
    llm=judge_llm,
    judges=[judge_llm],
    scoring_templates=["continuous"]
)

async def check_hallucination():
    # Feed the agent's answer into the panel for scoring
    results = await panel.generate_and_score(
        prompts=[f"Q: {prompt}\nA: {agent_output}"]
    )
    print("\nHallucination scoring:")
    print(results.to_df())

if __name__ == "__main__":
    asyncio.run(check_hallucination())