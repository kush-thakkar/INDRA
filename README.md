Analyzing the side effects of neurotoxicity and cardiotoxicity in different classes of chemotherapy drugs using INDRA

Background

On NCBI, you will find two types of research papers when it comes to neurotoxicity and cardiotoxicity side effects of the 19 chemotherapy drugs. First, you will have a study of different classes of chemotherapy drugs and how they affect either cardiotoxicity or neurotoxicity, and its mechanism analysis (Fumagalli et al., 2021). Second, you will have a specific chemotherapy drug or a specific class of the chemotherapy drug and its mechanism analysis for its side effects for either cardiotoxicity or neurotoxicity. Also, there are limited amounts of research papers present on neurotoxicity compared to cardiotoxicity (Christidi & Brunham, 2021; Linders et al., 2024). Therefore, our proposed project is based on 19 chemotherapy drugs and analyzing their toxicities mainly cardiotoxicity and neurotoxicity. The project goal is to identify the reason behind these toxicities and analyze their mechanism and eventually find their protective agents. 

INDRA is a powerful artificial intelligence platform that uses natural language processing (NLP) and structured database queries to read, extract, clean, and organize mechanistic biological knowledge from scientific literature and databases. Its pipeline involves three key steps, Reading and Understanding: INDRA uses NLP tools (such as REACH) to read sentences from biomedical papers or structured databases to identify interactions—for example, “Protein A activates Protein B.” Cleaning and Organizing: INDRA then removes duplicates, corrects errors, fills in missing details, and focuses on biologically meaningful statements supported by peer-reviewed evidence. Assembling Mechanistic Models: Finally, INDRA converts this information into mechanistic networks and diagrams that show how molecules, genes, proteins, drugs, and diseases interact inside biological systems (Gyori et al., 2017).


The difference between the proposed research contribution and previous research contribution is that we are using powerful tools and searching through hundreds of articles and trying to form mechanisms for all the drugs and different classes of drugs for both neurotoxicity and cardiotoxicity and verifying their results with peer-reviewed sources from INDRA results and INDRA Cogex 2-hop results. Then, we use INDRA CoGEX, Neo4J, and Network X on Python to create a network graph mapping out the mechanism. 



PyCharm Files

INDRA1.py file extracts evidence from the INDRA Database such as based on a single chemotherapy drug(modifiable) and side effects based on evidence count, prints statements relating to the chemotherapy drug, their side effects, and either Activation, Phosphorylation, etc. 
ProteinComplexes.py file extracts evidence based on 3-hop network graphs (can be modified to 2-hop network graphs), and belief score, and evidence count based on the MeshID (Cardiotoxicity or Neurotoxicity) from INDRA CogEx with the assistance of Neo4J.
NetworkGraphs file creates 19 network graphs based on the data extracted from ProteinComplexes.py file




References

Christidi, E., & Brunham, L. R. (2021). Regulated cell death pathways in doxorubicin-induced cardiotoxicity. Cell Death & Disease, 12, 339. https://doi.org/10.1038/s41419-021-03614-x
Fumagalli, G., Monza, L., Cavaletti, G., Rigolio, R., & Meregalli, C. (2021). Neuroinflammatory process involved in different preclinical models of chemotherapy-induced peripheral neuropathy. Frontiers in Immunology, 11, Article 626687. https://doi.org/10.3389/fimmu.2020.626687
Gyori Lab for Computational Biomedicine. (2024). indra_cogex: INDRA Context Graph Extension [Computer software]. GitHub. https://github.com/gyorilab/indra_cogex
Linders, A. N., Dias, I. B., López Fernández, T., et al. (2024). A review of the pathophysiological mechanisms of doxorubicin-induced cardiotoxicity and aging. npj Aging, 10, 9. https://doi.org/10.1038/s41514-024-00135-7

