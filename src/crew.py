from crewai import Crew
from src.agents import triage_agent, retriever_agent, resolution_agent, compliance_agent
from src.tasks import triage_task, retrieval_task, resolution_task, compliance_task

def run_crew(ticket, order_context):
    triage = triage_agent()
    retriever = retriever_agent()
    resolver = resolution_agent()
    compliance = compliance_agent()

    t1 = triage_task(triage, ticket, order_context)
    t2 = retrieval_task(retriever, ticket)
    t3 = resolution_task(resolver, ticket, order_context)
    t4 = compliance_task(compliance)

    crew = Crew(
        agents=[triage, retriever, resolver, compliance],
        tasks=[t1, t2, t3, t4],
        process="sequential"
    )

    result = crew.kickoff()

    # ✅ IMPORTANT FIX
    return result.raw   # ONLY final clean output