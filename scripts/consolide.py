# -*- coding: utf-8 -*-
"""Fusion, normalisation et dédoublonnage des offres collectées."""
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from analysis import OFFRES_DIR, COLLECTE_DIR
from normalize import (NC, classify_title, techs_in_title, normalize_region, nexa_zone, normalize_contract,
                       normalize_seniority, seniority_hint_title, parse_salary, extract_skills, is_nc, norm,
                       clean_city, COEUR, EVOL, SPEC, IA, ADJ, EXCLU)

SCRATCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SCRATCH, "build")

OFFER_FILES = sorted(set(glob.glob(os.path.join(OFFRES_DIR, "*_offres.jsonl")) + glob.glob(os.path.join(COLLECTE_DIR, "*_offres.jsonl"))))
VOLUME_FILES = sorted(set(glob.glob(os.path.join(OFFRES_DIR, "*volumes.jsonl")) + glob.glob(os.path.join(COLLECTE_DIR, "*_volumes.jsonl"))))


def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"  ! ligne JSON invalide ignorée {os.path.basename(path)}:{i+1} ({e})")
    return rows


def canonical_url(u):
    u = str(u or "").strip()
    u = re.sub(r"[?&](utm_[a-z]+|ref|from|source|trk|refId|trackingId|position|pageNum|originalSubdomain)=[^&#]*", "", u)
    u = u.rstrip("/").lower()
    m = re.search(r"indeed\.com/viewjob\?jk=([a-z0-9]+)", u)
    if m:
        return "indeed:" + m.group(1)
    m = re.search(r"francetravail\.fr/offres/recherche/detail/([a-z0-9]+)", u)
    if m:
        return "francetravail:" + m.group(1)
    m = re.search(r"apec\.fr/.*?detail-offre/([a-z0-9]+)", u)
    if m:
        return "apec:" + m.group(1)
    m = re.search(r"hellowork\.com/fr-fr/emplois/(\d+)", u)
    if m:
        return "hellowork:" + m.group(1)
    m = re.search(r"linkedin\.com/jobs/view/[^/]*?(\d{8,})", u)
    if m:
        return "linkedin:" + m.group(1)
    m = re.search(r"welcometothejungle\.com/[a-z]{2}/companies/([^/]+)/jobs/([^/?#]+)", u)
    if m:
        return "wttj:" + m.group(1) + "/" + m.group(2)
    return u


def company_key(v):
    if is_nc(v):
        return ""
    s = norm(v)
    s = re.sub(r"\b(sas|sa|sarl|groupe|group|france|the|le|la|les|inc|ltd|eu|sasu)\b", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    return s


def title_key(v):
    s = norm(v)
    s = re.sub(r"\b(h/f|f/h|h/f/x|f/h/x|hf|fh|\(h/f\)|\(f/h\))\b", " ", s)
    s = re.sub(r"[^a-z0-9#+.]+", " ", s)
    s = re.sub(r"\b(le|la|les|de|du|des|un|une|et|en|a|pour|chez)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    rows = []
    for f in OFFER_FILES:
        r = load_jsonl(f)
        print(f"{os.path.basename(f)}: {len(r)}")
        for x in r:
            x["_fichier"] = os.path.basename(f)
        rows.extend(r)
    print("Total brut :", len(rows))

    # ---- normalisation ----
    for r in rows:
        title = r.get("INTITULE_BRUT", "")
        metier, fam = classify_title(title)
        r["METIER_NORMALISE"] = metier
        r["FAMILLE_METIER"] = fam
        r["TECHNOS_DANS_TITRE"] = " ; ".join(techs_in_title(title)) or NC
        reg, dept, tele = normalize_region(r.get("REGION"), r.get("DEPARTEMENT"), r.get("VILLE"))
        r["REGION_NORMALISEE"] = reg
        r["DEPARTEMENT_NORMALISE"] = dept
        r["VILLE_NORMALISEE"] = clean_city(r.get("VILLE"))
        r["ZONE_NEXA"] = nexa_zone(reg, dept, r.get("VILLE"), tele)
        tv = norm(r.get("TELETRAVAIL"))
        if tele and (is_nc(r.get("TELETRAVAIL")) or "nc" in tv):
            r["TELETRAVAIL_NORMALISE"] = "Oui (annonce en télétravail)"
        elif is_nc(r.get("TELETRAVAIL")):
            r["TELETRAVAIL_NORMALISE"] = NC
        elif tv.startswith("oui") or "full" in tv or "100" in tv or "total" in tv:
            r["TELETRAVAIL_NORMALISE"] = "Oui"
        elif tv.startswith("partiel") or "hybride" in tv or "jour" in tv or re.search(r"\d", tv):
            r["TELETRAVAIL_NORMALISE"] = "Partiel"
        elif tv.startswith("non"):
            r["TELETRAVAIL_NORMALISE"] = "Non"
        else:
            r["TELETRAVAIL_NORMALISE"] = "Partiel" if "partiel" in tv else NC
        r["TYPE_CONTRAT_NORMALISE"] = normalize_contract(r.get("TYPE_CONTRAT"), title)
        sen, origine = normalize_seniority(r.get("EXPERIENCE"), title, r["TYPE_CONTRAT_NORMALISE"])
        r["SENIORITE"] = sen
        r["SENIORITE_ORIGINE"] = origine
        r["SENIORITE_INDICATIVE_TITRE"] = seniority_hint_title(title)
        smin, smax, unit, raw = parse_salary(r.get("SALAIRE_MINIMUM"), r.get("SALAIRE_MAXIMUM"), r["TYPE_CONTRAT_NORMALISE"])
        r["SALAIRE_MIN_NUM"] = smin
        r["SALAIRE_MAX_NUM"] = smax
        r["SALAIRE_UNITE"] = unit
        r["SALAIRE_MEDIAN_OFFRE"] = (smin + smax) / 2 if smin and smax else (smin or smax)
        skills = extract_skills(r)
        r["_skills"] = skills
        for fam_s, items in skills.items():
            r["COMP_" + fam_s] = " ; ".join(items)
        ia_expl = not is_nc(r.get("COMPETENCES_IA"))
        r["MENTION_IA_EXPLICITE"] = "Oui" if (ia_expl or "IA_GENERATIVE" in skills or "OUTILS_DE_CODAGE_IA" in skills) else "Non"
        r["OUTIL_CODAGE_IA_CITE"] = " ; ".join(skills.get("OUTILS_DE_CODAGE_IA", [])) or "Non"
        r["STATUT_DONNEE"] = "OBSERVE"

    # ---- dédoublonnage ----
    by_url = {}
    for r in rows:
        r["_curl"] = canonical_url(r.get("URL"))
    order = sorted(rows, key=lambda r: (r["_fichier"], r.get("ID_OFFRE", "")))
    clusters = {}
    cluster_of = {}
    for r in order:
        cu = r["_curl"]
        if cu in by_url:
            r["STATUT_DOUBLON"] = "REPUBLICATION" if r["SOURCE"] == by_url[cu]["SOURCE"] else "DUPLICATION_MULTI_PLATEFORME"
            r["DOUBLON_DE"] = by_url[cu]["ID_OFFRE"]
            continue
        by_url[cu] = r
        r["STATUT_DOUBLON"] = None
    uniques = [r for r in order if r["STATUT_DOUBLON"] is None]
    # clé floue : entreprise + titre + ville
    seen = {}
    for r in uniques:
        ck = company_key(r.get("ENTREPRISE"))
        tk = title_key(r.get("INTITULE_BRUT"))
        vk = norm(r["VILLE_NORMALISEE"]) if not is_nc(r["VILLE_NORMALISEE"]) else ""
        key_strict = (ck, tk, vk) if ck else None
        key_loose = (tk, vk)
        if key_strict and key_strict in seen:
            ref = seen[key_strict]
            r["STATUT_DOUBLON"] = "REPUBLICATION" if r["SOURCE"] == ref["SOURCE"] else "DUPLICATION_MULTI_PLATEFORME"
            r["DOUBLON_DE"] = ref["ID_OFFRE"]
            continue
        if key_loose in seen and not ck and vk:
            ref = seen[key_loose]
            r["STATUT_DOUBLON"] = "OFFRE_PROBABLEMENT_IDENTIQUE"
            r["DOUBLON_DE"] = ref["ID_OFFRE"]
            continue
        r["STATUT_DOUBLON"] = "OFFRE_UNIQUE"
        r["DOUBLON_DE"] = ""
        if key_strict:
            seen[key_strict] = r
        seen.setdefault(key_loose, r)

    stats = Counter(r["STATUT_DOUBLON"] for r in rows)
    print("Dédoublonnage :", dict(stats))

    with open(os.path.join(OUT, "offres_consolidees.json"), "w", encoding="utf-8") as f:
        json.dump([{k: v for k, v in r.items() if not k.startswith("_") or k == "_skills"} for r in rows], f, ensure_ascii=False, indent=0)

    # volumes
    vols = []
    for f in VOLUME_FILES:
        for v in load_jsonl(f):
            v["_fichier"] = os.path.basename(f)
            vols.append(v)
    # dédoublonner volumes identiques (URL + date + nombre)
    seenv = set()
    uv = []
    for v in vols:
        k = (norm(v.get("URL")), str(v.get("DATE_DU_COMPTE")), norm(v.get("NOMBRE")), norm(v.get("INTITULE_RECHERCHE")), norm(v.get("ZONE")))
        if k in seenv:
            continue
        seenv.add(k)
        uv.append(v)
    with open(os.path.join(OUT, "volumes_consolides.json"), "w", encoding="utf-8") as f:
        json.dump(uv, f, ensure_ascii=False, indent=0)
    print("Volumes :", len(vols), "->", len(uv))

    # quelques stats
    U = [r for r in rows if r["STATUT_DOUBLON"] == "OFFRE_UNIQUE"]
    print("Offres uniques :", len(U))
    print(Counter(r["FAMILLE_METIER"] for r in U))
    print(Counter(r["METIER_NORMALISE"] for r in U).most_common(40))
    print(Counter(r["REGION_NORMALISEE"] for r in U).most_common())
    print(Counter(r["ZONE_NEXA"] for r in U))
    print(Counter(r["TYPE_CONTRAT_NORMALISE"] for r in U))
    print(Counter(r["SENIORITE"] for r in U))
    print("Salaires renseignés :", sum(1 for r in U if r["SALAIRE_MEDIAN_OFFRE"]), Counter(r["SALAIRE_UNITE"] for r in U if r["SALAIRE_MEDIAN_OFFRE"]))
    print("Mention IA explicite :", Counter(r["MENTION_IA_EXPLICITE"] for r in U))
    print("Outils codage IA :", Counter(r["OUTIL_CODAGE_IA_CITE"] for r in U))
    nonclass = [r["INTITULE_BRUT"] for r in U if r["METIER_NORMALISE"] == "Non classé"]
    print("Non classés :", nonclass[:40])
    excl = [r["INTITULE_BRUT"] for r in U if r["FAMILLE_METIER"] == EXCLU]
    print("Exclus :", excl[:40])


if __name__ == "__main__":
    main()
