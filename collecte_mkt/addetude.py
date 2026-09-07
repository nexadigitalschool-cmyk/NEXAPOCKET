#!/usr/bin/env python3
"""Etudes/sources. stdin: TITRE|ORGANISME|DATE_PUBLICATION|PERIMETRE|METHODE|ECHANTILLON|RESULTAT_UTILISE|URL|PAGE|FIABILITE"""
import sys, json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mkt_etudes.jsonl")
seen = set()
if os.path.exists(p):
    for line in open(p, encoding="utf-8"):
        if line.strip():
            d = json.loads(line); seen.add((d.get("URL"), d.get("RESULTAT_UTILISE")[:60]))
K = ["TITRE","ORGANISME","DATE_PUBLICATION","PERIMETRE","METHODE","TAILLE_ECHANTILLON","RESULTAT_UTILISE","URL","PAGE_DU_RAPPORT","NIVEAU_DE_FIABILITE"]
n = s = 0
with open(p, "a", encoding="utf-8") as f:
    for raw in sys.stdin:
        if not raw.strip() or raw.lstrip().startswith("#"): continue
        c = [x.strip() for x in raw.rstrip("\n").split("|")]; c += [""] * (10 - len(c))
        rec = dict(zip(K, c[:10]))
        for k in rec:
            if not rec[k]: rec[k] = "NC"
        rec["DATE_CONSULTATION"] = "2026-09-07"
        key = (rec["URL"], rec["RESULTAT_UTILISE"][:60])
        if key in seen: s += 1; continue
        seen.add(key); f.write(json.dumps(rec, ensure_ascii=False) + "\n"); n += 1
print(f"etudes +{n}, {s} dbl, total={sum(1 for _ in open(p, encoding='utf-8'))}")
