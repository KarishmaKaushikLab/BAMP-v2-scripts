import pandas as pd
from math import isnan

pubmed_ids = pd.read_csv("pubmed_ids.csv")
pdb_pub_map = pd.read_csv("PDB_PubMed_mapping.csv").dropna()
uni_pub_map = pd.read_csv("UniProt_PubMed_mapping.csv")
PMID = set([int(pub_id) for pub_id in pubmed_ids['PubMed_ID']])
PDB_PMID = set([int(pub_id) for pub_id in pdb_pub_map['PMID']])

temp = [i for i in uni_pub_map['PubMed_ID'] if type(i) == str]
UNI_PMID = []

for item in temp:
    if item.split(';'):
        UNI_PMID += [int(i.strip()) for i in item.split(';')]
    else :
        UNI_PMID += [int(item.strip())]

UNI_PMID = set(UNI_PMID)

uniprot_ids = pd.read_csv("Uniprot_ids.csv")
UNI_ID = set(list(uniprot_ids['Uniprot_ID']))

uni_pdb_map = pd.read_csv("UniProt_PDB_mapping.csv")
UNI_PDB = set(list(uni_pdb_map['UniProt_ID']))

print (len(PDB_PMID),len(UNI_PMID), len(UNI_PDB))
print ("Intersection of PDB and PubMed = ", len(PDB_PMID.intersection(PMID)))
print ("Intersection of UniProt and PubMed = ", len(UNI_PMID.intersection(PMID)))
print ("Intersection of UniProt and PDB = ", len(UNI_PDB.intersection(UNI_ID)))
print ("Intersection of all three databases = ",len(UNI_PMID.intersection(PMID,PDB_PMID)))






