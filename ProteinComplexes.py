# Import Neo4jClient from the INDRA CogEx library to connect to the graph database
from indra_cogex.client import Neo4jClient

# Creates a connection to the Neo4j database using client
client = Neo4jClient()

# List of drug IDs that we need to query, each ID is a ChEBI identifier for the chemotherapy drug
drug_ids = [
    "chebi:46345", "chebi:17196", "chebi:22907", "chebi:31355", "chebi:27899",
    "chebi:4672", "chebi:28748", "chebi:63587", "chebi:4911", "chebi:80630",
    "chebi:44185", "chebi:50729", "chebi:6520", "chebi:31941", "chebi:45863",
    "chebi:27834", "chebi:27375", "chebi:28445", "chebi:4027"
]

# Loop over each drug ID, # Finds the drug node with the given ID (source:BioEntity), Follow a link r1 to a protein node (x) of type human_gene_protein,
# It follows a link r2 from the protein to a GO term node. After it only keeps the relationships where evidence_count is greater than 0 for r1 and r2.
# After it returns the drug ID, gene ID, GO term, and evidence counts for both links. Then, the code orders results by highest evidence counts and only gives 1 top result (LIMIT 1). Use curly braces to escape the literal curly braces in the output.
for drug_id in drug_ids:
    query = f"""
    MATCH (source:BioEntity {{id: '{drug_id}'}})-[r1:indra_rel]->
          (x:BioEntity {{type: 'human_gene_protein'}})-[r2:indra_rel]->
          (y:BioEntity {{type: 'human_gene_protein'}})-[r3:indra_rel]->
          (target:BioEntity {{id: 'mesh:D066126'}})

    WHERE r1.evidence_count > 0 
      AND r2.evidence_count > 0 
      AND r3.evidence_count > 0
      AND r1.belief > 0.5
      AND r2.belief > 0.5
      AND r3.belief > 0.5

    RETURN source.id AS drug,
           x.id AS gene1, 
           y.id AS gene2, 
           target.id AS mesh_id, 
           r1.evidence_count AS r1_evidence,
           r1.belief AS r1_belief,
           r2.evidence_count AS r2_evidence,
           r2.belief AS r2_belief,
           r3.evidence_count AS r3_evidence,
           r3.belief AS r3_belief

    ORDER BY r1.belief DESC, r2.belief DESC, r3.belief DESC

    LIMIT 10
    """

    res = client.query_tx(query)
    # Prints the drugs showing current results
    print(f"\nResults for drug {drug_id}:")
    # No results found is returned if no query doesn't return anything
    if not res:
        print("  No results found.")
    else:
        for record in res:  # Loop through all returned results
            print(f"  Drug: {record[0]}, Gene1: {record[1]}, Gene2: {record[2]}, "
                  f"MESH ID: {record[3]}, "
                  f"r1 evidence: {record[4]}, r1 belief: {record[5]}, "
                  f"r2 evidence: {record[6]}, r2 belief: {record[7]}, "
                  f"r3 evidence: {record[8]}, r3 belief: {record[9]}")