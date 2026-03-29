from crewai.tools import tool
from src.vector_store import load_db

@tool("Policy Retriever Tool")
def retrieve_policy(query: str) -> str:
    db = load_db()

    docs = db.similarity_search(query, k=5)

    if not docs:
        return "No relevant policy found."

    result = ""
    for d in docs:
        result += d.page_content + "\n\n"

    return result