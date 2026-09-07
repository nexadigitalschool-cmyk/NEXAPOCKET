#!/usr/bin/env python3
"""Ingestion compacte d'offres.
Entrée stdin : une offre par ligne, champs separes par |
ID|SOURCE|URL|TITRE|ENTREPRISE|VILLE|DEPT|CONTRAT|EXP|SAL|TT|COMP|PREUVE
La requete WebSearch est passee en argv[1]. REGION est deduite du departement.
Champs vides -> NC. Deduplication sur URL.
"""
import sys, json, os, re

DEPT_REGION = {}
def _reg(depts, region):
    for d in depts: DEPT_REGION[d] = region
_reg(['75','77','78','91','92','93','94','95'], "Île-de-France")
_reg(['01','03','07','15','26','38','42','43','63','69','73','74'], "Auvergne-Rhône-Alpes")
_reg(['21','25','39','58','70','71','89','90'], "Bourgogne-Franche-Comté")
_reg(['22','29','35','56'], "Bretagne")
_reg(['18','28','36','37','41','45'], "Centre-Val de Loire")
_reg(['2A','2B','20'], "Corse")
_reg(['08','10','51','52','54','55','57','67','68','88'], "Grand Est")
_reg(['02','59','60','62','80'], "Hauts-de-France")
_reg(['14','27','50','61','76'], "Normandie")
_reg(['16','17','19','23','24','33','40','47','64','79','86','87'], "Nouvelle-Aquitaine")
_reg(['09','11','12','30','31','32','34','46','48','65','66','81','82'], "Occitanie")
_reg(['44','49','53','72','85'], "Pays de la Loire")
_reg(['04','05','06','13','83','84'], "Provence-Alpes-Côte d'Azur")
_reg(['971','972','973','974','976'], "Outre-mer")

FIELDS = ["ID_OFFRE","SOURCE","URL","INTITULE_BRUT","ENTREPRISE","VILLE","DEPARTEMENT",
          "REGION","TYPE_CONTRAT","EXPERIENCE","SALAIRE_MINIMUM","SALAIRE_MAXIMUM",
          "TELETRAVAIL","COMPETENCES_BRUTES","PREUVE","REQUETE","DATE_COLLECTE"]

def norm(v):
    v = (v or "").strip()
    return v if v else "NC"

def split_sal(s):
    s = norm(s)
    if s == "NC": return "NC","NC"
    m = re.match(r'^\s*([\d]+)\s*-\s*([\d]+)\s*$', s)
    if m: return m.group(1), m.group(2)
    return s, s

def main():
    requete = sys.argv[1] if len(sys.argv) > 1 else "NC"
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mkt_offres.jsonl")
    seen = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try: seen.add(json.loads(line).get("URL"))
                    except Exception: pass
    added = skipped = 0
    out = open(path, "a", encoding="utf-8")
    for raw in sys.stdin:
        raw = raw.rstrip("\n")
        if not raw.strip() or raw.lstrip().startswith("#"): continue
        p = raw.split("|")
        if len(p) < 13:
            p = p + [""] * (13 - len(p))
        (oid, source, url, titre, ent, ville, dept, contrat, exp, sal, tt, comp, preuve) = [x.strip() for x in p[:13]]
        if not url: continue
        if url in seen:
            skipped += 1; continue
        seen.add(url)
        smin, smax = split_sal(sal)
        dept_n = norm(dept)
        rec = dict(zip(FIELDS, [
            norm(oid), norm(source), url, norm(titre), norm(ent), norm(ville), dept_n,
            DEPT_REGION.get(dept_n, "NC"), norm(contrat), norm(exp), smin, smax,
            norm(tt), norm(comp), norm(preuve), requete, "2026-09-07"]))
        out.write(json.dumps(rec, ensure_ascii=False) + "\n")
        added += 1
    out.close()
    total = sum(1 for _ in open(path, encoding="utf-8"))
    print(f"+{added} ajoutees, {skipped} doublons ignores, total={total}")

main()
