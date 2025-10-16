import agentops
from agno.agent import Agent
from agno.models.mistral import MistralChat
from agno.tools.googlesearch import GoogleSearchTools
from textwrap import dedent
from pprint import pprint
from dotenv import load_dotenv
import os
load_dotenv()

agentops.init(
    api_key=os.getenv("AGENTOPS_API_KEY"), 
    default_tags=['agno']
    )
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
### Latency per tool call ### Tokens usage per tool ###
if run_response.messages:
    for message in run_response.messages:
        print('-->', message.role)
        if message.role == "tool":
            if message.content:
                print(f"Message: {message.content}")
            elif message.tool_calls:
                print(f"Tool calls: {message.tool_calls}")
            print("---" * 5, "Metrics", "---" * 5)
            pprint(message.metrics)
            print("---" * 20)

