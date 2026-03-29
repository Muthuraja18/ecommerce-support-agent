from crewai import Task

# =========================
# 1️⃣ TRIAGE TASK
# =========================
def triage_task(agent, ticket, order_context):
    return Task(
        description=f"""
You are a customer support triage assistant.

Analyze the support ticket and structured order data.

Ticket:
{ticket}

Order Context:
{order_context}

Your job:

1. Classify the issue type:
   - refund
   - shipping
   - payment
   - promotion
   - fraud
   - other

2. Identify missing or unclear information.

3. If needed, generate up to 3 clarifying questions.

Output format:

Classification:
<issue_type> (confidence 0-1)

Missing Info:
<list or None>

Clarifying Questions:
<max 3 questions or None>
""",
        expected_output="Issue classification, missing info, and clarifying questions",
        agent=agent
    )


# =========================
# 2️⃣ RETRIEVAL TASK
# =========================
def retrieval_task(agent, ticket):
    return Task(
        description=f"""
You are a policy retrieval agent.

Your job:
- Search the vector database
- Return ONLY relevant policy excerpts

Ticket:
{ticket}

STRICT RULES:
- Return top relevant chunks only
- DO NOT explain anything
- DO NOT summarize
- INCLUDE citations (doc name + section/chunk id)
- If nothing found → return "No relevant policy found"

Output format:

Policy Excerpts:
- <text>

Citations:
- <doc_name + section>
""",
        expected_output="Relevant policy excerpts with citations",
        agent=agent
    )


# =========================
# 3️⃣ RESOLUTION WRITER TASK
# =========================
def resolution_task(agent, ticket, order_context):
    return Task(
        description=f"""
You are a STRICT e-commerce support resolution agent.

Ticket:
{ticket}

Order Context:
{order_context}

-----------------------------------
FINAL OUTPUT FORMAT (STRICT)
-----------------------------------

Classification: <issue type> (confidence: <0-1>)

Clarifying Questions:
- <question>
- <or write "None">

Decision: approve / deny / partial / needs escalation

Rationale:
<ONLY policy-based explanation>

Citations:
- <doc + section>

Customer Response Draft:
<professional message>

Next Steps:
- <step>

-----------------------------------
STRICT RULES
-----------------------------------

- DO NOT output JSON
- DO NOT include "Policy Excerpts"
- DO NOT repeat sections
- DO NOT include raw retrieval output
- ONLY include final structured answer
- If no questions → write "None"
- If policy missing → Decision: needs escalation
- EVERY claim MUST have citation
- NO hallucination (do not invent time, policy, rules)

ONLY return final formatted answer.
""",
        expected_output="Clean structured response",
        agent=agent
    )

# 4️⃣ COMPLIANCE / SAFETY TASK
# =========================
def compliance_task(agent):
    return Task(
        description="""
You are a STRICT compliance checker.

Check:
- All sections present
- Citations exist
- No hallucination
- Correct decision

Fix if needed.

IMPORTANT:
- NO JSON
- NO extra explanation
- ONLY final formatted response
""",
        expected_output="Clean output",
        agent=agent
    )