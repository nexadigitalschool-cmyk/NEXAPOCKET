#!/usr/bin/env python3
"""Volumes (stocks d'offres datés). stdin: SOURCE|URL|INTITULE_RECHERCHE|ZONE|CONTRAT|NOMBRE|DATE_DU_COMPTE|PREUVE ; argv[1]=requete"""
import sys, json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mkt_volumes.jsonl")
req = sys.argv[1] if len(sys.argv) > 1 else "NC"
seen = set()
if os.path.exists(p):
    for line in open(p, encoding="utf-8"):
        if line.strip():
            d = json.loads(line); seen.add((d.get("URL"), d.get("DATE_DU_COMPTE"), d.get("NOMBRE")))
n = s = 0
with open(p, "a", encoding="utf-8") as f:
    for raw in sys.stdin:
        if not raw.strip() or raw.lstrip().startswith("#"): continue
        c = [x.strip() for x in raw.rstrip("\n").split("|")]
        c += [""] * (8 - len(c))
        rec = dict(zip(["SOURCE","URL","INTITULE_RECHERCHE","ZONE","TYPE_CONTRAT","NOMBRE","DATE_DU_COMPTE","PREUVE"], c[:8]))
        for k in rec:
            if not rec[k]: rec[k] = "NC"
        rec["REQUETE"] = req; rec["DATE_COLLECTE"] = "2026-09-07"
        key = (rec["URL"], rec["DATE_DU_COMPTE"], rec["NOMBRE"])
        if key in seen: s += 1; continue
        seen.add(key); f.write(json.dumps(rec, ensure_ascii=False) + "\n"); n += 1
print(f"volumes +{n}, {s} doublons, total={sum(1 for _ in open(p, encoding='utf-8'))}")
