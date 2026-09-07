#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consolidation : normalisation, dédoublonnage, agrégats. Sortie : mkt_consolide.json"""
import json, os, re, sys, collections, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize_mkt as N

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "collecte_mkt")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "collecte_mkt", "mkt_consolide.json")

def load(f):
    p = os.path.join(BASE, f)
    if not os.path.exists(p): return []
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]

offres = load("mkt_offres.jsonl")
volumes = load("mkt_volumes.jsonl")
etudes = load("mkt_etudes.jsonl")

# ------------------------------------------------------------ NORMALISATION
for o in offres:
    txt = " ".join([o.get("INTITULE_BRUT",""), o.get("COMPETENCES_BRUTES",""), o.get("PREUVE","")])
    metier, famille, tech_base = N.classer(o["INTITULE_BRUT"], o.get("COMPETENCES_BRUTES",""))
    o["METIER_NORMALISE"] = metier
    o["FAMILLE_METIER"] = famille
    o["TYPE_CONTRAT_N"] = N.norm_contrat(o.get("TYPE_CONTRAT",""), o["INTITULE_BRUT"])
    o["SENIORITE"] = N.norm_seniorite(o.get("EXPERIENCE",""), o["TYPE_CONTRAT_N"], o["INTITULE_BRUT"])
    comps = N.detecter_competences(txt)
    o["COMPETENCES"] = comps
    plates = [c for l in comps.values() for c in l]
    o["COMPETENCES_PLATES"] = plates
    o["NIVEAU_TECHNICITE"] = N.niveau_technicite(plates, tech_base)
    o["VILLE_NEXA"] = N.ville_nexa(o.get("DEPARTEMENT","NC"))
    smin = N.parse_salaire(o.get("SALAIRE_MINIMUM"))
    smax = N.parse_salaire(o.get("SALAIRE_MAXIMUM"))
    o["SAL_MIN_N"], o["SAL_MAX_N"] = smin, smax
    o["SAL_MOY_N"] = (smin + smax) / 2 if smin and smax else (smin or smax)
    tt = N.key(o.get("TELETRAVAIL",""))
    o["TELETRAVAIL_N"] = ("Oui" if ("oui" in tt or "full remote" in tt or "total" in tt) else
                          "Partiel" if ("partiel" in tt or "hybride" in tt) else
                          "Non" if "non" in tt else "NC")
    o["IA_MENTIONNEE"] = bool(set(plates) & {
        "IA générative (ChatGPT, Claude, Gemini…)", "Agents IA / prompt engineering",
        "IA appliquée au marketing (packshot, création, workflow)", "GEO / AEO / AI Search"})

# ------------------------------------------------------------ DÉDOUBLONNAGE
def sig(o):
    t = re.sub(r"[^a-z0-9]", "", N.key(o["INTITULE_BRUT"]))[:40]
    e = re.sub(r"[^a-z0-9]", "", N.key(o.get("ENTREPRISE","")))[:20]
    v = re.sub(r"[^a-z0-9]", "", N.key(o.get("VILLE","")))[:15]
    return (t, e, v)

vus = {}
for o in offres:
    s = sig(o)
    if s in vus and o.get("ENTREPRISE","NC") != "NC":
        o["STATUT_DOUBLON"] = "DUPLICATION_MULTI_PLATEFORME" if o["SOURCE"] != vus[s]["SOURCE"] else "OFFRE_PROBABLEMENT_IDENTIQUE"
    elif s in vus:
        o["STATUT_DOUBLON"] = "OFFRE_PROBABLEMENT_IDENTIQUE"
    else:
        o["STATUT_DOUBLON"] = "OFFRE_UNIQUE"; vus[s] = o

VOLUME_BRUT = len(offres)
uniques = [o for o in offres if o["STATUT_DOUBLON"] == "OFFRE_UNIQUE"]
perimetre = [o for o in uniques if o["FAMILLE_METIER"] not in ("EXCLU_DU_PERIMETRE",)]
coeur = [o for o in perimetre if o["FAMILLE_METIER"] != "METIER_ADJACENT"]

# ------------------------------------------------------------ AGRÉGATS
def pct(n, d): return round(100.0 * n / d, 1) if d else 0.0

def bloc(sel):
    n = len(sel)
    if not n: return {}
    contrats = collections.Counter(o["TYPE_CONTRAT_N"] for o in sel)
    senior = collections.Counter(o["SENIORITE"] for o in sel)
    sal = sorted(o["SAL_MOY_N"] for o in sel if o["SAL_MOY_N"])
    comps = collections.Counter(c for o in sel for c in set(o["COMPETENCES_PLATES"]))
    tech = collections.Counter(o["NIVEAU_TECHNICITE"] for o in sel)
    tt = collections.Counter(o["TELETRAVAIL_N"] for o in sel)
    return {
        "n": n,
        "contrats": dict(contrats), "contrats_pct": {k: pct(v, n) for k, v in contrats.items()},
        "seniorite": dict(senior), "seniorite_pct": {k: pct(v, n) for k, v in senior.items()},
        "salaire_n": len(sal),
        "salaire_median": round(statistics.median(sal)) if sal else None,
        "salaire_q1": round(statistics.quantiles(sal, n=4)[0]) if len(sal) >= 4 else None,
        "salaire_q3": round(statistics.quantiles(sal, n=4)[2]) if len(sal) >= 4 else None,
        "salaire_min": sal[0] if sal else None, "salaire_max": sal[-1] if sal else None,
        "competences_top": comps.most_common(15),
        "technicite": dict(tech),
        "technicite_moy": round(sum(o["NIVEAU_TECHNICITE"] for o in sel) / n, 2),
        "teletravail": dict(tt),
        "ia_pct": pct(sum(1 for o in sel if o["IA_MENTIONNEE"]), n),
        "alternance_pct": pct(contrats.get("ALTERNANCE", 0), n),
        "debutant_junior_pct": pct(senior.get("DEBUTANT", 0) + senior.get("JUNIOR", 0), n),
    }

par_famille = {f: bloc([o for o in perimetre if o["FAMILLE_METIER"] == f])
               for f in sorted(set(o["FAMILLE_METIER"] for o in perimetre))}
par_metier = {}
for m in sorted(set(o["METIER_NORMALISE"] for o in perimetre)):
    sel = [o for o in perimetre if o["METIER_NORMALISE"] == m]
    b = bloc(sel); b["famille"] = sel[0]["FAMILLE_METIER"]
    b["intitules"] = sorted(set(o["INTITULE_BRUT"] for o in sel))[:8]
    b["part_marche"] = pct(len(sel), len(perimetre))
    b["sources"] = len(set(o["SOURCE"] for o in sel))
    par_metier[m] = b

par_region = {}
for r in sorted(set(o["REGION"] for o in perimetre)):
    sel = [o for o in perimetre if o["REGION"] == r]
    b = bloc(sel); b["part_nationale"] = pct(len(sel), len(perimetre))
    b["familles"] = dict(collections.Counter(o["FAMILLE_METIER"] for o in sel))
    b["metiers_top"] = collections.Counter(o["METIER_NORMALISE"] for o in sel).most_common(6)
    par_region[r] = b

par_ville = {}
for v in list(N.VILLES_NEXA) + ["National / distanciel"]:
    if v == "National / distanciel":
        sel = [o for o in perimetre if o["TELETRAVAIL_N"] == "Oui"]
    else:
        sel = [o for o in perimetre if o["VILLE_NEXA"] == v]
    b = bloc(sel)
    b["perimetre"] = N.PERIMETRES.get(v, "Offres explicitement en télétravail total / full remote, tous départements")
    b["familles"] = dict(collections.Counter(o["FAMILLE_METIER"] for o in sel))
    b["metiers_top"] = collections.Counter(o["METIER_NORMALISE"] for o in sel).most_common(8)
    b["part_marche"] = pct(len(sel), len(perimetre))
    par_ville[v] = b

# compétences détaillées
comp_detail = {}
for fam, comps in N.DICO.items():
    for nom in comps:
        sel = [o for o in perimetre if nom in o["COMPETENCES_PLATES"]]
        if not sel: 
            comp_detail[nom] = {"famille": fam, "n": 0, "pct": 0.0}
            continue
        comp_detail[nom] = {
            "famille": fam, "n": len(sel), "pct": pct(len(sel), len(perimetre)),
            "metiers": collections.Counter(o["METIER_NORMALISE"] for o in sel).most_common(4),
            "familles_metier": collections.Counter(o["FAMILLE_METIER"] for o in sel).most_common(4),
            "regions": collections.Counter(o["REGION"] for o in sel).most_common(3),
            "villes": collections.Counter(o["VILLE_NEXA"] for o in sel if o["VILLE_NEXA"]).most_common(3),
            "seniorite": collections.Counter(o["SENIORITE"] for o in sel).most_common(3),
            "contrats": collections.Counter(o["TYPE_CONTRAT_N"] for o in sel).most_common(3),
            "technicite_moy": round(sum(o["NIVEAU_TECHNICITE"] for o in sel) / len(sel), 2),
            "associations": [c for c, _ in collections.Counter(
                c for o in sel for c in o["COMPETENCES_PLATES"] if c != nom).most_common(4)],
        }

res = {
    "meta": {
        "date_collecte": "2026-09-07",
        "volume_brut": VOLUME_BRUT,
        "offres_uniques": len(uniques),
        "taux_doublons": pct(VOLUME_BRUT - len(uniques), VOLUME_BRUT),
        "offres_dans_perimetre": len(perimetre),
        "offres_coeur_marketing_digital": len(coeur),
        "offres_exclues": VOLUME_BRUT - len(perimetre),
        "sources": dict(collections.Counter(o["SOURCE"] for o in offres)),
        "nb_volumes": len(volumes), "nb_etudes": len(etudes),
        "statuts_doublon": dict(collections.Counter(o["STATUT_DOUBLON"] for o in offres)),
    },
    "national": bloc(perimetre),
    "coeur": bloc(coeur),
    "par_famille": par_famille,
    "par_metier": par_metier,
    "par_region": par_region,
    "par_ville": par_ville,
    "competences": comp_detail,
}
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(offres, open(OUT.replace("consolide", "offres_normalisees"), "w", encoding="utf-8"), ensure_ascii=False)

m = res["meta"]
print(f"Volume brut          : {m['volume_brut']}")
print(f"Offres uniques       : {m['offres_uniques']}  (taux doublons {m['taux_doublons']} %)")
print(f"Dans le périmètre    : {m['offres_dans_perimetre']}")
print(f"Cœur marketing digital: {m['offres_coeur_marketing_digital']}")
print(f"Exclues              : {m['offres_exclues']}")
print()
print("--- Par famille (offres uniques dans le périmètre) ---")
for f, b in sorted(par_famille.items(), key=lambda x: -x[1].get("n", 0)):
    print(f"{b['n']:4d}  {f:26s}  alt {b['alternance_pct']:5.1f}%  déb+jun {b['debutant_junior_pct']:5.1f}%  tech {b['technicite_moy']:.2f}  IA {b['ia_pct']:.1f}%")
