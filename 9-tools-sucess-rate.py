import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.mistral import MistralChat
from textwrap import dedent
from agno.tools.googlesearch import GoogleSearchTools
import os
load_dotenv()

# Definition: Percentage of successful tool interactions.
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
def get_date_time():
    # return 'The current date and time is 2025-09-04 10:00:00'
    raise Exception("Simulated failure for testing")

agent = Agent(
    name="Helpful Assistant",
    model=MistralChat(id="magistral-medium-2507", api_key=MISTRAL_API_KEY),
    instructions=dedent("""
        You are a helpful assistant.
        - If the user explicitly asks for the current date or time, call 'get_date_time'.
        - If the user asks for up-to-date information (e.g., stock prices, news), call the 'google_search' tool.
        - Always include the tool's result in your final answer.
        - Do not call 'get_date_time' unless the query is specifically about the date or time.
    """),
    tools=[GoogleSearchTools(), get_date_time],
)

# response = agent.run("what's the latest news in Finland today? In one sentence")
response = agent.run("what's the current date and time? and what's the latest news in Finland today? In one sentence")

# Extract tool calls and check their status
tool_success = []
for tool in response.tools:
    success = not getattr(tool, "tool_call_error", False) # True if no error
    tool_success.append(success)

# Compute tool success rate
tool_success_rate = (sum(tool_success) / len(tool_success)) * 100 if tool_success else 0
print(f"Tool Success Rate: {tool_success_rate}%")