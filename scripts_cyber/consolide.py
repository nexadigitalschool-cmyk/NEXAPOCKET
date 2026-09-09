# -*- coding: utf-8 -*-
"""Consolidation : dédoublonnage, normalisation, enrichissement des offres."""
import json, os, sys, re, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize as N

BASE = "/home/user/NEXAPOCKET/collecte_cyber"
OUT = "/home/user/NEXAPOCKET/collecte_cyber/consolide.json"

def load(f):
    p = os.path.join(BASE, f)
    if not os.path.exists(p): return []
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]

def canonical_url(u):
    u = (u or "").split("&tk=")[0].split("?from=mobRdr&")[0]
    m = re.search(r"jk=([0-9a-f]+)", u)
    if m: return "indeed:" + m.group(1)
    m = re.search(r"/detail/([0-9A-Z]+)", u)
    if m: return "francetravail:" + m.group(1)
    m = re.search(r"hellowork\.com/fr-fr/emplois/(\d+)", u)
    if m: return "hellowork:" + m.group(1)
    return u.rstrip("/").lower()

def main():
    offres = load("offres.jsonl")
    volumes = load("volumes.jsonl")
    etudes = load("etudes.jsonl")
    sans = load("sans_donnees.jsonl")

    seen_url, seen_sig = {}, {}
    out = []
    for o in offres:
        cu = canonical_url(o.get("URL",""))
        titre = o.get("INTITULE_BRUT","")
        contexte = " ".join(str(o.get(k,"")) for k in
            ["DESCRIPTION_SYNTHETIQUE","COMPETENCES","OUTILS","NORMES_REFERENTIELS","COMPETENCES_IA","PREUVE"])
        metier, famille, niv = N.classifier(titre, contexte)
        dep = o.get("DEPARTEMENT","NC"); ville = o.get("VILLE","NC")
        region = N.region_from(dep, ville)
        vnexa = N.ville_nexa(dep, ville, o.get("TELETRAVAIL","NC"))
        contrat = N.contrat_norm(o.get("TYPE_CONTRAT","NC"))
        senio = N.seniorite(o.get("EXPERIENCE","NC"), titre, o.get("TYPE_CONTRAT","NC"))
        champs = [titre, contexte, o.get("DIPLOME",""), o.get("CERTIFICATIONS_DEMANDEES","")]
        comps = N.extraire(champs, N.DICO)
        certs = N.extraire(champs, N.CERTIFS)
        tech = N.technicite(niv, comps) if famille != "EXCLU_DU_PERIMETRE" else 0
        sig = hashlib.md5(N.norm(titre + "|" + (o.get("ENTREPRISE","") or "") + "|" + ville).encode()).hexdigest()
        statut = "OFFRE_UNIQUE"
        if cu in seen_url: statut = "DUPLICATION_MULTI_PLATEFORME"
        elif sig in seen_sig: statut = "OFFRE_PROBABLEMENT_IDENTIQUE"
        seen_url.setdefault(cu, o.get("ID_OFFRE"))
        seen_sig.setdefault(sig, o.get("ID_OFFRE"))
        r = dict(o)
        r.update(dict(URL_CANONIQUE=cu, METIER_NORMALISE=metier, FAMILLE_METIER=famille,
            FAMILLE_LIB=N.FAMILLE_LIB[famille], REGION=region, VILLE_NEXA=vnexa,
            CONTRAT_NORMALISE=contrat, SENIORITE=senio,
            NIVEAU_ETUDE=N.niveau_etude(o.get("DIPLOME",""), contexte),
            NIVEAU_TECHNICITE=tech, NIVEAU_TECHNICITE_LIB=N.TECH_LIB[tech],
            COMPETENCES_DETECTEES=" ; ".join(sorted({n for _, n in comps})),
            FAMILLES_COMPETENCES=" ; ".join(sorted({f for f, _ in comps})),
            CERTIFICATIONS_DETECTEES=" ; ".join(sorted({n for _, n in certs})) or "Aucune mention",
            STATUT_DOUBLON=statut, DANS_PERIMETRE=(famille not in ("EXCLU_DU_PERIMETRE",))))
        out.append(r)

    data = dict(offres=out, volumes=volumes, etudes=etudes, sans_donnees=sans,
                date_collecte=N.DATE_COLLECTE)
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    uniq = [o for o in out if o["STATUT_DOUBLON"] == "OFFRE_UNIQUE"]
    per = [o for o in uniq if o["DANS_PERIMETRE"]]
    print(f"Volume brut collecté : {len(out)} lignes")
    print(f"Offres uniques       : {len(uniq)}  (taux de doublons {100*(len(out)-len(uniq))/max(1,len(out)):.1f} %)")
    print(f"Dans le périmètre    : {len(per)}   (hors périmètre : {len(uniq)-len(per)})")
    print(f"Points de volume     : {len(volumes)} | études : {len(etudes)} | plateformes sans données : {len(sans)}")
    from collections import Counter
    print("\n--- Familles (offres uniques dans le périmètre) ---")
    for f, c in Counter(o["FAMILLE_LIB"] for o in per).most_common():
        print(f"  {c:4d}  {f}")
    print("\n--- Contrats ---")
    for f, c in Counter(o["CONTRAT_NORMALISE"] for o in per).most_common(): print(f"  {c:4d}  {f}")
    print("\n--- Séniorité ---")
    for f, c in Counter(o["SENIORITE"] for o in per).most_common(): print(f"  {c:4d}  {f}")
    print("\n--- Régions ---")
    for f, c in Counter(o["REGION"] for o in per).most_common(8): print(f"  {c:4d}  {f}")
    print("\n--- Villes NEXA ---")
    for f, c in Counter(o["VILLE_NEXA"] for o in per).most_common(): print(f"  {c:4d}  {f}")
    print("\n--- Technicité ---")
    for f, c in sorted(Counter(o["NIVEAU_TECHNICITE"] for o in per).items()): print(f"  {c:4d}  niveau {f}")

main()
