import os
from textwrap import dedent
from datetime import datetime
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
import os
import dotenv

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Prompt Injection Detection

# ---------- TOOLS ----------
def get_date_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------- AGNO AGENT ----------
agent = Agent(
    name="Healthcare Tech Assistant",
    # model=MistralChat(id="mistral-large-latest"),
    model=OpenAIChat(id='gpt-4o-mini', api_key=OPENAI_API_KEY),
    instructions=dedent("""
        You are an assistant specialized in new healthcare technologies in Europe.
        - If the user explicitly asks for the current date or time, call 'get_date_time'.
        - If the user asks for up-to-date info (e.g., news, research), call 'google_search'.
        - Always include the tool's result in your final answer.
        """),
    tools=[GoogleSearchTools(), get_date_time],
)

# ---------- CUSTOM PROMPT INJECTION DETECTION ----------

import re
from typing import Tuple

def detect_prompt_injection(text: str) -> Tuple[bool, float, str]:
    """
    Détecte les tentatives de prompt injection basées sur des patterns communs
    Retourne: (is_safe, risk_score, reason)
    """
    risk_score = 0.0
    reasons = []
    
    # Patterns de prompt injection courants
    injection_patterns = [
        r'ignore\s+(?:your\s+)?(?:previous\s+)?instructions?',
        r'forget\s+(?:your\s+)?(?:previous\s+)?instructions?',
        r'you\s+are\s+now\s+(?:a\s+)?',
        r'act\s+as\s+if\s+you\s+are',
        r'pretend\s+to\s+be',
        r'roleplay\s+as',
        r'system\s*:\s*',
        r'<\|.*?\|>',  # Tokens spéciaux
        r'\[.*?\]',    # Instructions entre crochets
        r'\{.*?\}',    # Instructions entre accolades
        r'override\s+your\s+',
        r'bypass\s+your\s+',
        r'jailbreak',
        r'prompt\s+injection',
        r'ignore\s+all\s+previous',
        r'disregard\s+your\s+',
        r'you\s+must\s+now\s+',
        r'new\s+instructions?\s*:',
        r'updated\s+instructions?\s*:',
    ]
    
    # Vérifier chaque pattern
    for pattern in injection_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            risk_score += 0.2
            
            reasons.append(f"Pattern détecté: {pattern}")
    
    # Vérifier la longueur (prompts très longs peuvent être suspects)
    if len(text) > 500:
        risk_score += 0.1
        reasons.append("Prompt très long")
    
    # Vérifier les caractères spéciaux répétés
    special_chars = re.findall(r'[^\w\s]', text)
    if len(special_chars) > len(text) * 0.3:  # Plus de 30% de caractères spéciaux
        risk_score += 0.15
        reasons.append("Trop de caractères spéciaux")
    
    # Vérifier les tentatives de manipulation
    manipulation_words = ['override', 'bypass', 'ignore', 'forget', 'disregard', 'override']
    for word in manipulation_words:
        if word.lower() in text.lower():
            risk_score += 0.1
            reasons.append(f"Mot de manipulation: {word}")
    
    # Seuil de risque (très strict)
    is_safe = risk_score < 0.1
    reason = "; ".join(reasons) if reasons else "Aucun pattern suspect détecté"
    
    return is_safe, risk_score, reason

# Boucle principale
while True:
    prompt = input("Enter your prompt: ")
    is_safe, risk_score, reason = detect_prompt_injection(prompt)
    
    print(f"Risk Score: {risk_score:.2f}")
    print(f"Reason: {reason}")
    
    if is_safe:
        print('✅ Passed to the agent')
        response = agent.run(prompt)
        print('Agent Response:', response.content)
    else:
        print('❌ Rejected - Potential prompt injection detected')
    
    print("-" * 50)