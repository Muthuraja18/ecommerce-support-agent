import json
from src.crew import run_crew

with open("data/test_cases.json") as f:
    tests = json.load(f)

results = []

for t in tests:
    output = run_crew(t["ticket"], t["context"])
    results.append(output)

print("Evaluation completed")