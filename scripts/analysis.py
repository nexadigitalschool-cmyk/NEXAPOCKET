# -*- coding: utf-8 -*-
"""Agrégats partagés par l'Excel et le Word."""
import json
import os
import re
import statistics
from collections import Counter, defaultdict

from normalize import NC, is_nc, norm, COEUR, EVOL, SPEC, IA, ADJ, EXCLU, SKILLS

BUILD = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.path.dirname(BUILD)


def _first_existing(*cands):
    for c in cands:
        if os.path.isdir(c):
            return c
    return cands[0]


OFFRES_DIR = _first_existing(os.path.join(SCRATCH, "offres"), os.path.join(SCRATCH, "collecte", "offres"))
ETUDES_DIR = _first_existing(os.path.join(SCRATCH, "etudes"), os.path.join(SCRATCH, "collecte", "etudes"))
COLLECTE_DIR = os.path.join(SCRATCH, "collecte")

FAMILLE_LABEL = {COEUR: "COEUR_DE_MARCHE", EVOL: "EVOLUTION_NATURELLE", SPEC: "SPECIALISATION", IA: "METIER_EMERGENT_IA", ADJ: "METIER_ADJACENT", EXCLU: "EXCLU_DU_PERIMETRE"}
NEXA_CITIES = ["Paris et Île-de-France", "Lyon et métropole", "Lille et métropole", "Bordeaux et métropole", "Nantes et métropole", "Marseille et Aix-en-Provence", "Marché national à distance"]
NEXA_PERIMETRE = {
    "Paris et Île-de-France": "Région Île-de-France (75, 77, 78, 91, 92, 93, 94, 95)",
    "Lyon et métropole": "Département du Rhône / Métropole de Lyon (69 : Lyon, Villeurbanne, Bron, Vénissieux, Saint-Priest, Écully, Limonest...)",
    "Lille et métropole": "Métropole européenne de Lille (Lille, Villeneuve-d'Ascq, Roubaix, Tourcoing, Marcq-en-Barœul, Lesquin, Wasquehal, Loos, Lomme, Seclin)",
    "Bordeaux et métropole": "Bordeaux Métropole (Bordeaux, Mérignac, Pessac, Bègles, Talence, Cenon, Bruges, Le Haillan, Gradignan, Floirac, Lormont, Villenave-d'Ornon, Blanquefort, Eysines)",
    "Nantes et métropole": "Nantes Métropole (Nantes, Saint-Herblain, Carquefou, Rezé, Orvault, Bouguenais, Vertou, La Chapelle-sur-Erdre)",
    "Marseille et Aix-en-Provence": "Aix-Marseille-Provence (Marseille, Aix-en-Provence, Aubagne, Vitrolles, Les Milles, Gémenos, Rousset, Meyreuil, Martigues)",
    "Marché national à distance": "Offres en télétravail intégral sans rattachement à une ville (France entière)",
}
SENIORITES = ["DEBUTANT", "JUNIOR", "INTERMEDIAIRE", "SENIOR", "LEAD_OU_ARCHITECTE"]
CONTRATS = ["CDI", "CDD", "ALTERNANCE", "STAGE", "FREELANCE", "INTERIM", "MISSION_COURTE", "AUTRE"]


def load():
    with open(os.path.join(BUILD, "offres_consolidees.json"), encoding="utf-8") as f:
        rows = json.load(f)
    with open(os.path.join(BUILD, "volumes_consolides.json"), encoding="utf-8") as f:
        vols = json.load(f)
    return rows, vols


def uniques(rows):
    return [r for r in rows if r["STATUT_DOUBLON"] == "OFFRE_UNIQUE" and r["FAMILLE_METIER"] != EXCLU]


def pct(n, d):
    return round(100.0 * n / d, 1) if d else 0


def share_or_nc(n, d):
    return round(100.0 * n / d, 1) if d else NC


def median_or_nc(vals):
    vals = [v for v in vals if v]
    return round(statistics.median(vals)) if vals else NC


def q_or_nc(vals, q):
    vals = sorted(v for v in vals if v)
    if len(vals) < 4:
        return NC
    return round(statistics.quantiles(vals, n=4)[q])


def annual_salaries(rs):
    return [r["SALAIRE_MEDIAN_OFFRE"] for r in rs if r.get("SALAIRE_MEDIAN_OFFRE") and r.get("SALAIRE_UNITE") == "ANNUEL"]


def top_skills(rs, k=6, exclude=("SOFT_SKILLS", "PRODUIT_ET_BUSINESS", "FULL_STACK", "ANGLAIS")):
    c = Counter()
    for r in rs:
        for fam, items in r.get("_skills", {}).items():
            if fam in exclude:
                continue
            for it in items:
                if it == "IA (mention générale)":
                    continue
                c[it] += 1
    return c.most_common(k)


def ia_share(rs):
    n = sum(1 for r in rs if r.get("MENTION_IA_EXPLICITE") == "Oui")
    return n, share_or_nc(n, len(rs))


def teletravail_share(rs):
    """Les extraits ne mentionnent le télétravail que lorsqu'il est proposé : on mesure donc la part des offres
    dont le titre/extrait mentionne un télétravail total ou partiel, rapportée à TOUTES les offres du groupe."""
    yes = [r for r in rs if r.get("TELETRAVAIL_NORMALISE") in ("Oui", "Partiel", "Oui (annonce en télétravail)")]
    return len(yes), len(rs), share_or_nc(len(yes), len(rs))


def contract_counts(rs):
    c = Counter(r["TYPE_CONTRAT_NORMALISE"] for r in rs)
    return {k: c.get(k, 0) for k in CONTRATS}, c.get(NC, 0)


def seniority_counts(rs):
    c = Counter(r["SENIORITE"] for r in rs)
    return {k: c.get(k, 0) for k in SENIORITES}, c.get(NC, 0)


def median_experience(rs):
    vals = []
    for r in rs:
        e = norm(r.get("EXPERIENCE"))
        if not e or e.startswith("nc"):
            continue
        nums = [float(x.replace(",", ".")) for x in re.findall(r"(\d+(?:[.,]\d+)?)\s*(?:\+|ans|an\b|years|year)", e)]
        if nums:
            vals.append(min(nums))
        elif "debutant" in e or "sans experience" in e:
            vals.append(0)
    return (round(statistics.median(vals), 1), len(vals)) if vals else (NC, 0)


def confiance(n):
    if n >= 30:
        return "FORTE"
    if n >= 10:
        return "MOYENNE"
    return "FAIBLE"


def sources_count(rs):
    return len(set(r["SOURCE"] for r in rs))


# ----------------------------------------------------------------------------
# Volumes (stocks datés) : séries par intitulé / zone
# ----------------------------------------------------------------------------
def parse_count(s):
    s = norm(s).replace(" ", " ")
    m = re.search(r"(\d[\d ]*)", s)
    if not m:
        return None
    try:
        return int(m.group(1).replace(" ", ""))
    except ValueError:
        return None


def parse_date(s):
    s = str(s or "")
    m = re.match(r"(\d{4})-(\d{2})(?:-(\d{2}))?", s)
    if m:
        return m.group(1), m.group(2), (m.group(3) or "01")
    mois = {"janvier": "01", "fevrier": "02", "mars": "03", "avril": "04", "mai": "05", "juin": "06", "juillet": "07", "aout": "08", "septembre": "09", "octobre": "10", "novembre": "11", "decembre": "12"}
    mm = re.search(r"(\d{1,2})\s+([a-z]+)\s+(\d{4})", norm(s))
    if mm and mm.group(2) in mois:
        return mm.group(3), mois[mm.group(2)], mm.group(1).zfill(2)
    y = re.search(r"(20\d{2})", s)
    if y:
        return y.group(1), "00", "00"
    return NC, NC, NC


def norm_intitule(s):
    t = norm(s).replace("-", " ").replace("_", " ")
    t = re.sub(r"\b(emplois?|offres?|jobs?)\b", " ", t)
    t = re.sub(r"[«»\"']", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def norm_zone(s):
    t = norm(s)
    t = re.sub(r"\s*\([^)]*\)", "", t)  # 'lyon (69)' -> 'lyon'
    t = re.sub(r"\s*-\s*\d{5}$", "", t)
    t = t.replace("ile de france", "ile-de-france").replace("région ", "").replace("region ", "")
    if t in ("", "nc", "france entiere", "national", "toute la france", "france metropolitaine"):
        t = "france" if t not in ("", "nc") else t
    return t.strip()


def norm_contrat(s):
    t = norm(s)
    if not t or t in ("nc", "tous", "tous contrats", "all", "toutes"):
        return "nc"
    return t


def volume_series(vols):
    """Retourne dict (source, intitule_norm, zone_norm, contrat) -> liste (date, nombre, url, preuve)."""
    series = defaultdict(list)
    for v in vols:
        n = parse_count(v.get("NOMBRE"))
        y, m, d = parse_date(v.get("DATE_DU_COMPTE"))
        if n is None or y == NC:
            continue
        key = (v.get("SOURCE", NC), norm_intitule(v.get("INTITULE_RECHERCHE")), norm_zone(v.get("ZONE")), norm_contrat(v.get("TYPE_CONTRAT")))
        series[key].append((f"{y}-{m}-{d}", n, v.get("URL"), v.get("PREUVE"), v.get("NOMBRE")))
    for k in series:
        series[k].sort()
    return series


def evolution_from_series(series, intitule_patterns, zone_patterns=("france", "nc", ""), source="Indeed"):
    """Compare le dernier compte 2026 aux comptes 2025 et 2024 (même page/intitulé/zone/source). Retourne dict."""
    out = {"2026": None, "2025": None, "2024": None, "preuves": []}
    for (src, intit, zone, contrat), pts in series.items():
        if src != source or contrat not in ("nc", "tous", ""):
            continue
        if not any(re.fullmatch(p, intit) for p in intitule_patterns):
            continue
        if not any(re.fullmatch(z, zone) for z in zone_patterns):
            continue
        for date, n, url, preuve, nb in pts:
            y = date[:4]
            if y in out and (out[y] is None or date > out[y][0]):
                out[y] = (date, n, url, nb)
    return out


# ----------------------------------------------------------------------------
# Tension (règle explicite, documentée dans l'Excel)
# ----------------------------------------------------------------------------
def tension_level(n_offres, ia_flag=False, evol=None, senior_share=None, famille=None):
    """Règle simple et transparente : combinaison volume d'échantillon, évolution observée, part de seniors.
    Retourne (niveau, justification). Marqué ESTIMATION."""
    if n_offres < 5:
        return "DONNEES_INSUFFISANTES", "moins de 5 offres uniques dans l'échantillon"
    just = []
    score = 0
    if evol is not None:
        if evol <= -40:
            score -= 2; just.append(f"stock d'offres en fort recul ({evol:+.0f} % sur un an)")
        elif evol < -10:
            score -= 1; just.append(f"stock d'offres en légère baisse ({evol:+.0f} %)")
        elif evol > 15:
            score += 1; just.append(f"stock d'offres en hausse ({evol:+.0f} %)")
        else:
            just.append(f"stock d'offres stable ({evol:+.0f} %)")
    if senior_share is not None and senior_share >= 50:
        score += 1; just.append(f"forte proportion de profils expérimentés demandés ({senior_share:.0f} %)")
    if famille in (SPEC, IA):
        score += 1; just.append("famille identifiée comme en tension par Apec/BMO (cloud, cyber, IA, data)")
    if score >= 2:
        return "TRES_EN_TENSION", " ; ".join(just)
    if score == 1:
        return "EN_TENSION", " ; ".join(just)
    if score == 0:
        return "EQUILIBRE", " ; ".join(just) or "aucun signal de déséquilibre observé"
    if score == -1:
        return "RALENTISSEMENT", " ; ".join(just)
    return "SATURE", " ; ".join(just)


# ----------------------------------------------------------------------------
# Études de la vague D (schéma complet TITRE / ORGANISME_OU_MEDIA / ... / THEME)
# ----------------------------------------------------------------------------
def load_d_etudes():
    out = []
    import glob as _glob
    for fp in sorted(_glob.glob(os.path.join(COLLECTE_DIR, "[DE]*_etudes.jsonl"))):
        for i, line in enumerate(open(fp, encoding="utf-8")):
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            if e.get("URL"):
                e["_fichier"] = os.path.basename(fp)
                out.append(e)
    return out


def actifs_from_d_etudes(etudes, regions):
    """Population active (ou emploi) régionale INSEE issue des études D (THEME POPULATION_ACTIVE)."""
    res = {}
    for e in etudes:
        if norm(e.get("THEME")) != "population_active" and "population active" not in norm(e.get("TITRE", "") + e.get("RESULTAT_UTILISE", "")):
            continue
        if "insee" not in norm(e.get("ORGANISME_OU_MEDIA", "") + e.get("TITRE", "") + e.get("URL", "")):
            continue
        txt = str(e.get("RESULTAT_UTILISE", "")) + " " + str(e.get("PERIMETRE", ""))
        for reg in regions:
            rn = norm(reg)
            # motif : "<région> : 5 123 000 actifs" ou "<région> 5,1 millions"
            for m in re.finditer(re.escape(rn) + r"[^0-9]{0,40}(\d[\d  .,]{2,}\s*(?:millions?|m)?)", norm(txt)):
                raw = m.group(1).strip()
                try:
                    if "million" in raw or raw.endswith(" m"):
                        val = float(re.sub(r"[^0-9,\.]", "", raw).replace(",", ".")) * 1e6
                    else:
                        val = float(re.sub(r"[^0-9]", "", raw))
                except ValueError:
                    continue
                if 50000 <= val <= 8e6 and reg not in res:
                    res[reg] = (int(val), e.get("URL"), e.get("TITRE"), e.get("DATE_PUBLICATION"))
    return res
