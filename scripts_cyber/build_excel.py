# -*- coding: utf-8 -*-
import json, os, sys, statistics
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize as N, referentiel as R
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.chart import BarChart, PieChart, Reference

DATA = json.load(open("/home/user/NEXAPOCKET/collecte_cyber/consolide.json", encoding="utf-8"))
OUT = "/home/user/NEXAPOCKET/NEXA_Marche_Emploi_Cybersecurite_France_2026.xlsx"
OFFRES = DATA["offres"]
UNIQ = [o for o in OFFRES if o["STATUT_DOUBLON"] == "OFFRE_UNIQUE"]
PER = [o for o in UNIQ if o["DANS_PERIMETRE"]]
VOL, ETU, SANS = DATA["volumes"], DATA["etudes"], DATA["sans_donnees"]

H1 = PatternFill("solid", fgColor="1F3864"); H2 = PatternFill("solid", fgColor="2E75B6")
ACC = PatternFill("solid", fgColor="DCE6F1"); WARN = PatternFill("solid", fgColor="FCE4D6")
WHITE = Font(color="FFFFFF", bold=True, size=10)
TITLE = Font(bold=True, size=14, color="1F3864")
THIN = Border(*[Side(style="thin", color="BFBFBF")]*4)

def put_table(ws, row0, col0, headers, rows, name, style="TableStyleMedium2", width=None):
    for j, h in enumerate(headers):
        c = ws.cell(row=row0, column=col0+j, value=h); c.fill = H1; c.font = WHITE
        c.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center"); c.border = THIN
    for i, r in enumerate(rows):
        for j, v in enumerate(r):
            c = ws.cell(row=row0+1+i, column=col0+j, value=v)
            c.alignment = Alignment(wrap_text=True, vertical="top"); c.border = THIN
    ref = f"{get_column_letter(col0)}{row0}:{get_column_letter(col0+len(headers)-1)}{row0+len(rows)}"
    t = Table(displayName=name, ref=ref)
    t.tableStyleInfo = TableStyleInfo(name=style, showRowStripes=True)
    ws.add_table(t)
    for j, h in enumerate(headers):
        w = (width or {}).get(h, min(42, max(13, len(str(h)) + 4)))
        ws.column_dimensions[get_column_letter(col0+j)].width = w
    ws.row_dimensions[row0].height = 42
    return row0 + len(rows) + 1

def titre(ws, row, col, txt, sub=None):
    c = ws.cell(row=row, column=col, value=txt); c.font = TITLE
    if sub:
        ws.cell(row=row+1, column=col, value=sub).font = Font(italic=True, size=9, color="595959")
        return row + 3
    return row + 2

def pct(n, d): return round(100.0*n/d, 1) if d else 0.0
def dom(counter, k=4, excl=("NC",)):
    items = [(a, b) for a, b in counter.most_common() if a not in excl]
    return " ; ".join(f"{a} ({b})" for a, b in items[:k]) or "NC"

def skills_of(offres, famille_filter=None):
    c = Counter()
    for o in offres:
        for s in (o.get("COMPETENCES_DETECTEES") or "").split(" ; "):
            if s: c[s] += 1
    return c

def certs_of(offres):
    c = Counter()
    for o in offres:
        for s in (o.get("CERTIFICATIONS_DETECTEES") or "").split(" ; "):
            if s and s != "Aucune mention": c[s] += 1
    return c

OUTILS = {"Splunk","Microsoft Sentinel","QRadar","Elastic / ELK","EDR / XDR","SOAR / playbooks","SIEM",
 "Firewall / Palo Alto / Fortinet","Outils offensifs (Burp, Metasploit, Nmap...)","SAST / DAST / SCA",
 "CSPM / CNAPP / Prisma / Wiz","Kubernetes","Conteneurs / Docker","Infrastructure as Code / Terraform",
 "Outils IAM (SailPoint, Okta, Ping...)","PAM / accès à privilèges","AWS","Azure","GCP","Git","CI/CD",
 "Active Directory","Entra ID / Azure AD","VPN / Proxy / SASE / Zero Trust","IDS / IPS / NDR"}
IA_SKILLS = {"IA générative / LLM","AI Security / sécurisation des systèmes IA","Agents IA / RAG"}

wb = Workbook(); wb.remove(wb.active)

# ============================================================ ONGLET 1
ws = wb.create_sheet("SYNTHESE_METIERS")
r = titre(ws, 1, 1, "NEXA Digital School — Marché de l'emploi cybersécurité en France (collecte du 8 septembre 2026)",
  "Échantillon : %d lignes collectées, %d offres uniques, %d dans le périmètre cyber. "
  "ATTENTION MÉTHODE : la colonne OFFRES_UNIQUES mesure NOTRE échantillon (constitué par requêtes ciblées par famille) et NON des parts de marché. "
  "Les volumes de marché sont portés par les colonnes STOCK_NATIONAL_OBSERVE / STOCK_PARIS_OBSERVE (compteurs datés relevés sur les pages de liste publiques) et par les études (onglet sources). "
  "0 = absence constatée, NC = donnée indisponible, ESTIMATION = valeur reconstituée." % (len(OFFRES), len(UNIQ), len(PER)))

by_metier = defaultdict(list)
for o in PER: by_metier[o["METIER_NORMALISE"]].append(o)
rows = []
for metier, lst in sorted(by_metier.items(), key=lambda kv: -len(kv[1])):
    ref = R.ref(metier)
    ct = Counter(o["CONTRAT_NORMALISE"] for o in lst)
    sn = Counter(o["SENIORITE"] for o in lst)
    sk = skills_of(lst); ce = certs_of(lst)
    tech = Counter(o["NIVEAU_TECHNICITE"] for o in lst).most_common(1)[0][0]
    ia = sum(1 for o in lst if set((o.get("COMPETENCES_DETECTEES") or "").split(" ; ")) & IA_SKILLS)
    tt = sum(1 for o in lst if (o.get("TELETRAVAIL") or "NC") != "NC")
    fam = lst[0]["FAMILLE_LIB"]
    intitules = " ; ".join(sorted({o["INTITULE_BRUT"] for o in lst})[:5])
    nsrc = len({o["SOURCE"] for o in lst})
    conf = "FORTE" if len(lst) >= 25 and ref["STOCK_NATIONAL"] != "NC" else ("MOYENNE" if len(lst) >= 8 else "FAIBLE")
    rows.append([fam, metier, intitules, len([o for o in OFFRES if o["METIER_NORMALISE"] == metier]),
      len(lst), pct(len(lst), len(PER)), "NC (séries insuffisantes)", "NC (séries insuffisantes)",
      ct.get("CDI",0), ct.get("CDD",0), ct.get("ALTERNANCE",0), ct.get("STAGE",0), ct.get("FREELANCE",0),
      sn.get("DEBUTANT",0), sn.get("JUNIOR",0), sn.get("INTERMEDIAIRE",0), sn.get("SENIOR",0),
      sn.get("MANAGER_HEAD_DIRECTOR",0),
      "NC (expérience renseignée dans %d offres sur %d)" % (sum(1 for o in lst if (o.get("EXPERIENCE") or "NC")!="NC"), len(lst)),
      ref["ACCESSIBILITE"], Counter(o["NIVEAU_ETUDE"] for o in lst).most_common(1)[0][0],
      dom(ce, 3) if ce else "Aucune mention dans les extraits",
      ref["SALAIRE"], tt, N.TECH_LIB[tech],
      dom(Counter({k: v for k, v in sk.items() if k not in OUTILS}), 6),
      dom(Counter({k: v for k, v in sk.items() if k in OUTILS}), 6),
      f"{ia} offre(s) avec mention IA" if ia else "0",
      ref["AUTOMATISATION"], ref["TENSION"], ref["QUALITE"], nsrc, conf,
      ref["STOCK_NATIONAL"], ref["STOCK_PARIS"], ref["ATTRACTIVITE_ETUDIANT"],
      ref["TENSION_JUST"], ref["ACCESSIBILITE_JUST"], ref["AUTOMATISATION_JUST"], ref.get("RESERVE","-")])
HEAD1 = ["FAMILLE_METIER","METIER_NORMALISE","INTITULES_ASSOCIES","VOLUME_BRUT","OFFRES_UNIQUES",
 "PART_ECHANTILLON_%","EVOLUTION_2025","EVOLUTION_2024","CDI","CDD","ALTERNANCE","STAGE","FREELANCE",
 "DEBUTANT","JUNIOR","INTERMEDIAIRE","SENIOR","MANAGER_HEAD","EXPERIENCE_MEDIANE","ACCESSIBILITE_JUNIOR",
 "NIVEAU_ETUDE_DOMINANT","CERTIFICATIONS_DOMINANTES","SALAIRE_MEDIAN","TELETRAVAIL_MENTIONNE",
 "NIVEAU_TECHNICITE","COMPETENCES_DOMINANTES","OUTILS_DOMINANTS","COMPETENCES_IA","EXPOSITION_AUTOMATISATION",
 "TENSION_MARCHE","QUALITE_DU_DEBOUCHE","NOMBRE_SOURCES","CONFIANCE","STOCK_NATIONAL_OBSERVE",
 "STOCK_PARIS_OBSERVE","ATTRACTIVITE_ETUDIANT_PRESUMEE","JUSTIFICATION_TENSION","JUSTIFICATION_ACCESSIBILITE",
 "JUSTIFICATION_AUTOMATISATION","RESERVES_ET_CONTRADICTIONS"]
W = {"INTITULES_ASSOCIES":50,"COMPETENCES_DOMINANTES":46,"OUTILS_DOMINANTS":46,"SALAIRE_MEDIAN":40,
 "STOCK_NATIONAL_OBSERVE":48,"STOCK_PARIS_OBSERVE":44,"JUSTIFICATION_TENSION":70,
 "JUSTIFICATION_ACCESSIBILITE":78,"JUSTIFICATION_AUTOMATISATION":60,"RESERVES_ET_CONTRADICTIONS":66,
 "NIVEAU_TECHNICITE":40,"CERTIFICATIONS_DOMINANTES":34,"EXPERIENCE_MEDIANE":34,"METIER_NORMALISE":38}
r2 = put_table(ws, r, 1, HEAD1, rows, "T_METIERS", width=W)

# --- graphiques
def barchart(ws, titre_g, cats, vals, anchor, h=8, w=18):
    ch = BarChart(); ch.type = "bar"; ch.title = titre_g; ch.height = h; ch.width = w
    ch.add_data(vals, titles_from_data=False); ch.set_categories(cats); ch.legend = None
    ws.add_chart(ch, anchor)

gstart = r2 + 2
ws.cell(row=gstart, column=1, value="MINI-VUE NATIONALE ET GRAPHIQUES").font = TITLE
gs = gstart + 2
fam_c = Counter(o["FAMILLE_LIB"] for o in PER)
ct_c = Counter(o["CONTRAT_NORMALISE"] for o in PER)
sn_c = Counter(o["SENIORITE"] for o in PER)
tc_c = Counter(N.TECH_LIB[o["NIVEAU_TECHNICITE"]] for o in PER)
acc_c = Counter(R.ref(o["METIER_NORMALISE"])["ACCESSIBILITE"] for o in PER)
ten_c = Counter(R.ref(o["METIER_NORMALISE"])["TENSION"] for o in PER)
qual_c = Counter(R.ref(o["METIER_NORMALISE"])["QUALITE"] for o in PER)
alt_c = Counter(o["FAMILLE_LIB"] for o in PER if o["CONTRAT_NORMALISE"] == "ALTERNANCE")
blocks = [("Offres uniques par famille métier", fam_c), ("Offres par type de contrat", ct_c),
  ("Offres par séniorité demandée", sn_c), ("Alternances par famille métier", alt_c),
  ("Répartition par niveau de technicité", tc_c), ("Accessibilité junior (offres pondérées)", acc_c),
  ("Tension marché (offres pondérées)", ten_c), ("Qualité du débouché (offres pondérées)", qual_c)]
col = 1
for i, (t, c) in enumerate(blocks):
    ws.cell(row=gs, column=col, value=t).font = Font(bold=True, size=10)
    items = c.most_common()
    for j, (k, v) in enumerate(items):
        ws.cell(row=gs+1+j, column=col, value=k); ws.cell(row=gs+1+j, column=col+1, value=v)
    cats = Reference(ws, min_col=col, min_row=gs+1, max_row=gs+len(items))
    vals = Reference(ws, min_col=col+1, min_row=gs+1, max_row=gs+len(items))
    barchart(ws, t, cats, vals, f"{get_column_letter(col+3)}{gs}")
    col += 12
ws.cell(row=gs+len(fam_c)+22, column=1,
  value="Lecture : ces graphiques décrivent la composition de NOTRE échantillon de 342 offres dans le périmètre, "
        "construit par requêtes ciblées famille par famille. Ils ne mesurent PAS les parts de marché : "
        "pour les volumes de marché, se reporter aux colonnes STOCK_NATIONAL_OBSERVE et au tableau des stocks datés (colonne AS).").font = Font(italic=True, size=9, color="C00000")

# --- stocks datés (colonne AS)
c0 = len(HEAD1) + 3
rr = titre(ws, 1, c0, "STOCKS D'OFFRES DATÉS OBSERVÉS (compteurs publics)",
  "Relevés dans les titres de pages de liste indexées. Comptes de PERTINENCE par mots-clés (requêtes larges, recouvrements) : "
  "indicateurs RELATIFS entre métiers et entre zones, jamais un nombre d'emplois disponibles. Ne jamais additionner.")
put_table(ws, rr, c0, ["SOURCE","INTITULE_RECHERCHE","ZONE","TYPE_CONTRAT","NOMBRE","DATE_DU_COMPTE",
  "DATE_COLLECTE","PREUVE","URL","REQUETE"],
  [[v.get(k,"NC") for k in ["SOURCE","INTITULE_RECHERCHE","ZONE","TYPE_CONTRAT","NOMBRE","DATE_DU_COMPTE",
    "DATE_COLLECTE","PREUVE","URL","REQUETE"]] for v in sorted(VOL, key=lambda x:(x.get("ZONE",""), x.get("INTITULE_RECHERCHE","")))],
  "T_STOCKS", "TableStyleMedium7",
  width={"PREUVE":70,"URL":58,"REQUETE":48,"INTITULE_RECHERCHE":38,"NOMBRE":30})

# --- sources
c1 = c0 + 12
rr = titre(ws, 1, c1, "ÉTUDES ET SOURCES DOCUMENTAIRES", "Chaque résultat important du document de synthèse renvoie à l'une de ces sources.")
put_table(ws, rr, c1, ["TITRE","ORGANISME","AUTEUR","DATE_PUBLICATION","DATE_CONSULTATION","PERIMETRE",
  "METHODE","TAILLE_ECHANTILLON","RESULTAT_UTILISE","URL","PAGE_DU_RAPPORT","NIVEAU_DE_FIABILITE"],
  [[e.get(k,"NC") for k in ["TITRE","ORGANISME","AUTEUR","DATE_PUBLICATION","DATE_CONSULTATION","PERIMETRE",
    "METHODE","TAILLE_ECHANTILLON","RESULTAT_UTILISE","URL","PAGE_DU_RAPPORT","NIVEAU_DE_FIABILITE"]] for e in ETU],
  "T_SOURCES", "TableStyleMedium9",
  width={"TITRE":54,"RESULTAT_UTILISE":90,"URL":58,"METHODE":40,"NIVEAU_DE_FIABILITE":46,"PERIMETRE":30})
ws.freeze_panes = "C3"

# ============================================================ ONGLET 2
ws2 = wb.create_sheet("REGIONS_METIERS")
r = titre(ws2, 1, 1, "Régions × métiers — offres uniques du périmètre",
  "Une ligne par couple région × métier normalisé. PART_NATIONALE = part dans notre échantillon (pas une part de marché). "
  "Les colonnes de qualification (accessibilité, tension, qualité) sont celles du métier, appliquées au contexte régional.")
rows = []
by_rm = defaultdict(list)
for o in PER: by_rm[(o["REGION"], o["METIER_NORMALISE"])].append(o)
reg_tot = Counter(o["REGION"] for o in PER)
for (reg, met), lst in sorted(by_rm.items(), key=lambda kv: (-reg_tot[kv[0][0]], kv[0][0], -len(kv[1]))):
    ref = R.ref(met); ct = Counter(o["CONTRAT_NORMALISE"] for o in lst); sn = Counter(o["SENIORITE"] for o in lst)
    sk = skills_of(lst); ce = certs_of(lst)
    rows.append([reg, lst[0]["FAMILLE_LIB"], met, len(lst), len(lst), pct(len(lst), len(PER)),
      "NC (population active non appariée dans cette collecte)",
      ct.get("CDI",0), ct.get("CDD",0), ct.get("ALTERNANCE",0), ct.get("STAGE",0), ct.get("FREELANCE",0),
      sn.get("DEBUTANT",0)+sn.get("JUNIOR",0), sn.get("INTERMEDIAIRE",0), sn.get("SENIOR",0)+sn.get("MANAGER_HEAD_DIRECTOR",0),
      ref["ACCESSIBILITE"], ref["SALAIRE"], sum(1 for o in lst if (o.get("TELETRAVAIL") or "NC")!="NC"),
      N.TECH_LIB[Counter(o["NIVEAU_TECHNICITE"] for o in lst).most_common(1)[0][0]],
      dom(Counter({k:v for k,v in sk.items() if k not in OUTILS}), 5),
      dom(Counter({k:v for k,v in sk.items() if k in OUTILS}), 5),
      dom(ce, 3) if ce else "Aucune mention",
      dom(Counter(o.get("SECTEUR_ENTREPRISE","NC") for o in lst), 3),
      "NC (séries insuffisantes)", ref["TENSION"], ref["QUALITE"],
      "FORTE" if len(lst) >= 10 else ("MOYENNE" if len(lst) >= 4 else "FAIBLE")])
put_table(ws2, r, 1, ["REGION","FAMILLE_METIER","METIER_NORMALISE","VOLUME_BRUT","OFFRES_UNIQUES",
 "PART_ECHANTILLON_NATIONAL_%","OFFRES_POUR_100_000_ACTIFS","CDI","CDD","ALTERNANCE","STAGE","FREELANCE",
 "JUNIOR_ET_DEBUTANT","INTERMEDIAIRE","SENIOR_ET_MANAGER","ACCESSIBILITE_JUNIOR","SALAIRE_MEDIAN","TELETRAVAIL_MENTIONNE",
 "NIVEAU_TECHNICITE","COMPETENCES_DOMINANTES","OUTILS_DOMINANTS","CERTIFICATIONS_DOMINANTES","SECTEUR_RECRUTEUR",
 "EVOLUTION","TENSION","QUALITE_DU_DEBOUCHE","CONFIANCE"], rows, "T_REGIONS",
 width={"COMPETENCES_DOMINANTES":44,"OUTILS_DOMINANTS":40,"METIER_NORMALISE":36,"SALAIRE_MEDIAN":34,
        "SECTEUR_RECRUTEUR":32,"NIVEAU_TECHNICITE":36,"OFFRES_POUR_100_000_ACTIFS":30})
# matrice régions × familles
r3 = len(rows) + r + 3
ws2.cell(row=r3, column=1, value="MATRICE RÉGIONS × FAMILLES MÉTIERS (offres uniques de l'échantillon)").font = TITLE
fams = [f for f, _ in Counter(o["FAMILLE_LIB"] for o in PER).most_common()]
regs = [rg for rg, _ in reg_tot.most_common()]
mat = [[rg] + [sum(1 for o in PER if o["REGION"] == rg and o["FAMILLE_LIB"] == f) for f in fams] + [reg_tot[rg]] for rg in regs]
put_table(ws2, r3+2, 1, ["REGION"] + fams + ["TOTAL"], mat, "T_MATRICE", "TableStyleMedium6")
ws2.freeze_panes = "D3"

# ============================================================ ONGLET 3
ws3 = wb.create_sheet("VILLES_NEXA")
r = titre(ws3, 1, 1, "Villes NEXA × métiers", "Périmètres géographiques retenus documentés dans le bloc du bas.")
rows = []
by_vm = defaultdict(list)
for o in PER: by_vm[(o["VILLE_NEXA"], o["METIER_NORMALISE"])].append(o)
v_tot = Counter(o["VILLE_NEXA"] for o in PER)
ORDRE = ["Paris / Île-de-France","Lyon métropole","Lille métropole","Bordeaux métropole","Nantes métropole",
         "Marseille - Aix-en-Provence","National / distanciel","Hors villes NEXA"]
POTENTIEL = {
 "Paris / Île-de-France": ("TRES_ELEVE","Tous les axes sont soutenables. Prioriser Cloud Security, DevSecOps/AppSec, IAM et GRC ; le SOC reste pertinent en alternance chez les MSSP franciliens."),
 "Lyon métropole": ("ELEVE","Bassin industriel, énergie/nucléaire (EDF, Framatome), santé et ESN. Prioriser SecOps + OT + GRC industrielle ; Cloud/DevSecOps en second axe."),
 "Lille métropole": ("MOYEN-ELEVE","Retail, ESN et un acteur cyber structurant (Advens). Prioriser SOC/Detection Engineering et GRC ; volume local modeste (≥ 100 offres) : prévoir l'alternance sur la région élargie."),
 "Bordeaux métropole": ("MOYEN-ELEVE","Défense/aéronautique (Thales), éditeurs et ESN. Prioriser AppSec/pentest applicatif encadré et GRC/homologation ; attention au très faible volume d'alternance observé localement."),
 "Nantes métropole": ("MOYEN","Public/protection sociale (Urssaf), transport (SNCF), ESN (CGI, Niji, Devoteam Revolve) et EDF DIGIT sur l'IAM. Prioriser IAM, Cloud Security et GRC."),
 "Marseille - Aix-en-Provence": ("MOYEN","Paiement/monétique (Monext), services (Onet), Eviden Aix. Prioriser SOC/Cloud Microsoft et GRC ; volume local le plus faible des campus."),
 "National / distanciel": ("MOYEN","Postes explicitement full remote observés surtout sur AppSec, SOC managé et DevSecOps, plutôt à partir de 3-5 ans d'expérience : peu mobilisable pour un premier emploi."),
 "Hors villes NEXA": ("SANS_OBJET","Toulouse, Rennes, Grenoble, Strasbourg et Sophia Antipolis concentrent une part notable des offres : à traiter comme bassins d'alternance à distance raisonnable ou comme débouchés de mobilité."),
}
for v in ORDRE:
    for (vv, met), lst in sorted([(k, l) for k, l in by_vm.items() if k[0] == v], key=lambda kv: -len(kv[1])):
        ref = R.ref(met); ct = Counter(o["CONTRAT_NORMALISE"] for o in lst); sn = Counter(o["SENIORITE"] for o in lst)
        sk = skills_of(lst); ce = certs_of(lst)
        ia = sum(1 for o in lst if set((o.get("COMPETENCES_DETECTEES") or "").split(" ; ")) & IA_SKILLS)
        pot, rec = POTENTIEL[v]
        rows.append([v, N.VILLES_NEXA.get(v, {}).get("perimetre", "Bassins hors campus NEXA (Toulouse, Rennes, Grenoble, Strasbourg, Sophia Antipolis, Normandie, Grand Est...)"),
          met, lst[0]["FAMILLE_LIB"], len(lst), pct(len(lst), v_tot[v]),
          ct.get("CDI",0), ct.get("CDD",0), ct.get("ALTERNANCE",0), ct.get("STAGE",0),
          sn.get("DEBUTANT",0)+sn.get("JUNIOR",0), sn.get("INTERMEDIAIRE",0), sn.get("SENIOR",0)+sn.get("MANAGER_HEAD_DIRECTOR",0),
          ref["ACCESSIBILITE"], ref["SALAIRE"], sum(1 for o in lst if (o.get("TELETRAVAIL") or "NC")!="NC"),
          N.TECH_LIB[Counter(o["NIVEAU_TECHNICITE"] for o in lst).most_common(1)[0][0]],
          dom(Counter({k:v2 for k,v2 in sk.items() if k not in OUTILS}), 5),
          dom(Counter({k:v2 for k,v2 in sk.items() if k in OUTILS}), 5),
          dom(ce, 3) if ce else "Aucune mention", f"{ia}",
          dom(Counter(o.get("SECTEUR_ENTREPRISE","NC") for o in lst), 3),
          "NC (séries insuffisantes)", ref["TENSION"], ref["QUALITE"], pot, rec])
put_table(ws3, r, 1, ["VILLE","PERIMETRE","METIER_NORMALISE","FAMILLE_METIER","OFFRES_UNIQUES",
 "PART_DU_MARCHE_LOCAL_%","CDI","CDD","ALTERNANCE","STAGE","JUNIOR_ET_DEBUTANT","INTERMEDIAIRE","SENIOR_ET_MANAGER",
 "ACCESSIBILITE_JUNIOR","SALAIRE_MEDIAN","TELETRAVAIL_MENTIONNE","NIVEAU_TECHNICITE","COMPETENCES_DOMINANTES",
 "OUTILS_DOMINANTS","CERTIFICATIONS_DOMINANTES","COMPETENCES_IA","SECTEURS_RECRUTEURS","EVOLUTION","TENSION",
 "QUALITE_DU_DEBOUCHE","POTENTIEL_NEXA","RECOMMANDATION_CAMPUS"], rows, "T_VILLES",
 width={"PERIMETRE":72,"RECOMMANDATION_CAMPUS":80,"COMPETENCES_DOMINANTES":42,"OUTILS_DOMINANTS":38,
        "METIER_NORMALISE":36,"SALAIRE_MEDIAN":32,"NIVEAU_TECHNICITE":36,"SECTEURS_RECRUTEURS":30})
r4 = r + len(rows) + 3
ws3.cell(row=r4, column=1, value="SYNTHÈSE COMPARATIVE ENTRE CAMPUS").font = TITLE
comp = []
for v in ORDRE:
    lst = [o for o in PER if o["VILLE_NEXA"] == v]
    if not lst: continue
    ct = Counter(o["CONTRAT_NORMALISE"] for o in lst)
    fam = Counter(o["FAMILLE_LIB"] for o in lst)
    pot, rec = POTENTIEL[v]
    stock = {"Paris / Île-de-France":"≥ 2 444 (Indeed IdF, 31/08/2026) ; ≥ 2 261 Paris (02/09/2026)",
      "Lyon métropole":"≥ 400 (10/05/2026), ≥ 335 (16/06/2026)","Lille métropole":"≥ 100 (23/07/2026)",
      "Bordeaux métropole":"≥ 200 (29/05/2026) ; ≥ 615 sur variante orthographique (24/05/2026)",
      "Nantes métropole":"≥ 100 (04/09/2026)","Marseille - Aix-en-Provence":"NC en propre ; 17 ingénieurs cyber Aix (07/01/2026)",
      "National / distanciel":"NC","Hors villes NEXA":"Toulouse ≥ 500 (08/09/2026) ; Sophia Antipolis ≥ 209 (01/06/2026)"}.get(v,"NC")
    stock_alt = {"Paris / Île-de-France":"≥ 359 alternances cyber IdF (28/05/2026) ; ≥ 97 (27/08/2026)",
      "Lyon métropole":"NC","Lille métropole":"NC","Bordeaux métropole":"6 alternances (06/08/2026), 12 stages (20/08/2026)",
      "Nantes métropole":"10 alternances (30/06/2026)","Marseille - Aix-en-Provence":"10 alternances Marseille (07/09/2026), 16 stages Aix (02/06/2026)",
      "National / distanciel":"NC","Hors villes NEXA":"NC"}.get(v,"NC")
    comp.append([v, len(lst), stock, stock_alt, ct.get("ALTERNANCE",0), ct.get("STAGE",0), ct.get("CDI",0),
      dom(fam, 4), pot, rec])
put_table(ws3, r4+2, 1, ["VILLE","OFFRES_ECHANTILLON","STOCK_LOCAL_OBSERVE","STOCK_ALTERNANCE_STAGE_OBSERVE",
 "ALTERNANCES_ECHANTILLON","STAGES_ECHANTILLON","CDI_ECHANTILLON","FAMILLES_DOMINANTES","POTENTIEL_NEXA",
 "RECOMMANDATION"], comp, "T_CAMPUS", "TableStyleMedium6",
 width={"STOCK_LOCAL_OBSERVE":52,"STOCK_ALTERNANCE_STAGE_OBSERVE":50,"FAMILLES_DOMINANTES":48,"RECOMMANDATION":86})
ws3.freeze_panes = "D3"

# ============================================================ ONGLET 4
ws4 = wb.create_sheet("COMPETENCES_TECH_CERTIFS_IA")
r = titre(ws4, 1, 1, "Compétences, outils, certifications et IA",
  "Fréquence mesurée sur les %d offres du périmètre. Une compétence non détectée peut être présente dans l'offre complète "
  "sans figurer dans l'extrait indexé : la fréquence est donc une BORNE BASSE." % len(PER))
CLASSIF = {}
def classe(nb, part, fam):
    if part >= 25: return "INDISPENSABLE"
    if part >= 12: return "FORTE_DEMANDE"
    if fam == "IA" and nb > 0: return "EMERGENTE"
    if part >= 5: return "SPECIALISEE"
    if nb >= 3: return "RARE_MAIS_STRATEGIQUE"
    if nb == 0: return "NON_CONFIRMEE"
    return "RARE_MAIS_STRATEGIQUE"
FAMCOMP = {n: f for f, n, _ in N.DICO}
PERT = {
 "INDISPENSABLE": ("Bachelor : socle obligatoire", "Mastère : approfondissement"),
 "FORTE_DEMANDE": ("Bachelor : à enseigner", "Mastère : spécialisation"),
 "SPECIALISEE": ("Bachelor : sensibilisation", "Mastère : à enseigner en spécialisation"),
 "EMERGENTE": ("Bachelor : sensibilisation / veille", "Mastère : module dédié"),
 "RARE_MAIS_STRATEGIQUE": ("Bachelor : hors socle", "Mastère : option / veille"),
 "NON_CONFIRMEE": ("Bachelor : non prioritaire", "Mastère : veille uniquement"),
}
rows = []
allsk = skills_of(PER); allce = certs_of(PER)
for fam, nom, _ in N.DICO:
    nb = allsk.get(nom, 0); part = pct(nb, len(PER))
    lst = [o for o in PER if nom in (o.get("COMPETENCES_DETECTEES") or "")]
    cl = classe(nb, part, fam)
    typ = "OUTIL" if nom in OUTILS else "COMPETENCE"
    tech = round(statistics.mean([o["NIVEAU_TECHNICITE"] for o in lst]), 1) if lst else 0
    lien_ia = {"IA générative / LLM":"Compétence IA directe","AI Security / sécurisation des systèmes IA":"Sécurisation des systèmes d'IA",
      "Agents IA / RAG":"Sécurisation des agents et pipelines RAG","Detection engineering / règles":"Fortement outillée par l'IA (génération de règles)",
      "SOAR / playbooks":"Cœur de l'automatisation assistée par IA","Vulnerability management / CVE-CVSS":"Priorisation assistée par IA",
      "SAST / DAST / SCA":"Analyse de code assistée par IA","Threat Intelligence / OSINT":"Collecte et enrichissement automatisables"}.get(nom, "-")
    expo = {"SOC / supervision":"ELEVEE (tri d'alertes N1)","Threat Intelligence / OSINT":"MOYENNE-ELEVEE",
      "Vulnerability management / CVE-CVSS":"MOYENNE-ELEVEE","Audit":"MOYENNE","Sensibilisation":"MOYENNE",
      "Gouvernance / PSSI":"MOYENNE","RGPD / conformité":"MOYENNE"}.get(nom, "FAIBLE")
    rows.append([typ, fam, nom, nb, part, dom(Counter(o["METIER_NORMALISE"] for o in lst), 4),
      dom(Counter(o["REGION"] for o in lst), 3), dom(Counter(o["VILLE_NEXA"] for o in lst), 3),
      dom(Counter(o["SENIORITE"] for o in lst), 3), dom(Counter(o["CONTRAT_NORMALISE"] for o in lst), 3),
      "NC (séries insuffisantes)", "Non distinguable dans les extraits (obligatoire vs souhaitée)",
      dom(Counter(s for o in lst for s in (o.get("COMPETENCES_DETECTEES") or "").split(" ; ") if s and s != nom), 4),
      tech, lien_ia, expo, "MATURE" if part >= 10 else ("EN_CROISSANCE" if part >= 3 else "EMERGENTE_OU_RARE"),
      PERT[cl][0], PERT[cl][1], cl])
for nom, _ in N.CERTIFS:
    nb = allce.get(nom, 0); part = pct(nb, len(PER))
    lst = [o for o in PER if nom in (o.get("CERTIFICATIONS_DETECTEES") or "")]
    cl = classe(nb, part, "CERT")
    rows.append(["CERTIFICATION", "CERTIFICATIONS", nom, nb, part,
      dom(Counter(o["METIER_NORMALISE"] for o in lst), 3) if lst else "Aucune offre de notre corpus",
      dom(Counter(o["REGION"] for o in lst), 2) if lst else "NC",
      dom(Counter(o["VILLE_NEXA"] for o in lst), 2) if lst else "NC",
      dom(Counter(o["SENIORITE"] for o in lst), 2) if lst else "NC",
      dom(Counter(o["CONTRAT_NORMALISE"] for o in lst), 2) if lst else "NC",
      "NC", "Non distinguable dans les extraits", "-", 0,
      "-", "-", "MATURE" if nb else "NON_MESUREE_DANS_NOS_EXTRAITS", PERT[cl][0], PERT[cl][1], cl])
put_table(ws4, r, 1, ["TYPE","FAMILLE_COMPETENCE","COMPETENCE_OU_OUTIL","NOMBRE_OFFRES","PART_DES_OFFRES_%",
 "METIERS","REGIONS","VILLES","SENIORITE","CONTRATS","EVOLUTION","OBLIGATOIRE_OU_OPTIONNELLE","ASSOCIATIONS",
 "NIVEAU_TECHNICITE_MOYEN","LIEN_AVEC_IA","EXPOSITION_AUTOMATISATION","MATURITE","PERTINENCE_BACHELOR",
 "PERTINENCE_MASTERE","CLASSEMENT"], rows, "T_COMP",
 width={"COMPETENCE_OU_OUTIL":40,"METIERS":52,"ASSOCIATIONS":52,"REGIONS":32,"VILLES":32,"SENIORITE":30,
        "CONTRATS":28,"LIEN_AVEC_IA":38,"OBLIGATOIRE_OU_OPTIONNELLE":40,"PERTINENCE_BACHELOR":34,"PERTINENCE_MASTERE":38})
rc = r + len(rows) + 3
ws4.cell(row=rc, column=1, value="LECTURE CRITIQUE DES CERTIFICATIONS").font = TITLE
notes = [
 ["Constat", "Sur nos %d offres du périmètre, seules %d mentionnent explicitement une certification dans les extraits indexés (%.1f %%)." % (len(PER), sum(1 for o in PER if o.get("CERTIFICATIONS_DETECTEES") != "Aucune mention"), pct(sum(1 for o in PER if o.get("CERTIFICATIONS_DETECTEES") != "Aucune mention"), len(PER)))],
 ["Limite majeure", "Les extraits indexés ne restituent qu'une fraction du texte des offres : ce taux est une BORNE BASSE et ne prouve pas que les certifications sont peu demandées."],
 ["Ce que disent les sources", "CISSP, OSCP, CEH et CompTIA Security+ sont citées comme les plus demandées en France par plusieurs sources secondaires convergentes ; correspondance métier : Security+ pour les analystes, OSCP pour le pentest, CISSP/CISM pour les RSSI, CCSP/AZ-500/AWS Security pour le cloud, ISO 27001 Lead Auditor pour le GRC, SC-200 pour le SOC Microsoft."],
 ["Conséquence pour NEXA", "Aucune certification ne peut être recommandée sur la seule base de sa notoriété. Les certifications à intégrer sont celles qui sont (a) accessibles au niveau visé, (b) alignées sur les outils réellement cités dans les offres (Microsoft Sentinel/Defender, Azure, AWS, ISO 27001, EBIOS RM) et (c) utiles dès l'alternance."],
 ["Certifications de niveau expert", "CISSP (5 ans d'expérience requis) et OSCP ne sont PAS des objectifs de Bachelor : les positionner en Mastère ou en post-diplôme."],
]
put_table(ws4, rc+2, 1, ["POINT","ANALYSE"], notes, "T_CERTNOTE", "TableStyleMedium7", width={"ANALYSE":150})
ws4.freeze_panes = "D3"

# ============================================================ ONGLET 5
ws5 = wb.create_sheet("OFFRES_DETAILLEES")
r = titre(ws5, 1, 1, "Offres détaillées collectées (une ligne par offre)",
  "Champ PREUVE = copie du titre et/ou de l'extrait public ayant justifié le remplissage. « NC » = donnée absente de l'extrait, jamais déduite. "
  "Les champs normalisés (METIER_NORMALISE, REGION, SENIORITE, NIVEAU_TECHNICITE, COMPETENCES_DETECTEES) sont des CALCULS de l'étude, pas des données sources.")
COLS = ["ID_OFFRE","SOURCE","URL","URL_CANONIQUE","STATUT_DOUBLON","DANS_PERIMETRE","DATE_PUBLICATION","DATE_COLLECTE",
 "ENTREPRISE","CABINET_OU_INTERMEDIAIRE","INTITULE_BRUT","METIER_NORMALISE","FAMILLE_METIER","FAMILLE_LIB",
 "REGION","DEPARTEMENT","VILLE","VILLE_NEXA","TELETRAVAIL","TYPE_CONTRAT","CONTRAT_NORMALISE","DUREE",
 "SALAIRE_MINIMUM","SALAIRE_MAXIMUM","EXPERIENCE","SENIORITE","DIPLOME","NIVEAU_ETUDE","CERTIFICATIONS_DEMANDEES",
 "CERTIFICATIONS_DETECTEES","SECTEUR_ENTREPRISE","OUTILS","COMPETENCES","NORMES_REFERENTIELS","COMPETENCES_IA",
 "COMPETENCES_DETECTEES","FAMILLES_COMPETENCES","NIVEAU_TECHNICITE","NIVEAU_TECHNICITE_LIB","ANGLAIS",
 "DESCRIPTION_SYNTHETIQUE","PREUVE","REQUETE"]
put_table(ws5, r, 1, COLS, [[o.get(c, "NC") for c in COLS] for o in OFFRES], "T_OFFRES", "TableStyleMedium4",
 width={"URL":56,"PREUVE":90,"REQUETE":56,"DESCRIPTION_SYNTHETIQUE":70,"INTITULE_BRUT":48,"COMPETENCES_DETECTEES":54,
        "METIER_NORMALISE":34,"NIVEAU_TECHNICITE_LIB":40,"OUTILS":36,"COMPETENCES":36,"EXPERIENCE":28,"DIPLOME":32})
rj = r + len(OFFRES) + 3
ws5.cell(row=rj, column=1, value="JOURNAL DES PLATEFORMES SANS DONNÉES EXPLOITABLES (détail complet dans le fichier Markdown)").font = TITLE
KS = ["PLATEFORME","URL","DATE_DU_TEST","METIERS_TESTES","ZONES_TESTEES","DONNEES_RECHERCHEES","RESULTAT",
      "DONNEES_MANQUANTES","AUTRES_CHEMINS_TESTES","SOURCE_DE_REMPLACEMENT","IMPACT_SUR_L_ANALYSE"]
put_table(ws5, rj+2, 1, KS, [[s.get(k, "NC") for k in KS] for s in SANS], "T_SANSDATA", "TableStyleMedium7",
 width={"URL":50,"RESULTAT":66,"DONNEES_MANQUANTES":50,"AUTRES_CHEMINS_TESTES":50,"SOURCE_DE_REMPLACEMENT":54,
        "IMPACT_SUR_L_ANALYSE":60,"DONNEES_RECHERCHEES":48,"METIERS_TESTES":32,"ZONES_TESTEES":32})
ws5.freeze_panes = "D3"

wb.save(OUT)
print("Excel écrit :", OUT)
print("Onglets :", wb.sheetnames)
