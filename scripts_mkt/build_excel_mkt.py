#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Livrable 1 — NEXA_Marche_Emploi_Marketing_Digital_France_2026.xlsx (5 onglets)."""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize_mkt as N
from analyse_mkt import FAMILLE_INDIC, HYPOTHESES, SCENARIOS, CRITERES, OPTIONS, scores
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from openpyxl.chart import BarChart, PieChart, Reference

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = os.path.join(ROOT, "collecte_mkt")
D = json.load(open(os.path.join(BASE, "mkt_consolide.json"), encoding="utf-8"))
OFFRES = json.load(open(os.path.join(BASE, "mkt_offres_normalisees.json"), encoding="utf-8"))
VOLUMES = [json.loads(l) for l in open(os.path.join(BASE, "mkt_volumes.jsonl"), encoding="utf-8") if l.strip()]
ETUDES = [json.loads(l) for l in open(os.path.join(BASE, "mkt_etudes.jsonl"), encoding="utf-8") if l.strip()]

NAVY = "1F3864"; BLUE = "2E75B6"; LIGHT = "DEEAF6"; GREY = "F2F2F2"; AMBER = "FFF2CC"; GREEN = "E2EFDA"; RED = "FCE4EC"
H = Font(bold=True, color="FFFFFF", size=10)
HF = PatternFill("solid", fgColor=NAVY)
TITLE = Font(bold=True, size=13, color=NAVY)
SUB = Font(bold=True, size=11, color=BLUE)
SMALL = Font(size=8, italic=True, color="666666")
THIN = Border(*[Side(style="thin", color="BFBFBF")] * 4)

def head(ws, row, cols, widths=None):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.font = H; cell.fill = HF
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[row].height = 42
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[get_column_letter(i)].width = w

def table(ws, ref, name):
    t = Table(displayName=name, ref=ref)
    t.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True)
    ws.add_table(t)

def title(ws, row, txt, font=TITLE):
    c = ws.cell(row=row, column=1, value=txt); c.font = font
    return row + 1

def pct(v): return f"{v} %" if v is not None else "NC"
def nc(v): return v if v not in (None, "", "NC") else "NC"

wb = Workbook()

# ================================================================ ONGLET 1
ws = wb.active; ws.title = "SYNTHESE_METIERS"
r = title(ws, 1, "NEXA DIGITAL SCHOOL — MARCHÉ DE L'EMPLOI DU MARKETING DIGITAL EN FRANCE — SYNTHÈSE PAR MÉTIER")
ws.cell(row=2, column=1, value=f"Collecte du 2026-09-07 · {D['meta']['volume_brut']} lignes collectées · {D['meta']['offres_uniques']} offres uniques · {D['meta']['offres_dans_perimetre']} dans le périmètre marketing digital · {D['meta']['nb_volumes']} stocks d'offres datés · {D['meta']['nb_etudes']} sources documentaires").font = SMALL
ws.cell(row=3, column=1, value="Convention : 0 = absence réellement constatée · NC = donnée indisponible dans les extraits indexés · ESTIMATION = valeur reconstituée à partir de sources identifiées. Les parts de contrat et de séniorité sont calculées sur les offres où l'information est présente ET sur le total (colonnes NC).").font = SMALL

COLS = ["FAMILLE_METIER","METIER_NORMALISE","INTITULES_ASSOCIES","VOLUME_BRUT","OFFRES_UNIQUES","PART_DU_MARCHE",
        "EVOLUTION_2025","EVOLUTION_2024","CDI","CDD","ALTERNANCE","STAGE","FREELANCE","NC_CONTRAT",
        "DEBUTANT","JUNIOR","INTERMEDIAIRE","SENIOR","MANAGER_HEAD","NC_SENIORITE","EXPERIENCE_MEDIANE",
        "NIVEAU_ETUDE_DOMINANT","SALAIRE_MEDIAN","TELETRAVAIL","NIVEAU_TECHNICITE","COMPETENCES_DOMINANTES",
        "OUTILS_DOMINANTS","COMPETENCES_IA","EXPOSITION_AUTOMATISATION","TENSION","QUALITE_DU_DEBOUCHE",
        "NOMBRE_SOURCES","CONFIANCE"]
W = [24,34,52,11,13,13,26,26,7,7,11,8,10,12,10,8,14,8,13,13,18,22,14,13,16,42,34,26,26,20,22,12,11]
hr = 5; head(ws, hr, COLS, W)

EXPO = {1: "FORTE", 2: "MOYENNE", 3: "FAIBLE", 4: "FAIBLE"}
NIV_ETUDE = {"MARTECH_MARKETING_OPS":"Bac+5","DATA_ANALYTICS_CRO":"Bac+5","PRODUCT_MARKETING":"Bac+5",
             "CRM_LIFECYCLE":"Bac+4/5","ACQUISITION_PERFORMANCE":"Bac+4/5","SEO_SEA":"Bac+3/5",
             "ECOMMERCE":"Bac+3/5","METIER_IA_EMERGENT":"Bac+5","CONTENT_BRAND":"Bac+3/5",
             "COEUR_GENERALISTE":"Bac+3","SOCIAL_MEDIA":"Bac+2/3","METIER_ADJACENT":"Bac+3/5"}
EVOL_NOTE = ("NC — séries historiques comparables non reconstituables par métier (pages de liste indexées à des dates "
             "hétérogènes et libellés de requête différents). Voir le bloc STOCKS D'OFFRES DATÉS en bas de cet onglet "
             "et la section Évolution du document Word.")

row = hr + 1
for m, b in sorted(D["par_metier"].items(), key=lambda x: -x[1]["n"]):
    fam = b["famille"]; ind = FAMILLE_INDIC.get(fam, ("DONNEES_INSUFFISANTES","DONNEES_INSUFFISANTES","NC","NC",""))
    outils = [c for c, _ in b["competences_top"] if any(k in c for k in
              ("Google","Meta","HubSpot","Salesforce","Braze","Klaviyo","GA4","GTM","Looker","SQL","BigQuery","Power","Shopify","Brevo","Adobe","Amplitude","AB Tasty","Zapier"))]
    comps = [c for c, _ in b["competences_top"][:6]]
    ia = [c for c in [x for x, _ in b["competences_top"]] if "IA" in c or "GEO" in c or "no-code" in c.lower()]
    vals = [fam, m, " | ".join(b["intitules"][:5]), b["n"], b["n"], b["part_marche"],
            EVOL_NOTE, EVOL_NOTE,
            b["contrats"].get("CDI",0), b["contrats"].get("CDD",0), b["contrats"].get("ALTERNANCE",0),
            b["contrats"].get("STAGE",0), b["contrats"].get("FREELANCE",0), b["contrats"].get("NC",0),
            b["seniorite"].get("DEBUTANT",0), b["seniorite"].get("JUNIOR",0), b["seniorite"].get("INTERMEDIAIRE",0),
            b["seniorite"].get("SENIOR",0), b["seniorite"].get("MANAGER_HEAD_DIRECTOR",0), b["seniorite"].get("NC",0),
            "NC (expérience non renseignée dans la majorité des extraits)",
            NIV_ETUDE.get(fam,"NC"),
            b["salaire_median"] if b["salaire_median"] else "NC",
            b["teletravail"].get("Oui",0) + b["teletravail"].get("Partiel",0),
            b["technicite_moy"], " | ".join(comps) if comps else "NC",
            " | ".join(outils[:6]) if outils else "0",
            " | ".join(ia) if ia else "0",
            EXPO.get(round(b["technicite_moy"]), "NC"), ind[0], ind[1], b["sources"],
            "FORTE" if b["n"] >= 20 else "MOYENNE" if b["n"] >= 8 else "FAIBLE"]
    for i, v in enumerate(vals, 1):
        c = ws.cell(row=row, column=i, value=v); c.border = THIN
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if i in (30, 31):
            c.fill = PatternFill("solid", fgColor=GREEN if v in ("EN_TENSION","TRES_FAVORABLE","FAVORABLE")
                                 else RED if v in ("SATURE","FRAGILE","DEFAVORABLE","RALENTISSEMENT") else AMBER)
    row += 1
table(ws, f"A{hr}:{get_column_letter(len(COLS))}{row-1}", "T_METIERS")
last_metier = row - 1

# --- mini-vue nationale + graphiques
row += 2
row = title(ws, row, "MINI-VUE NATIONALE", SUB)
nat = D["national"]
vue = [
 ("Offres collectées (lignes brutes)", D["meta"]["volume_brut"]),
 ("Offres uniques après dédoublonnage", D["meta"]["offres_uniques"]),
 ("Taux de doublons", f"{D['meta']['taux_doublons']} %"),
 ("Offres dans le périmètre marketing digital", D["meta"]["offres_dans_perimetre"]),
 ("Dont cœur marketing digital (hors métiers adjacents)", D["meta"]["offres_coeur_marketing_digital"]),
 ("Offres exclues du périmètre (faux positifs)", D["meta"]["offres_exclues"]),
 ("Part CDI (sur total, y compris NC)", f"{nat['contrats_pct'].get('CDI',0)} %"),
 ("Part ALTERNANCE (sur total, y compris NC)", f"{nat['contrats_pct'].get('ALTERNANCE',0)} %"),
 ("Part STAGE", f"{nat['contrats_pct'].get('STAGE',0)} %"),
 ("Part contrat non renseigné (NC)", f"{nat['contrats_pct'].get('NC',0)} %"),
 ("Part débutants + juniors (sur total)", f"{nat['debutant_junior_pct']} %"),
 ("Part séniorité non renseignée (NC)", f"{nat['seniorite_pct'].get('NC',0)} %"),
 ("Niveau de technicité moyen (échelle 1-4)", nat["technicite_moy"]),
 ("Offres de technicité 1 (exécution)", nat["technicite"].get("1",nat["technicite"].get(1,0))),
 ("Offres de technicité 2 (expertise canal)", nat["technicite"].get("2",nat["technicite"].get(2,0))),
 ("Offres de technicité 3 (performance/data/automation)", nat["technicite"].get("3",nat["technicite"].get(3,0))),
 ("Offres de technicité 4 (MarTech/systèmes)", nat["technicite"].get("4",nat["technicite"].get(4,0))),
 ("Part des offres mentionnant explicitement l'IA", f"{nat['ia_pct']} %"),
 ("Salaire annuel brut médian (offres renseignées)", f"{nat['salaire_median']} € (n={nat['salaire_n']})"),
 ("Salaire Q1 / Q3", f"{nat['salaire_q1']} € / {nat['salaire_q3']} €"),
]
for k, v in vue:
    ws.cell(row=row, column=1, value=k).font = Font(bold=True, size=9)
    ws.cell(row=row, column=2, value=v); row += 1

# zone graphiques (données sources)
gs = row + 2
ws.cell(row=gs, column=1, value="Données des graphiques").font = SUB
gs += 1
ws.cell(row=gs, column=1, value="Famille"); ws.cell(row=gs, column=2, value="Offres uniques")
ws.cell(row=gs, column=3, value="Alternance %"); ws.cell(row=gs, column=4, value="Débutants+juniors %")
ws.cell(row=gs, column=5, value="Technicité moyenne"); ws.cell(row=gs, column=6, value="Qualité du débouché")
fams = sorted(D["par_famille"].items(), key=lambda x: -x[1]["n"])
for i, (f, b) in enumerate(fams, 1):
    ws.cell(row=gs+i, column=1, value=f); ws.cell(row=gs+i, column=2, value=b["n"])
    ws.cell(row=gs+i, column=3, value=b["alternance_pct"]); ws.cell(row=gs+i, column=4, value=b["debutant_junior_pct"])
    ws.cell(row=gs+i, column=5, value=b["technicite_moy"])
    ws.cell(row=gs+i, column=6, value=FAMILLE_INDIC.get(f, ("","NC"))[1])
ge = gs + len(fams)

ch = BarChart(); ch.title = "Offres uniques par famille de métiers"; ch.height = 9; ch.width = 20
ch.add_data(Reference(ws, min_col=2, min_row=gs, max_row=ge), titles_from_data=True)
ch.set_categories(Reference(ws, min_col=1, min_row=gs+1, max_row=ge))
ws.add_chart(ch, f"H{gs}")
ch2 = BarChart(); ch2.title = "Alternance et accès débutants/juniors par famille (%)"; ch2.height = 9; ch2.width = 20
ch2.add_data(Reference(ws, min_col=3, max_col=4, min_row=gs, max_row=ge), titles_from_data=True)
ch2.set_categories(Reference(ws, min_col=1, min_row=gs+1, max_row=ge))
ws.add_chart(ch2, f"H{gs+19}")
ch3 = BarChart(); ch3.title = "Niveau de technicité moyen par famille (1-4)"; ch3.height = 9; ch3.width = 20
ch3.add_data(Reference(ws, min_col=5, min_row=gs, max_row=ge), titles_from_data=True)
ch3.set_categories(Reference(ws, min_col=1, min_row=gs+1, max_row=ge))
ws.add_chart(ch3, f"H{gs+38}")

gp = ge + 3
ws.cell(row=gp, column=1, value="Contrat"); ws.cell(row=gp, column=2, value="Offres")
for i, (k, v) in enumerate(sorted(nat["contrats"].items(), key=lambda x: -x[1]), 1):
    ws.cell(row=gp+i, column=1, value=k); ws.cell(row=gp+i, column=2, value=v)
pc = PieChart(); pc.title = "Répartition des contrats (périmètre marketing digital)"; pc.height = 9; pc.width = 14
pc.add_data(Reference(ws, min_col=2, min_row=gp, max_row=gp+len(nat["contrats"])), titles_from_data=True)
pc.set_categories(Reference(ws, min_col=1, min_row=gp+1, max_row=gp+len(nat["contrats"])))
ws.add_chart(pc, f"H{gs+57}")

gq = gp + len(nat["contrats"]) + 3
ws.cell(row=gq, column=1, value="Séniorité"); ws.cell(row=gq, column=2, value="Offres")
for i, (k, v) in enumerate(sorted(nat["seniorite"].items(), key=lambda x: -x[1]), 1):
    ws.cell(row=gq+i, column=1, value=k); ws.cell(row=gq+i, column=2, value=v)
pc2 = PieChart(); pc2.title = "Répartition par séniorité"; pc2.height = 9; pc2.width = 14
pc2.add_data(Reference(ws, min_col=2, min_row=gq, max_row=gq+len(nat["seniorite"])), titles_from_data=True)
pc2.set_categories(Reference(ws, min_col=1, min_row=gq+1, max_row=gq+len(nat["seniorite"])))
ws.add_chart(pc2, f"P{gs+57}")

# métiers en progression / en recul (qualitatif documenté)
gr = gq + len(nat["seniorite"]) + 3
gr = title(ws, gr, "MÉTIERS EN PROGRESSION ET EN RECUL — lecture qualitative documentée (les séries de flux annuelles ne sont pas reconstituables)", SUB)
head(ws, gr, ["SENS", "MÉTIER / SEGMENT", "SIGNAUX CONVERGENTS"], [18, 44, 120]); gr += 1
PROG = [
 ("PROGRESSION","Growth / Acquisition / Performance","1re famille spécialisée (85 offres) ; stocks Indeed Growth Marketing France 1 842 (08/2026) et IDF 1 295 (09/2026) ; marché publicitaire digital +11 % en 2025 et +12 % au S1 2026 (SRI/UDECAM/Oliver Wyman) ; salaires senior 80-90 k€."),
 ("PROGRESSION","CRM / Lifecycle / Marketing Automation","Stocks Indeed CRM Manager France 2 000+ (09/2026), Marketing Automation 759 (05/2026) ; CRM = 2e compétence la plus citée du périmètre (11,5 %) ; technicité 2,50 ; faible exposition à l'automatisation."),
 ("PROGRESSION","Data marketing / Analytics / Tracking","Technicité 2,45 ; SQL, BigQuery, GA4, GTM, Looker Studio explicitement exigés ; intitulés hybrides observés (Senior Data Analyst SEO chez Havas, Lead Marketing Data Analyst chez Doctolib)."),
 ("PROGRESSION","E-commerce","Marché à 196,4 Md€ en 2025 (+7 %) et 234 000 emplois (+9 %) — Fevad 2026."),
 ("PROGRESSION","GEO / AEO / AI Search (émergent)","7 offres citant GEO/AEO/AI Search ; intitulés réels : Consultant SEO/GEO, SEO SEA GEO AI Visibility Manager E-commerce, Community Manager spécialiste Agents IA & GEO/SEO. Volume encore très faible."),
 ("STABLE","SEO / SEA","51 offres ; stocks élevés (SEO Manager France 318, HelloWork SEO 1 521) ; salaires en hausse (+3 à +4 %/an) mais transformation du Search par l'IA générative."),
 ("RECUL / SATURATION","Social Media / Community Management","Technicité 1,03 (la plus faible) ; 317 offres de community manager sur France Travail en 2026 pour un vivier de candidats très large ; saturation documentée ; 52 % des annonceurs prévoient de réduire leur budget média 2026."),
 ("RECUL / FRAGILISATION","Production de contenus génériques","76 % des marketeurs utilisent l'IA générative pour la création de contenu ; les postes de contenu se maintiennent sur la stratégie éditoriale et le brand content, pas sur la production."),
 ("FRAGILISATION","Marketing digital généraliste d'exécution","Technicité 1,42 ; 136 offres de technicité 1 dans l'échantillon décrivent des tâches directement automatisables ; salaires observés 20-30 k€."),
]
for s, mm, sig in PROG:
    ws.cell(row=gr, column=1, value=s).fill = PatternFill("solid", fgColor=GREEN if s=="PROGRESSION" else RED if "RECUL" in s or "FRAGIL" in s else AMBER)
    ws.cell(row=gr, column=2, value=mm)
    c = ws.cell(row=gr, column=3, value=sig); c.alignment = Alignment(wrap_text=True, vertical="top")
    gr += 1
ws.freeze_panes = "C6"


# --- stocks d'offres datés (flux vs stock) et sources documentaires
gr += 2
gr = title(ws, gr, "STOCKS D'OFFRES ACTIVES À UNE DATE DONNÉE (jobboards) — NE PAS ADDITIONNER ENTRE PLATEFORMES", SUB)
ws.cell(row=gr, column=1, value=("Ces comptes sont des STOCKS d'offres actives affichés par les plateformes à une date précise, et non des flux annuels. "
        "Ils ne sont pas dédoublonnés entre plateformes et recouvrent des périmètres lexicaux larges : ils établissent un ordre de grandeur, "
        "jamais un nombre d'emplois. Les comptes des agrégateurs de type Jooble et les requêtes captant la relation client "
        "(fidélisation clients, chargé client) ont été écartés — voir le fichier Markdown.")).font = SMALL
gr += 2
head(ws, gr, ["SOURCE","INTITULE_RECHERCHE","ZONE","TYPE_CONTRAT","NOMBRE","DATE_DU_COMPTE","URL","PREUVE"],
     [16,42,26,15,20,16,64,90]); gr += 1
vstart = gr
for v in sorted(VOLUMES, key=lambda x: (x["SOURCE"], x["ZONE"], x["DATE_DU_COMPTE"])):
    for i, k in enumerate(["SOURCE","INTITULE_RECHERCHE","ZONE","TYPE_CONTRAT","NOMBRE","DATE_DU_COMPTE","URL","PREUVE"], 1):
        c = ws.cell(row=gr, column=i, value=v.get(k, "NC")); c.border = THIN
        c.alignment = Alignment(wrap_text=(i in (7, 8)), vertical="top")
    gr += 1
table(ws, f"A{vstart-1}:H{gr-1}", "T_VOLUMES")

gr += 2
gr = title(ws, gr, "ÉTUDES, RAPPORTS ET DONNÉES DE MARCHÉ MOBILISÉS", SUB)
head(ws, gr, ["TITRE","ORGANISME","DATE_PUBLICATION","PERIMETRE","METHODE","TAILLE_ECHANTILLON",
              "RESULTAT_UTILISE","URL","PAGE_DU_RAPPORT","FIABILITE","DATE_CONSULTATION"],
     [56,26,17,30,34,26,110,64,16,13,16]); gr += 1
estart = gr
for e in sorted(ETUDES, key=lambda x: (x["NIVEAU_DE_FIABILITE"], x["ORGANISME"])):
    for i, k in enumerate(["TITRE","ORGANISME","DATE_PUBLICATION","PERIMETRE","METHODE","TAILLE_ECHANTILLON",
                           "RESULTAT_UTILISE","URL","PAGE_DU_RAPPORT","NIVEAU_DE_FIABILITE","DATE_CONSULTATION"], 1):
        c = ws.cell(row=gr, column=i, value=e.get(k, "NC")); c.border = THIN
        c.alignment = Alignment(wrap_text=(i in (1, 4, 5, 7, 8)), vertical="top")
        if i == 10:
            c.fill = PatternFill("solid", fgColor=GREEN if e.get(k)=="FORTE" else AMBER if e.get(k)=="MOYENNE" else RED)
    gr += 1
table(ws, f"A{estart-1}:K{gr-1}", "T_ETUDES")

# ================================================================ ONGLET 2
ws = wb.create_sheet("REGIONS_METIERS")
r = title(ws, 1, "RÉPARTITION RÉGIONALE — RÉGION × MÉTIER")
ws.cell(row=2, column=1, value="Base : 495 offres uniques dans le périmètre. OFFRES_POUR_100_000_ACTIFS = ESTIMATION calculée à partir des populations actives régionales Insee 2023 (ordre de grandeur, comparaison relative uniquement).").font = SMALL
COLS2 = ["REGION","FAMILLE_METIER","METIER_NORMALISE","VOLUME_BRUT","OFFRES_UNIQUES","PART_NATIONALE",
         "OFFRES_POUR_100_000_ACTIFS","CDI","CDD","ALTERNANCE","STAGE","FREELANCE","DEBUTANT_JUNIOR",
         "INTERMEDIAIRE","SENIOR","SALAIRE_MEDIAN","TELETRAVAIL","NIVEAU_TECHNICITE","COMPETENCES_DOMINANTES",
         "OUTILS_DOMINANTS","SECTEUR_RECRUTEUR","EVOLUTION","TENSION","QUALITE_DU_DEBOUCHE","CONFIANCE"]
W2 = [26,24,34,11,13,13,20,7,7,11,8,10,15,14,8,14,13,16,40,30,26,24,20,22,11]
hr = 4; head(ws, hr, COLS2, W2)
ACTIFS = {"Île-de-France":6300000,"Auvergne-Rhône-Alpes":3600000,"Nouvelle-Aquitaine":2600000,
          "Occitanie":2400000,"Hauts-de-France":2500000,"Provence-Alpes-Côte d'Azur":2200000,
          "Grand Est":2300000,"Pays de la Loire":1700000,"Bretagne":1500000,"Normandie":1400000,
          "Bourgogne-Franche-Comté":1200000,"Centre-Val de Loire":1100000,"Corse":140000,"Outre-mer":700000}
row = hr + 1
PERIM = [o for o in OFFRES if o["FAMILLE_METIER"] not in ("EXCLU_DU_PERIMETRE",) and o["STATUT_DOUBLON"]=="OFFRE_UNIQUE"]
for reg in sorted(set(o["REGION"] for o in PERIM), key=lambda x: -sum(1 for o in PERIM if o["REGION"]==x)):
    sel_r = [o for o in PERIM if o["REGION"] == reg]
    for m in sorted(set(o["METIER_NORMALISE"] for o in sel_r), key=lambda x: -sum(1 for o in sel_r if o["METIER_NORMALISE"]==x)):
        sel = [o for o in sel_r if o["METIER_NORMALISE"] == m]
        n = len(sel); fam = sel[0]["FAMILLE_METIER"]
        ct = collections.Counter(o["TYPE_CONTRAT_N"] for o in sel)
        sn = collections.Counter(o["SENIORITE"] for o in sel)
        comps = collections.Counter(c for o in sel for c in set(o["COMPETENCES_PLATES"]))
        sal = [o["SAL_MOY_N"] for o in sel if o["SAL_MOY_N"]]
        ind = FAMILLE_INDIC.get(fam, ("DONNEES_INSUFFISANTES","DONNEES_INSUFFISANTES","","",""))
        act = ACTIFS.get(reg)
        vals = [reg, fam, m, n, n, round(100*n/len(PERIM),1),
                f"ESTIMATION {round(100000*n/act,2)}" if act else "NC",
                ct.get("CDI",0), ct.get("CDD",0), ct.get("ALTERNANCE",0), ct.get("STAGE",0), ct.get("FREELANCE",0),
                sn.get("DEBUTANT",0)+sn.get("JUNIOR",0), sn.get("INTERMEDIAIRE",0), sn.get("SENIOR",0),
                round(sum(sal)/len(sal)) if sal else "NC",
                sum(1 for o in sel if o["TELETRAVAIL_N"] in ("Oui","Partiel")),
                round(sum(o["NIVEAU_TECHNICITE"] for o in sel)/n, 2),
                " | ".join(c for c,_ in comps.most_common(4)) or "NC",
                " | ".join(c for c,_ in comps.most_common(8) if any(k in c for k in ("Google","Meta","HubSpot","Salesforce","GA4","GTM","SQL","Looker","Braze","Shopify"))) or "0",
                "NC (secteur rarement précisé dans les extraits)",
                "NC — séries historiques régionales non reconstituables", ind[0], ind[1],
                "FORTE" if n >= 10 else "MOYENNE" if n >= 4 else "FAIBLE"]
        for i, v in enumerate(vals, 1):
            c = ws.cell(row=row, column=i, value=v); c.border = THIN
            c.alignment = Alignment(wrap_text=True, vertical="top")
        row += 1
table(ws, f"A{hr}:{get_column_letter(len(COLS2))}{row-1}", "T_REGIONS")

# matrice régions x familles
row += 2
row = title(ws, row, "MATRICE RÉGIONS × FAMILLES DE MÉTIERS (carte thermique : plus la valeur est élevée, plus la cellule est foncée)", SUB)
FAMS = [f for f, _ in sorted(D["par_famille"].items(), key=lambda x: -x[1]["n"])]
REGS = sorted(set(o["REGION"] for o in PERIM), key=lambda x: -sum(1 for o in PERIM if o["REGION"]==x))
head(ws, row, ["RÉGION"] + FAMS + ["TOTAL"], [26] + [17]*len(FAMS) + [10])
mstart = row; row += 1
maxv = max(sum(1 for o in PERIM if o["REGION"]==r_ and o["FAMILLE_METIER"]==f_) for r_ in REGS for f_ in FAMS) or 1
for reg in REGS:
    ws.cell(row=row, column=1, value=reg).font = Font(bold=True, size=9)
    tot = 0
    for j, fam in enumerate(FAMS, 2):
        v = sum(1 for o in PERIM if o["REGION"]==reg and o["FAMILLE_METIER"]==fam); tot += v
        c = ws.cell(row=row, column=j, value=v); c.border = THIN
        c.alignment = Alignment(horizontal="center")
        if v:
            inten = int(255 - 150 * min(v / maxv, 1))
            c.fill = PatternFill("solid", fgColor=f"{inten:02X}{inten:02X}FF")
    ws.cell(row=row, column=len(FAMS)+2, value=tot).font = Font(bold=True)
    row += 1

row += 2
row = title(ws, row, "LECTURE RÉGIONALE POUR NEXA", SUB)
head(ws, row, ["ANGLE D'ANALYSE", "RÉSULTAT"], [46, 130]); row += 1
LECT = [
 ("Régions leaders", "Île-de-France (262 offres, 52,9 % du périmètre), Auvergne-Rhône-Alpes (64), Nouvelle-Aquitaine (35), Provence-Alpes-Côte d'Azur (31), Hauts-de-France (26), Occitanie et Pays de la Loire (20 chacune)."),
 ("Régions favorables aux juniors", "Île-de-France et Auvergne-Rhône-Alpes concentrent l'essentiel des offres de niveau débutant, très majoritairement par l'alternance. En dehors de ces deux régions, les volumes d'offres juniors sont trop faibles pour être analysés métier par métier."),
 ("Régions favorables à l'alternance", "Île-de-France très largement en tête (1 254 offres d'alternance marketing digital recensées sur Indeed en 06/2026, plus de 1 000 au niveau national), puis Auvergne-Rhône-Alpes. L'alternance est le canal d'entrée dominant partout."),
 ("Régions favorables aux métiers Growth / Performance", "Île-de-France (Growth Marketing : 1 295 offres Indeed en 09/2026) puis Auvergne-Rhône-Alpes (agences lyonnaises : Neocamino, L'Express Connect, Mon Petit Placement, Markentive, Vulog, EPSA). Ailleurs, présence ponctuelle (ASight à Bordeaux, MO&JO à Lille, Gens de Confiance à Nantes)."),
 ("Régions favorables aux métiers CRM / Data / MarTech", "Quasi exclusivement Île-de-France pour le MarTech et le RevOps. Le CRM est en revanche présent en région (Lyon, Lille, Bordeaux avec Cdiscount, Nantes)."),
 ("Point de vigilance", "L'étude Alliance Digitale / EY établit que près de la moitié des 310 000 emplois de la filière marketing digital sont situés hors Île-de-France : la surreprésentation francilienne observée sur les jobboards reflète surtout la concentration des postes qualifiés et des agences, pas la totalité de l'emploi."),
]
for k, v in LECT:
    ws.cell(row=row, column=1, value=k).font = Font(bold=True, size=9)
    c = ws.cell(row=row, column=2, value=v); c.alignment = Alignment(wrap_text=True, vertical="top"); row += 1
ws.freeze_panes = "D5"

# ================================================================ ONGLET 3
ws = wb.create_sheet("VILLES_NEXA")
r = title(ws, 1, "VILLES NEXA — ANALYSE PAR CAMPUS")
ws.cell(row=2, column=1, value="Périmètre géographique retenu autour de chaque campus documenté en colonne PERIMETRE. La ligne « National / distanciel » regroupe les offres explicitement en télétravail total.").font = SMALL
COLS3 = ["VILLE","PERIMETRE","METIER_NORMALISE","FAMILLE_METIER","OFFRES_UNIQUES","PART_DU_MARCHE_LOCAL",
         "CDI","CDD","ALTERNANCE","STAGE","DEBUTANT_JUNIOR","INTERMEDIAIRE","SENIOR","SALAIRE_MEDIAN",
         "TELETRAVAIL","NIVEAU_TECHNICITE","COMPETENCES_DOMINANTES","OUTILS_DOMINANTS","COMPETENCES_IA",
         "SECTEURS_RECRUTEURS","EVOLUTION","TENSION","QUALITE_DU_DEBOUCHE","POTENTIEL_NEXA","RECOMMANDATION_CAMPUS"]
W3 = [22,44,34,24,13,18,7,7,11,8,15,14,8,14,13,16,40,30,22,26,24,20,22,16,60]
hr = 4; head(ws, hr, COLS3, W3)
RECO_CAMPUS = {
 "Paris / Île-de-France": ("TRES_FORT", "Seul campus pouvant porter la totalité de l'offre : Bachelor socle technicisé + les deux Mastères (Growth & Performance ; CRM, Data & Marketing Automation) + module MarTech/RevOps et Product Marketing. 52,9 % des offres du périmètre et la totalité des métiers rares (RevOps, CDP, Product Marketing, Paid Media en agence)."),
 "Lyon métropole": ("FORT", "Second pôle national : Bachelor socle technicisé + Mastère Growth & Performance. Écosystème d'agences d'acquisition dense (Neocamino, L'Express Connect, Markentive, Yumens) et présence CRM/RevOps (UPTOO, EPSA, Vulog). Stock Indeed 258 à 317 offres marketing digital."),
 "Lille métropole": ("MOYEN", "Bachelor socle technicisé + coloration CRM et e-commerce (retail et distribution : IRCEM, FOOTKORNER, Comarch, Altavia Wetail, L'Olivier Assurance, MO&JO). Stock Indeed 113 offres. Mastère uniquement en co-diplomation ou distanciel avec Paris."),
 "Bordeaux métropole": ("MOYEN", "Bachelor socle technicisé + coloration e-commerce et acquisition (Cdiscount, ASight, Asphalte, Yumens, Digitalkeys). Stock Indeed 90 offres marketing digital. Mastère en distanciel adossé à Paris."),
 "Nantes métropole": ("FAIBLE_A_MOYEN", "Marché le plus étroit des six campus (stock Indeed 82 offres, le plus faible). Bachelor socle technicisé uniquement, avec coloration e-commerce et SEO/SEA (Gens de Confiance, JVWEB, Digitalkeys, Camif). Ne pas ouvrir de Mastère spécialisé en présentiel."),
 "Marseille - Aix": ("MOYEN", "Bachelor socle technicisé + coloration e-commerce et social ads. Stock Indeed 92 offres, marché d'alternance actif (Chambre de Métiers PACA, Prozon, Style Network). Mastère en distanciel."),
 "National / distanciel": ("FORT", "Levier décisif pour rentabiliser les Mastères spécialisés à faible volume local (CRM/Data, MarTech). Des offres full remote existent réellement sur les métiers techniques (Consultant SEO senior, CRM Manager Yousign, Expert Social Ads, Consultant Paid Media Ad's up, Growth Marketing Manager 55-65 k€)."),
}
row = hr + 1
for v, b in D["par_ville"].items():
    if v == "National / distanciel":
        sel_v = [o for o in PERIM if o["TELETRAVAIL_N"] == "Oui"]
    else:
        sel_v = [o for o in PERIM if o["VILLE_NEXA"] == v]
    pot, reco = RECO_CAMPUS.get(v, ("NC", "NC"))
    if not sel_v:
        ws.cell(row=row, column=1, value=v); ws.cell(row=row, column=2, value=b["perimetre"])
        ws.cell(row=row, column=3, value="0 — aucune offre du périmètre rattachée"); row += 1; continue
    for m in sorted(set(o["METIER_NORMALISE"] for o in sel_v), key=lambda x: -sum(1 for o in sel_v if o["METIER_NORMALISE"]==x)):
        sel = [o for o in sel_v if o["METIER_NORMALISE"] == m]
        n = len(sel); fam = sel[0]["FAMILLE_METIER"]
        ct = collections.Counter(o["TYPE_CONTRAT_N"] for o in sel)
        sn = collections.Counter(o["SENIORITE"] for o in sel)
        comps = collections.Counter(c for o in sel for c in set(o["COMPETENCES_PLATES"]))
        sal = [o["SAL_MOY_N"] for o in sel if o["SAL_MOY_N"]]
        ind = FAMILLE_INDIC.get(fam, ("DONNEES_INSUFFISANTES","DONNEES_INSUFFISANTES","","",""))
        ia = [c for c in comps if "IA" in c or "GEO" in c]
        vals = [v, b["perimetre"], m, fam, n, round(100*n/len(sel_v),1),
                ct.get("CDI",0), ct.get("CDD",0), ct.get("ALTERNANCE",0), ct.get("STAGE",0),
                sn.get("DEBUTANT",0)+sn.get("JUNIOR",0), sn.get("INTERMEDIAIRE",0), sn.get("SENIOR",0),
                round(sum(sal)/len(sal)) if sal else "NC",
                sum(1 for o in sel if o["TELETRAVAIL_N"] in ("Oui","Partiel")),
                round(sum(o["NIVEAU_TECHNICITE"] for o in sel)/n, 2),
                " | ".join(c for c,_ in comps.most_common(4)) or "NC",
                " | ".join(c for c,_ in comps.most_common(8) if any(k in c for k in ("Google","Meta","HubSpot","Salesforce","GA4","GTM","SQL","Braze","Shopify","Looker"))) or "0",
                " | ".join(ia) if ia else "0",
                "NC (secteur rarement précisé dans les extraits)",
                "NC — séries historiques locales non reconstituables", ind[0], ind[1], pot, reco]
        for i, val in enumerate(vals, 1):
            c = ws.cell(row=row, column=i, value=val); c.border = THIN
            c.alignment = Alignment(wrap_text=True, vertical="top")
        row += 1
table(ws, f"A{hr}:{get_column_letter(len(COLS3))}{row-1}", "T_VILLES")

row += 2
row = title(ws, row, "SYNTHÈSE COMPARATIVE DES CAMPUS NEXA", SUB)
head(ws, row, ["CAMPUS","STOCK D'OFFRES MARKETING DIGITAL (jobboard, daté)","OFFRES DU PÉRIMÈTRE (échantillon)",
               "PART DE L'ÉCHANTILLON","ALTERNANCE (%)","TECHNICITÉ MOY.","FAMILLES DOMINANTES","POTENTIEL NEXA","RECOMMANDATION"],
     [22,44,22,18,15,17,44,18,64]); row += 1
STOCKS = {
 "Paris / Île-de-France":"Paris : 2 000+ offres Digital Marketing (Indeed, 14/07/2026) · Île-de-France : 3 000+ (18/04/2026) · 3 496 (25/06/2025) · Alternance IDF : 1 254 (26/06/2026)",
 "Lyon métropole":"Lyon (69) : 317 offres Digital Marketing (02/05/2026) · 258 Marketing Digital (28/05/2026) · 200+ Marketing (12/08/2026)",
 "Lille métropole":"Lille (59) : 113 offres Marketing Digital (16/01/2026)",
 "Bordeaux métropole":"Bordeaux (33) : 90 offres Marketing Digital (19/07/2026) · 100+ Digital (25/03/2026)",
 "Nantes métropole":"Nantes (44) : 82 offres Marketing Digital (21/04/2026) · 75+ Digital Marketing (01/07/2026) · 100+ Marketing (09/08/2026)",
 "Marseille - Aix":"Marseille (13) : 92 offres Marketing Digital (03/09/2026)",
 "National / distanciel":"Marketing Digital à distance : 100+ (19/05/2026) · Full remote Marketing Digital : 75+ (11/08/2026) · Freelance Marketing Digital : 25+ (21/08/2026)",
}
for v, b in D["par_ville"].items():
    pot, reco = RECO_CAMPUS.get(v, ("NC","NC"))
    fams_v = sorted(b.get("familles", {}).items(), key=lambda x: -x[1])[:3]
    vals = [v, STOCKS.get(v,"NC"), b.get("n",0), f"{b.get('part_marche',0)} %",
            f"{b.get('alternance_pct',0)} %", b.get("technicite_moy","NC"),
            " | ".join(f"{f} ({n})" for f, n in fams_v) or "NC", pot, reco]
    for i, val in enumerate(vals, 1):
        c = ws.cell(row=row, column=i, value=val); c.border = THIN
        c.alignment = Alignment(wrap_text=True, vertical="top")
    row += 1
ws.freeze_panes = "C5"

# ================================================================ ONGLET 4
ws = wb.create_sheet("COMPETENCES_TECH_IA")
r = title(ws, 1, "COMPÉTENCES, OUTILS, TECHNICITÉ ET IA")
ws.cell(row=2, column=1, value="Base : 495 offres uniques du périmètre. NOMBRE_OFFRES = nombre d'offres où la compétence est explicitement citée dans le titre ou l'extrait indexé. Ces valeurs sont des BORNES BASSES : les extraits ne restituent qu'une partie du contenu des offres.").font = SMALL
COLS4 = ["FAMILLE_COMPETENCE","COMPETENCE","NOMBRE_OFFRES","PART_DES_OFFRES","METIERS","FAMILLES_METIER",
         "REGIONS","VILLES_NEXA","SENIORITE","CONTRATS","EVOLUTION","OBLIGATOIRE_OU_OPTIONNELLE",
         "ASSOCIATIONS","NIVEAU_TECHNICITE","LIEN_AVEC_IA","EXPOSITION_AUTOMATISATION","MATURITE","PERTINENCE_NEXA","CLASSEMENT"]
W4 = [24,46,14,15,44,34,30,26,26,26,22,24,44,16,26,24,24,20,22]
hr = 4; head(ws, hr, COLS4, W4)

MATURITE = {}  # compétence -> (maturité, lien IA, pertinence NEXA)
def mat(nom, n):
    if "IA" in nom or "Agents IA" in nom or "GEO" in nom or "no-code" in nom.lower() or "No-code" in nom:
        return ("EMERGENTE", "Compétence directement liée à l'IA / l'automatisation", "INDISPENSABLE_EN_TRANSVERSAL")
    if n == 0: return ("NON_CONFIRMEE", "0", "A_SURVEILLER")
    if n >= 40: return ("MATURE", "Peu affectée directement", "SOCLE_OBLIGATOIRE")
    if n >= 15: return ("MATURE", "Peu affectée directement", "SOCLE_OBLIGATOIRE")
    if n >= 5: return ("EN_DEVELOPPEMENT", "Peu affectée directement", "SPECIALISATION_MASTERE")
    return ("RARE_MAIS_STRATEGIQUE", "Peu affectée directement", "SPECIALISATION_MASTERE")

def classement(n, nom):
    if n == 0: return "NON_CONFIRMEE"
    if "IA" in nom or "GEO" in nom or "No-code" in nom: return "EMERGENTE"
    if n >= 40: return "FORTE_DEMANDE"
    if n >= 10: return "DEJA_DEMANDEE"
    if n >= 3: return "RARE_MAIS_STRATEGIQUE"
    return "RARE_MAIS_STRATEGIQUE"

EXPO_C = {"Réseaux sociaux (organique)":"FORTE","Création de contenu / rédaction":"TRES_FORTE",
          "Vidéo / motion / création visuelle":"FORTE","Emailing / newsletters / push":"MOYENNE",
          "KPI / reporting / analyse de performance":"MOYENNE"}
row = hr + 1
for nom, v in sorted(D["competences"].items(), key=lambda x: (-x[1]["n"], x[0])):
    n = v["n"]; m_, lien, pert = mat(nom, n)
    tech = v.get("technicite_moy", "NC")
    vals = [v["famille"], nom, n, f"{v['pct']} %",
            " | ".join(f"{a} ({b})" for a, b in v.get("metiers", [])) or "0",
            " | ".join(f"{a} ({b})" for a, b in v.get("familles_metier", [])) or "0",
            " | ".join(f"{a} ({b})" for a, b in v.get("regions", [])) or "0",
            " | ".join(f"{a} ({b})" for a, b in v.get("villes", [])) or "0",
            " | ".join(f"{a} ({b})" for a, b in v.get("seniorite", [])) or "0",
            " | ".join(f"{a} ({b})" for a, b in v.get("contrats", [])) or "0",
            "NC — séries historiques par compétence non reconstituables",
            "OBLIGATOIRE" if n >= 40 else "OPTIONNELLE" if n > 0 else "NON_OBSERVEE",
            " | ".join(v.get("associations", [])) or "0",
            tech, lien, EXPO_C.get(nom, "FAIBLE" if isinstance(tech,(int,float)) and tech >= 2.4 else "MOYENNE"),
            m_, pert, classement(n, nom)]
    for i, val in enumerate(vals, 1):
        c = ws.cell(row=row, column=i, value=val); c.border = THIN
        c.alignment = Alignment(wrap_text=True, vertical="top")
        if i == 19:
            c.fill = PatternFill("solid", fgColor=GREEN if val=="FORTE_DEMANDE" else LIGHT if val=="DEJA_DEMANDEE"
                                 else AMBER if val=="EMERGENTE" else RED if val=="NON_CONFIRMEE" else GREY)
    row += 1
table(ws, f"A{hr}:{get_column_letter(len(COLS4))}{row-1}", "T_COMPETENCES")

# blocs thématiques
row += 2
row = title(ws, row, "BLOCS DE COMPÉTENCES — LECTURE PÉDAGOGIQUE POUR NEXA", SUB)
head(ws, row, ["BLOC","COMPÉTENCES CONCERNÉES (avec nombre d'offres)","VOLUME CUMULÉ","LECTURE"], [40,90,16,80]); row += 1
def somme(noms):
    return sum(D["competences"].get(x, {}).get("n", 0) for x in noms)
BLOCS = [
 ("COMPETENCES_MARKETING_GENERALISTE",
  ["Réseaux sociaux (organique)","Création de contenu / rédaction","Gestion de projet","Vidéo / motion / création visuelle","Stratégie marketing"],
  "Socle indispensable mais NON différenciant : très demandé, très faiblement technique, et directement exposé à l'automatisation. À enseigner en première année, jamais comme spécialisation d'arrivée."),
 ("COMPETENCES_MARKETING_TECHNIQUE",
  ["SEO","SEA / Paid Search","Google Ads","Meta Ads / Facebook Ads","LinkedIn Ads","TikTok Ads","Programmatique / DV360","SEO technique","Microsoft / Bing Ads","Amazon Ads / retail media"],
  "Cœur de la technicisation de niveau 2 : expertise canal. C'est le premier palier de différenciation, accessible dès le Bachelor et directement valorisé en alternance."),
 ("COMPETENCES_DATA_MARKETING",
  ["Google Analytics 4 / GA4","Google Tag Manager / GTM","Tracking / data layer / plan de taggage","Attribution","Looker Studio / dashboards","SQL","BigQuery / data warehouse","Power BI / Tableau / Looker","KPI / reporting / analyse de performance","Excel / Google Sheets","Amplitude / Mixpanel / Matomo / Piano"],
  "Palier de technicité 3-4. Peu cité explicitement dans les extraits indexés (bornes basses) mais systématiquement présent dans les offres de Web Analyst, Traffic Manager et CRM. C'est le socle qui rend un diplômé NEXA non substituable."),
 ("COMPETENCES_CRM_AUTOMATION",
  ["CRM (générique)","HubSpot","Salesforce / Marketing Cloud / Pardot","Braze","Klaviyo","Brevo / Sendinblue","Adobe Campaign","Marketing automation","Emailing / newsletters / push","Segmentation / scoring / nurturing","CDP / Customer Data Platform","ActiveCampaign / Mailchimp / Splio / Dotdigital / Actito"],
  "2e compétence la plus demandée de tout le périmètre (CRM générique : 11,5 % des offres). Faible exposition à l'automatisation, forte pérennité, salaires élevés. C'est la spécialisation de Mastère la plus solide."),
 ("COMPETENCES_GROWTH_PERFORMANCE",
  ["CRO / optimisation de conversion","A/B testing / expérimentation","AB Tasty / Kameleoon / Optimizely / Contentsquare / Hotjar","Business / ROI / revenue","Pilotage budgétaire / média","Demand / lead generation"],
  "Peu cité explicitement dans les intitulés mais structurant dans les descriptions de postes Growth et e-commerce. Le CRO n'existe quasiment pas comme métier autonome en France : c'est une compétence, pas une spécialisation."),
 ("COMPETENCES_MARKETEUR_AUGMENTE_PAR_IA",
  ["IA générative (ChatGPT, Claude, Gemini…)","Agents IA / prompt engineering","No-code / automatisation (Zapier, Make, n8n)","IA appliquée au marketing (packshot, création, workflow)","GEO / AEO / AI Search","API / webhook / intégrations"],
  "RÉSULTAT CLÉ : au total 16 mentions seulement sur 495 offres. La demande est RÉELLE mais MARGINALE, et converge avec la mesure Apec (2 % des offres commercial-marketing mentionnent l'IA). Ces compétences doivent être enseignées en transversal et rendues obligatoires, mais ne peuvent PAS fonder un parcours dédié."),
]
for nomb, comps, lecture in BLOCS:
    detail = " | ".join(f"{c} ({D['competences'].get(c,{}).get('n',0)})" for c in comps)
    ws.cell(row=row, column=1, value=nomb).font = Font(bold=True, size=9)
    ws.cell(row=row, column=2, value=detail).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=row, column=3, value=somme(comps)).font = Font(bold=True)
    ws.cell(row=row, column=4, value=lecture).alignment = Alignment(wrap_text=True, vertical="top")
    row += 1

row += 2
row = title(ws, row, "NIVEAUX DE TECHNICITÉ — DÉFINITION ET RÉPARTITION OBSERVÉE", SUB)
head(ws, row, ["NIVEAU","DÉFINITION","EXEMPLES DE TÂCHES / COMPÉTENCES","OFFRES OBSERVÉES","PART","LECTURE NEXA"], [12,44,70,18,12,64]); row += 1
nt = D["national"]["technicite"]; tot = sum(nt.values())
NIV = [
 ("NIVEAU_1","Généraliste / exécution","Publication réseaux sociaux, rédaction simple, emailing simple, coordination, animation, mise à jour de contenus",
  nt.get("1",nt.get(1,0)), "Zone la plus exposée à l'automatisation par l'IA générative. C'est aussi la zone qui porte l'alternance : elle doit être traversée, pas visée."),
 ("NIVEAU_2","Expertise canal","SEO, SEA, Paid Social, CRM, e-commerce, content strategy, influence",
  nt.get("2",nt.get(2,0)), "Premier palier de valeur. Cible réaliste de sortie de Bachelor NEXA."),
 ("NIVEAU_3","Performance / data / automation","GA4, GTM, tracking, attribution, CRO, CRM automation, dashboards, SQL, segmentation, automatisation, API",
  nt.get("3",nt.get(3,0)), "Cible de sortie de Mastère. Peu accessible aux juniors : 16 % de juniors en Data, 11,8 % en MarTech."),
 ("NIVEAU_4","MarTech / data / systèmes","Architecture CRM, CDP, server-side tracking, data warehouse, BigQuery, automatisations complexes, intégration API, Marketing Ops, RevOps, orchestration IA",
  nt.get("4",nt.get(4,0)), "Marché étroit (11 offres observées) et réservé aux profils expérimentés. À traiter en module de Mastère, jamais en parcours autonome."),
]
for n_, d_, ex, cnt, lect in NIV:
    ws.cell(row=row, column=1, value=n_).font = Font(bold=True)
    ws.cell(row=row, column=2, value=d_).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=row, column=3, value=ex).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=row, column=4, value=cnt)
    ws.cell(row=row, column=5, value=f"{round(100*cnt/tot,1)} %")
    ws.cell(row=row, column=6, value=lect).alignment = Alignment(wrap_text=True, vertical="top")
    row += 1

row += 2
row = title(ws, row, "TÂCHES EXPOSÉES À L'AUTOMATISATION ET COMPÉTENCES DONT LA VALEUR AUGMENTE", SUB)
head(ws, row, ["SENS","ÉLÉMENT","FONDEMENT"], [26,52,110]); row += 1
IA_T = [
 ("EXPOSEE","Rédaction de contenus génériques","76 % des marketeurs déclarent utiliser l'IA générative pour la création de contenu."),
 ("EXPOSEE","Déclinaisons publicitaires et production créative","Offre AI Content Manager observée : déclinaisons, automatisations, adaptations visuelles, production de packshots par IA."),
 ("EXPOSEE","Publication et animation simple des réseaux sociaux","Technicité 1,03 sur la famille Social Media ; 88 % des équipes marketing déclarent utiliser l'IA au quotidien."),
 ("EXPOSEE","Reporting manuel et synthèse de performances","Automatisation par les fonctions natives de Google Ads, Meta Ads, HubSpot et par les dashboards."),
 ("EXPOSEE","Recherche de mots-clés basique et briefs simples","Fonctions natives des plateformes et outils génératifs."),
 ("EXPOSEE","Création d'emails simples et segmentation élémentaire","Fonctions natives des plateformes de marketing automation."),
 ("VALEUR_EN_HAUSSE","Analyse et interprétation des données","L'Apec constate le redéploiement de la valeur ajoutée des cadres commercial-marketing vers l'analyse."),
 ("VALEUR_EN_HAUSSE","Personnalisation et stratégie de la relation client","Apec, L'intelligence artificielle en commercial-marketing (2026)."),
 ("VALEUR_EN_HAUSSE","Qualité de la donnée, tracking et attribution","Compétences de niveau 3-4, présentes dans les offres Web Analyst et CRM à 5 ans d'expérience minimum."),
 ("VALEUR_EN_HAUSSE","Architecture CRM et orchestration de systèmes","Offres RevOps et CDP : 0 % d'alternance, expérience de 3 à 7 ans exigée."),
 ("VALEUR_EN_HAUSSE","Expérimentation et CRO","Le CRO reste une compétence transverse recherchée dans les postes e-commerce et growth."),
 ("VALEUR_EN_HAUSSE","Contrôle des sorties IA et gouvernance","86 % des marketeurs retravaillent systématiquement les contenus générés par l'IA, 92 % imposent une validation humaine."),
 ("VALEUR_EN_HAUSSE","Pilotage budgétaire et compréhension business","Compétence Business/ROI citée dans 5,3 % des offres, transverse à toutes les familles techniques."),
 ("VALEUR_EN_HAUSSE","Capacité à intégrer l'IA dans des processus métier","Compétence explicitement identifiée comme émergente par l'Apec, aux côtés de la maîtrise des outils génératifs."),
]
for s, e, f_ in IA_T:
    ws.cell(row=row, column=1, value=s).fill = PatternFill("solid", fgColor=RED if s=="EXPOSEE" else GREEN)
    ws.cell(row=row, column=2, value=e).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(row=row, column=3, value=f_).alignment = Alignment(wrap_text=True, vertical="top")
    row += 1
ws.freeze_panes = "C5"

# ================================================================ ONGLET 5
ws = wb.create_sheet("OFFRES_DETAILLEES")
r = title(ws, 1, "OFFRES DÉTAILLÉES — BASE SOURCE")
ws.cell(row=2, column=1, value="Une ligne par offre collectée. STATUT_OBSERVE_OU_ESTIME : toutes les valeurs de ce tableau sont OBSERVÉES (issues du titre ou de l'extrait indexé) ; les champs non présents dans l'extrait sont notés NC et n'ont jamais été déduits. La colonne PREUVE contient l'extrait textuel qui justifie les champs renseignés.").font = SMALL
COLS5 = ["ID_OFFRE","SOURCE","URL","STATUT_DOUBLON","DATE_COLLECTE","ENTREPRISE","INTITULE_BRUT",
         "METIER_NORMALISE","FAMILLE_METIER","REGION","DEPARTEMENT","VILLE","VILLE_NEXA","TELETRAVAIL",
         "TYPE_CONTRAT","EXPERIENCE","SENIORITE","SALAIRE_MINIMUM","SALAIRE_MAXIMUM","NIVEAU_TECHNICITE",
         "IA_MENTIONNEE","COMPETENCES_DETECTEES","COMPETENCES_BRUTES","STATUT_OBSERVE_OU_ESTIME","PREUVE","REQUETE"]
W5 = [11,18,54,28,13,26,52,34,24,24,13,20,20,26,14,26,18,14,14,14,14,60,50,24,110,60]
hr = 4; head(ws, hr, COLS5, W5)
row = hr + 1
for o in OFFRES:
    vals = [o["ID_OFFRE"], o["SOURCE"], o["URL"], o["STATUT_DOUBLON"], o["DATE_COLLECTE"], o["ENTREPRISE"],
            o["INTITULE_BRUT"], o["METIER_NORMALISE"], o["FAMILLE_METIER"], o["REGION"], o["DEPARTEMENT"],
            o["VILLE"], o["VILLE_NEXA"] or "0", o["TELETRAVAIL_N"], o["TYPE_CONTRAT_N"], o["EXPERIENCE"],
            o["SENIORITE"], o["SALAIRE_MINIMUM"], o["SALAIRE_MAXIMUM"], o["NIVEAU_TECHNICITE"],
            "Oui" if o["IA_MENTIONNEE"] else "Non", " | ".join(o["COMPETENCES_PLATES"]) or "0",
            o["COMPETENCES_BRUTES"], "OBSERVE", o["PREUVE"], o["REQUETE"]]
    for i, v in enumerate(vals, 1):
        c = ws.cell(row=row, column=i, value=v); c.border = THIN
        c.alignment = Alignment(wrap_text=(i in (7, 22, 23, 25, 26)), vertical="top")
    row += 1
table(ws, f"A{hr}:{get_column_letter(len(COLS5))}{row-1}", "T_OFFRES")
ws.freeze_panes = "H5"

path = os.path.join(ROOT, "NEXA_Marche_Emploi_Marketing_Digital_France_2026.xlsx")
wb.save(path)
print("Écrit :", path)
print("Onglets :", wb.sheetnames)
