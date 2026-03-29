from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm():
    return LLM(
        model="llama-3.1-8b-instant",   # ✅ BEST (fast + low limit usage)
        api_key=os.getenv("GROQ_API_KEY"),
        base_url="https://api.groq.com/openai/v1",
        temperature=0

    )


def triage_agent():
    return Agent(
        role="Triage Agent",
        goal="Classify issue and detect missing info",
        backstory="Expert support classifier",
        llm=get_llm()
    )


def retriever_agent():
    return Agent(
        role="Retriever Agent",
        goal="Fetch policy data",
        backstory="Policy search expert",
        llm=get_llm()
    )


def resolution_agent():
    return Agent(
        role="Resolution Agent",
        goal="Generate support response",
        backstory="Customer support expert",
        llm=get_llm()
    )


def compliance_agent():
    return Agent(
        role="Compliance Agent",
        goal="Ensure safe output",
        backstory="Policy compliance expert",
        llm=get_llm()
    )