import textwrap
from agno.agent import Agent
from datetime import datetime
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.googlesearch import GoogleSearchTools
import os
from dotenv import load_dotenv
from rich.pretty import pprint
# Number of steps per task
# Definition: Number of steps needed to complete a task

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
def get_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

agent = Agent(
    name="Helpful Assistant",
    model=OpenAIChat(id='gpt-4o-mini', api_key=OPENAI_API_KEY),
    instructions=textwrap.dedent("""
        You are a helpful assistant.
        If the user explicitly asks for the current date or time, call 'get_date_time'.
        If the user asks for up-to-date information (e.g., stock prices, news), call the 'google_search' and 'reasoning' tool.
        Always include the tool's result in your final answer.
        Do not call 'get_date_time' unless the query is specifically about the date or time.
    """),
    tools=[ReasoningTools(add_instructions=True), GoogleSearchTools(), get_date_time],
)


response = agent.run(" and what are the current trends in artificial intelligence and machine learning?")
print('Response:', response.content)

def count_steps(run_response):
    steps = 0
    for msg in run_response.messages:
        # 1. Assistant reasoning/thinking (if present)
        if getattr(msg, "thinking", None):
            steps += 1
        if getattr(msg, "reasoning_content", None):
            steps += 1
        
        # 2. Assistant tool call(s)
        if msg.role == "assistant" and msg.tool_calls:
            steps += len(msg.tool_calls)
        
        # 3. Tool execution (the tool's reply)
        if msg.role == "tool":
            steps += 1
        
        # 4. Assistant final response (text answer to user)
        if msg.role == "assistant" and msg.content and msg.content.strip() and not msg.tool_calls:
            steps += 1
    
    return steps

print('-' * 20)
print(f"Number of steps: {count_steps(response)}")