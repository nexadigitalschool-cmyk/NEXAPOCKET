import json, sys, os
BASE="/home/user/NEXAPOCKET/collecte_cyber"
CH=["ID_OFFRE","SOURCE","URL","DATE_PUBLICATION","DATE_COLLECTE","ENTREPRISE","CABINET_OU_INTERMEDIAIRE","INTITULE_BRUT","VILLE","DEPARTEMENT","TELETRAVAIL","TYPE_CONTRAT","SALAIRE_MINIMUM","SALAIRE_MAXIMUM","EXPERIENCE","DIPLOME","CERTIFICATIONS_DEMANDEES","SECTEUR_ENTREPRISE","OUTILS","COMPETENCES","NORMES_REFERENTIELS","COMPETENCES_IA","ANGLAIS","DESCRIPTION_SYNTHETIQUE","PREUVE","REQUETE"]
def main():
    data=json.load(sys.stdin); path=os.path.join(BASE,"offres.jsonl")
    seen=set()
    if os.path.exists(path):
        for l in open(path,encoding="utf-8"):
            l=l.strip()
            if l: seen.add(json.loads(l)["URL"])
    n=0
    with open(path,"a",encoding="utf-8") as f:
        for r in data:
            if r.get("URL") in seen: continue
            seen.add(r["URL"])
            rec={k:r.get(k,"NC") for k in CH}
            rec["DATE_COLLECTE"]="2026-09-08"
            f.write(json.dumps(rec,ensure_ascii=False)+"\n"); n+=1
    print(f"offres.jsonl: +{n} (total {sum(1 for _ in open(path,encoding='utf-8'))})")
main()
