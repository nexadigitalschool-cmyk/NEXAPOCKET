# -*- coding: utf-8 -*-
"""Livrable 1 : NEXA_Marche_Emploi_Developpement_Web_France_2026.xlsx (5 onglets)."""
import json
import os
import re
import sys
from collections import Counter, defaultdict

from openpyxl import Workbook
from openpyxl.chart import BarChart, PieChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.formatting.rule import ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis import *  # noqa
from normalize import NC, is_nc, norm, COEUR, EVOL, SPEC, IA, ADJ, EXCLU, SKILLS, REGIONS

OUTDIR = os.environ.get("NEXA_OUT", "/home/user/NEXAPOCKET")
DATE_COLLECTE = "2026-09-06"

HDR_FILL = PatternFill("solid", fgColor="1F3864")
HDR_FONT = Font(bold=True, color="FFFFFF")
TITLE_FONT = Font(bold=True, size=14, color="1F3864")
SUB_FONT = Font(bold=True, size=11, color="1F3864")
NOTE_FONT = Font(italic=True, size=9, color="595959")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

# Correspondance métier normalisé -> intitulés Indeed (séries de stocks nationales)
METIER_SERIES = {
    "Développeur web (intitulé générique)": [r"developpeur web", r"developpeur informatique web"],
    "Développeur full stack": [r"developpeur full stack", r"developpeur web full stack", r"full stack developer"],
    "Développeur front-end": [r"developpeur front end", r"developpeur front-end"],
    "Développeur back-end": [r"developpeur back end", r"developpeur back-end"],
    "Développeur PHP / Symfony / Laravel": [r"developpeur php", r"developpeur symfony"],
    "Développeur Java / Spring": [r"developpeur java"],
    "Développeur .NET / C#": [r"developpeur \.net", r"developpeur net", r"developpeur c#"],
    "Développeur Python / Django": [r"developpeur python"],
    "Développeur JavaScript / TypeScript": [r"developpeur javascript", r"developpeur react", r"developpeur angular", r"developpeur node", r"developpeur typescript"],
    "Développeur (intitulé générique)": [r"developpeur"],
    "Software Engineer / Ingénieur logiciel": [r"software engineer", r"ingenieur logiciel", r"ingenieur developpement logiciel"],
    "Développeur mobile": [r"developpeur mobile"],
    "DevOps Engineer": [r"devops", r"ingenieur devops"],
    "Cloud Engineer": [r"cloud engineer", r"ingenieur cloud"],
    "AI Engineer / Développeur IA": [r"ai engineer", r"developpeur intelligence artificielle", r"developpeur ia", r"ingenieur ia"],
    "LLM / Generative AI Engineer": [r"developpeur llm", r"llm engineer", r"llm rag", r"rag llm"],
    "Tech Lead / Lead Developer": [r"tech lead", r"lead developer", r"lead developpeur"],
    "Concepteur développeur d'applications / logiciel": [r"developpeur logiciel", r"developpeur application", r"developpeur informatique"],
}
ZONE_SERIES = {
    "Paris et Île-de-France": [r"paris.*", r"ile-de-france.*", r"idf"],
    "Lyon et métropole": [r"lyon.*"],
    "Lille et métropole": [r"lille.*", r"nord.*"],
    "Bordeaux et métropole": [r"bordeaux.*", r"gironde.*"],
    "Nantes et métropole": [r"nantes.*", r"loire-atlantique.*"],
    "Marseille et Aix-en-Provence": [r"marseille.*", r"aix.*", r"bouches-du-rhone.*"],
    "Marché national à distance": [r"france \(teletravail\)", r"teletravail.*", r"remote.*"],
}
REGION_SERIES = {r: [norm(r) + ".*"] for r in REGIONS}
REGION_SERIES["Île-de-France"] += [r"paris.*", r"idf"]
REGION_SERIES["Auvergne-Rhône-Alpes"] += [r"lyon.*", r"grenoble.*", r"clermont.*", r"annecy.*", r"saint-etienne.*", r"rhone.*"]
REGION_SERIES["Hauts-de-France"] += [r"lille.*", r"amiens.*", r"nord.*"]
REGION_SERIES["Nouvelle-Aquitaine"] += [r"bordeaux.*", r"poitiers.*", r"limoges.*", r"pau.*", r"la rochelle.*", r"gironde.*"]
REGION_SERIES["Pays de la Loire"] += [r"nantes.*", r"angers.*", r"le mans.*"]
REGION_SERIES["Provence-Alpes-Côte d'Azur"] += [r"marseille.*", r"aix.*", r"nice.*", r"toulon.*", r"paca.*", r"provence.*"]
REGION_SERIES["Occitanie"] += [r"toulouse.*", r"montpellier.*"]
REGION_SERIES["Grand Est"] += [r"strasbourg.*", r"nancy.*", r"metz.*", r"reims.*"]
REGION_SERIES["Bretagne"] += [r"rennes.*", r"brest.*"]
REGION_SERIES["Normandie"] += [r"rouen.*", r"caen.*", r"le havre.*"]
REGION_SERIES["Centre-Val de Loire"] += [r"tours.*", r"orleans.*"]
REGION_SERIES["Bourgogne-Franche-Comté"] += [r"dijon.*", r"besancon.*"]


EVOL_SOURCES = ("Indeed", "HelloWork", "Apec", "France Travail")


def evol_pct(series, intit_patterns, zone_patterns, sources=EVOL_SOURCES):
    """Retourne (evol_2025, evol_2024, detail) à partir des stocks datés (buckets 'plus de N') : Indeed en priorité,
    puis HelloWork / Apec / France Travail si Indeed n'offre pas deux années comparables pour le même intitulé × zone."""
    for src_ in sources:
        e25, e24, det = _evol_pct_src(series, intit_patterns, zone_patterns, src_)
        if e25 != NC or e24 != NC:
            return e25, e24, det
    return NC, NC, ""


def _evol_pct_src(series, intit_patterns, zone_patterns, source):
    """Pour une source, apparie les comptes d'une MÊME page (même intitulé × même zone) : dernier compte de chaque année.
    Quand plusieurs pages sont comparables, retient celle dont le compte 2026 est le plus élevé (page la plus représentative)."""
    cands = {}
    for (src, intit, zone, contrat), pts in series.items():
        if src != source or contrat not in ("nc", "tous", ""):
            continue
        if not any(re.fullmatch(p, intit) for p in intit_patterns):
            continue
        if not any(re.fullmatch(z, zone) for z in zone_patterns):
            continue
        best = {}
        for date, n, url, preuve, nb in pts:
            y = date[:4]
            if y in ("2024", "2025", "2026") and (y not in best or date > best[y][0]):
                best[y] = (date, n)
        if "2026" in best and ("2025" in best or "2024" in best):
            cands[(intit, zone)] = best
    e25 = e24 = NC
    detail = []
    c25 = [(k, v) for k, v in cands.items() if "2025" in v]
    if c25:
        k, v = max(c25, key=lambda kv: (kv[1]["2026"][1], kv[1]["2026"][0]))
        if v["2025"][1]:
            e25 = round(100.0 * (v["2026"][1] - v["2025"][1]) / v["2025"][1])
            detail.append(f"{source} '{k[0]}' {k[1]} : {v['2025'][1]} ({v['2025'][0]}) -> {v['2026'][1]} ({v['2026'][0]})")
    c24 = [(k, v) for k, v in cands.items() if "2024" in v]
    if c24:
        k, v = max(c24, key=lambda kv: (kv[1]["2026"][1], kv[1]["2026"][0]))
        if v["2024"][1]:
            e24 = round(100.0 * (v["2026"][1] - v["2024"][1]) / v["2024"][1])
            detail.append(f"{source} '{k[0]}' {k[1]} : {v['2024'][1]} ({v['2024'][0]}) -> {v['2026'][1]} ({v['2026'][0]})")
    return e25, e24, " ; ".join(detail)


def fmt_evol(e):
    return NC if e == NC else f"ESTIMATION {e:+d} % (stocks jobboard arrondis, voir DETAIL_EVOLUTION)"


# ---------------------------------------------------------------------------
def style_header(ws, row, ncols, start_col=1):
    for c in range(start_col, start_col + ncols):
        cell = ws.cell(row=row, column=c)
        cell.fill = HDR_FILL
        cell.font = HDR_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BORDER


def write_table(ws, start_row, headers, rows, name, widths=None, start_col=1):
    for j, h in enumerate(headers):
        ws.cell(row=start_row, column=start_col + j, value=h)
    style_header(ws, start_row, len(headers), start_col)
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            c = ws.cell(row=start_row + 1 + i, column=start_col + j, value=v)
            c.border = BORDER
            c.alignment = Alignment(vertical="top", wrap_text=isinstance(v, str) and len(v) > 40)
    end_row = start_row + max(1, len(rows))
    ref = f"{get_column_letter(start_col)}{start_row}:{get_column_letter(start_col + len(headers) - 1)}{end_row}"
    if rows:
        t = Table(displayName=name, ref=ref)
        t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
        ws.add_table(t)
    if widths:
        for j, w in enumerate(widths):
            ws.column_dimensions[get_column_letter(start_col + j)].width = w
    return end_row


def title(ws, row, text, font=TITLE_FONT):
    ws.cell(row=row, column=1, value=text).font = font


def note(ws, row, text):
    ws.cell(row=row, column=1, value=text).font = NOTE_FONT


def skills_str(rs, k=6):
    return " ; ".join(f"{s} ({n})" for s, n in top_skills(rs, k)) or NC


def ia_skills_str(rs):
    c = Counter()
    for r in rs:
        for fam in ("IA_GENERATIVE", "OUTILS_DE_CODAGE_IA", "LOW_CODE_NO_CODE"):
            for it in r.get("_skills", {}).get(fam, []):
                c[it] += 1
    return " ; ".join(f"{s} ({n})" for s, n in c.most_common(6)) or "0"


def metier_row(m, rs, all_u, series, fam):
    n = len(rs)
    contrats, c_nc = contract_counts(rs)
    sen, s_nc = seniority_counts(rs)
    exp_med, exp_n = median_experience(rs)
    sal = annual_salaries(rs)
    tel_y, tel_k, tel_s = teletravail_share(rs)
    ia_n, ia_s = ia_share(rs)
    e25, e24, det = evol_pct(series, METIER_SERIES.get(m, [r"__none__"]), [r"france.*", r"nc", r""])
    known_sen = sum(sen.values())
    senior_share = 100.0 * (sen["SENIOR"] + sen["LEAD_OU_ARCHITECTE"]) / known_sen if known_sen else None
    tension, just = tension_level(n, evol=(e25 if e25 != NC else None), senior_share=senior_share, famille=fam)
    brut = sum(1 for r in all_u if r["METIER_NORMALISE"] == m)
    return [
        FAMILLE_LABEL[fam], m, " ; ".join(sorted(set(r["INTITULE_BRUT"] for r in rs))[:12]) + (" ..." if n > 12 else ""),
        brut, n, pct(n, len([x for x in all_u if x["STATUT_DOUBLON"] == "OFFRE_UNIQUE" and x["FAMILLE_METIER"] != EXCLU])),
        fmt_evol(e25), fmt_evol(e24),
        contrats["CDI"], contrats["CDD"], contrats["ALTERNANCE"], contrats["STAGE"], contrats["FREELANCE"], contrats["MISSION_COURTE"] + contrats["INTERIM"],
        sen["DEBUTANT"], sen["JUNIOR"], sen["INTERMEDIAIRE"], sen["SENIOR"], sen["LEAD_OU_ARCHITECTE"],
        (f"{exp_med} ans (n={exp_n})" if exp_med != NC else NC),
        (f"{median_or_nc(sal)} € (n={len(sal)})" if sal else NC),
        (f"{tel_s} % (n={tel_k})" if tel_k else NC),
        skills_str(rs), (f"{ia_s} % ({ia_n} offres) : " + ia_skills_str(rs)) if ia_n else "0",
        f"ESTIMATION {tension} ({just})", sources_count(rs), confiance(n),
        c_nc, s_nc, det or NC,
    ]


SYNTH_HEADERS = ["FAMILLE_METIER", "METIER_NORMALISE", "INTITULES_ASSOCIES", "VOLUME_BRUT", "OFFRES_UNIQUES", "PART_DU_MARCHE (% échantillon)", "EVOLUTION_2025", "EVOLUTION_2024",
                 "CDI", "CDD", "ALTERNANCE", "STAGE", "FREELANCE", "MISSIONS_COURTES", "DEBUTANT", "JUNIOR", "INTERMEDIAIRE", "SENIOR", "LEAD_ARCHITECTE", "EXPERIENCE_MEDIANE", "SALAIRE_MEDIAN (offres, annuel brut)", "TELETRAVAIL (% offres mentionnant un télétravail total/partiel)",
                 "COMPETENCES_DOMINANTES", "COMPETENCES_IA", "TENSION", "NOMBRE_SOURCES", "CONFIANCE", "CONTRAT_NON_RENSEIGNE", "SENIORITE_NON_RENSEIGNEE", "DETAIL_EVOLUTION"]


def build_synthese(wb, rows, U, series, vols):
    ws = wb.active
    ws.title = "SYNTHESE_METIERS"
    title(ws, 1, "SYNTHÈSE PAR MÉTIER NORMALISÉ — marché français du développement web, collecte du " + DATE_COLLECTE)
    note(ws, 2, "Conventions : 0 = absence réellement constatée dans l'échantillon ; NC = donnée indisponible dans les extraits collectés ; ESTIMATION = valeur reconstituée à partir de sources identifiées (stocks Indeed arrondis 'plus de N', règle de tension documentée en bas d'onglet). Échantillon = offres uniques après dédoublonnage (voir OFFRES_DETAILLEES). Les parts et médianes portent uniquement sur les offres dont le champ est renseigné.")
    fam_order = [COEUR, EVOL, SPEC, IA, ADJ]
    data = []
    by_m = defaultdict(list)
    for r in U:
        by_m[(r["FAMILLE_METIER"], r["METIER_NORMALISE"])].append(r)
    for fam in fam_order:
        keys = sorted([k for k in by_m if k[0] == fam], key=lambda k: -len(by_m[k]))
        for k in keys:
            data.append(metier_row(k[1], by_m[k], rows, series, fam))
    end = write_table(ws, 4, SYNTH_HEADERS, data, "T_SYNTHESE_METIERS",
                      widths=[22, 38, 60, 10, 10, 12, 22, 22, 7, 7, 11, 7, 9, 9, 9, 8, 12, 8, 10, 16, 20, 18, 60, 50, 60, 9, 10, 10, 10, 60])
    ws.freeze_panes = "C5"

    # ---- mini-vue nationale ----
    r0 = end + 3
    title(ws, r0, "MINI-VUE NATIONALE (échantillon collecté + repères externes)", SUB_FONT)
    brut = len(rows)
    uniq = [r for r in rows if r["STATUT_DOUBLON"] == "OFFRE_UNIQUE"]
    dup = Counter(r["STATUT_DOUBLON"] for r in rows)
    contrats, c_nc = contract_counts(U)
    sen, s_nc = seniority_counts(U)
    sal = annual_salaries(U)
    tel_y, tel_k, tel_s = teletravail_share(U)
    ia_n, ia_s = ia_share(U)
    known_c = sum(contrats.values())
    known_s = sum(sen.values())
    kv = [
        ("VOLUME_BRUT (lignes collectées, toutes plateformes)", brut, "OBSERVE"),
        ("OFFRES_UNIQUES (après dédoublonnage URL + entreprise/intitulé/ville)", len(uniq), "OBSERVE"),
        ("OFFRES_UNIQUES dans le périmètre (hors exclusions)", len(U), "OBSERVE"),
        ("TAUX_DE_DOUBLONS (multi-plateforme + probablement identiques)", f"{pct(dup.get('DUPLICATION_MULTI_PLATEFORME', 0) + dup.get('OFFRE_PROBABLEMENT_IDENTIQUE', 0), brut)} %", "OBSERVE"),
        ("TAUX_DE_REPUBLICATION (même plateforme)", f"{pct(dup.get('REPUBLICATION', 0), brut)} %", "OBSERVE"),
        ("Part CDI / CDD / ALTERNANCE / STAGE / FREELANCE (offres au contrat renseigné, n=%d)" % known_c,
         " / ".join(f"{k} {pct(contrats[k], known_c)} %" for k in ("CDI", "CDD", "ALTERNANCE", "STAGE", "FREELANCE")), "OBSERVE"),
        ("Part DEBUTANT / JUNIOR / INTERMEDIAIRE / SENIOR / LEAD (offres à la séniorité renseignée, n=%d)" % known_s,
         " / ".join(f"{k} {pct(sen[k], known_s)} %" for k in SENIORITES), "OBSERVE"),
        ("Part des offres accessibles sans expérience (DEBUTANT, y compris stage/alternance) sur séniorité renseignée", f"{pct(sen['DEBUTANT'], known_s)} %", "OBSERVE"),
        ("Salaire médian annuel brut affiché (offres renseignées)", f"{median_or_nc(sal)} € (n={len(sal)} ; Q1 {q_or_nc(sal, 0)} ; Q3 {q_or_nc(sal, 2)})", "OBSERVE"),
        ("Part des offres dont l'extrait mentionne un télétravail total ou partiel (les extraits ne signalent pas l'absence de télétravail)", f"{tel_s} % ({tel_y} offres)", "OBSERVE"),
        ("Part des offres avec mention explicite d'IA (outil, LLM, RAG, IA générative, agents)", f"{ia_s} % ({ia_n} offres)", "OBSERVE"),
        ("Part des offres citant un outil de codage IA (Copilot, Cursor, Claude Code, ChatGPT...)", f"{pct(sum(1 for r in U if r['OUTIL_CODAGE_IA_CITE'] != 'Non'), len(U))} % ({sum(1 for r in U if r['OUTIL_CODAGE_IA_CITE'] != 'Non')} offres)", "OBSERVE"),
        ("Nombre de sources (jobboards) couvertes", sources_count(U), "OBSERVE"),
        ("Repère Apec : offres cadres 'développeur' publiées sur apec.fr en 2025", "12 690 (-20 % vs 2024 ; -60 % vs 2022) — Apec, Les métiers cadres porteurs éd. 2026 (19/02/2026)", "ETUDE"),
        ("Repère Indeed : stock national 'Développeur Web' (fr.indeed.com)", "plus de 4 000 (02/07/2025) -> plus de 3 000 (26/05/2026 et 03/09/2026)", "OBSERVE (stocks arrondis)"),
        ("Repère Indeed Hiring Lab France (01/04/2026)", "offres Indeed revenues au niveau de février 2020, volume divisé par 2 depuis le pic de décembre 2022 ; 21 % des annonces de développement logiciel mentionnent l'IA", "ETUDE"),
        ("Repère Dares (04/02/2026, données 2024)", "métiers de l'informatique sortent de la tension 'très forte' (niveau 5) vers 'forte' (niveau 4), 1re fois depuis 2016", "ETUDE"),
        ("Repère BMO 2026 (France Travail)", "84 227 projets de recrutement dans le numérique, 49,5 % jugés difficiles ; 2,27 M projets tous secteurs (-6,5 %)", "ETUDE"),
        ("Repère Numeum (S1 2026)", "33 % des ESN ont réduit leurs recrutements de jeunes diplômés ; effectifs du secteur -1,8 % entre 2023 et 2025", "ETUDE"),
        ("Repère Apec prévisions 2026", "61 160 recrutements de cadres informaticiens prévus en 2026 (+4 %)", "ETUDE"),
    ]
    ws.cell(row=r0 + 1, column=1, value="INDICATEUR"); ws.cell(row=r0 + 1, column=2, value="VALEUR"); ws.cell(row=r0 + 1, column=3, value="STATUT")
    style_header(ws, r0 + 1, 3)
    for i, (k, v, s) in enumerate(kv):
        ws.cell(row=r0 + 2 + i, column=1, value=k).border = BORDER
        ws.cell(row=r0 + 2 + i, column=2, value=v).border = BORDER
        ws.cell(row=r0 + 2 + i, column=3, value=s).border = BORDER
    r1 = r0 + 2 + len(kv) + 1

    # ---- séries de stocks nationales ----
    title(ws, r1, "SÉRIES DE STOCKS D'OFFRES ACTIVES (comptes datés relevés sur les pages publiques des jobboards ; 'plus de N' = borne basse arrondie par la plateforme)", SUB_FONT)
    nat = []
    for (src, intit, zone, contrat), pts in sorted(series.items()):
        if not re.fullmatch(r"france.*|nc|", zone):
            continue
        for date, n, url, preuve, nb in pts:
            nat.append([src, intit, zone, contrat.upper() if contrat != "nc" else "Tous", date, n, nb, url, preuve])
    nat.sort(key=lambda x: (x[1], x[4]))
    end2 = write_table(ws, r1 + 1, ["SOURCE", "INTITULE_RECHERCHE", "ZONE", "TYPE_CONTRAT", "DATE_DU_COMPTE", "NOMBRE (borne basse)", "NOMBRE_AFFICHE", "URL", "PREUVE"], nat, "T_STOCKS_NATIONAUX")
    r2 = end2 + 2
    title(ws, r2, "MÉTHODE TENSION (ESTIMATION) : DONNEES_INSUFFISANTES si < 5 offres ; score = évolution du stock Indeed (≤ -40 % : -2 ; < -10 % : -1 ; > +15 % : +1) + part de seniors/leads ≥ 50 % (+1) + famille cloud/cyber/IA/data (+1, signalée en tension par Apec et BMO). Score ≥ 2 TRES_EN_TENSION, 1 EN_TENSION, 0 EQUILIBRE, -1 RALENTISSEMENT, ≤ -2 SATURE.", NOTE_FONT)

    # ---- études et données de marché (vague D, schéma complet) ----
    d_et = load_d_etudes()
    r2b = r2 + 2
    title(ws, r2b, "ÉTUDES ET DONNÉES DE MARCHÉ UTILISÉES (schéma complet : titre, organisme, auteur, date, périmètre, méthode, résultat, URL, page, fiabilité)", SUB_FONT)
    et_rows = [[e.get("THEME"), e.get("TITRE"), e.get("ORGANISME_OU_MEDIA"), e.get("AUTEUR") or "non indiqué", e.get("DATE_PUBLICATION"), e.get("DATE_CONSULTATION"), e.get("PERIMETRE"), e.get("METHODE"), e.get("RESULTAT_UTILISE"), e.get("URL"), e.get("PAGE_DU_RAPPORT"), str(e.get("FIABILITE", "")).upper()] for e in d_et]
    et_rows.sort(key=lambda x: (str(x[0]), str(x[2])))
    r2c = write_table(ws, r2b + 1, ["THEME", "TITRE", "ORGANISME", "AUTEUR", "DATE_PUBLICATION", "DATE_CONSULTATION", "PERIMETRE", "METHODE", "RESULTAT_UTILISE", "URL", "PAGE_DU_RAPPORT", "NIVEAU_DE_FIABILITE"], et_rows, "T_ETUDES") if et_rows else r2b
    r2 = r2c + 1

    # ---- graphiques ----
    # 1 offres par métier (top 15)
    top = sorted(data, key=lambda d: -d[4])[:15]
    cr = r2 + 3
    ws.cell(row=cr, column=1, value="Métier"); ws.cell(row=cr, column=2, value="Offres uniques")
    for i, d in enumerate(top):
        ws.cell(row=cr + 1 + i, column=1, value=d[1]); ws.cell(row=cr + 1 + i, column=2, value=d[4])
    ch = BarChart(); ch.type = "bar"; ch.title = "Offres uniques par métier (top 15, échantillon)"; ch.height = 9; ch.width = 22
    ch.add_data(Reference(ws, min_col=2, min_row=cr, max_row=cr + len(top)), titles_from_data=True)
    ch.set_categories(Reference(ws, min_col=1, min_row=cr + 1, max_row=cr + len(top)))
    ch.legend = None
    ws.add_chart(ch, f"E{cr}")
    # 2 séniorité
    sr = cr + len(top) + 2
    ws.cell(row=sr, column=1, value="Séniorité"); ws.cell(row=sr, column=2, value="Offres")
    for i, k in enumerate(SENIORITES):
        ws.cell(row=sr + 1 + i, column=1, value=k); ws.cell(row=sr + 1 + i, column=2, value=sen[k])
    p = PieChart(); p.title = "Séniorité demandée (offres renseignées)"; p.height = 8; p.width = 12
    p.add_data(Reference(ws, min_col=2, min_row=sr, max_row=sr + 5), titles_from_data=True)
    p.set_categories(Reference(ws, min_col=1, min_row=sr + 1, max_row=sr + 5))
    p.dataLabels = DataLabelList(); p.dataLabels.showPercent = True
    ws.add_chart(p, f"E{sr + 2}")
    # 3 contrats
    kr = sr + 8
    ws.cell(row=kr, column=1, value="Contrat"); ws.cell(row=kr, column=2, value="Offres")
    ck = ["CDI", "CDD", "ALTERNANCE", "STAGE", "FREELANCE"]
    for i, k in enumerate(ck):
        ws.cell(row=kr + 1 + i, column=1, value=k); ws.cell(row=kr + 1 + i, column=2, value=contrats[k])
    p2 = PieChart(); p2.title = "Types de contrat (offres renseignées)"; p2.height = 8; p2.width = 12
    p2.add_data(Reference(ws, min_col=2, min_row=kr, max_row=kr + 5), titles_from_data=True)
    p2.set_categories(Reference(ws, min_col=1, min_row=kr + 1, max_row=kr + 5))
    p2.dataLabels = DataLabelList(); p2.dataLabels.showPercent = True
    ws.add_chart(p2, f"L{sr + 2}")
    # 4 métiers en progression / recul (stocks Indeed nationaux avec 2 points d'années différentes)
    er = kr + 8
    ws.cell(row=er, column=1, value="Intitulé (Indeed France)"); ws.cell(row=er, column=2, value="Évolution stock 2026 vs 2025 (%)")
    ev = []
    for m in METIER_SERIES:
        e25, e24, det = evol_pct(series, METIER_SERIES[m], [r"france.*", r"nc", r""])
        if e25 != NC:
            ev.append((m, e25))
        elif e24 != NC:
            ev.append((m + " (vs 2024)", e24))
    for i, (m, e) in enumerate(ev):
        ws.cell(row=er + 1 + i, column=1, value=m); ws.cell(row=er + 1 + i, column=2, value=e)
    if ev:
        b = BarChart(); b.type = "bar"; b.title = "Métiers en progression ou en recul (stocks Indeed, ESTIMATION)"; b.height = 8; b.width = 22
        b.add_data(Reference(ws, min_col=2, min_row=er, max_row=er + len(ev)), titles_from_data=True)
        b.set_categories(Reference(ws, min_col=1, min_row=er + 1, max_row=er + len(ev)))
        b.legend = None
        ws.add_chart(b, f"E{er}")
    return data


# ---------------------------------------------------------------------------
REG_HEADERS = ["REGION", "FAMILLE_METIER", "METIER_NORMALISE", "VOLUME_BRUT", "OFFRES_UNIQUES", "PART_NATIONALE (% échantillon)", "OFFRES_POUR_100_000_ACTIFS", "CDI", "CDD", "ALTERNANCE", "STAGE", "FREELANCE",
               "JUNIOR (débutant + junior)", "INTERMEDIAIRE", "SENIOR (senior + lead)", "SALAIRE_MEDIAN", "TELETRAVAIL", "COMPETENCES_DOMINANTES", "SECTEUR_RECRUTEUR", "EVOLUTION", "TENSION", "CONFIANCE"]


def secteurs_str(rs):
    c = Counter(r["SECTEUR_ENTREPRISE"] for r in rs if not is_nc(r.get("SECTEUR_ENTREPRISE")))
    ent = Counter(r["ENTREPRISE"] for r in rs if not is_nc(r.get("ENTREPRISE")))
    s = " ; ".join(f"{k} ({n})" for k, n in c.most_common(4))
    e = " ; ".join(f"{k}" for k, n in ent.most_common(5))
    return (s or "secteur NC") + (" | recruteurs : " + e if e else "")


def load_regional_external():
    path = os.path.join(ETUDES_DIR, "regions_donnees.jsonl")
    out = []
    for p in [path] + [os.path.join(COLLECTE_DIR, "C_regions.jsonl")]:
        if os.path.exists(p):
            with open(p, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            out.append(json.loads(line))
                        except json.JSONDecodeError:
                            pass
    return out


def actifs_by_region(ext):
    """Population active / emploi par région si une ligne INSEE a été collectée."""
    res = {}
    for e in ext:
        th = norm(e.get("THEME")) + " " + norm(e.get("INDICATEUR"))
        if ("population active" in th or "actifs" in th or "emploi total" in th) and "insee" in norm(e.get("ORGANISME", "") + e.get("SOURCE", "")):
            reg = e.get("REGION_OU_VILLE")
            m = re.search(r"(\d[\d  ]{3,})", str(e.get("VALEUR")))
            if reg and m:
                try:
                    res[reg] = (int(re.sub(r"\D", "", m.group(1))), e.get("URL"))
                except ValueError:
                    pass
    return res


POP_2021 = {"Île-de-France": 12.0, "Auvergne-Rhône-Alpes": 8.1, "Nouvelle-Aquitaine": 6.0, "Occitanie": 6.0, "Hauts-de-France": 6.0}  # millions d'habitants au 1er janvier 2021, INSEE (Tableaux de l'économie française), relevé via collecte C
POP_URL = "https://www.insee.fr/fr/statistiques/3303305?sommaire=3353488"


def build_regions(wb, rows, U, series):
    ws = wb.create_sheet("REGIONS_METIERS")
    title(ws, 1, "RÉGIONS × MÉTIERS — échantillon d'offres uniques (collecte " + DATE_COLLECTE + ") et données externes régionales")
    note(ws, 2, "Une ligne par combinaison région × métier normalisé. PART_NATIONALE = part de l'échantillon national. OFFRES_POUR_100_000_ACTIFS = ESTIMATION calculée sur l'échantillon rapporté à la population active régionale INSEE quand elle a été relevée (source citée dans la cellule) ; à défaut, ESTIMATION pour 100 000 habitants (population INSEE 2021) ; sinon NC. Les ratios portent sur l'échantillon, pas sur le marché total. EVOLUTION = ESTIMATION à partir des stocks Indeed datés de la région/ville quand deux années sont disponibles.")
    ext = load_regional_external()
    actifs = actifs_by_region(ext)
    d_et = load_d_etudes()
    for reg, val in actifs_from_d_etudes(d_et, REGIONS).items():
        actifs.setdefault(reg, (val[0], val[1]))
    for e in d_et:
        if norm(e.get("THEME")) in ("regions", "tension") or any(norm(r) in norm(e.get("PERIMETRE", "")) for r in REGIONS if r != "Corse"):
            ext.append({"THEME": e.get("THEME"), "REGION_OU_VILLE": e.get("PERIMETRE"), "METIER": "", "INDICATEUR": e.get("TITRE"), "VALEUR": e.get("RESULTAT_UTILISE"),
                        "DATE_OU_PERIODE": e.get("DATE_PUBLICATION"), "ORGANISME": e.get("ORGANISME_OU_MEDIA"), "SOURCE": e.get("METHODE"), "URL": e.get("URL"), "CITATION": e.get("RESULTAT_UTILISE"), "FIABILITE": e.get("FIABILITE")})
    by = defaultdict(list)
    for r in U:
        by[(r["REGION_NORMALISEE"], r["FAMILLE_METIER"], r["METIER_NORMALISE"])].append(r)
    data = []
    reg_tot = Counter(r["REGION_NORMALISEE"] for r in U)
    for (reg, fam, m), rs in sorted(by.items(), key=lambda kv: (-reg_tot[kv[0][0]], kv[0][0], -len(kv[1]))):
        n = len(rs)
        contrats, _ = contract_counts(rs)
        sen, _ = seniority_counts(rs)
        sal = annual_salaries(rs)
        tel_y, tel_k, tel_s = teletravail_share(rs)
        e25, e24, det = evol_pct(series, METIER_SERIES.get(m, [r"__none__"]), REGION_SERIES.get(reg, [r"__none__"]))
        known_sen = sum(sen.values())
        senior_share = 100.0 * (sen["SENIOR"] + sen["LEAD_OU_ARCHITECTE"]) / known_sen if known_sen else None
        tension, just = tension_level(n, evol=(e25 if e25 != NC else None), senior_share=senior_share, famille=fam)
        brut = sum(1 for r in rows if r["REGION_NORMALISEE"] == reg and r["METIER_NORMALISE"] == m)
        per100k = "NC (population active régionale INSEE non extraite)"
        if reg in actifs:
            per100k = f"ESTIMATION {round(100000.0 * n / actifs[reg][0], 2)} offre(s) de l'échantillon pour 100 000 actifs (INSEE : {actifs[reg][0]:,} actifs)".replace(",", " ")
        elif reg in POP_2021:
            per100k = f"NC actifs ; ESTIMATION {round(100000.0 * n / (POP_2021[reg] * 1e6), 2)} offre(s) de l'échantillon pour 100 000 habitants (INSEE 2021 : {POP_2021[reg]} M hab.)"
        data.append([reg, FAMILLE_LABEL[fam], m, brut, n, pct(n, len(U)), per100k, contrats["CDI"], contrats["CDD"], contrats["ALTERNANCE"], contrats["STAGE"], contrats["FREELANCE"],
                     sen["DEBUTANT"] + sen["JUNIOR"], sen["INTERMEDIAIRE"], sen["SENIOR"] + sen["LEAD_OU_ARCHITECTE"],
                     (f"{median_or_nc(sal)} € (n={len(sal)})" if sal else NC), (f"{tel_s} % (n={tel_k})" if tel_k else NC),
                     skills_str(rs, 5), secteurs_str(rs), (fmt_evol(e25) if e25 != NC else (fmt_evol(e24) + " vs 2024" if e24 != NC else NC)), f"ESTIMATION {tension} ({just})", confiance(n)])
    end = write_table(ws, 4, REG_HEADERS, data, "T_REGIONS_METIERS", widths=[24, 22, 36, 9, 9, 12, 22, 6, 6, 10, 7, 9, 12, 12, 12, 16, 14, 50, 50, 26, 50, 10])
    ws.freeze_panes = "D5"

    # ---- matrice régions × familles / métiers principaux + carte thermique ----
    r0 = end + 3
    title(ws, r0, "MATRICE RÉGIONS × MÉTIERS (offres uniques, carte thermique)", SUB_FONT)
    mets = [m for m, _ in Counter(r["METIER_NORMALISE"] for r in U).most_common(14)]
    hdr = ["REGION", "TOTAL"] + mets + ["Part alternance+stage (%)", "Part junior/débutant (%, renseignées)", "Offres IA (mention explicite)", "Part télétravail mentionné (%)"]
    regs = [r for r, _ in reg_tot.most_common()]
    mat = []
    ks_by_reg = {}
    for reg in regs:
        rs = [r for r in U if r["REGION_NORMALISEE"] == reg]
        cnt = Counter(r["METIER_NORMALISE"] for r in rs)
        contrats, _ = contract_counts(rs)
        sen, _ = seniority_counts(rs)
        ks = sum(sen.values())
        ks_by_reg[reg] = ks
        tel_y, tel_k, tel_s = teletravail_share(rs)
        mat.append([reg, len(rs)] + [cnt.get(m, 0) for m in mets] + [pct(contrats["ALTERNANCE"] + contrats["STAGE"], len(rs)), (pct(sen["DEBUTANT"] + sen["JUNIOR"], ks) if ks else NC), ia_share(rs)[0], (tel_s if tel_k else NC)])
    end2 = write_table(ws, r0 + 1, hdr, mat, "T_MATRICE_REGIONS")
    if mat:
        rng = f"C{r0 + 2}:{get_column_letter(2 + len(mets))}{r0 + 1 + len(mat)}"
        ws.conditional_formatting.add(rng, ColorScaleRule(start_type="num", start_value=0, start_color="FFFFFF", mid_type="percentile", mid_value=50, mid_color="FFD966", end_type="max", end_color="C00000"))

    # ---- classements ----
    r1 = end2 + 3
    title(ws, r1, "CLASSEMENTS (échantillon collecté — à lire avec les repères BMO/Apec ci-dessous)", SUB_FONT)
    matr = [x for x in mat if x[0] in REGIONS]  # régions administratives uniquement (hors NC et télétravail)
    lead = sorted(matr, key=lambda x: -x[1])[:5]
    alt = sorted([x for x in matr if x[1] >= 15], key=lambda x: -x[-4])[:5]
    ia = sorted(matr, key=lambda x: -x[-2])[:5]
    lines = [
        ("Régions leaders (volume d'offres uniques dans l'échantillon)", " ; ".join(f"{x[0]} ({x[1]})" for x in lead)),
        ("Régions les plus favorables aux juniors (part débutant+junior sur séniorité renseignée, ≥ 10 offres renseignées)", " ; ".join(f"{x[0]} ({x[-3]} %, n={ks_by_reg[x[0]]})" for x in sorted([x for x in matr if ks_by_reg.get(x[0], 0) >= 10 and x[-3] != NC], key=lambda x: -x[-3])[:5])),
        ("Régions les plus favorables à l'alternance (part alternance+stage dans les offres uniques, ≥ 15 offres)", " ; ".join(f"{x[0]} ({x[-4]} %)" for x in alt)),
        ("Régions les plus porteuses pour les métiers liés à l'IA (offres avec mention IA explicite)", " ; ".join(f"{x[0]} ({x[-2]})" for x in ia)),
        ("Régions leaders selon BMO 2026 (tous métiers, projets de recrutement)", "Île-de-France 388 806 ; Auvergne-Rhône-Alpes 255 400 ; Nouvelle-Aquitaine 248 800 ; PACA 209 630 ; Occitanie 200 470 (France Travail, BMO 2026)"),
        ("Régions leaders selon Apec 2026 (recrutements de cadres prévus hors IDF)", "Auvergne-Rhône-Alpes ~35 300 (+3 %) ; Occitanie 19 500 (+6 %) ; PACA-Corse 18 800 (+4 %) ; Hauts-de-France 17 340 (+2 %) ; Pays de la Loire 15 400 (+5 %) (Apec, prévisions 2026)"),
    ]
    for i, (k, v) in enumerate(lines):
        ws.cell(row=r1 + 1 + i, column=1, value=k).font = Font(bold=True)
        ws.cell(row=r1 + 1 + i, column=2, value=v)

    # ---- données externes régionales ----
    r2 = r1 + len(lines) + 3
    title(ws, r2, "DONNEES_EXTERNES_REGIONALES (BMO, Apec, Dares, INSEE, jobboards — lignes collectées avec URL)", SUB_FONT)
    ext_rows = [[e.get("THEME"), e.get("REGION_OU_VILLE"), e.get("METIER"), e.get("INDICATEUR"), e.get("VALEUR"), e.get("DATE_OU_PERIODE"), e.get("ORGANISME"), e.get("SOURCE"), e.get("URL"), e.get("CITATION"), str(e.get("FIABILITE", "")).upper()] for e in ext]
    write_table(ws, r2 + 1, ["THEME", "REGION_OU_VILLE", "METIER", "INDICATEUR", "VALEUR", "DATE_OU_PERIODE", "ORGANISME", "SOURCE", "URL", "CITATION", "FIABILITE"], ext_rows, "T_EXTERNES_REGIONS")
    # stocks régionaux
    r3 = r2 + 3 + len(ext_rows)
    title(ws, r3, "STOCKS D'OFFRES DATÉS PAR RÉGION / VILLE (jobboards)", SUB_FONT)
    st = []
    for (src, intit, zone, contrat), pts in sorted(series.items()):
        if re.fullmatch(r"france.*|nc|", zone):
            continue
        for date, n, url, preuve, nb in pts:
            st.append([src, zone, intit, contrat.upper() if contrat != "nc" else "Tous", date, n, nb, url, preuve])
    st.sort(key=lambda x: (x[1], x[2], x[4]))
    write_table(ws, r3 + 1, ["SOURCE", "ZONE", "INTITULE_RECHERCHE", "TYPE_CONTRAT", "DATE_DU_COMPTE", "NOMBRE (borne basse)", "NOMBRE_AFFICHE", "URL", "PREUVE"], st, "T_STOCKS_REGIONS")
    return data


# ---------------------------------------------------------------------------
VILLE_HEADERS = ["VILLE", "PERIMETRE", "METIER_NORMALISE", "OFFRES_UNIQUES", "PART_DU_MARCHE_LOCAL (%)", "CDI", "CDD", "ALTERNANCE", "STAGE", "JUNIOR (débutant + junior)", "INTERMEDIAIRE", "SENIOR (senior + lead)", "SALAIRE_MEDIAN", "TELETRAVAIL",
                 "COMPETENCES_DOMINANTES", "COMPETENCES_IA", "SECTEURS_RECRUTEURS", "EVOLUTION", "TENSION", "POTENTIEL_NEXA", "RECOMMANDATION_CAMPUS"]


def potentiel(n, fam, contrats, sen, ia_n, total_ville):
    part = pct(n, total_ville)
    acc = contrats["ALTERNANCE"] + contrats["STAGE"]
    if n < 3:
        return "FAIBLE (données insuffisantes)", "Ne pas construire de promesse d'insertion locale sur ce métier sans collecte complémentaire."
    if fam == IA:
        return ("FORT" if n >= 8 else "MOYEN"), "Métier émergent : à traiter comme spécialisation de Mastère (M1/M2) et comme module transversal du Bachelor, pas comme filière Bachelor autonome."
    if fam == SPEC:
        return ("FORT" if n >= 8 else "MOYEN"), "Spécialisation : cible de Mastère (cloud, DevOps, qualité, sécurité) ; introduire les fondamentaux dès la 3e année."
    if fam == EVOL:
        return ("FORT" if n >= 8 else "MOYEN"), "Évolution du dev web : débouché naturel à 3-5 ans ; pertinent pour la communication M1/M2."
    if part >= 25 or n >= 15:
        p = "FORT"
    elif n >= 6:
        p = "MOYEN"
    else:
        p = "FAIBLE"
    reco = f"Cœur de marché local ({part} % de l'échantillon ville) ; {acc} offre(s) alternance/stage observée(s)"
    reco += " : socle Bachelor à maintenir, orienté full stack, tests et déploiement." if p == "FORT" else " : maintenir dans le socle commun, sans surdimensionner la promotion locale."
    return p, reco


def build_villes(wb, rows, U, series):
    ws = wb.create_sheet("VILLES_NEXA")
    title(ws, 1, "VILLES NEXA × MÉTIERS — Paris/IDF, Lyon, Lille, Bordeaux, Nantes, Marseille-Aix et marché national à distance")
    note(ws, 2, "PERIMETRE = périmètre géographique retenu autour de chaque campus (voir colonne). PART_DU_MARCHE_LOCAL = part du métier dans l'échantillon de la ville. POTENTIEL_NEXA et RECOMMANDATION_CAMPUS = lecture analytique (ESTIMATION) fondée sur l'échantillon et les repères externes, pas une mesure.")
    data = []
    for z in NEXA_CITIES:
        rz = [r for r in U if r["ZONE_NEXA"] == z]
        by = defaultdict(list)
        for r in rz:
            by[(r["FAMILLE_METIER"], r["METIER_NORMALISE"])].append(r)
        for (fam, m), rs in sorted(by.items(), key=lambda kv: -len(kv[1])):
            n = len(rs)
            contrats, _ = contract_counts(rs)
            sen, _ = seniority_counts(rs)
            sal = annual_salaries(rs)
            tel_y, tel_k, tel_s = teletravail_share(rs)
            ia_n, ia_s = ia_share(rs)
            e25, e24, det = evol_pct(series, METIER_SERIES.get(m, [r"__none__"]), ZONE_SERIES[z])
            ks = sum(sen.values())
            senior_share = 100.0 * (sen["SENIOR"] + sen["LEAD_OU_ARCHITECTE"]) / ks if ks else None
            tension, just = tension_level(n, evol=(e25 if e25 != NC else None), senior_share=senior_share, famille=fam)
            pot, reco = potentiel(n, fam, contrats, sen, ia_n, len(rz))
            data.append([z, NEXA_PERIMETRE[z], m, n, pct(n, len(rz)), contrats["CDI"], contrats["CDD"], contrats["ALTERNANCE"], contrats["STAGE"],
                         sen["DEBUTANT"] + sen["JUNIOR"], sen["INTERMEDIAIRE"], sen["SENIOR"] + sen["LEAD_OU_ARCHITECTE"],
                         (f"{median_or_nc(sal)} € (n={len(sal)})" if sal else NC), (f"{tel_s} % (n={tel_k})" if tel_k else NC),
                         skills_str(rs, 5), (f"{ia_s} % ({ia_n}) : " + ia_skills_str(rs)) if ia_n else "0", secteurs_str(rs),
                         (fmt_evol(e25) if e25 != NC else (fmt_evol(e24) + " vs 2024" if e24 != NC else NC)), f"ESTIMATION {tension} ({just})", pot, reco])
    end = write_table(ws, 4, VILLE_HEADERS, data, "T_VILLES_NEXA", widths=[26, 40, 36, 9, 10, 6, 6, 10, 7, 12, 12, 12, 16, 14, 50, 40, 50, 26, 50, 22, 70])
    ws.freeze_panes = "D5"

    # ---- synthèse comparative ----
    r0 = end + 3
    title(ws, r0, "SYNTHÈSE COMPARATIVE DES VILLES NEXA (échantillon + stocks Indeed datés)", SUB_FONT)
    hdr = ["VILLE", "OFFRES_UNIQUES", "PART_ECHANTILLON (%)", "METIER_N1", "METIER_N2", "METIER_N3", "CDI (%)", "ALTERNANCE+STAGE (%)", "FREELANCE (%)", "DEBUTANT+JUNIOR (% renseignées)", "SENIOR+LEAD (% renseignées)", "SALAIRE_MEDIAN", "TELETRAVAIL mentionné (%)", "MENTION_IA (%)", "STOCK INDEED 'Développeur web' (dernier compte)", "STOCK INDEED 'Développeur' (dernier compte)", "SOURCES"]
    comp = []
    for z in NEXA_CITIES:
        rz = [r for r in U if r["ZONE_NEXA"] == z]
        cnt = Counter(r["METIER_NORMALISE"] for r in rz).most_common(3)
        contrats, _ = contract_counts(rz)
        kc = sum(contrats.values())
        sen, _ = seniority_counts(rz)
        ks = sum(sen.values())
        sal = annual_salaries(rz)
        tel_y, tel_k, tel_s = teletravail_share(rz)

        def last_stock(pats):
            best = None
            for (src, intit, zone, contrat), pts in series.items():
                if src != "Indeed" or contrat not in ("nc", "tous", ""):
                    continue
                if not any(re.fullmatch(p, intit) for p in pats) or not any(re.fullmatch(zz, zone) for zz in ZONE_SERIES[z]):
                    continue
                for date, n, url, preuve, nb in pts:
                    if best is None or date > best[0]:
                        best = (date, nb, zone)
            return f"{best[1]} ({best[0]}, {best[2]})" if best else NC
        comp.append([z, len(rz), pct(len(rz), len(U))] + [f"{m} ({n})" for m, n in cnt] + [NC] * (3 - len(cnt)) +
                    [pct(contrats["CDI"], kc) if kc else NC, pct(contrats["ALTERNANCE"] + contrats["STAGE"], kc) if kc else NC, pct(contrats["FREELANCE"], kc) if kc else NC,
                     pct(sen["DEBUTANT"] + sen["JUNIOR"], ks) if ks else NC, pct(sen["SENIOR"] + sen["LEAD_OU_ARCHITECTE"], ks) if ks else NC,
                     (f"{median_or_nc(sal)} € (n={len(sal)})" if sal else NC), (tel_s if tel_k else NC), ia_share(rz)[1],
                     last_stock([r"developpeur web"]), last_stock([r"developpeur"]), sources_count(rz)])
    write_table(ws, r0 + 1, hdr, comp, "T_COMPARATIF_VILLES")
    return data, comp


# ---------------------------------------------------------------------------
COMP_HEADERS = ["FAMILLE_COMPETENCE", "COMPETENCE", "NOMBRE_OFFRES", "PART_DES_OFFRES (%)", "METIERS", "REGIONS", "VILLES", "SENIORITE", "EVOLUTION", "OBLIGATOIRE_OU_OPTIONNELLE", "ASSOCIATIONS", "LIEN_AVEC_IA", "MATURITE", "PERTINENCE_NEXA"]

IA_LINK = {"IA_GENERATIVE": "DIRECT", "OUTILS_DE_CODAGE_IA": "DIRECT", "LOW_CODE_NO_CODE": "DIRECT", "TEST_ET_QUALITE": "INDIRECT (contrôle des sorties IA)", "CYBERSECURITE": "INDIRECT (sécurisation du code généré)", "ARCHITECTURE": "INDIRECT (conception, découpage)", "DEVOPS_ET_CI_CD": "INDIRECT (déploiement, industrialisation)", "CONTENEURS": "INDIRECT (déploiement)", "CLOUD": "INDIRECT (déploiement)", "API_ET_MICROSERVICES": "INDIRECT (intégration d'API de modèles)", "PRODUIT_ET_BUSINESS": "INDIRECT (compréhension métier)", "DATA": "INDIRECT (données pour l'IA)"}


FONDAMENTALES = {"JavaScript", "TypeScript", "HTML/CSS", "SQL", "React", "Node.js", "PHP", "Symfony", "Java", "Spring", "Python", "PostgreSQL", "MySQL/MariaDB", "API REST", "Git", "Docker", "CI/CD", "Agile/Scrum", "Tests unitaires", "GitLab", "GitHub", "Anglais"}
FAM_ETABLIES = {"LANGAGES", "FRONT_END", "BACK_END", "FULL_STACK", "BASES_DE_DONNEES", "API_ET_MICROSERVICES", "CLOUD", "DEVOPS_ET_CI_CD", "CONTENEURS", "GESTION_DE_PROJET", "ANGLAIS", "MOBILE", "CMS_ECOMMERCE", "SOFT_SKILLS", "PRODUIT_ET_BUSINESS", "DATA", "UX_UI", "ARCHITECTURE", "PERFORMANCE"}


def maturite(n, total, fam):
    p = 100.0 * n / total
    if fam in ("IA_GENERATIVE", "OUTILS_DE_CODAGE_IA", "LOW_CODE_NO_CODE"):
        if p >= 10:
            return "DEJA_DEMANDEE"
        if p >= 2:
            return "EMERGENTE"
        if n >= 2:
            return "RARE_MAIS_STRATEGIQUE"
        return "NON_CONFIRMEE"
    if fam in ("TEST_ET_QUALITE", "CYBERSECURITE", "ACCESSIBILITE"):
        if p >= 10:
            return "DEJA_DEMANDEE"
        if p >= 3:
            return "EMERGENTE"
        return "RARE_MAIS_STRATEGIQUE" if n >= 1 else "NON_CONFIRMEE"
    # familles établies
    if p >= 3:
        return "DEJA_DEMANDEE"
    if n >= 2:
        return "DEJA_DEMANDEE (faible fréquence dans l'échantillon)"
    return "NON_CONFIRMEE"


def pertinence(fam, comp, n, total):
    p = 100.0 * n / total
    if comp in FONDAMENTALES or fam == "FULL_STACK":
        return "FONDAMENTALE (socle Bachelor obligatoire)"
    if fam in ("TEST_ET_QUALITE", "DEVOPS_ET_CI_CD", "CONTENEURS", "CLOUD", "CYBERSECURITE", "ARCHITECTURE", "PERFORMANCE", "ACCESSIBILITE"):
        return "A_RENFORCER (Bachelor 3e année + Mastère)"
    if fam in ("IA_GENERATIVE", "OUTILS_DE_CODAGE_IA"):
        return "TRANSVERSALE_IA (à intégrer dans tous les modules, spécialisation en Mastère)"
    if fam in ("GESTION_DE_PROJET", "SOFT_SKILLS", "ANGLAIS", "PRODUIT_ET_BUSINESS", "UX_UI"):
        return "TRANSVERSALE (projets, alternance)"
    if p >= 2:
        return "OPTIONNELLE (module ou spécialisation)"
    return "VEILLE"


def build_competences(wb, rows, U, series):
    ws = wb.create_sheet("COMPETENCES_ET_IA")
    title(ws, 1, "COMPÉTENCES ET IA — fréquence dans les offres uniques (extraits publics) et lecture pour NEXA")
    note(ws, 2, "NOMBRE_OFFRES = offres uniques dont le titre ou l'extrait cite la compétence (sous-estimation : les extraits ne reprennent pas toute l'annonce). OBLIGATOIRE_OU_OPTIONNELLE = OBLIGATOIRE si la compétence figure dans le titre de l'offre pour ≥ 50 % des mentions, sinon OPTIONNELLE/CONTEXTE. EVOLUTION = stock Indeed France daté quand disponible, sinon NC. MATURITE et PERTINENCE_NEXA = lecture analytique (ESTIMATION).")
    total = len(U)
    data = []
    fam_counts = defaultdict(lambda: defaultdict(list))
    for r in U:
        for fam, items in r.get("_skills", {}).items():
            for it in items:
                fam_counts[fam][it].append(r)
    for fam in SKILLS:
        for comp, rs in sorted(fam_counts.get(fam, {}).items(), key=lambda kv: -len(kv[1])):
            n = len(rs)
            rx = next((x for nm, x in SKILLS[fam] if nm == comp), None)
            in_title = sum(1 for r in rs if rx and re.search(rx, norm(r["INTITULE_BRUT"])))
            oblig = "OBLIGATOIRE (dans le titre)" if in_title >= max(1, n / 2) else "OPTIONNELLE / CONTEXTE"
            mets = Counter(r["METIER_NORMALISE"] for r in rs).most_common(4)
            regs = Counter(r["REGION_NORMALISEE"] for r in rs).most_common(4)
            villes = Counter(r["ZONE_NEXA"] for r in rs if r["ZONE_NEXA"] not in ("Hors villes NEXA",)).most_common(4)
            sen = Counter(r["SENIORITE"] for r in rs if r["SENIORITE"] != NC).most_common(3)
            assoc = Counter()
            for r in rs:
                for f2, its in r.get("_skills", {}).items():
                    for it in its:
                        if it != comp and f2 not in ("SOFT_SKILLS", "PRODUIT_ET_BUSINESS", "FULL_STACK"):
                            assoc[it] += 1
            e25, e24, det = NC, NC, ""
            if comp in ("React", "Angular", "Vue.js", "PHP", "Symfony", "Java", "Python", "Node.js", ".NET", "Laravel", "Spring", "TypeScript", "JavaScript", "WordPress", "Shopify", "PrestaShop", "Docker", "Kubernetes", "AWS", "Azure", "DevOps", "GitHub Copilot", "Claude Code", "RAG", "IA générative / LLM"):
                e25, e24, det = evol_pct(series, [r"developpeur " + re.escape(norm(comp).replace(" / llm", "")), norm(comp), r"developpeur " + re.escape(norm(comp)) + r".*"], [r"france.*", r"nc", r""])
            data.append([fam, comp, n, pct(n, total), " ; ".join(f"{m} ({c})" for m, c in mets), " ; ".join(f"{m} ({c})" for m, c in regs), " ; ".join(f"{m} ({c})" for m, c in villes),
                         " ; ".join(f"{m} ({c})" for m, c in sen) or NC, (fmt_evol(e25) if e25 != NC else (fmt_evol(e24) + " vs 2024" if e24 != NC else NC)), oblig,
                         " ; ".join(f"{a} ({c})" for a, c in assoc.most_common(5)) or NC, IA_LINK.get(fam, "AUCUN"), maturite(n, total, fam), pertinence(fam, comp, n, total)])
    end = write_table(ws, 4, COMP_HEADERS, data, "T_COMPETENCES", widths=[22, 30, 10, 10, 50, 40, 40, 30, 24, 22, 50, 30, 22, 40])
    ws.freeze_panes = "C5"

    # ---- bloc développeur augmenté ----
    r0 = end + 3
    title(ws, r0, "COMPETENCES_DU_DEVELOPPEUR_AUGMENTE_PAR_IA (ce qui est observé dans les offres françaises collectées vs ce qui reste non confirmé)", SUB_FONT)
    ia_rows = [r for r in U if r["MENTION_IA_EXPLICITE"] == "Oui"]
    web_ia = [r for r in ia_rows if r["FAMILLE_METIER"] in (COEUR, EVOL)]
    tools = Counter()
    for r in U:
        for it in r.get("_skills", {}).get("OUTILS_DE_CODAGE_IA", []):
            tools[it] += 1
    gen = Counter()
    for r in U:
        for it in r.get("_skills", {}).get("IA_GENERATIVE", []):
            gen[it] += 1
    bloc = [
        ["Offres uniques avec mention IA explicite (toutes familles)", len(ia_rows), f"{pct(len(ia_rows), total)} %", "OBSERVE", "Titre ou extrait citant IA générative, LLM, RAG, agents, outil de codage IA"],
        ["... dont métiers émergents IA (AI Engineer, LLM, RAG, agents)", sum(1 for r in ia_rows if r["FAMILLE_METIER"] == IA), f"{pct(sum(1 for r in ia_rows if r['FAMILLE_METIER'] == IA), total)} %", "OBSERVE", "Recherchés spécifiquement : surreprésentés dans l'échantillon"],
        ["... dont offres de développeur web / full stack / logiciel 'classique' citant l'IA", len(web_ia), f"{pct(len(web_ia), len([r for r in U if r['FAMILLE_METIER'] in (COEUR, EVOL)]))} % des offres cœur+évolution", "OBSERVE", "Signal du 'développeur augmenté' : " + (" ; ".join(f"{r['ENTREPRISE'] if not is_nc(r['ENTREPRISE']) else r['SOURCE']} - {r['INTITULE_BRUT'][:60]}" for r in web_ia[:8]) or "aucune")],
        ["Outils de codage IA cités", sum(tools.values()), " ; ".join(f"{k} ({v})" for k, v in tools.most_common()) or "0", "OBSERVE", "GitHub Copilot, Cursor, Claude Code, ChatGPT, Codex"],
        ["Briques IA générative citées", sum(gen.values()), " ; ".join(f"{k} ({v})" for k, v in gen.most_common()) or "0", "OBSERVE", "LLM, RAG, agents, MCP, prompt"],
        ["Repère externe : part des annonces de développement logiciel mentionnant l'IA (Indeed France)", "21 %", "Indeed Hiring Lab France, 01/04/2026", "ETUDE", "https://www.hiringlab.org/fr/blog/2026/04/01/avril-2026-lia-progresse-dans-un-marche-du-travail-en-recul/"],
        ["Repère externe : usage des outils IA par les développeurs (international)", "84 % utilisent ou prévoient ; 51 % quotidiennement ; 46 % se méfient de l'exactitude", "Stack Overflow Developer Survey 2025", "ETUDE (INTERNATIONAL)", "https://survey.stackoverflow.co/2025/ai"],
        ["Repère externe : ESN et jeunes diplômés", "33 % des ESN ont réduit leurs recrutements de jeunes diplômés au S1 2026 ; l'IA se substitue à des tâches de débutants", "Numeum S1 2026 / Blog du Modérateur", "ETUDE", "https://www.blogdumoderateur.com/emploi-numerique-loin-job-apocalypse-promet/"],
    ]
    write_table(ws, r0 + 1, ["ELEMENT", "NOMBRE", "VALEUR / DETAIL", "STATUT", "COMMENTAIRE / SOURCE"], bloc, "T_DEV_AUGMENTE")
    r1 = r0 + 3 + len(bloc)
    title(ws, r1, "RÉFÉRENTIEL CIBLE 'DÉVELOPPEUR AUGMENTÉ PAR L'IA' (proposition NEXA fondée sur les fréquences ci-dessus ; statut par compétence)", SUB_FONT)
    ref = [
        ["Socle", "Langage principal maîtrisé (JavaScript/TypeScript ou PHP ou Java ou Python) + HTML/CSS + SQL", "DEJA_DEMANDEE", "Obligatoire Bachelor"],
        ["Socle", "Framework front (React en priorité, Angular ou Vue) et framework back (Node/Nest, Symfony/Laravel, Spring, .NET ou Django)", "DEJA_DEMANDEE", "Obligatoire Bachelor"],
        ["Socle", "API REST, bases de données relationnelles (PostgreSQL/MySQL), Git", "DEJA_DEMANDEE", "Obligatoire Bachelor"],
        ["Industrialisation", "Tests unitaires et automatisés, CI/CD, Docker, déploiement cloud (AWS/Azure/GCP)", "DEJA_DEMANDEE / EMERGENTE", "Obligatoire Bachelor 3e année, approfondi en Mastère"],
        ["Industrialisation", "Sécurité applicative (OWASP, authentification), observabilité, performance", "EMERGENTE / RARE_MAIS_STRATEGIQUE", "Bachelor 3e année + Mastère"],
        ["IA appliquée", "Utilisation raisonnée d'assistants de code (Copilot, Cursor, Claude Code) avec revue, tests et contrôle des sorties", "EMERGENTE", "Transversal dès la 1re année, évalué"],
        ["IA appliquée", "Intégration d'API de modèles (OpenAI, Mistral, Anthropic), RAG, agents, MCP, évaluation et sécurité des applications LLM", "EMERGENTE / RARE_MAIS_STRATEGIQUE", "Spécialisation Mastère (M1/M2)"],
        ["Conception", "Architecture (hexagonale, microservices, clean code), modélisation, compréhension produit et métier", "DEJA_DEMANDEE (seniors)", "Mastère"],
        ["Posture", "Anglais technique, communication, autonomie, travail en équipe agile", "DEJA_DEMANDEE", "Transversal"],
        ["Non confirmé", "Prompt engineering comme métier autonome ; low-code/no-code comme débouché principal", "NON_CONFIRMEE", "Veille, pas de parcours dédié"],
    ]
    write_table(ws, r1 + 1, ["BLOC", "COMPETENCE", "STATUT_MARCHE", "PLACE_DANS_LE_CURSUS_NEXA"], ref, "T_REFERENTIEL_AUGMENTE")

    # ---- études externes compétences / IA ----
    r2 = r1 + 3 + len(ref)
    title(ws, r2, "DONNÉES EXTERNES COMPÉTENCES ET IA (études collectées, avec URL)", SUB_FONT)
    ext = []
    for p in ["competences.jsonl", "ia_transformation.jsonl"]:
        fp = os.path.join(ETUDES_DIR, p)
        if os.path.exists(fp):
            for line in open(fp, encoding="utf-8"):
                line = line.strip()
                if line:
                    try:
                        e = json.loads(line)
                        ext.append([p.replace(".jsonl", ""), e.get("COMPETENCE") or e.get("THEME"), e.get("FAMILLE") or "", e.get("INDICATEUR") or e.get("RESULTAT"), e.get("VALEUR") or e.get("CHIFFRE"), e.get("PERIMETRE"), e.get("SOURCE"), e.get("DATE"), e.get("URL"), e.get("CITATION"), str(e.get("FIABILITE", "")).upper()])
                    except json.JSONDecodeError:
                        pass
    for p in ["C_competences.jsonl", "C_ia.jsonl"]:
        fp = os.path.join(COLLECTE_DIR, p)
        if os.path.exists(fp):
            for line in open(fp, encoding="utf-8"):
                line = line.strip()
                if line:
                    try:
                        e = json.loads(line)
                        ext.append([p.replace(".jsonl", ""), e.get("COMPETENCE") or e.get("THEME"), e.get("FAMILLE") or "", e.get("INDICATEUR") or e.get("RESULTAT"), e.get("VALEUR") or e.get("CHIFFRE"), e.get("PERIMETRE"), e.get("SOURCE"), e.get("DATE"), e.get("URL"), e.get("CITATION"), str(e.get("FIABILITE", "")).upper()])
                    except json.JSONDecodeError:
                        pass
    for e in load_d_etudes():
        if norm(e.get("THEME")) in ("competences", "ia_transformation", "international", "salaires"):
            ext.append(["D_" + str(e.get("THEME")), e.get("TITRE"), "", e.get("METHODE"), e.get("RESULTAT_UTILISE"), e.get("PERIMETRE"), e.get("ORGANISME_OU_MEDIA"), e.get("DATE_PUBLICATION"), e.get("URL"), e.get("RESULTAT_UTILISE"), str(e.get("FIABILITE", "")).upper()])
    write_table(ws, r2 + 1, ["VOLET", "COMPETENCE_OU_THEME", "FAMILLE", "INDICATEUR / RESULTAT", "VALEUR", "PERIMETRE", "SOURCE", "DATE", "URL", "CITATION", "FIABILITE"], ext, "T_EXTERNES_COMPETENCES")
    return data


# ---------------------------------------------------------------------------
DETAIL_COLS = ["ID_OFFRE", "STATUT_DOUBLON", "DOUBLON_DE", "STATUT_DONNEE", "SOURCE", "URL", "DATE_PUBLICATION", "DATE_COLLECTE", "ENTREPRISE", "CABINET_OU_INTERMEDIAIRE", "INTITULE_BRUT", "METIER_NORMALISE", "FAMILLE_METIER", "TECHNOS_DANS_TITRE",
               "REGION_NORMALISEE", "DEPARTEMENT_NORMALISE", "VILLE_NORMALISEE", "ZONE_NEXA", "REGION", "DEPARTEMENT", "VILLE", "TELETRAVAIL", "TELETRAVAIL_NORMALISE", "TYPE_CONTRAT", "TYPE_CONTRAT_NORMALISE", "DUREE", "TEMPS_PLEIN_OU_PARTIEL",
               "SALAIRE_MINIMUM", "SALAIRE_MAXIMUM", "SALAIRE_MIN_NUM", "SALAIRE_MAX_NUM", "SALAIRE_UNITE", "EXPERIENCE", "SENIORITE", "SENIORITE_ORIGINE", "SENIORITE_INDICATIVE_TITRE", "DIPLOME",
               "LANGAGES", "FRAMEWORKS", "BASES_DE_DONNEES", "CLOUD", "DEVOPS", "TEST", "CYBERSECURITE", "ARCHITECTURE", "METHODES_PROJET", "COMPETENCES_IA", "SOFT_SKILLS", "ANGLAIS", "SECTEUR_ENTREPRISE", "DESCRIPTION_SYNTHETIQUE",
               "MENTION_IA_EXPLICITE", "OUTIL_CODAGE_IA_CITE"] + ["COMP_" + f for f in SKILLS] + ["PREUVE", "REQUETE"]


def build_detail(wb, rows):
    ws = wb.create_sheet("OFFRES_DETAILLEES")
    title(ws, 1, "OFFRES DÉTAILLÉES — une ligne par offre collectée (toutes plateformes), champs bruts + champs normalisés")
    note(ws, 2, "STATUT_DONNEE = OBSERVE pour tous les champs bruts (extraits publics indexés) ; les colonnes *_NORMALISE(E), SENIORITE, ZONE_NEXA, COMP_* sont dérivées par règles documentées (normalize.py) à partir des champs observés. STATUT_DOUBLON : OFFRE_UNIQUE / DUPLICATION_MULTI_PLATEFORME / REPUBLICATION / OFFRE_PROBABLEMENT_IDENTIQUE. NC = non renseigné dans l'extrait.")
    data = []
    for r in sorted(rows, key=lambda x: (x["FAMILLE_METIER"], x["METIER_NORMALISE"], x["ID_OFFRE"])):
        data.append([r.get(c, NC) if r.get(c) not in (None, "") else NC for c in DETAIL_COLS])
    write_table(ws, 4, DETAIL_COLS, data, "T_OFFRES", widths=[10, 22, 10, 10, 16, 40, 12, 11, 24, 16, 45, 34, 20, 18, 22, 8, 18, 22, 18, 8, 16, 14, 14, 14, 14, 10, 10, 12, 12, 10, 10, 9, 20, 16, 22, 14, 14] + [18] * 14 + [10, 14] + [18] * len(SKILLS) + [60, 40])
    ws.freeze_panes = "L5"


def main():
    rows, vols = load()
    U = uniques(rows)
    series = volume_series(vols)
    wb = Workbook()
    build_synthese(wb, rows, U, series, vols)
    build_regions(wb, rows, U, series)
    build_villes(wb, rows, U, series)
    build_competences(wb, rows, U, series)
    build_detail(wb, rows)
    out = os.path.join(OUTDIR, "NEXA_Marche_Emploi_Developpement_Web_France_2026.xlsx")
    wb.save(out)
    print("Excel écrit :", out, "| offres brutes", len(rows), "| uniques périmètre", len(U), "| séries de stocks", len(series))


if __name__ == "__main__":
    main()
