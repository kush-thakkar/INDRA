from Bio import Entrez
from indra.sources import indra_db_rest
from Bio import Entrez
import requests

# Retreive statements from the ___________ drug(CHEBI:______)
retrieve = indra_db_rest.get_statements(subject='CHEBI:45863@CHEBI', limit=100)

# Keep statements with two agents and the second has a MESH ID
statements_filtered = []
for stmt in retrieve.statements:
    agents = stmt.real_agent_list()
    if len(agents) >= 1:
            statements_filtered.append(stmt)

# Rank by number of evidences
ranked_stmts = sorted(statements_filtered, key=lambda x: len(x.evidence), reverse=True)

# Print top __ strongest links
for stmt in ranked_stmts[:40]:
    agents = stmt.real_agent_list()
    print(f"Statement type: {type(stmt).__name__}")
    print(f"Agents involved:", [a.name for a in agents])
    print(f"Evidence count: {len(stmt.evidence)}")
    print("-" * 40)

keywords_tox = [
    'neurotoxicity', 'cardiotoxicity', 'peripheral neuropathy', 'cardiac dysfunction', 'nerve damage',
'myelosuppression', 'CNS Toxicity', 'cardiac toxicity', 'cardiotoxic', 'heart', 'heart damage'
]

# Sort statements with how much evidence they have
statements_filtered.sort(key=lambda x:len(x.evidence), reverse=True)



# Rank by number of evidences
ranked_stmts = sorted(statements_filtered, key=lambda x:len(x.evidence), reverse=True)


print("\nToxicity-related evidence:")
for stmt in retrieve.statements:
    for ev in stmt.evidence:
        if ev.text:
            text = ev.text.lower()
            if any(keyword in text for keyword in keywords_tox):
               print("Evidence text:", ev.text)
               print("Statement:", stmt)
               # Reference Information
               #if ev.pmid:
                   #print("PMID:", ev.pmid)
               #else:
                   #print("Source:", ev.source_api)
               print("-" * 40)
               break

# Step 3: Side Effects from INDRA Discovery API
print("\n=== Reported Side Effects (via INDRA API) ===")
url = "https://discovery.indra.bio/api/get_side_effects_for_drug"
payload = {
    "drug": ["CHEBI", "CHEBI:45863"]
}
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)

#if response.status_code == 200:
    #side_effects = response.json()
    #for node in side_effects:
        #if 'name' in node['data']:
            #print(f"- {node['data']['name']} (from {node['data'].get('db_ns', 'unknown source')})")
#else:
    #print("Failed to fetch side effects:", response.status_code)