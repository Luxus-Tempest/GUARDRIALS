from textwrap import dedent
from agno.agent import Agent
from datetime import datetime
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.googlesearch import GoogleSearchTools
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Cost per request
# Definition: Financial cost to complete an assigned task

def get_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

agent = Agent(
    name="Helpful Assistant",
    model=OpenAIChat(id='gpt-4o-mini', api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are a helpful assistant.
        If the user explicitly asks for the current date or time, call 'get_date_time'.
        If the user asks for up-to-date information (e.g., stock prices, news), call the 'google_search' tool.
        Always include the tool's result in your final answer.
        Do not call 'get_date_time' unless the query is specifically about the date or time.
    """),
    tools=[GoogleSearchTools(), get_date_time],
)

response = agent.run("what's the current date and time? and what are the current trends in artificial intelligence and machine learning?")
# print('Response:', response.content)

# Sum tokens
total_input_tokens = response.metrics.input_tokens
total_output_tokens = response.metrics.output_tokens
total_tokens = response.metrics.total_tokens

# Pricing per 1M tokens
input_price_per_m = 3 # $3 per million input tokens
output_price_per_m = 15 # $15 per million output tokens

# Calculate cost
input_cost = total_input_tokens / 1_000_000 * input_price_per_m
output_cost = total_output_tokens / 1_000_000 * output_price_per_m
total_cost = input_cost + output_cost

print("total tokens: ", total_tokens)
print("Input cost: $", input_cost)
print("Output cost: $", output_cost)
print("Total cost: $", total_cost)