from dotenv import load_dotenv
import os
from agno.agent import Agent
from datetime import datetime
from textwrap import dedent
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.embedder.mistral import MistralEmbedder

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model and System cards, including clear documentation of intended agent purpose and limitations

# ---------- Initializing Knowledge Base ----------

knowledge_base = Knowledge(
    vector_db=PgVector(
        table_name="system_card",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        embedder=MistralEmbedder(api_key=os.getenv('MISTRAL_API_KEY')),
    )
)

knowledge_base.add_content(
    path="34-system_card.md",
)


# -------------------- TOOLS --------------------

def get_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# -------------------- MAIN AGENT --------------------

main_agent = Agent(
    name="Helpful Assistant",
    model=OpenAIChat(id='gpt-4o-mini', api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are a Healthcare Tech Assistant.
        - Use the knowledge base as your main reference.
        - If the user asks about anything outside knowledge base boundaries, you must strictly decline
        - Do not answer questions outside this domain, even if tools could provide an answer.
        - Always be clear and concise.
    """),
    tools=[DuckDuckGoTools(), get_date_time],
    knowledge=knowledge_base,
)


main_agent.print_response('What are latest AI News in healthcare in europe')
#main_agent.print_response('what are the best travelling places in Italy')