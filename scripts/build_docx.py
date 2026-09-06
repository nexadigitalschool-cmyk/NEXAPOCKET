# -*- coding: utf-8 -*-
"""Livrable 2 : NEXA_Synthese_Marche_Emploi_Developpement_Web_2026.docx"""
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Cm

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis import *  # noqa
from normalize import NC, is_nc, norm, COEUR, EVOL, SPEC, IA, ADJ, EXCLU, SKILLS
from build_excel import evol_pct, METIER_SERIES, ZONE_SERIES, REGION_SERIES

OUTDIR = os.environ.get("NEXA_OUT", "/home/user/NEXAPOCKET")
DATE = "2026-09-06"
DATE_FR = "6 septembre 2026"


# ---------------------------------------------------------------------------
def add_hyperlink(paragraph, url, text=None):
    part = paragraph.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), "0563C1"); rPr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rPr.append(u)
    new_run.append(rPr)
    t = OxmlElement("w:t"); t.text = text or url; t.set(qn("xml:space"), "preserve")
    new_run.append(t)
    hl.append(new_run)
    paragraph._p.append(hl)
    return hl


def set_cell_bg(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd"); shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), color)
    tcPr.append(shd)


def table(doc, headers, rows, widths=None, font_size=8):
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]
        c.text = ""
        run = c.paragraphs[0].add_run(str(h)); run.bold = True; run.font.size = Pt(font_size); run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_bg(c, "1F3864")
    for r in rows:
        cells = t.add_row().cells
        for i, v in enumerate(r):
            cells[i].text = ""
            run = cells[i].paragraphs[0].add_run("" if v is None else str(v)); run.font.size = Pt(font_size)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph()
    return t


def p(doc, text, bold=False, italic=False, size=None, style=None):
    para = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    run = para.add_run(text); run.bold = bold; run.italic = italic
    if size:
        run.font.size = Pt(size)
    return para


def bullet(doc, text, src=None, url=None):
    para = doc.add_paragraph(style="List Bullet")
    para.add_run(text)
    if src:
        r = para.add_run(f" [{src}]"); r.italic = True; r.font.size = Pt(8)
    if url:
        para.add_run(" ")
        add_hyperlink(para, url, "source")
    return para


def ref(doc, text):
    para = doc.add_paragraph()
    r = para.add_run(text); r.italic = True; r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x59, 0x59, 0x59)


def load_jsonl_any(paths):
    out = []
    for pth in paths:
        for fp in glob.glob(pth):
            for line in open(fp, encoding="utf-8"):
                line = line.strip()
                if line:
                    try:
                        out.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    return out


# ---------------------------------------------------------------------------
def main():
    rows, vols = load()
    U = uniques(rows)
    series = volume_series(vols)
    brut = len(rows)
    dup = Counter(r["STATUT_DOUBLON"] for r in rows)
    contrats, c_nc = contract_counts(U)
    kc = sum(contrats.values())
    sen, s_nc = seniority_counts(U)
    ks = sum(sen.values())
    sal = annual_salaries(U)
    tel_y, tel_k, tel_s = teletravail_share(U)
    ia_n, ia_s = ia_share(U)
    fam = Counter(r["FAMILLE_METIER"] for r in U)
    met = Counter(r["METIER_NORMALISE"] for r in U)
    core = [r for r in U if r["FAMILLE_METIER"] in (COEUR, EVOL)]
    core_ia = [r for r in core if r["MENTION_IA_EXPLICITE"] == "Oui"]
    tools = Counter()
    for r in U:
        for it in r.get("_skills", {}).get("OUTILS_DE_CODAGE_IA", []):
            tools[it] += 1
    skills_top = top_skills(U, 15)
    reg = Counter(r["REGION_NORMALISEE"] for r in U)
    zones = {z: [r for r in U if r["ZONE_NEXA"] == z] for z in NEXA_CITIES}
    n_sources = sources_count(U)
    e25_web, e24_web, det_web = evol_pct(series, METIER_SERIES["Développeur web (intitulé générique)"], [r"france.*", r"nc", r""])
    e25_fs, e24_fs, det_fs = evol_pct(series, METIER_SERIES["Développeur full stack"], [r"france.*", r"nc", r""])
    e25_idf, e24_idf, det_idf = evol_pct(series, [r"developpeur web"], [r"ile-de-france.*"])
    studies = load_jsonl_any([os.path.join(ETUDES_DIR, "etudes_marche.jsonl"), os.path.join(ETUDES_DIR, "notes_nationales.jsonl")])
    salaires = load_jsonl_any([os.path.join(ETUDES_DIR, "salaires.jsonl")])
    comps = load_jsonl_any([os.path.join(ETUDES_DIR, "competences.jsonl"), os.path.join(COLLECTE_DIR, "C_competences.jsonl")])
    ias = load_jsonl_any([os.path.join(ETUDES_DIR, "ia_transformation.jsonl"), os.path.join(COLLECTE_DIR, "C_ia.jsonl")])
    regions_ext = load_jsonl_any([os.path.join(ETUDES_DIR, "regions_donnees.jsonl"), os.path.join(COLLECTE_DIR, "C_regions.jsonl")])

    junior_share = pct(sen["DEBUTANT"] + sen["JUNIOR"], ks) if ks else NC
    senior_share = pct(sen["SENIOR"] + sen["LEAD_OU_ARCHITECTE"], ks) if ks else NC
    alt_share = pct(contrats["ALTERNANCE"] + contrats["STAGE"], kc) if kc else NC
    deb_alt = sum(1 for r in U if r["SENIORITE"] == "DEBUTANT" and r["TYPE_CONTRAT_NORMALISE"] in ("ALTERNANCE", "STAGE"))
    deb_cdi = sum(1 for r in U if r["SENIORITE"] in ("DEBUTANT", "JUNIOR") and r["TYPE_CONTRAT_NORMALISE"] == "CDI")

    doc = Document()
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
    for s in ("Heading 1", "Heading 2", "Heading 3"):
        doc.styles[s].font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

    # ---- page de titre ----
    t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("NEXA Digital School\nObservatoire du marché de l'emploi du développement web en France"); r.bold = True; r.font.size = Pt(20); r.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)
    t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = t.add_run("Synthèse pour la Direction Générale, la Direction Marketing et la Direction Pédagogique"); r.font.size = Pt(13)
    t = doc.add_paragraph(); t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.add_run(f"Collecte et analyse arrêtées au {DATE_FR} — livrables associés : NEXA_Marche_Emploi_Developpement_Web_France_2026.xlsx (5 onglets) et NEXA_Perimetre_Metiers_et_Plateformes_Sans_Donnees.md (journal de collecte)").italic = True

    doc.add_heading("Conclusion en une phrase", 1)
    p(doc, "Le marché français du développement web n'est pas en train de disparaître, mais il s'est contracté d'environ 20 % en 2025 et de plus de moitié depuis le pic de 2022, il s'est recomposé autour du profil full stack industrialisé (tests, CI/CD, cloud, sécurité) et de l'intégration de l'IA, et il est devenu nettement plus sélectif envers les débutants : NEXA doit transformer sa filière Développement Web (scénario B) et la renforcer par une offre M1/M2 (scénario C), sans la maintenir en l'état ni l'abandonner.", bold=True)
    p(doc, "Verdict pour la filière : TRANSFORMEE + RENFORCEE_EN_MASTERE (l'IA intégrée comme compétence transversale, pas comme repositionnement marketing exclusif). Le détail des preuves, des contradictions et du niveau de confiance figure dans le tableau des hypothèses (section 14) et dans l'Excel.", italic=True)

    doc.add_heading("Méthode et limites (à lire avant les chiffres)", 1)
    bullet(doc, f"Échantillon collecté : {brut} lignes d'offres brutes sur {n_sources} plateformes (Indeed, Welcome to the Jungle, France Travail, HelloWork, Apec, LinkedIn, Free-Work, Talent.com, sites carrières), {len([r for r in rows if r['STATUT_DOUBLON'] == 'OFFRE_UNIQUE'])} offres uniques après dédoublonnage, {len(U)} dans le périmètre étudié (Excel, onglet OFFRES_DETAILLEES). Taux de doublons multi-plateformes ou probables : {pct(dup.get('DUPLICATION_MULTI_PLATEFORME', 0) + dup.get('OFFRE_PROBABLEMENT_IDENTIQUE', 0), brut)} % ; republications : {pct(dup.get('REPUBLICATION', 0), brut)} %.")
    bullet(doc, "Contrainte technique majeure : aucun accès direct aux sites (proxy réseau), ni à l'API France Travail ; toutes les offres et tous les comptes d'offres proviennent des pages publiques indexées par un moteur de recherche (titres, URL, extraits), avec un plafond de 200 requêtes par session de collecte, d'où une collecte en plusieurs vagues (A à E) et plusieurs sessions parallèles, chacune journalisée. De nombreux champs (expérience, salaire, télétravail) ne figurent pas dans les extraits et sont notés NC ; les parts calculées portent uniquement sur les offres renseignées, avec l'effectif indiqué. Les fourchettes d'expérience du type « 1 à 7 ans » sont classées d'après leur borne basse. Voir le fichier Markdown pour le journal complet.")
    bullet(doc, "Les comptes d'offres actives des jobboards (« plus de N emplois », datés) sont des stocks à une date, arrondis à la baisse par la plateforme ; ils servent à comparer une même page à des dates différentes (2024, 2025, 2026), pas à additionner des plateformes. Les évolutions qui en sont tirées sont marquées ESTIMATION.")
    bullet(doc, "Les tendances annuelles reposent sur les séries et études externes (Apec, France Travail BMO, Dares, Insee, Numeum, Indeed Hiring Lab), citées avec leur URL dans la section « Études, articles et sources pour approfondir ». Les études internationales (Stack Overflow) éclairent la transformation par l'IA mais ne servent pas à conclure sur la France.")
    bullet(doc, "Convention : 0 = absence constatée dans l'échantillon ; NC = donnée indisponible ; ESTIMATION = valeur reconstituée à partir de sources identifiées ; FORTE / MOYENNE / FAIBLE = niveau de confiance.")

    # ---- 1. état du marché national ----
    doc.add_heading("1. État du marché national", 1)
    p(doc, "Le marché du développement web reste le premier gisement d'offres cadres en informatique, mais il a fortement reculé depuis 2022 et ne retrouve pas encore son niveau d'avant-crise.")
    bullet(doc, "Apec : 12 690 offres cadres « développeur » publiées sur apec.fr en 2025, soit -20 % en un an et -60 % par rapport à 2022 ; le développeur reste le 2e métier cadre en volume national ; 21 % des offres visent des débutants ; 29 % sont en Île-de-France ; la majorité émane d'ESN.", "Apec, Les métiers cadres porteurs éd. 2026, 19/02/2026 ; relais Programmez", "https://corporate.apec.fr/home/nos-etudes/toutes-nos-etudes/les-metiers-cadres-porteurs-edition-2026.html")
    bullet(doc, "Indeed Hiring Lab France (avril 2026) : les offres Indeed sont revenues à leur niveau de février 2020 et leur volume a été divisé par deux depuis le pic de décembre 2022 ; la tech et les médias sont les secteurs les plus touchés.", "Indeed Hiring Lab, 01/04/2026", "https://www.hiringlab.org/fr/blog/2026/04/01/avril-2026-lia-progresse-dans-un-marche-du-travail-en-recul/")
    bullet(doc, "Lecture de l'indice FRED/Indeed « Software Development Job Postings in France » relayée par la presse : plus de -80 % entre janvier 2023 et juillet 2025 (source secondaire, fiabilité MOYENNE ; l'indice lui-même est de fiabilité FORTE mais ses valeurs n'ont pas pu être lues directement).", "Developpez.com relayant FRED IHLIDXFRTPSOFTDEVE", "https://fred.stlouisfed.org/series/IHLIDXFRTPSOFTDEVE")
    bullet(doc, "Dares (février 2026, données 2024) : pour la première fois depuis 2016, les métiers de l'informatique quittent la catégorie « tension très forte » (niveau 5) pour « tension forte » (niveau 4) ; c'est la plus forte baisse de tension de tous les domaines professionnels. En 2023 l'indicateur de tension des ingénieurs de l'informatique atteignait encore 1,1 (tension extrême, 67 % de recrutements jugés difficiles).", "Dares Résultats n°5, 04/02/2026 ; Insee Références 2025", "https://dares.travail-emploi.gouv.fr/publication/les-tensions-sur-le-marche-du-travail-en-2024")
    bullet(doc, "Numeum : effectifs du secteur numérique en recul pour la deuxième année consécutive (-1,8 % entre 2023 et 2025, environ 666 000 salariés, -7 500 emplois en 2024) ; croissance du marché révisée à +3 % pour 2026.", "Numeum, baromètre S1 2026", "https://numeum.fr/etude-le-marche-du-numerique-francais-sort-de-la-zone-de-turbulences-mais-lattentisme-freine-encore-la-reprise/")
    bullet(doc, "Insee Île-de-France, T1 2026 : heures rémunérées en baisse de 2,2 % sur un an dans la programmation, le conseil et les autres activités informatiques.", "Insee, conjoncture IDF T1 2026", "https://www.insee.fr/fr/statistiques/8616805?sommaire=8616883")
    bullet(doc, "Signaux de reprise : Apec prévoit 61 160 recrutements de cadres informaticiens en 2026 (+4 %) et 60 100 dans les activités informatiques et télécoms (+5 %) après -4 % en 2025 ; France Travail BMO 2026 recense 84 227 projets de recrutement dans le numérique dont 49,5 % jugés difficiles (contre 43,8 % tous secteurs). Mais le baromètre Apec du 2e trimestre 2026 note un fléchissement des intentions de recrutement (PME 12 %, -4 pts ; grandes entreprises 48 %, -3 pts) lié à l'incertitude géopolitique.", "Apec prévisions 2026 (02/04/2026) ; France Travail BMO 2026 ; Apec baromètre T2 2026", "https://corporate.apec.fr/files/live/sites/corporate/files/Nos%20etudes/PDF/Previsions-de-recrutements-de-cadres-2026")
    bullet(doc, f"Stocks d'offres actives observés (pages Indeed France) : « Développeur Web » plus de 4 000 (2 juillet 2025) puis plus de 3 000 (26 mai et 3 septembre 2026) ; « Développeur Full Stack » plus de 500 (2 août 2025) puis plus de 800 à 900 (août-septembre 2026) ; « Développeur » plus de 3 000 (septembre 2026) ; HelloWork « Développeur informatique » plus de 9 650 (18 août 2026). Excel, onglet SYNTHESE_METIERS, table T_STOCKS_NATIONAUX.", "collecte du " + DATE)
    p(doc, "Réponse à la question 1 (le marché baisse-t-il réellement ?) : oui pour le flux d'offres 2023-2025, avec une ampleur documentée par des sources indépendantes (Apec -20 % en 2025, Indeed volume divisé par deux depuis fin 2022, Dares sortie de la tension très forte) ; non pour l'emploi total, qui recule faiblement (-1,8 % sur deux ans selon Numeum) ; et les prévisions 2026 pointent une stabilisation plutôt qu'une reprise franche. Confiance FORTE.", bold=True)

    # ---- 2. évolution de la demande ----
    doc.add_heading("2. Évolution de la demande sur trois à cinq ans", 1)
    table(doc, ["Indicateur", "2022-2023", "2024", "2025", "2026 (au " + DATE_FR + ")", "Source / statut"], [
        ["Offres cadres « développeur » sur apec.fr (flux annuel)", "pic 2022 (base -60 %)", "≈ 15 900 (déduit de -20 % en 2025, ESTIMATION)", "12 690 (-20 %)", "NC (flux annuel non publié)", "Apec, éd. 2026 (FORTE)"],
        ["Recrutements de cadres, tous métiers (flux annuel)", "330 400 (2023, record)", "303 400 (-8 %)", "294 500 (-3 %)", "305 800 prévus (+4 %)", "Apec (FORTE)"],
        ["Recrutements de cadres informaticiens (flux)", "NC", "NC", "≈ 58 800 (déduit de +4 %, ESTIMATION)", "61 160 prévus (+4 %)", "Apec (FORTE)"],
        ["Offres Indeed France, tous métiers (stock indexé)", "pic déc. 2022", "en baisse", "retour au niveau fév. 2020", "point bas 7 janv. 2026 puis reprise", "Indeed Hiring Lab (FORTE)"],
        ["Stock Indeed « Développeur Web » France", "NC", "NC", "plus de 4 000 (02/07/2025)", "plus de 3 000 (26/05 et 03/09/2026)", "pages indexées (OBSERVE, arrondi)"],
        ["Stock Indeed « Développeur Web » Île-de-France", "NC", "plus de 1 000 (20/12/2024)", "NC", "plus de 900 (23/06/2026)", "pages indexées (OBSERVE, arrondi)"],
        ["Stock Indeed « Développeur Web » Occitanie", "NC", "plus de 400 (02/09/2024)", "plus de 200 (08/10/2025)", "NC", "pages indexées (OBSERVE, arrondi)"],
        ["Tension Dares métiers informatiques", "niveau 5 (très forte), indicateur 1,1 en 2023", "niveau 4 (forte)", "NC", "NC", "Dares (FORTE)"],
        ["Projets de recrutement BMO numérique", "≈ 80 000 (2023)", "79 297 (info-télécoms, 6 métiers)", "NC", "84 227 (49,5 % difficiles)", "France Travail BMO (FORTE)"],
        ["Effectifs secteur numérique (Numeum)", "≈ 673 000 (2023)", "≈ 666 000 (-7 500)", "stabilisation ; -1,8 % vs 2023", "NC", "Numeum (FORTE)"],
    ], widths=[5, 2.5, 2.8, 2.8, 3, 2.5])
    p(doc, "Distinction stock / flux : les baisses les plus fortes concernent les flux d'offres (annonces publiées), pas l'emploi en place. Le stock d'offres actives « développeur web » sur Indeed est passé d'un palier « plus de 4 000 » à « plus de 3 000 » entre juillet 2025 et 2026 (-25 % au niveau des paliers, ESTIMATION), alors que le palier « développeur full stack » a progressé (« plus de 500 » en août 2025, « plus de 800 » en septembre 2026). Une année 2026 incomplète n'est jamais comparée à une année complète : seules des dates comparables (stocks) ou des prévisions annuelles (Apec, BMO) sont mises en regard.")

    # ---- 3. métiers ----
    doc.add_heading("3. Métiers qui progressent et métiers qui reculent", 1)
    p(doc, f"Dans l'échantillon d'offres uniques ({len(U)}), le cœur de marché représente {pct(fam[COEUR], len(U))} % des offres, les évolutions naturelles {pct(fam[EVOL], len(U))} %, les spécialisations {pct(fam[SPEC], len(U))} % et les métiers émergents liés à l'IA {pct(fam[IA], len(U))} % (ces derniers ont été recherchés spécifiquement et sont donc surreprésentés). Excel, onglet SYNTHESE_METIERS, table T_SYNTHESE_METIERS.")
    top = met.most_common(12)
    table(doc, ["Métier normalisé", "Offres uniques", "Part de l'échantillon", "Lecture"], [
        [m, n, f"{pct(n, len(U))} %", {
            "Développeur full stack": "Intitulé dominant : le « développeur web » se recrute désormais sous cette étiquette (front + back + déploiement).",
            "Développeur web (intitulé générique)": "Intitulé en recul relatif (stock Indeed -25 % de palier entre 2025 et 2026) ; concentre alternance et stages.",
            "Développeur front-end": "Volume stable, dominé par React ; exigence de TypeScript et de tests.",
            "AI Engineer / Développeur IA": "Métier émergent en croissance (stock Indeed « Développeur Intelligence Artificielle » plus de 600 au 05/09/2026), profils souvent seniors.",
            "Développeur PHP / Symfony / Laravel": "Écosystème français toujours présent (ESN, agences, médias) mais en recul sur Indeed (« Développeur PHP » plus de 4 000 en juillet 2025, plus de 2 000 en août 2026).",
            "Développeur mobile": "Débouché adjacent des profils JavaScript (React Native, Flutter).",
            "DevOps Engineer": "Spécialisation en tension, majoritairement senior.",
            "Site Reliability Engineer (SRE)": "Métier senior d'exploitation, hors portée d'un Bachelor.",
            "Développeur Java / Spring": "Premier volume back-end en ESN (Indeed « Développeur Java » plus de 1 000, août 2026).",
            "Développeur .NET / C#": "Stack Microsoft, forte part de profils expérimentés.",
            "LLM / Generative AI Engineer": "Émergent, quelques dizaines d'offres nationales (« Développeur LLM » plus de 200 sur Indeed, 04/09/2026).",
        }.get(m, "Voir Excel.")] for m, n in top], widths=[5, 1.8, 2.2, 8])
    p(doc, "Réponse à la question 2 (la baisse concerne-t-elle tous les métiers ?) : non. Le recul est concentré sur les intitulés génériques (« développeur web », « intégrateur web », PHP) et sur les postes débutants ; les intitulés full stack, software engineer, DevOps/cloud et les métiers IA résistent ou progressent (Apec : data engineer +10 % en 2025 ; Indeed : paliers full stack et IA en hausse). Réponse à la question 3 : les métiers qui prolongent le développeur web sont le développeur full stack, l'ingénieur logiciel (software engineer), le tech lead à 5 ans, et de façon émergente l'AI software engineer.", bold=True)

    # ---- 4. régions ----
    doc.add_heading("4. Répartition régionale", 1)
    p(doc, "Excel, onglet REGIONS_METIERS (table T_REGIONS_METIERS, matrice T_MATRICE_REGIONS, données externes T_EXTERNES_REGIONS, stocks T_STOCKS_REGIONS).")
    rr = []
    for region, n in reg.most_common():
        rs = [r for r in U if r["REGION_NORMALISEE"] == region]
        c, _ = contract_counts(rs); s, _ = seniority_counts(rs); kss = sum(s.values())
        rr.append([region, n, f"{pct(n, len(U))} %", pct(c["ALTERNANCE"] + c["STAGE"], len(rs)), (pct(s["DEBUTANT"] + s["JUNIOR"], kss) if kss else NC), ia_share(rs)[0], " ; ".join(f"{m} ({k})" for m, k in Counter(r["METIER_NORMALISE"] for r in rs).most_common(2))])
    table(doc, ["Région", "Offres uniques", "Part échantillon", "Alternance + stage (%)", "Débutant + junior (% renseignées)", "Offres IA", "Métiers dominants"], rr, widths=[3.5, 1.6, 1.8, 2, 2.4, 1.4, 5.5], font_size=7.5)
    bullet(doc, "Repères externes : Apec compte 29 % des offres « développeur » en Île-de-France (2025) ; BMO 2026 place l'Île-de-France (388 806 projets tous métiers, numérique 15 492 projets dont 52,5 % difficiles), Auvergne-Rhône-Alpes (255 400), Nouvelle-Aquitaine (248 800), PACA (209 630) et Occitanie (200 470) en tête ; Apec prévoit pour 2026 environ 35 300 recrutements de cadres en Auvergne-Rhône-Alpes (+3 %), 19 500 en Occitanie (+6 %), 18 800 en PACA-Corse (+4 %), 17 340 dans les Hauts-de-France (+2 %), 15 400 en Pays de la Loire (+5 %) et 143 160 en Île-de-France (+5 %).", "France Travail BMO 2026 ; Apec prévisions régionales 2026", "https://www.francetravail.org/regions/ile-de-france/actualites/2026/enquete-bmo-2026-des-opportunites-dans-tous-les-secteurs.html?type=article")
    bullet(doc, "Stocks Indeed régionaux datés (bornes basses) : Occitanie « Développeur Web » plus de 400 (sept. 2024) puis plus de 200 (oct. 2025) ; Toulouse plus de 100 (juillet 2026) ; Rennes plus de 100 (juin 2026) ; Strasbourg plus de 75 à 100 (août-sept. 2026) ; Nancy plus de 100 (juin 2026) ; Montpellier plus de 75 (juillet 2026) ; Grenoble plus de 50 ; Nice plus de 50 ; Tours et Rouen plus de 25. Excel, T_STOCKS_REGIONS.")
    bullet(doc, "Télétravail : {} % des offres uniques de l'échantillon ({} offres) mentionnent dans leur titre ou extrait un télétravail total ou partiel (les extraits ne signalent pas l'absence de télétravail, la part réelle est donc supérieure) ; Indeed compte plus de 300 offres « Développeur Web Remote » (2 sept. 2026) et plus de 100 « Télétravail Développeur Full Stack » (29 mai 2026), soit environ un dixième du stock national : le marché à distance existe mais reste minoritaire et plutôt réservé aux profils expérimentés.".format(tel_s, tel_y))
    bullet(doc, "Limite : le ratio offres pour 100 000 actifs n'a pas pu être calculé, la population active régionale INSEE 2024-2025 n'étant pas lisible dans les extraits ; l'Excel fournit à défaut une ESTIMATION pour 100 000 habitants (population INSEE au 1er janvier 2021) pour l'Île-de-France, Auvergne-Rhône-Alpes, la Nouvelle-Aquitaine, l'Occitanie et les Hauts-de-France, calculée sur l'échantillon et non sur le marché total.")
    p(doc, f"Réponse à la question 7 : l'Île-de-France concentre entre un quart et un tiers de la demande nationale (29 % des offres Apec ; {pct(reg.get('Île-de-France', 0), len(U))} % de notre échantillon), suivie d'Auvergne-Rhône-Alpes (Lyon, Grenoble), d'Occitanie (Toulouse, Montpellier), des Hauts-de-France, de la Nouvelle-Aquitaine, des Pays de la Loire et de PACA. Les six campus NEXA couvrent les six premiers bassins hors Toulouse. Confiance MOYENNE (échantillon) à FORTE (BMO/Apec).", bold=True)

    # ---- 5. villes NEXA ----
    doc.add_heading("5. Analyse des villes NEXA", 1)
    p(doc, "Périmètres retenus : Île-de-France entière pour Paris ; département du Rhône pour Lyon ; Métropole européenne de Lille ; Bordeaux Métropole ; Nantes Métropole ; Aix-Marseille-Provence ; « marché national à distance » = offres en télétravail intégral. Excel, onglet VILLES_NEXA (table T_VILLES_NEXA et T_COMPARATIF_VILLES).")
    vr = []
    for z in NEXA_CITIES:
        rs = zones[z]
        c, _ = contract_counts(rs); kcz = sum(c.values()); s, _ = seniority_counts(rs); ksz = sum(s.values())
        salz = annual_salaries(rs)
        vr.append([z, len(rs), " ; ".join(f"{m} ({k})" for m, k in Counter(r["METIER_NORMALISE"] for r in rs).most_common(3)), (f"{pct(c['ALTERNANCE'] + c['STAGE'], kcz)} %" if kcz else NC), (f"{pct(s['DEBUTANT'] + s['JUNIOR'], ksz)} %" if ksz else NC), (f"{pct(s['SENIOR'] + s['LEAD_OU_ARCHITECTE'], ksz)} %" if ksz else NC), f"{ia_share(rs)[1]} %", (f"{median_or_nc(salz)} € (n={len(salz)})" if salz else NC)])
    table(doc, ["Ville NEXA", "Offres uniques", "Métiers dominants", "Alternance + stage", "Débutant + junior", "Senior + lead", "Mention IA", "Salaire médian affiché"], vr, widths=[3.2, 1.4, 5.5, 1.8, 1.8, 1.8, 1.5, 2.2], font_size=7.5)
    lect = {
        "Paris et Île-de-France": f"Marché le plus profond (Indeed « Développeur Web » plus de 900 offres actives à Paris au 4 septembre 2026 ; HelloWork « Développeur » plus de 1 700 en IDF en juillet 2026) et le plus exposé à l'IA : {pct(sum(1 for r in U if r['FAMILLE_METIER'] == IA and r['ZONE_NEXA'] == 'Paris et Île-de-France'), max(1, fam[IA]))} % des offres des métiers IA de l'échantillon y sont localisées ; stages et alternances abondants (Indeed « Stage Développeur Web » IDF plus de 800 en janvier 2025). Concurrence forte entre écoles ; les profils juniors doivent se différencier (industrialisation, IA appliquée).",
        "Lyon et métropole": "Deuxième bassin : Indeed « Développeur » 300 à 400 offres actives (mai-août 2026), « Développeur Web » plus de 200 (sept. 2025 et juillet 2026, stable), « Développeur Full Stack » plus de 100 ; tissu ESN + éditeurs + industrie ; peu de mentions IA dans les offres locales ; forte part d'alternance dans l'échantillon.",
        "Lille et métropole": "Bassin dynamique (retail/e-commerce, AdTech, ESN, stacks Java et .NET) ; offres citant explicitement Copilot/Cursor (Groupe M6 AdTech) ; alternance présente. Presse régionale : demande orientée vers développeurs expérimentés et leads.",
        "Bordeaux et métropole": "Bassin de taille moyenne : Indeed « Développeur Web » plus de 100 (août 2025 et juillet 2026, stable) ; mélange PHP/Laravel/Vue, .NET/React, Angular ; plusieurs offres senior ; alternance présente (CONVO, NLFL).",
        "Nantes et métropole": "Bassin ESN et éditeurs (Sopra Steria, Aubay, Edflex, Yuzu) : Indeed « Développeur » plus de 200 (oct. 2025), forte présence de postes de tech lead et DevOps (ESN) ; alternance bien représentée (WTTJ). Apec signale des tensions spécifiques informatique en Pays de la Loire.",
        "Marseille et Aix-en-Provence": "Bassin le plus petit des six : Indeed « Développeur » environ 100 offres actives (mars-août 2026), « Développeur Web » plus de 75 (sept. 2026), « Développeur Alternance » plus de 75 (avril 2026) ; très peu de mentions IA ; part d'alternance et de stages la plus élevée de l'échantillon. Le télétravail et le marché national à distance comptent davantage ici.",
        "Marché national à distance": "Offres en télétravail intégral : majoritairement full stack et back-end, profils expérimentés (part de seniors et leads la plus élevée) ; débouché réaliste seulement après une première expérience.",
    }
    for z in NEXA_CITIES:
        bullet(doc, f"{z} : {lect[z]}")
    p(doc, "Réponse à la question 12 (adaptations par campus) : socle commun identique sur les six campus, mais accent alternance et e-commerce/retail à Lille et Nantes, industrialisation et ESN à Lyon, IA appliquée et scale-ups à Paris, préparation au marché à distance et à la mobilité à Marseille-Aix et Bordeaux, où le volume local reste limité. Confiance MOYENNE (échantillon de {} à {} offres par ville).".format(min(len(v) for v in zones.values()), max(len(v) for v in zones.values())), bold=True)

    # ---- 6. contrats et séniorité ----
    doc.add_heading("6. Contrats et séniorité", 1)
    p(doc, f"Sur les {kc} offres uniques dont le contrat est renseigné : CDI {pct(contrats['CDI'], kc)} %, alternance {pct(contrats['ALTERNANCE'], kc)} %, stage {pct(contrats['STAGE'], kc)} %, freelance {pct(contrats['FREELANCE'], kc)} %, CDD {pct(contrats['CDD'], kc)} %. Sur les {ks} offres dont la séniorité est déterminable (expérience demandée ou contrat stage/alternance) : DEBUTANT {pct(sen['DEBUTANT'], ks)} %, JUNIOR {pct(sen['JUNIOR'], ks)} %, INTERMEDIAIRE {pct(sen['INTERMEDIAIRE'], ks)} %, SENIOR {pct(sen['SENIOR'], ks)} %, LEAD/ARCHITECTE {pct(sen['LEAD_OU_ARCHITECTE'], ks)} %. Les offres DEBUTANT sont à {pct(deb_alt, sen['DEBUTANT']) if sen['DEBUTANT'] else 0} % des stages ou alternances ; seules {deb_cdi} offres débutant/junior en CDI ont été observées. Excel, SYNTHESE_METIERS (colonnes CDI…LEAD_ARCHITECTE) et OFFRES_DETAILLEES (SENIORITE, SENIORITE_ORIGINE).")
    bullet(doc, "Apec : 21 % des offres « développeur » de 2025 visent des profils débutants ; les recrutements de cadres débutants (moins d'un an) ont reculé de 19 % en 2024 et de 16 % attendus en 2025 ; 70 % des Bac+5 de la promotion 2024 étaient en emploi salarié douze mois après (-2 pts), avec un recul « particulièrement marqué » en informatique.", "Apec 2025-2026", "https://corporate.apec.fr/home/nos-etudes/toutes-nos-etudes/les-metiers-cadres-porteurs-edition-2026.html")
    bullet(doc, "Numeum : 33 % des ESN ont réduit leurs recrutements de jeunes diplômés au 1er semestre 2026 ; 40 % recrutent moins de profils juniors (alternants et reconvertis inclus) ; 59 % privilégient la formation à l'embauche ; l'emploi des moins de 30 ans dans l'informatique a reculé de 3 % entre 2023 et 2025.", "Numeum S1 2026 ; Blog du Modérateur", "https://www.blogdumoderateur.com/emploi-numerique-loin-job-apocalypse-promet/")
    bullet(doc, "Presse et cabinets : « profils 5 à 10 ans d'expérience très recherchés » (Le Monde Informatique) ; pénurie structurelle de développeurs seniors (8 ans et plus) signalée par les baromètres freelance ; Indeed compte plus de 100 offres « Développeur Web Junior » actives en France (3 sept. 2026) contre plus de 3 000 « Développeur Web » : environ 3 % des offres portent le mot junior dans leur intitulé.", "Le Monde Informatique ; pages Indeed", "https://www.lemondeinformatique.fr/actualites/lire-l-emploi-it-devrait-rebondir-en-france-en-2026-98522.html")
    bullet(doc, "Freelance : TJM médian développeur 525 €/jour (TJMètre), full stack 413 € en direct et 433 € via intermédiaire (Free-Work, juin 2026) ; IA 750-1 500 €, cybersécurité 700-1 200 €, architecture cloud 650-1 100 € ; Île-de-France environ 613 €/j, régions 15 à 30 % en dessous. Le freelance reste un marché de profils confirmés.", "Free-Work / TJMètre / Extra Dev 2026", "https://extradev.fr/blog/tjm-developpeur-freelance-vrais-tarifs-2026-techno-seniorite")
    cross = []
    for s_lvl in SENIORITES:
        rs_s = [r for r in U if r["SENIORITE"] == s_lvl]
        cc, _ = contract_counts(rs_s)
        cross.append([s_lvl, len(rs_s), cc["CDI"], cc["CDD"], cc["ALTERNANCE"], cc["STAGE"], cc["FREELANCE"], sum(1 for r in rs_s if r["TYPE_CONTRAT_NORMALISE"] == NC)])
    p(doc, "Croisement séniorité × contrat (offres uniques de l'échantillon, séniorité déterminée par l'expérience demandée ou par le contrat stage/alternance) — Excel, OFFRES_DETAILLEES :", italic=True)
    table(doc, ["Séniorité", "Offres", "CDI", "CDD", "Alternance", "Stage", "Freelance", "Contrat NC"], cross, widths=[3.2, 1.6, 1.4, 1.4, 1.8, 1.4, 1.8, 1.8])
    p(doc, "Réponses aux questions 4, 5 et 6 : les entreprises recrutent encore des juniors, mais surtout en alternance et en stage (dans l'échantillon, l'alternance et le stage représentent {} % des contrats renseignés et la quasi-totalité des offres débutant) ; le CDI direct pour débutant est rare et concentré dans les ESN et les PME ; la demande en CDI se concentre sur les profils intermédiaires et seniors (3 ans et plus) ; le freelance et les missions courtes concernent les profils confirmés. Confiance FORTE sur la tendance (Apec, Numeum convergents), MOYENNE sur les proportions (échantillon).".format(alt_share), bold=True)

    # ---- 7. salaires ----
    doc.add_heading("7. Salaires", 1)
    sal_rows_u = sorted([r for r in U if r.get("SALAIRE_MEDIAN_OFFRE") and r.get("SALAIRE_UNITE") == "ANNUEL"], key=lambda r: r["SALAIRE_MEDIAN_OFFRE"])
    lo, hi = sal_rows_u[0], sal_rows_u[-1]
    mens = [r for r in U if r.get("SALAIRE_UNITE") == "MENSUEL" and r.get("SALAIRE_MIN_NUM")]
    p(doc, f"Salaires affichés dans les offres collectées (SALAIRE_AFFICHE_DANS_OFFRE) : {len(sal)} offres uniques avec une fourchette annuelle ; médiane {median_or_nc(sal)} € brut/an, quartile bas {q_or_nc(sal, 0)} €, quartile haut {q_or_nc(sal, 2)} € ; fourchettes observées de {round(lo['SALAIRE_MIN_NUM'])} € ({lo['INTITULE_BRUT'][:50]}, {lo['VILLE_NORMALISEE']}) à {round(hi['SALAIRE_MAX_NUM'])} € ({hi['INTITULE_BRUT'][:50]}, {hi['VILLE_NORMALISEE']}) ; {len(mens)} offres (alternances) affichent un salaire mensuel de {round(min(r['SALAIRE_MIN_NUM'] for r in mens)) if mens else NC} à {round(max(r['SALAIRE_MAX_NUM'] for r in mens)) if mens else NC} €/mois. Effectif faible : à lire comme des ordres de grandeur. Excel, OFFRES_DETAILLEES (SALAIRE_MIN_NUM, SALAIRE_MAX_NUM).")
    def sal_stats(rs_):
        v = annual_salaries(rs_)
        return [len(v), (f"{median_or_nc(v)} €" if v else NC), (f"{q_or_nc(v, 0)} €" if len(v) >= 4 else NC), (f"{q_or_nc(v, 2)} €" if len(v) >= 4 else NC), (f"{round(min(v))} – {round(max(v))} €" if v else NC)]
    srows = [[s_lvl] + sal_stats([r for r in U if r["SENIORITE"] == s_lvl]) for s_lvl in SENIORITES]
    srows.append(["Séniorité non renseignée"] + sal_stats([r for r in U if r["SENIORITE"] == NC]))
    p(doc, "Salaires annuels bruts affichés dans les offres, par séniorité (SALAIRE_AFFICHE_DANS_OFFRE ; médiane de la fourchette de chaque offre) :", italic=True)
    table(doc, ["Séniorité", "Offres renseignées", "Médiane", "Quartile bas", "Quartile haut", "Fourchette observée"], srows, widths=[3.5, 2, 2, 2, 2, 3.5])
    zrows = [[z] + sal_stats(zones[z]) for z in NEXA_CITIES] + [["Hors villes NEXA"] + sal_stats([r for r in U if r["ZONE_NEXA"] == "Hors villes NEXA"])]
    p(doc, "Salaires annuels bruts affichés, par zone NEXA (échantillon) :", italic=True)
    table(doc, ["Zone", "Offres renseignées", "Médiane", "Quartile bas", "Quartile haut", "Fourchette observée"], zrows, widths=[3.5, 2, 2, 2, 2, 3.5])
    mrows = []
    for m_, n_ in met.most_common(14):
        st_ = sal_stats([r for r in U if r["METIER_NORMALISE"] == m_])
        if st_[0] >= 3:
            mrows.append([m_] + st_)
    if mrows:
        p(doc, "Salaires annuels bruts affichés, par métier normalisé (au moins 3 offres renseignées) :", italic=True)
        table(doc, ["Métier", "Offres renseignées", "Médiane", "Quartile bas", "Quartile haut", "Fourchette observée"], mrows, widths=[4.5, 2, 2, 2, 2, 3.5])
    sal_rows = []
    for s_ in salaires:
        sal_rows.append([s_.get("METIER"), s_.get("SENIORITE"), s_.get("ZONE"), s_.get("MEDIANE") or NC, s_.get("FOURCHETTE") or NC, s_.get("TYPE"), f"{s_.get('SOURCE')} ({s_.get('DATE')})"])
    table(doc, ["Métier", "Séniorité", "Zone", "Médiane", "Fourchette", "Type", "Source (date)"], sal_rows[:32], widths=[3, 2, 2, 1.6, 4, 3, 3.5], font_size=7)
    bullet(doc, "Convergence des sources déclaratives (SALAIRE_ISSU_D_ETUDE) : médiane nationale développeur web autour de 40 000 € brut/an (Talent.com 40 000 ; WeLoveDevs 40 000 ; Glassdoor 39 450, P25 33 000 / P75 46 000) ; Paris autour de 44 000 € (+10 à 15 %) ; métropoles régionales 38 000-40 000 € ; junior 30 000-35 000 € ; senior 5 ans et plus 55 000-75 000 € à Paris ; Apec : développeurs cadres 34 000-53 000 € (moyenne 43 000 €).", "voir tableau et sources")
    bullet(doc, "Estimations de cabinets (ESTIMATION_DE_CABINET : Robert Half, Michael Page, Hays, Silkhom) : salaires des développeurs « classiques » stables ou en légère baisse en 2026 (Silkhom Java/Python -1,1 %) ; hausses réservées à la cybersécurité, au cloud, à la data et à l'IA ; grilles de cabinets parisiens (junior 38-48 k€, senior 65-85 k€) nettement au-dessus des médianes déclaratives : à ne pas utiliser comme promesse.")
    bullet(doc, "Contradictions relevées : Talent.com donne 33 000 € pour le full stack France contre 42 000-44 000 € pour Indeed Lyon/Lille ; l'écart Paris/régions varie de -10 % à -20 % (Michael Page, Bureau des Talents) à +45 % (Salaire-Métier) selon les sources ; retenir 10 à 20 %.")

    # ---- 8. compétences ----
    doc.add_heading("8. Compétences demandées", 1)
    p(doc, f"Fréquence dans les extraits des {len(U)} offres uniques (sous-estimation, les extraits ne reprennent pas toute l'annonce) : " + " ; ".join(f"{s_} ({n}, {pct(n, len(U))} %)" for s_, n in skills_top) + ". Excel, onglet COMPETENCES_ET_IA, table T_COMPETENCES.")
    fams = defaultdict(Counter)
    for r in U:
        for f_, items in r.get("_skills", {}).items():
            for it in items:
                fams[f_][it] += 1
    table(doc, ["Famille", "Compétences les plus citées (offres)", "Statut marché", "Place dans le cursus (proposition)"], [
        ["Langages", " ; ".join(f"{k} ({v})" for k, v in fams["LANGAGES"].most_common(6)), "DEJA_DEMANDEE", "Socle Bachelor obligatoire (JS/TS + PHP ou Java ou Python + SQL)"],
        ["Front-end", " ; ".join(f"{k} ({v})" for k, v in fams["FRONT_END"].most_common(5)), "DEJA_DEMANDEE (React dominant)", "Obligatoire : React + TypeScript, un second framework en option"],
        ["Back-end", " ; ".join(f"{k} ({v})" for k, v in fams["BACK_END"].most_common(6)), "DEJA_DEMANDEE", "Obligatoire : Node/Nest ou Symfony/Laravel, découverte Spring/.NET"],
        ["Bases de données", " ; ".join(f"{k} ({v})" for k, v in fams["BASES_DE_DONNEES"].most_common(5)), "DEJA_DEMANDEE", "Obligatoire : PostgreSQL/MySQL, notions NoSQL"],
        ["API et microservices", " ; ".join(f"{k} ({v})" for k, v in fams["API_ET_MICROSERVICES"].most_common(4)), "DEJA_DEMANDEE", "Obligatoire : REST ; microservices en Mastère"],
        ["Cloud", " ; ".join(f"{k} ({v})" for k, v in fams["CLOUD"].most_common(5)), "DEJA_DEMANDEE / EMERGENTE", "Bachelor 3e année : déploiement AWS/Azure/GCP ; Mastère : architecture cloud"],
        ["DevOps, CI/CD, conteneurs", " ; ".join(f"{k} ({v})" for k, v in (fams["DEVOPS_ET_CI_CD"] + fams["CONTENEURS"]).most_common(6)), "DEJA_DEMANDEE", "Obligatoire : Git, CI/CD, Docker ; Kubernetes en Mastère"],
        ["Tests et qualité", " ; ".join(f"{k} ({v})" for k, v in fams["TEST_ET_QUALITE"].most_common(4)), "EMERGENTE / RARE_MAIS_STRATEGIQUE", "À renforcer dès la 2e année (tests unitaires, E2E, revue de code)"],
        ["Sécurité", " ; ".join(f"{k} ({v})" for k, v in fams["CYBERSECURITE"].most_common(3)) or "0", "RARE_MAIS_STRATEGIQUE", "OWASP et authentification en Bachelor ; AppSec en Mastère (passerelle Cybersécurité)"],
        ["Architecture", " ; ".join(f"{k} ({v})" for k, v in fams["ARCHITECTURE"].most_common(3)) or "0", "DEJA_DEMANDEE (seniors)", "Mastère"],
        ["Méthodes / projet", " ; ".join(f"{k} ({v})" for k, v in fams["GESTION_DE_PROJET"].most_common(3)), "DEJA_DEMANDEE", "Transversal (projets, alternance)"],
        ["Anglais", f"Anglais ({fams['ANGLAIS'].get('Anglais', 0)})", "DEJA_DEMANDEE", "Transversal"],
    ], widths=[3, 6, 3.2, 5], font_size=7.5)
    ext_comp = [c for c in comps if c.get("VALEUR")]
    if ext_comp:
        bullet(doc, "Repères externes : React/Next.js domine le front (70-75 % des offres front selon les comparatifs 2026, fiabilité MOYENNE), Vue 20-25 %, Angular 15-20 % ; Java Spring reste le premier volume back en ESN (Indeed « développeur Java Spring » 860 offres au 29/06/2026) devant PHP/Symfony ; Python et JavaScript/TypeScript sont les premiers langages en volume freelance (Free-Work) ; cybersécurité, Rust/Go et Kubernetes sont les compétences les mieux valorisées (Robert Half). Excel, T_EXTERNES_COMPETENCES.")
    p(doc, "Réponse à la question 8 : les compétences les plus demandées restent JavaScript/TypeScript, React, Node.js, PHP/Symfony, Java/Spring, SQL/PostgreSQL et Git, mais l'exigence a monté d'un cran sur l'industrialisation (tests, CI/CD, Docker, cloud) et sur l'architecture. Confiance FORTE.", bold=True)

    # ---- 9. IA ----
    doc.add_heading("9. Transformation liée à l'IA", 1)
    bullet(doc, "Indeed Hiring Lab France : 21 % des annonces de développement logiciel contiennent des termes liés à l'IA (avril 2026), contre 3,1 % de l'ensemble des offres françaises (octobre 2025) ; les offres mentionnant l'IA progressent à contre-courant d'un marché en recul ; la France reste le pays où la part d'offres mentionnant l'IA est la plus faible (3,4 %).", "Indeed Hiring Lab, 10/12/2025 et 01/04/2026", "https://hiringlab.indeed.com/fr/blog/2025/12/10/le-marche-de-lemploi-en-2026-en-pleine-mutation-face-aux-nouveaux-equilibres-economiques/")
    bullet(doc, f"Échantillon collecté : {ia_n} offres uniques ({ia_s} %) mentionnent explicitement l'IA ; parmi les offres de développeur web/full stack/logiciel « classiques » (hors métiers IA), {len(core_ia)} sur {len(core)} ({pct(len(core_ia), len(core))} %) citent l'IA ; outils de codage IA cités : " + (" ; ".join(f"{k} ({v})" for k, v in tools.most_common()) or "aucun") + ". Stocks Indeed : « Développeur Intelligence Artificielle » plus de 600 (05/09/2026), « Développeur LLM » plus de 200 (04/09/2026), « Claude Code » plus de 200 (21/08/2026), « Full Stack JS Intelligence Artificielle » plus de 100 (02/09/2026). Excel, COMPETENCES_ET_IA, table T_DEV_AUGMENTE.")
    bullet(doc, "Numeum : l'impact direct de l'IA sur les effectifs reste limité ; l'IA modifie d'abord les métiers, les compétences et l'organisation ; gains de productivité attendus chez les ESN de 15 % à 22 % entre 2025 et 2027 ; l'IA se substitue à des tâches confiées aux débutants (code de base, rédaction, analyse de premier niveau), d'où une sélectivité accrue : « le secteur recrute des gens qui savent déjà livrer ».", "Numeum S1 2026 ; Blog du Modérateur", "https://numeum.fr/etude-le-marche-du-numerique-francais-sort-de-la-zone-de-turbulences-mais-lattentisme-freine-encore-la-reprise/")
    bullet(doc, "International (éclairage, pas de conclusion France) : 84 % des développeurs utilisent ou prévoient d'utiliser des outils IA, 51 % quotidiennement, mais 46 % se méfient de leur exactitude et 45 % estiment que déboguer du code généré prend plus de temps que l'écrire ; Indeed Hiring Lab (juillet 2026) observe un rebond de la part des offres de développement logiciel dans la plupart des grandes économies, porté par des rôles mentionnant l'IA.", "Stack Overflow 2025 ; Indeed Hiring Lab 08/07/2026", "https://survey.stackoverflow.co/2025/ai")
    p(doc, "Réponse à la question 9 : les données françaises ne montrent pas une substitution des développeurs par l'IA mais une transformation du métier (un cinquième des annonces de développement citent l'IA, contre 3 % tous métiers) et un relèvement du niveau d'entrée : les tâches simples et répétitives des débutants sont les premières automatisées, la valeur se déplace vers la conception, le contrôle, les tests, la sécurité et l'intégration. Confiance MOYENNE à FORTE.", bold=True)

    # ---- 10. développeur augmenté ----
    doc.add_heading("10. Réalité du « développeur augmenté par l'IA »", 1)
    tool_rows = [r for r in core if r["OUTIL_CODAGE_IA_CITE"] != "Non"]
    ex_tools = " ; ".join(f"{(r['ENTREPRISE'] if not is_nc(r['ENTREPRISE']) else r['SOURCE'])} ({r['VILLE_NORMALISEE'] if not is_nc(r['VILLE_NORMALISEE']) else 'ville NC'} : {r['OUTIL_CODAGE_IA_CITE']})" for r in tool_rows[:8]) or "aucune"
    p(doc, f"Le terme « développeur augmenté » n'apparaît dans aucune offre collectée. En revanche trois signaux observables existent : (1) des offres de développeur web/full stack/logiciel « classiques » qui citent l'IA : {len(core_ia)} dans l'échantillon ({pct(len(core_ia), len(core))} % des offres cœur de marché et évolutions), dont {len(tool_rows)} exigent ou mentionnent explicitement un assistant de code (Copilot, Cursor, Claude Code, ChatGPT, Codex, développement assisté par IA), par exemple {ex_tools} ; (2) une famille de métiers émergents (AI Engineer, AI Software Engineer, LLM/GenAI Engineer, développeur RAG/agents) qui représente {fam[IA]} offres uniques, presque toutes à Paris et pour des profils expérimentés ; (3) le chiffre Indeed de 21 % d'annonces de développement logiciel mentionnant l'IA, qui inclut aussi bien l'usage d'outils que le développement de fonctionnalités IA.")
    p(doc, "Conclusion (H7) : PARTIELLEMENT_CONFIRMEE. Le besoin observable n'est pas un métier « développeur augmenté » mais un développeur full stack industrialisé qui sait utiliser, intégrer et contrôler l'IA. Le positionnement marketing « développeur augmenté par l'IA » est défendable comme promesse pédagogique, pas comme intitulé de poste ; il doit s'appuyer sur des compétences vérifiables (tests, revue de code, intégration d'API de modèles, RAG, sécurité) et non sur quelques mentions isolées.", bold=True)

    # ---- 11. implications pédagogiques ----
    doc.add_heading("11. Implications pédagogiques et référentiel cible", 1)
    p(doc, "Les programmes NEXA n'ayant pas été fournis, il ne s'agit pas d'un audit des contenus existants mais d'un référentiel cible construit à partir des fréquences observées (Excel, table T_REFERENTIEL_AUGMENTE et colonne PERTINENCE_NEXA de T_COMPETENCES).")
    table(doc, ["Question", "Réponse fondée sur les résultats"], [
        ["Faut-il conserver la formation généraliste ?", "Oui pour le socle (langages, front, back, SQL, Git), non pour l'intitulé et la promesse : le marché ne recrute plus « un développeur web » mais un full stack capable de déployer et de tester."],
        ["Faut-il la repositionner vers le full stack ?", f"Oui : {pct(met.get('Développeur full stack', 0), len(U))} % des offres uniques de l'échantillon portent l'intitulé full stack, contre {pct(met.get('Développeur web (intitulé générique)', 0), len(U))} % « développeur web » ; le stock Indeed full stack progresse quand celui de « développeur web » recule."],
        ["Faut-il intégrer l'IA comme compétence transversale ?", "Oui, dès la première année : usage raisonné des assistants de code avec revue et tests, puis intégration d'API de modèles et RAG en 3e année."],
        ["Faut-il créer un parcours « développeur augmenté par l'IA » ?", "Pas comme filière Bachelor autonome (aucun intitulé de poste, offres rares et seniors) ; oui comme spécialisation de Mastère « IA applicative » et comme fil rouge de la communication."],
        ["Compétences fondamentales à garder obligatoires", "JavaScript/TypeScript, React, Node ou PHP/Symfony (ou Java/Spring), SQL/PostgreSQL, API REST, Git, HTML/CSS, algorithmique, anglais."],
        ["Compétences à ajouter ou renforcer", "Tests unitaires et E2E, CI/CD, Docker, déploiement cloud, sécurité applicative (OWASP), observabilité, architecture, intégration IA (API de modèles, RAG, agents, MCP), évaluation et contrôle des sorties IA."],
        ["Faut-il renforcer l'offre M1/M2 ?", "Oui : la demande se concentre sur les profils intermédiaires et seniors et sur des spécialisations (cloud/DevOps, sécurité, IA applicative, architecture) inaccessibles à Bac+3 ; l'alternance en M1/M2 est le principal canal d'accès des juniors."],
        ["Spécialisations à proposer en Mastère", "1) Architecture et industrialisation (cloud, DevOps, SRE) ; 2) IA applicative (LLM, RAG, agents, évaluation) ; 3) Sécurité applicative et DevSecOps (passerelle Cybersécurité) ; 4) Pilotage technique et produit (tech lead)."],
        ["Compétences à enseigner dès le Bachelor", "Socle ci-dessus + Git/CI/CD + tests + Docker + un premier déploiement cloud + usage contrôlé des assistants IA + projet en équipe agile."],
        ["Place du cloud, DevOps, test, sécurité, architecture", "Initiation obligatoire en Bachelor (3e année), approfondissement et certification en Mastère."],
        ["Adaptations par campus", "Voir section 5 : alternance e-commerce/retail à Lille et Nantes, ESN/industrie à Lyon, IA/scale-ups à Paris, mobilité et marché à distance à Marseille-Aix et Bordeaux."],
        ["Métiers à mettre en avant dans la communication", "Développeur full stack, software engineer, développeur front-end React/TypeScript, développeur back-end Node/Symfony/Java, puis (Mastère) DevOps/cloud engineer, AI software engineer, tech lead, architecte. Éviter « développeur web » et « intégrateur web » seuls, en recul."],
    ], widths=[5, 12], font_size=8)
    p(doc, "Gap analysis : sans programme fourni, le tableau ci-dessus vaut référentiel cible ; l'Excel (COMPETENCES_ET_IA) donne pour chaque compétence sa fréquence, sa maturité et sa pertinence NEXA, à confronter aux maquettes existantes pour compléter les colonnes PRESENTE_CHEZ_NEXA, NIVEAU_ACTUEL, NIVEAU_REQUIS et ECART.", italic=True)

    # ---- 12. scénarios ----
    doc.add_heading("12. Scénarios", 1)
    table(doc, ["Critère", "SCÉNARIO A — MAINTIEN", "SCÉNARIO B — TRANSFORMATION", "SCÉNARIO C — MONTÉE EN GAMME (M1/M2)"], [
        ["JUSTIFICATION", "Le cœur de marché existe encore (plus de 3 000 offres « développeur web » actives sur Indeed, 12 690 offres cadres Apec en 2025).", "Le marché a basculé vers le full stack industrialisé et l'IA intégrée ; les intitulés génériques et les débutants non outillés reculent.", "La demande se concentre sur les profils intermédiaires/seniors et sur des spécialisations (cloud, sécurité, IA, architecture) ; l'alternance M1/M2 est la porte d'entrée réaliste."],
        ["PUBLIC_CIBLE", "Bacheliers, reconversions", "Bacheliers, reconversions, alternants Bac+2/3", "Diplômés Bac+3 (NEXA et externes), alternants, salariés en évolution"],
        ["METIERS_VISES", "Développeur web, intégrateur, front, back", "Développeur full stack, front-end React/TS, back-end Node/Symfony/Java, développeur logiciel", "Software engineer, DevOps/cloud engineer, AI software engineer, AppSec, architecte, tech lead"],
        ["COMPETENCES", "Socle actuel", "Socle + tests, CI/CD, Docker, cloud, sécurité de base, assistants IA contrôlés, API de modèles", "Architecture, cloud/DevOps, IA applicative (LLM, RAG, agents), sécurité applicative, industrialisation, produit, pilotage technique"],
        ["POTENTIEL_NATIONAL", "En recul : stock « développeur web » -25 % de palier 2025-2026, offres cadres -20 %", f"Stable à croissant : full stack premier intitulé ({pct(met.get('Développeur full stack', 0), len(U))} % de l'échantillon), stock Indeed en hausse", "Croissant : cloud/cyber/IA en tension (BMO 49,5 % de projets difficiles, Apec +5 % activités informatiques 2026)"],
        ["POTENTIEL_PAR_VILLE", "Paris fort ; Lyon, Lille moyen ; Bordeaux, Nantes, Marseille faible à moyen", "Fort à Paris et Lyon, moyen à Lille, Nantes, Bordeaux, plus limité à Marseille-Aix (compenser par le marché à distance)", "Fort à Paris (IA, scale-ups), moyen à Lyon et Lille (ESN, industrie), à construire ailleurs via l'alternance et le distanciel"],
        ["AVANTAGES", "Coût nul, continuité", "Alignement avec les intitulés réels, meilleure employabilité en alternance, différenciation crédible", "Réponse à la demande de seniorité, revenus par étudiant plus élevés, passerelles avec les filières IA & Data et Cybersécurité"],
        ["RISQUES", "Baisse continue de l'attractivité et de l'insertion ; promesse en décalage avec le marché", "Effort de refonte, besoin de formateurs à jour sur DevOps/IA, risque de dilution si trop large", "Investissement pédagogique lourd, concurrence des écoles d'ingénieurs et des Mastères IA, risque de sous-effectif en M1 la première année"],
        ["EFFORT_PEDAGOGIQUE", "Faible", "Moyen (refonte de 30 à 40 % des modules, projets industrialisés)", "Élevé (nouvelles maquettes, intervenants experts, partenariats ESN/éditeurs)"],
        ["DIFFERENCIATION", "Faible", "Moyenne à forte (« full stack industrialisé et augmenté par l'IA »)", "Forte (Mastère orienté architecture, IA applicative, sécurité, industrialisation)"],
        ["RECOMMANDATION", "NON RETENU seul", "RETENU (socle Bachelor)", "RETENU (en continuité du Bachelor transformé)"],
    ], widths=[2.6, 4.6, 4.9, 4.9], font_size=7.5)

    # ---- 13. recommandation ----
    doc.add_heading("13. Recommandation finale", 1)
    p(doc, "Décision recommandée : TRANSFORMEE (scénario B) et RENFORCEE_EN_MASTERE (scénario C), l'IA étant intégrée comme compétence transversale plutôt que comme repositionnement exclusif ; la filière n'est ni maintenue en l'état ni abandonnée.", bold=True)
    for txt in [
        "Renommer et repositionner le Bachelor : « Développeur full stack » (ou « Développement logiciel et web »), avec un socle JavaScript/TypeScript-React-Node ou PHP/Symfony, SQL, API, Git, complété dès la 2e année par les tests, la CI/CD, Docker et un premier déploiement cloud, et par l'usage contrôlé des assistants de code (Copilot, Cursor, Claude Code) évalué sur la qualité du code livré.",
        "Faire de l'alternance le canal principal d'insertion à partir de la 2e année : c'est là que se trouvent les offres accessibles aux débutants (dans l'échantillon, la quasi-totalité des offres DEBUTANT sont des stages ou alternances ; Apec : 21 % d'offres développeur pour débutants).",
        "Créer ou renforcer un Mastère en deux ans avec quatre majeures : Architecture et cloud/DevOps ; IA applicative (LLM, RAG, agents, MCP, évaluation) ; Sécurité applicative et DevSecOps (passerelle avec la filière Cybersécurité) ; Pilotage technique et produit. Ces majeures correspondent aux familles en tension identifiées par Apec, BMO et les baromètres freelance.",
        "Communiquer sur des intitulés que le marché utilise réellement (full stack, software engineer, DevOps, AI software engineer, tech lead) et sur des preuves (projets industrialisés, portefeuille GitHub, certifications cloud), plutôt que sur le seul slogan « développeur augmenté ».",
        "Adapter par campus : Paris (IA appliquée, scale-ups, volume), Lyon (ESN, industrie, industrialisation), Lille et Nantes (alternance, retail/e-commerce, éditeurs), Bordeaux et Marseille-Aix (mobilité, marché à distance, partenariats ESN locaux).",
        "Mettre en place un observatoire semestriel (même méthode, mêmes pages de stocks datées, mêmes études Apec/BMO/Dares/Indeed) pour suivre le rebond annoncé pour 2026 et ajuster les effectifs de M1 en conséquence ; la première mesure de contrôle est le stock Indeed « Développeur Web » au 1er janvier 2027 par rapport à « plus de 3 000 » en septembre 2026.",
    ]:
        bullet(doc, txt)

    # ---- 14. hypothèses ----
    doc.add_heading("14. Test des hypothèses", 1)
    H = [
        ["H1. La demande de développeurs web diminue réellement.", "CONFIRMEE (sur le flux d'offres 2023-2025)", "Apec -20 % en 2025 et -60 % vs 2022 ; Indeed volume ÷2 depuis déc. 2022 ; Dares sortie de la tension très forte ; stock Indeed « développeur web » de plus de 4 000 à plus de 3 000.", "Apec 2026 ; Indeed Hiring Lab 04/2026 ; Dares 02/2026", "Emploi total quasi stable (Numeum -1,8 % sur 2 ans) ; prévisions Apec +4 % en 2026 ; palier full stack en hausse.", "FORTE", "Ne pas communiquer sur un marché « en pénurie » ; sécuriser l'insertion par l'alternance et la spécialisation."],
        ["H2. La demande se déplace vers le full stack, le software engineering, le cloud, le DevOps, la sécurité ou la data.", "CONFIRMEE", f"Full stack = {pct(met.get('Développeur full stack', 0), len(U))} % de l'échantillon ; Indeed « Développeur Full Stack » plus de 500 (08/2025) → plus de 800 (09/2026) ; Apec data engineer +10 % ; BMO numérique 49,5 % de projets difficiles ; cabinets : hausses réservées à cloud/cyber/data/IA.", "collecte ; Apec ; BMO 2026 ; Robert Half", "Le déplacement vers la sécurité et la data est documenté par les études plus que par l'échantillon (peu d'offres AppSec observées).", "FORTE", "Repositionner le Bachelor sur le full stack industrialisé ; spécialisations en Mastère."],
        ["H3. Les entreprises recrutent moins de juniors et davantage de profils expérimentés.", "CONFIRMEE", f"Apec débutants -19 % (2024), -16 % (2025) ; Numeum 33 % des ESN réduisent les jeunes diplômés ; échantillon : seniors + leads = {senior_share} % des offres à séniorité renseignée, {deb_cdi} offres débutant/junior en CDI.", "Apec ; Numeum S1 2026 ; collecte", "21 % des offres Apec développeur restent ouvertes aux débutants ; Indeed « Développeur Web Junior » plus de 100 offres actives.", "FORTE", "Renforcer l'alternance et le niveau de sortie ; offre M1/M2."],
        ["H4. Les opportunités juniors se concentrent sur l'alternance, les stages ou certains secteurs.", "CONFIRMEE", f"Dans l'échantillon, {pct(deb_alt, sen['DEBUTANT']) if sen['DEBUTANT'] else 0} % des offres DEBUTANT sont des stages/alternances ; Indeed « Stage Développeur Web » IDF plus de 800 (01/2025) ; secteurs : ESN, agences, e-commerce, médias.", "collecte ; pages Indeed", "Quelques CDI juniors en ESN et PME régionales (Astek Lyon, Ouidou Lille…).", "MOYENNE (échantillon) / FORTE (tendance)", "Alternance dès la 2e année ; partenariats ESN et e-commerce."],
        ["H5. L'IA réduit les besoins sur les tâches simples et répétitives.", "PARTIELLEMENT_CONFIRMEE", "Numeum : l'IA se substitue aux tâches de débutants, gains de productivité 15-22 % attendus ; Stack Overflow : 84 % d'usage ; recul des intitulés « intégrateur web » et « développeur web » génériques.", "Numeum S1 2026 ; Blog du Modérateur ; Stack Overflow 2025 (international)", "Aucune source française ne mesure directement une réduction d'emplois due à l'IA ; Numeum juge l'impact direct « limité » ; le recul 2023-2025 est d'abord conjoncturel.", "MOYENNE", "Supprimer les modules purement « intégration HTML/CSS » au profit des tests, du déploiement et de l'IA contrôlée."],
        ["H6. L'IA augmente la valeur des développeurs capables de concevoir, contrôler, tester, sécuriser et intégrer.", "CONFIRMEE", "Cabinets : primes salariales réservées à IA/cloud/cyber ; TJM IA 750-1 500 € vs 413-525 € développeur ; offres AI engineer seniors (60-80 k€) ; compétences tests/CI/CD/cloud parmi les plus citées.", "Free-Work/TJMètre 2026 ; Robert Half ; collecte", "Les mentions explicites de « contrôle des sorties IA » restent rares dans les offres.", "MOYENNE à FORTE", "Axer le Mastère sur architecture, qualité, sécurité et intégration IA."],
        ["H7. Le positionnement « développeur augmenté par l'IA » possède une réalité observable dans les offres françaises.", "PARTIELLEMENT_CONFIRMEE", f"{len(core_ia)} offres cœur de marché ({pct(len(core_ia), len(core))} %) citent un outil ou une compétence IA ; Indeed : 21 % des annonces de développement logiciel mentionnent l'IA ; stocks « Claude Code » plus de 200, « Full Stack JS IA » plus de 100.", "collecte ; Indeed Hiring Lab 04/2026", "Le terme « développeur augmenté » n'apparaît dans aucune offre ; les métiers IA sont seniors et parisiens.", "MOYENNE", "Promesse pédagogique et argument de différenciation, pas intitulé de diplôme."],
        ["H8. Le besoin existe, mais les entreprises utilisent d'autres intitulés.", "CONFIRMEE", f"« Développeur web » = {pct(met.get('Développeur web (intitulé générique)', 0), len(U))} % de l'échantillon contre {pct(met.get('Développeur full stack', 0), len(U))} % full stack ; Indeed « Ingénieur Logiciel » plus de 4 000, « Développeur » plus de 3 000, « Software Engineer » plus de 1 000 ; HelloWork « Développeur informatique » plus de 9 650.", "collecte ; pages Indeed/HelloWork", "Une partie de ces intitulés couvre du logiciel non web (embarqué, ERP).", "FORTE", "Aligner les intitulés de formation et de communication sur full stack / software engineer."],
        ["H9. Une offre M1/M2 répondrait mieux à certains besoins qu'une formation généraliste de niveau Bachelor.", "CONFIRMEE", f"Seniors + leads = {senior_share} % des offres renseignées ; spécialisations et métiers IA quasi exclusivement seniors ; Apec : profils 5-10 ans très recherchés ; Bac+5 informatique en recul d'insertion mais toujours 70 % en emploi à 12 mois.", "collecte ; Apec ; Le Monde Informatique", "Le M1/M2 ne résout pas le manque d'expérience : l'alternance en Mastère est indispensable.", "FORTE", "Créer/renforcer le Mastère avec alternance obligatoire."],
        ["H10. Les différences territoriales justifient une stratégie distincte selon les campus NEXA.", "PARTIELLEMENT_CONFIRMEE", f"Paris = 29 % des offres Apec et {pct(reg.get('Île-de-France', 0), len(U))} % de l'échantillon, ville qui concentre l'essentiel des offres IA ({pct(sum(1 for r in U if r['FAMILLE_METIER'] == IA and r['ZONE_NEXA'] == 'Paris et Île-de-France'), max(1, fam[IA]))} % des offres IA de l'échantillon) ; Lyon 300-400 offres « développeur » actives, Marseille ≈ 100 ; Lille/Nantes alternance et e-commerce ; Apec prévisions régionales +2 à +6 %.", "collecte ; Apec régional ; BMO 2026", "Les compétences demandées sont homogènes d'une ville à l'autre : la stratégie diffère par le volume, l'alternance et les partenaires, pas par le contenu.", "MOYENNE", "Socle commun national, déclinaison locale des partenariats et du volume d'admission."],
    ]
    table(doc, ["HYPOTHESE", "RESULTAT", "PREUVES / CHIFFRES", "SOURCES", "CONTRADICTIONS", "CONFIANCE", "IMPLICATION_POUR_NEXA"], H, widths=[3.2, 2, 4.5, 2.2, 3, 1.4, 2.8], font_size=7)

    # ---- sources ----
    doc.add_heading("Études, articles et sources pour approfondir", 1)
    p(doc, "Chaque entrée : TITRE ; ORGANISME_OU_MEDIA ; AUTEUR ; DATE_PUBLICATION ; DATE_CONSULTATION ; URL_COMPLETE_CLIQUABLE ; PERIMETRE ; RESULTAT_UTILISE ; PAGE_SI_PDF ; FIABILITE. Les sources nationales et régionales de fiabilité FORTE ou MOYENNE utilisées dans le texte sont listées d'abord, puis les sources salaires, compétences et IA.", italic=True)
    seen = set()
    entries = []
    for s_ in load_d_etudes():
        url = s_.get("URL")
        if not url or url in seen:
            continue
        seen.add(url)
        entries.append((s_.get("TITRE"), s_.get("ORGANISME_OU_MEDIA"), s_.get("AUTEUR") or "non indiqué", s_.get("DATE_PUBLICATION"), s_.get("DATE_CONSULTATION") or DATE, url, s_.get("PERIMETRE"), s_.get("RESULTAT_UTILISE"), s_.get("PAGE_DU_RAPPORT") or "-", s_.get("FIABILITE")))
    for s_ in studies:
        url = s_.get("URL_COMPLETE") or s_.get("URL")
        if not url or url in seen:
            continue
        seen.add(url)
        res = s_.get("RESULTAT") or s_.get("RESULTATS_CHIFFRES")
        if isinstance(res, list):
            res = " ; ".join(res)
        entries.append((s_.get("TITRE"), s_.get("ORGANISME"), s_.get("AUTEUR") or "non indiqué", s_.get("DATE_PUBLICATION"), s_.get("DATE_CONSULTATION") or DATE, url, s_.get("PERIMETRE"), res, s_.get("PAGE_SI_PDF") or "-", s_.get("NIVEAU_DE_FIABILITE") or s_.get("FIABILITE")))
    for s_ in regions_ext:
        url = s_.get("URL")
        if not url or url in seen:
            continue
        seen.add(url)
        entries.append((f"{s_.get('THEME')} — {s_.get('REGION_OU_VILLE')}", s_.get("ORGANISME"), "non indiqué", s_.get("DATE_OU_PERIODE"), DATE, url, s_.get("REGION_OU_VILLE"), f"{s_.get('INDICATEUR')} : {s_.get('VALEUR')}", "-", str(s_.get("FIABILITE", "")).upper()))
    for s_ in salaires + comps + ias:
        url = s_.get("URL")
        if not url or url in seen:
            continue
        seen.add(url)
        res = s_.get("FOURCHETTE") or s_.get("VALEUR") or s_.get("CHIFFRE") or s_.get("RESULTAT")
        entries.append((s_.get("METIER") or s_.get("COMPETENCE") or s_.get("THEME"), s_.get("SOURCE") or s_.get("ORGANISME"), "non indiqué", s_.get("DATE"), DATE, url, s_.get("ZONE") or s_.get("PERIMETRE"), f"{str(s_.get('MEDIANE')) + ' € ; ' if s_.get('MEDIANE') else ''}{res}", "-", s_.get("FIABILITE") or s_.get("TYPE") or "MOYENNE"))
    for i, e in enumerate(entries, 1):
        para = doc.add_paragraph()
        r = para.add_run(f"{i}. {e[0]}"); r.bold = True
        para.add_run(f"\nORGANISME_OU_MEDIA : {e[1]} | AUTEUR : {e[2]} | DATE_PUBLICATION : {e[3]} | DATE_CONSULTATION : {e[4]}\nURL : ")
        add_hyperlink(para, e[5], e[5])
        para.add_run(f"\nPERIMETRE : {e[6]} | RESULTAT_UTILISE : {str(e[7])[:600]} | PAGE_SI_PDF : {e[8]} | FIABILITE : {str(e[9]).upper()}")
        for run in para.runs:
            run.font.size = Pt(8)
    out = os.path.join(OUTDIR, "NEXA_Synthese_Marche_Emploi_Developpement_Web_2026.docx")
    doc.save(out)
    print("Word écrit :", out, "| sources listées :", len(entries))


if __name__ == "__main__":
    main()
