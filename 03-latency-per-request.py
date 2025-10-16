#import agentops
from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.tools.googlesearch import GoogleSearchTools
from textwrap import dedent
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

# Create agent
agent = Agent(
    name="Helpful Assistant",
    model=MistralChat(id="magistral-medium-2507", api_key=os.getenv("MISTRAL_API")),
    instructions=dedent("""
        You are a helpful assistant, you will help the user with their questions.
        For up to date information, you can use the search web tool.
    """),
    tools=[GoogleSearchTools()],
)

# Make a query

run_response = agent.run(
    "What's the latest news about the Morocco national football team? In one sentence.")
### Latency per request ### -->>> Time to completion
print(" --- " * 5, "Collected Metrics", " --- " * 5)
result = run_response.metrics
pprint(result)
pprint(f"Time to completion: {(result.duration) : } seconds")
print(" --- " * 20)

