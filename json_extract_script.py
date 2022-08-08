import pandas as pd
import json

data = pd.read_csv("bamp_target_data.csv")

organisms, activity, tarids = dict(), dict(),dict()

for index, row in data.iterrows():
    organisms[row["source_organism"]] = list()
    activity[row["Function_PDB"]] = list()
    tarids[row['TARID']] = dict()
    
for index, row in data.iterrows():
    organisms[row["source_organism"]].append(str(row['TARID']))
    activity[row["Function_PDB"]].append(str(row['TARID']))
    tarids[row['TARID']]['src_org'] = row['source_organism']
    tarids[row['TARID']]['activity'] = row['Function_PDB']
    tarids[row['TARID']]['name'] = row['protein_name']
    tarids[row['TARID']]['uniprot_id'] = "https://www.uniprot.org/uniprot/" + row['UniProt_ID']

    pubmed_ids = [pubid.strip() for pubid in row['UniProt PubMed IDs'].split(";")]
    tarids[row['TARID']]['pubmed_id'] = pubmed_ids

    pdb_ids = [pdb_id.strip() for pdb_id in row['PDB_ID'].split(",")]
    pdb_link = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22full_text%22%2C%22parameters%22%3A%7B%22value%22%3A%22"
    tarids[row['TARID']]['pdb_link'] = pdb_link + "%2C%20".join(pdb_ids) + "%22%7D%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22logical_operator%22%3A%22and%22%2C%22label%22%3A%22full_text%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22start%22%3A0%2C%22rows%22%3A25%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%222eb4a5788c4133f52f8ff95cc9d518cd%22%7D%7D"

org_str = "organisms = '" + json.dumps(organisms) + "'"
act_str = "activity = '" + json.dumps(activity) + "'"
tarid_str = "tarids = '" + json.dumps(tarids) + "'"

with open("organisms_tarid.json","w") as handle:
    handle.write(org_str)

with open("activity_tarid.json","w") as handle:
    handle.write(act_str)

with open("tarids.json","w") as handle:
    handle.write(tarid_str)
