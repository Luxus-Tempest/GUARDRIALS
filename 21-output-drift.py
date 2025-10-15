from textwrap import dedent
from datetime import datetime
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from agno.eval.accuracy import AccuracyEval, AccuracyResult
from typing import Optional
import os
import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Output Drift

# ---------- TOOLS ----------
def get_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ---------- AGNO AGENT ----------
agent = Agent(
    name="Climate Change Research Assistant",
    # model=MistralChat(id="mistral-large-latest"),
    model=OpenAIChat(id='gpt-4o-mini', api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are an assistant specialized in climate change research and environmental solutions in Africa.
        - If the user explicitly asks for the current date or time, call 'get_date_time'.
        - If the user asks for up-to-date info (e.g., news, research), call 'google_search'.
        - Always include the tool's result in your final answer.
        """),
    tools=[GoogleSearchTools(), get_date_time],
)


evaluation = AccuracyEval(
    model=OpenAIChat(id="gpt-4o-mini", api_key=OPENAI_API_KEY),
    agent=agent,
    input="What are the latest climate change solutions and technologies in Africa?",
    expected_output="Recent climate change solutions in Africa include renewable energy innovations, carbon capture technologies, sustainable agriculture practices, and green transportation systems",
    additional_guidelines="Check if the agent's response contains the same key information and style as the expected output.",
)

result: Optional[AccuracyResult] = evaluation.run(print_results=True)