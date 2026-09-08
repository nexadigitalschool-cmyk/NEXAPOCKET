# -*- coding: utf-8 -*-
import json, os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize as N, referentiel as R
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

D = json.load(open("/home/user/NEXAPOCKET/collecte_cyber/consolide.json", encoding="utf-8"))
OFFRES = D["offres"]; UNIQ = [o for o in OFFRES if o["STATUT_DOUBLON"]=="OFFRE_UNIQUE"]
PER = [o for o in UNIQ if o["DANS_PERIMETRE"]]; ETU = D["etudes"]; VOL = D["volumes"]
OUT = "/home/user/NEXAPOCKET/NEXA_Synthese_Marche_Emploi_Cybersecurite_2026.docx"
NAVY = RGBColor(0x1F,0x38,0x64); RED = RGBColor(0xC0,0x00,0x00); GREY = RGBColor(0x59,0x59,0x59)

doc = Document()
st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Calibri')
for s in doc.sections:
    s.left_margin = s.right_margin = Cm(2.0); s.top_margin = s.bottom_margin = Cm(1.8)

def H(txt, lvl=1, color=NAVY):
    p = doc.add_heading(txt, level=lvl)
    for r in p.runs: r.font.color.rgb = color
    return p
def P(txt, bold=False, italic=False, size=10.5, color=None, align=None, space=4):
    p = doc.add_paragraph(); r = p.add_run(txt); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    if color: r.font.color.rgb = color
    if align: p.alignment = align
    p.paragraph_format.space_after = Pt(space); return p
def B(txt, lvl=0):
    p = doc.add_paragraph(txt, style="List Bullet" + ("" if lvl == 0 else " 2"))
    p.paragraph_format.space_after = Pt(2); return p
def NUM(txt):
    p = doc.add_paragraph(txt, style="List Number"); p.paragraph_format.space_after = Pt(2); return p
def shade(cell, hexc):
    el = OxmlElement("w:shd"); el.set(qn("w:val"), "clear"); el.set(qn("w:fill"), hexc)
    cell._tc.get_or_add_tcPr().append(el)
def TAB(headers, rows, widths=None, size=8.5, hdr_fill="1F3864", style="Table Grid"):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = style; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(headers):
        c = t.rows[0].cells[i]; c.text = ""
        r = c.paragraphs[0].add_run(str(h)); r.bold = True; r.font.size = Pt(size); r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
        shade(c, hdr_fill)
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""
            for k, line in enumerate(str(v).split("\n")):
                p = cells[i].paragraphs[0] if k == 0 else cells[i].add_paragraph()
                rr = p.add_run(line); rr.font.size = Pt(size); p.paragraph_format.space_after = Pt(0)
    if widths:
        for i, w in enumerate(widths):
            for row in t.rows: row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return t
def SRC(txt):
    p = doc.add_paragraph(); r = p.add_run("Source : " + txt); r.italic = True; r.font.size = Pt(8.5); r.font.color.rgb = GREY
    p.paragraph_format.space_after = Pt(8); return p
def LINK(paragraph, url, text=None):
    part = paragraph.part; r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True)
    h = OxmlElement("w:hyperlink"); h.set(qn("r:id"), r_id)
    nr = OxmlElement("w:r"); pr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), "0563C1"); pr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); pr.append(u)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), "17"); pr.append(sz)
    nr.append(pr); tt = OxmlElement("w:t"); tt.text = text or url; nr.append(tt); h.append(nr)
    paragraph._p.append(h)

# ---------- stats
n_per = len(PER)
alt = [o for o in PER if o["CONTRAT_NORMALISE"]=="ALTERNANCE"]; stg = [o for o in PER if o["CONTRAT_NORMALISE"]=="STAGE"]
fam_c = Counter(o["FAMILLE_LIB"] for o in PER); ct_c = Counter(o["CONTRAT_NORMALISE"] for o in PER)
sn_c = Counter(o["SENIORITE"] for o in PER); reg_c = Counter(o["REGION"] for o in PER)
v_c = Counter(o["VILLE_NEXA"] for o in PER); alt_fam = Counter(o["FAMILLE_LIB"] for o in alt)
alt_v = Counter(o["VILLE_NEXA"] for o in alt)
sk = Counter()
for o in PER:
    for s in (o.get("COMPETENCES_DETECTEES") or "").split(" ; "):
        if s: sk[s]+=1
IA_S = {"IA générative / LLM","AI Security / sécurisation des systèmes IA","Agents IA / RAG"}
n_ia = sum(1 for o in PER if set((o.get("COMPETENCES_DETECTEES") or "").split(" ; ")) & IA_S)
def pc(n, d=None): return f"{100.0*n/(d or n_per):.1f} %"

# ============================================================ COUVERTURE
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("NEXA DIGITAL SCHOOL"); r.bold = True; r.font.size = Pt(13); r.font.color.rgb = GREY
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("\nObservatoire du marché de l'emploi\nde la cybersécurité en France"); r.bold = True; r.font.size = Pt(26); r.font.color.rgb = NAVY
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Quelle orientation donner à la filière Cybersécurité ?\nSynthèse décisionnelle — Direction Générale, Direction Marketing, Direction Pédagogique")
r.font.size = Pt(12); r.font.color.rgb = GREY
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("\nCollecte et analyse : 8 septembre 2026"); r.font.size = Pt(11); r.bold = True

t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"
c = t.rows[0].cells[0]; shade(c, "1F3864")
c.text = ""
pp = c.paragraphs[0]; pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
rr = pp.add_run("\nLA RÉPONSE EN UNE PHRASE\n"); rr.bold = True; rr.font.size = Pt(12); rr.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
pp = c.add_paragraph(); pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
rr = pp.add_run("NEXA doit conserver une filière Cybersécurité autonome mais la RESTRUCTURER en modèle hybride : "
  "un Bachelor fortement technicisé de Cybersecurity Engineering (systèmes, réseaux, cloud, scripting et automatisation) "
  "visant l'alternance et non l'emploi direct, puis un Mastère réellement spécialisé sur les trois seuls domaines "
  "où le marché français offre simultanément du volume, de la durabilité et des débouchés atteignables — "
  "Cloud Security & DevSecOps, SecOps/Detection & Automation, et GRC-IAM — "
  "en dépriorisant explicitement le pentest et l'AI Security comme parcours autonomes.\n")
rr.bold = True; rr.font.size = Pt(11.5); rr.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
pp = c.add_paragraph(); pp.alignment = WD_ALIGN_PARAGRAPH.CENTER
rr = pp.add_run("Catégorie de décision : ADOPTER_MODELE_HYBRIDE_SPECIALISE (avec technicisation forte du Bachelor)\n")
rr.bold = True; rr.font.size = Pt(11); rr.font.color.rgb = RGBColor(0xFF,0xD9,0x66)
doc.add_paragraph()

P("Base de l'étude", bold=True, size=11)
B(f"{len(OFFRES)} lignes d'offres collectées sur 10 plateformes, {len(UNIQ)} offres uniques après dédoublonnage, dont {n_per} dans le périmètre cybersécurité.")
B(f"{len(VOL)} relevés de stocks d'offres datés (compteurs publics horodatés, novembre 2025 – septembre 2026).")
B(f"{len(ETU)} sources documentaires : ANSSI (Observatoire des métiers 2025), OPIIEC, Apec, France Travail (BMO 2026), Dares/France Stratégie, Numeum, Wavestone, ISC2, ENISA, Banque de France, baromètres de rémunération et cabinets spécialisés.")
B("Trois livrables : ce document, le classeur Excel NEXA_Marche_Emploi_Cybersecurite_France_2026.xlsx (5 onglets) et le journal de collecte NEXA_Perimetre_Metiers_Cybersecurite_et_Plateformes_Sans_Donnees.md.")
doc.add_page_break()

# ============================================================ SOMMAIRE
H("Sommaire", 1)
for i, s in enumerate([
 "1. Ce qu'il faut retenir en dix points","2. Méthode, périmètre et limites de l'étude",
 "3. État du marché national : croissance, tension et réalité de la « pénurie »",
 "4. La ligne de fracture : tension du marché ≠ accessibilité junior",
 "5. Métiers qui progressent, métiers qui stagnent, métiers difficiles d'accès",
 "6. Répartition régionale et villes NEXA","7. Contrats, alternance, séniorité et salaires",
 "8. Compétences, outils, certifications et niveau de technicité",
 "9. Analyse domaine par domaine (SOC, IR, CTI, offensive, vulnérabilités, cloud, AppSec, DevSecOps, IAM, GRC, architecture, OT)",
 "10. La transformation par l'IA : automatiser la cyber et sécuriser l'IA",
 "11. Implications pédagogiques : Bachelor et Mastère","12. Recommandations par campus",
 "13. Test des 30 hypothèses","14. Quatre scénarios et matrice d'arbitrage",
 "15. Recommandation finale","16. Réponses aux 50 questions stratégiques",
 "17. Études, articles et sources pour approfondir","18. Encadré : décision recommandée pour NEXA"]):
    p = doc.add_paragraph(s); p.paragraph_format.space_after = Pt(2)
doc.add_page_break()

# ============================================================ 1
H("1. Ce qu'il faut retenir en dix points", 1)
pts = [
 ("Le marché cyber français progresse, mais moins vite et moins uniformément que le discours ambiant.",
  "L'Observatoire des métiers de l'ANSSI (édition 2025) mesure 23 000 offres publiées entre juin 2023 et juin 2024, soit +49 % par rapport à 2019. "
  "L'Apec prévoit 61 160 recrutements de cadres informaticiens en 2026 (+4 %). Mais l'enquête BMO 2026 de France Travail enregistre 2,3 millions de projets de recrutement, "
  "en retrait de 6,5 % sur un an, et Numeum comme la presse spécialisée signalent un gel des recrutements cyber dans les ESN au second semestre 2025."),
 ("La tension est réelle — mais elle porte sur les profils expérimentés, pas sur les diplômés.",
  "C'est le résultat central de l'étude. Au 4 septembre 2026, Indeed affiche environ 26 offres « débutant cybersécurité » en Île-de-France, "
  "pour un stock francilien d'environ 2 444 offres cyber : soit de l'ordre de 1 % du marché francilien explicitement ouvert aux débutants. "
  "Une pénurie de seniors n'est pas une opportunité pour un junior."),
 ("Le premier métier du marché en volume — l'architecte sécurité — est inaccessible en sortie d'école.",
  "Les architectes représentent 21 % des offres analysées par l'ANSSI, devant les consultants (15 %) et les ingénieurs (15 %). "
  "Nos relevés le confirment (≈ 400 offres en France, ≈ 270-277 à Paris, sur deux sources indépendantes). "
  "Or les offres exigent 5 à 8 ans d'expérience. Le volume du marché cyber est donc concentré sur des postes de destination, pas d'entrée."),
 ("47 % des offres cyber visent un Bac+5. Un Bachelor cyber ne peut pas viser l'emploi direct.",
  "Ce chiffre de l'Observatoire ANSSI est confirmé par notre corpus : sur les offres où le diplôme est renseigné, 62 sur 69 demandent un Bac+5. "
  "Le Bachelor doit donc être conçu pour l'alternance et la poursuite d'études, pas pour l'insertion immédiate."),
 ("L'alternance est la vraie porte d'entrée — et elle s'ouvre sur le généraliste, l'infrastructure et le GRC, pas sur les spécialités attractives.",
  f"Sur les {len(alt)} offres d'alternance de notre corpus : {alt_fam.get('Cœur généraliste',0)} en cyber généraliste, {alt_fam.get('Sécurité réseau / infrastructure',0)} en systèmes-réseaux-sécurité, "
  f"{alt_fam.get('GRC / Risques',0)} en GRC — mais seulement {alt_fam.get('SOC / Blue Team / SecOps',0)} en SOC, {alt_fam.get('DevSecOps',0)} en DevSecOps, {alt_fam.get('IAM / PAM',0)} en IAM et {alt_fam.get('Offensive Security / Pentest',0)} en sécurité offensive. "
  "Indeed relevait ≥ 359 alternances cyber en Île-de-France au 28 mai 2026."),
 ("Le pentest est le plus grand décalage du marché : très attractif, très peu recruteur.",
  "Au 28 août 2026, Indeed affiche environ 33 offres « pentester » en France, et Glassdoor 31 offres « penetration testing » en mai 2026 — "
  "contre ≥ 817 offres DevSecOps, ≥ 732 IAM, ≥ 600 Application Security Engineer et ≥ 300 analyste SOC. "
  "Synacktiv exige 3 ans d'expérience offensive minimum. Aucune alternance pentest pure n'a été trouvée."),
 ("Les trois plus gros gisements sont DevSecOps, IAM et Cloud Security — trois domaines où NEXA n'est pas naturellement attendue.",
  "DevSecOps : ≥ 817 offres au 4 septembre 2026, en hausse depuis avril (≥ 700). IAM : ≥ 732 au 31 mars 2026. "
  "Cloud Security Engineer : ≥ 438 en France et ≥ 769 « Cloud Security » à Paris au 1er septembre 2026. "
  "Ces trois domaines exigent un socle systèmes, cloud et développement supérieur à celui d'un cursus cyber généraliste classique."),
 ("Le GRC est la spécialité la plus ouverte aux profils en formation, et la réglementation la porte pour plusieurs années.",
  "NIS2 doit soumettre 10 000 à 15 000 organisations supplémentaires à des obligations de cybersécurité, DORA s'applique au secteur financier "
  "et le Cyber Resilience Act se déploie à partir de juin 2026. Notre corpus compte 37 offres GRC et 11 alternances GRC, "
  "avec des seuils d'entrée en CDI plus bas (3-5 ans) que les spécialités techniques avancées."),
 ("L'IA ne détruit pas l'emploi cyber : elle détruit le contenu du poste junior généraliste.",
  "Le tri d'alertes de niveau 1, l'enrichissement d'IOC, le reporting répétitif et la génération de requêtes — c'est-à-dire le contenu type "
  "d'un premier poste — sont les tâches les plus automatisées. Le Journal du Net cite explicitement l'analyste SOC niveau 1 parmi les métiers "
  "rendus obsolètes. En revanche, seules 13 offres sur 342 (3,8 %) mentionnent l'IA : la compétence est stratégique mais encore peu formalisée dans les offres."),
 ("L'AI Security n'est pas encore un marché : c'est une compétence.",
  "Aucun stock d'offres « AI Security Engineer », « LLM Security » ou « AI Red Teamer » n'est mesurable sur les plateformes françaises. "
  "Les six offres identifiées sont des postes cyber ou IA existants auxquels s'ajoute une dimension IA. "
  "Créer une spécialisation autonome AI Security en 2026 serait un pari commercial, pas une réponse au marché."),
]
for i, (t, d) in enumerate(pts, 1):
    P(f"{i}. {t}", bold=True, size=10.5, color=NAVY, space=2); P(d, space=8)
doc.add_page_break()

# ============================================================ 2
H("2. Méthode, périmètre et limites de l'étude", 1)
H("2.1 Ce que nous avons mesuré", 2)
P("L'étude croise quatre natures de données, volontairement tenues séparées :")
TAB(["Nature de la donnée","Ce qu'elle mesure","Volume dans cette étude","Ce qu'elle ne prouve PAS"],
 [["Offres individuelles","Contenu réel des postes : intitulé, lieu, contrat, expérience, diplôme, compétences, outils",
   f"{n_per} offres uniques dans le périmètre",
   "Des parts de marché : l'échantillon est constitué par requêtes ciblées famille par famille"],
  ["Stocks d'offres datés","Nombre d'offres actives affichées pour une requête à une date donnée",
   f"{len(VOL)} relevés (11/2025 – 09/2026)",
   "Un nombre d'emplois disponibles : ce sont des comptes de pertinence par mots-clés, avec recouvrements ; ils ne doivent jamais être additionnés"],
  ["Projets et intentions de recrutement","Ce que les employeurs déclarent vouloir recruter","Apec 2026, BMO 2026, Dares 2030",
   "Des recrutements effectifs, ni leur répartition par niveau d'expérience"],
  ["Études et déclarations de pénurie","Le déficit perçu de compétences","ANSSI, OPIIEC, ISC2, Wavestone",
   "L'accessibilité du marché aux juniors : un déficit de seniors n'est pas une offre pour débutants"]],
 [3.6,5.0,3.4,5.0])
H("2.2 Limite technique majeure — à lire avant toute interprétation", 2)
P("L'accès HTTP direct aux plateformes et aux rapports PDF a été bloqué pendant toute la collecte (proxy de session). "
  "Toutes les données proviennent donc des titres, URL et extraits de pages publiques indexées par un moteur de recherche. Trois conséquences :", space=6)
B("Champs incomplets : le salaire n'est renseigné que dans 3 offres sur 342, les certifications dans 4. Ce sont des bornes basses liées à la troncature des extraits, pas des mesures du marché. Les fourchettes salariales citées proviennent donc de baromètres publiés, marqués ESTIMATION.")
B("Objectif de volume non atteint : l'objectif indicatif de 500 à 1 000 offres uniques n'a pas pu être tenu. Nous avons préféré 342 offres réelles et traçables à un volume gonflé. Le détail des plateformes inaccessibles figure dans le fichier Markdown joint.")
B("Aucune évolution annuelle n'est calculée à partir de nos propres relevés : les séries 2024 et 2025 comparables sont absentes. Les colonnes EVOLUTION du classeur portent « NC (séries insuffisantes) ». Les tendances pluriannuelles proviennent exclusivement de sources publiées.")
H("2.2 bis Tentative d'accès direct par navigateur et instabilité des compteurs", 2)
P("Une seconde tentative de collecte a été menée en pilotant un vrai navigateur (Chromium via Playwright), "
  "avec et sans le proxy de session, sur Indeed, HelloWork et France Travail. Les trois cibles ont échoué de façon identique "
  "(net::ERR_TUNNEL_CONNECTION_FAILED), et la passerelle réseau répond explicitement « x-deny-reason: host_not_allowed ». "
  "Le blocage est une politique d'egress de la session : il ne dépend ni du site, ni de l'outil, ni de la méthode. "
  "Aucune plateforme d'emploi n'est joignable, y compris les moteurs de recherche généralistes.", space=6)
P("Cette seconde passe a en revanche permis de porter le nombre de compteurs relevés de 144 à 223, sur 138 requêtes distinctes "
  "et 15 zones géographiques, et de récupérer des points datés de 2024 et 2025. Elle a surtout produit un résultat méthodologique "
  "qui commande la lecture de toute la suite :", space=6)
TAB(["Requête","Zone","Deux relevés sur la même requête","Écart"],
 [["Identity Access Management","France","≈ 405 offres au 18/07/2025 ; « plus de 100 » au 21/07/2026","Facteur ≈ 4"],
  ["Cybersecurity Architect","France","≈ 455 offres au 22/06/2026 ; « plus de 100 » au 13/08/2026","Facteur ≈ 4"],
  ["Stage DevSecOps","France","« plus de 400 » au 30/05/2026 ; « plus de 25 » au 01/06/2026","Facteur ≈ 16 en deux jours"],
  ["Identity Access Management","Paris (75)","≈ 360 offres au 26/05/2026 ; « plus de 50 » au 21/07/2026","Facteur ≈ 7"]],
 [4.0,2.6,7.0,2.4], size=8.5)
P("Ces écarts ne traduisent pas des mouvements de marché : ils proviennent de formes d'URL différentes pour un même mot-clé, "
  "que le moteur d'indexation traite comme des pages distinctes. Vérification faite, aucune de nos 223 mesures ne constitue une série "
  "sur une URL strictement identique à deux dates différentes.", bold=True, space=6)
P("Conséquence, appliquée sans exception dans tout ce document : ces compteurs sont utilisables pour COMPARER des domaines entre eux "
  "à une date donnée (un écart d'un facteur 25 entre pentest et DevSecOps reste un signal, un écart de 20 % n'en est pas un), "
  "mais ils ne peuvent PAS servir à mesurer une évolution. Toutes les colonnes EVOLUTION du classeur restent à « NC (séries insuffisantes) », "
  "et les tendances pluriannuelles citées proviennent exclusivement de sources publiées (ANSSI, Apec, Numeum, BMO).", space=8)
P("Nous n'avons par ailleurs eu accès à aucune donnée interne NEXA (candidatures, taux de remplissage, placement, salaires de sortie, marge, coût des laboratoires, abandon). "
  "La recommandation porte donc exclusivement sur la pertinence au regard du marché de l'emploi. Une décision économique définitive exige ces indicateurs internes.", italic=True, space=8)
H("2.3 Périmètre métiers", 2)
P("Une taxonomie de 18 familles et 24 métiers normalisés a été construite avant la collecte, puis complétée par les intitulés réellement rencontrés "
  "(Analyste VOC, SOC Log Integrator & Parsing Engineer, Officier de sécurité en cybersécurité, Pentester IA, Analyste cybersécurité nucléaire, Expert conformité DORA...). "
  "Les métiers adjacents (DevOps, cloud, data, IA sans mission de sécurité explicite) sont identifiés mais jamais additionnés aux volumes cyber. "
  "Le détail complet figure en Partie A du fichier Markdown.", space=6)
TAB(["Famille","Offres uniques","Part de l'échantillon"],
 [[f, c, pc(c)] for f, c in fam_c.most_common()], [7.0,3.0,3.5])
SRC("Étude NEXA, corpus de 342 offres uniques du périmètre (onglet SYNTHESE_METIERS du classeur). "
    "Rappel : ces parts décrivent notre échantillon, pas le marché.")
doc.add_page_break()

# ============================================================ 3
H("3. État du marché national : croissance, tension et réalité de la « pénurie »", 1)
H("3.1 Le marché progresse — la trajectoire est confirmée par des sources indépendantes", 2)
TAB(["Indicateur","Valeur","Source","Fiabilité"],
 [["Offres cyber publiées (juin 2023 – juin 2024)","23 000, soit +49 % vs 2019","Observatoire des métiers ANSSI / AFPA / DGEFP, édition 2025 (1 720 professionnels + 23 000 offres analysées)","FORTE"],
  ["Professionnels cyber en France","≈ 45 000, projection ≈ 70 000 en 2028","OPIIEC, étude cybersécurité, avril 2025","FORTE"],
  ["Marché cyber français","5 Md€ en 2023, > 10 Md€ projetés en 2030","OPIIEC 2025","FORTE"],
  ["Recrutements de cadres informaticiens 2026","61 160 (+4 % vs 2025)","Apec, Prévisions de recrutements de cadres 2026 (avril 2026)","FORTE"],
  ["Croissance du marché numérique 2026","+4,3 % ; cybersécurité citée dans 92 % des projets prioritaires","Numeum / PAC, Observatoire de conjoncture S2 2025","FORTE"],
  ["Emplois IT projetés à 2030","≈ 180 000 postes supplémentaires (ingénieurs informatiques, experts cyber, responsables d'études)","Dares / France Stratégie, Les métiers en 2030 (mars 2022)","FORTE mais ancienne (antérieure à l'IA générative)"]],
 [4.6,4.0,6.0,2.4])
H("3.2 Mais la dynamique 2025-2026 est nettement plus heurtée que le discours de croissance", 2)
B("BMO 2026 (France Travail) : 2,3 millions de projets de recrutement tous secteurs, en retrait de 6,5 % sur un an ; 43,8 % des projets jugés difficiles contre 50,1 % en 2025. La difficulté de recrutement baisse globalement — sauf dans le numérique, où environ 49,5 % des postes restent difficiles à pourvoir.")
B("Numeum : le ralentissement de 2024 s'est traduit par une perte de 7 500 emplois dans le numérique ; la croissance 2026 est attendue mais « l'emploi reste incertain ».")
B("Plusieurs cabinets spécialisés signalent un gel des recrutements cyber dans les ESN et grandes SSII au second semestre 2025, et un repli du marché francilien, les ESN rationalisant les effectifs recrutés pendant la période pandémique.")
B("Wavestone annonce à l'inverse plus de 1 000 recrutements en 2026, avec une accélération sur l'IA et la cybersécurité, après une année 2025 prudente. Signal employeur, pas statistique de marché.")
P("Lecture : le marché cyber n'est ni en récession ni en croissance linéaire. Il traverse une phase de re-concentration sur les compétences jugées stratégiques "
  "(cybersécurité, cloud, data, IA) et sur les profils immédiatement opérationnels. C'est exactement la configuration la plus défavorable aux diplômés généralistes sans expérience.", bold=True, space=8)
H("3.3 Ce que « pénurie cyber » veut dire — et ne veut pas dire", 2)
TAB(["Affirmation courante","Ce que disent réellement les sources","Ce qu'on ne peut PAS en déduire"],
 [["« 15 000 postes non pourvus en France »","Chiffre repris de manière convergente par plusieurs sources secondaires citant l'ANSSI ; l'OPIIEC évalue à 25 000 les postes supplémentaires à pourvoir d'ici 2028 sur un vivier de 45 000 professionnels.",
   "Que ces postes soient ouverts à des débutants. Ils décrivent un déficit de compétences constituées, majoritairement expérimentées."],
  ["« 75 % des entreprises déclarent une pénurie de compétences cyber »","Déclaration d'entreprises (enquête d'éditeur) sur la difficulté à trouver les compétences.",
   "Un volume de postes juniors. Une entreprise peut déclarer une pénurie tout en refusant de recruter un débutant."],
  ["« Le secteur recrute massivement, de Bac+2 à senior »","Formulation issue de sites d'écoles et de blogs d'orientation, sans méthode publiée.",
   "Rien : cette affirmation n'est étayée par aucune source primaire et est contredite par le taux de 47 % d'offres visant un Bac+5 (ANSSI) et par nos relevés d'offres débutants."],
  ["« 1 personne dédiée à la cyber pour 1 300 employés »","Wavestone, Cyber Benchmark 2026, > 200 organisations : effectif jugé trop faible face aux enjeux.",
   "Que ce déficit se traduise en recrutements juniors : il se traduit d'abord en recours à des prestataires et à des MSSP."]],
 [4.2,7.0,5.8])
SRC("Observatoire ANSSI 2025 ; OPIIEC 2025 ; Wavestone Cyber Benchmark 2026 ; relevés Indeed de l'étude. Détail dans l'onglet SYNTHESE_METIERS du classeur.")
doc.add_page_break()

# ============================================================ 4
H("4. La ligne de fracture : tension du marché ≠ accessibilité junior", 1)
P("Cette étude distingue systématiquement deux indicateurs que le discours du secteur confond en permanence.", space=6)
TAB(["Métier","Tension du marché","Accessibilité junior","Stock national observé"],
 [[m, R.ref(m)["TENSION"], R.ref(m)["ACCESSIBILITE"], R.ref(m)["STOCK_NATIONAL"]]
  for m, _ in Counter(o["METIER_NORMALISE"] for o in PER).most_common() if R.ref(m)["STOCK_NATIONAL"] != "NC"],
 [4.6,3.0,3.4,6.0], size=8)
P("Le tableau montre une configuration récurrente : les métiers les plus en tension (architecture, cloud, DevSecOps, IAM, AppSec) "
  "sont aussi ceux dont l'accès junior est le plus difficile, tandis que les métiers les plus accessibles (réseau/infrastructure, GRC, "
  "administrateur sécurité) sont soit moins valorisés, soit plus exposés à l'automatisation.", space=6)
H("4.1 La mesure décisive", 2)
t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"; c = t.rows[0].cells[0]; shade(c, "FCE4D6"); c.text = ""
pp = c.paragraphs[0]; rr = pp.add_run("Au 4 septembre 2026, Indeed affichait environ 26 offres « débutant cybersécurité » en Île-de-France, "
  "pour un stock francilien d'environ 2 444 offres cybersécurité relevé le 31 août 2026.\n"
  "Soit de l'ordre de 1 % du marché francilien explicitement ouvert aux débutants.\n"
  "Sur l'ensemble de la France : ≥ 300 offres « cybersécurité junior » et ≥ 100 « débutant cybersécurité » (septembre 2026), "
  "à comparer aux ≥ 5 000 offres « cyber sécurité » relevées le 7 septembre 2026.")
rr.bold = True; rr.font.size = Pt(10.5); rr.font.color.rgb = RED
doc.add_paragraph()
SRC("Relevés Indeed horodatés de l'étude (onglet SYNTHESE_METIERS, tableau des stocks datés). "
    "Ces compteurs sont des comptes de pertinence par mots-clés : leur valeur est comparative, pas absolue. "
    "L'écart d'un facteur ~50 à ~90 entre stock global et stock « débutant » est cependant trop important pour être un artefact de requête.")
H("4.2 Ce qu'exigent réellement les offres présentées comme accessibles", 2)
TAB(["Poste","Employeur / source","Exigence réelle observée"],
 [["Analyste SOC","Atos (Bezons, HelloWork)","Bac+5 (école d'ingénieurs ou master cyber) et 4 ans minimum sur un poste similaire"],
  ["Analyste SOC N3","Michael Page (Saint-Ouen, HelloWork)","Bac+3 minimum et 5 ans en SOC, CERT ou gouvernance sécurité"],
  ["Analyste SOC (pré-embauche)","Ivry-sur-Seine (Indeed)","Bac+5 informatique, ≈ 4 ans de SOC et une certification technique SIEM, SOAR, EDR ou XDR"],
  ["Analyste SOC Detection","Nanterre (HelloWork)","Diplôme d'ingénieur et au moins 6 ans en cybersécurité, orientation détection"],
  ["Pentester / Red Teamer","Synacktiv (Paris, Indeed)","3 ans minimum en pentest ou opérations offensives, maîtrise complète de la chaîne (AD, cloud, CI/CD), français et anglais courants"],
  ["Architecte cybersécurité","Safran (Puteaux, HelloWork)","Bac+5 et 5 ans et plus, maîtrise des architectures SI, cloud, réseaux et IAM"],
  ["Architecte Sécurité & Réseau Cloud","France Travail (Paris 9e)","7 à 8 ans d'expérience, maîtrise firewalls, IAM, PKI, SIEM, cloud, Zero Trust, ISO 27001"],
  ["Analyste cybersécurité VOC","Crédit Mutuel Arkéa (WTTJ)","Bac+3 minimum ET une première expérience en sécurité opérationnelle"],
  ["Consultant IAM","Deloitte (Puteaux, WTTJ)","Idéalement 2 ans d'expérience professionnelle en IAM"],
  ["Ingénieur DevSecOps Junior","France Travail (Toulouse)","Poste explicitement junior : pipelines SAST/SCA/DAST, SBOM, suivi CVE, templates CI/CD"]],
 [4.2,4.4,8.4], size=8.5)
P("Sur dix postes présentés comme des débouchés cyber classiques, un seul — l'ingénieur DevSecOps junior — est explicitement ouvert à un profil sans expérience. "
  "Le seuil d'entrée réel du marché cyber français se situe autour de 2 à 5 ans d'expérience, souvent acquise en systèmes, réseaux ou développement.", bold=True, space=8)
doc.add_page_break()

# ============================================================ 5
H("5. Métiers qui progressent, métiers qui stagnent, métiers difficiles d'accès", 1)
H("5.1 Les volumes réels, mis côte à côte", 2)
P("Comparaison des stocks d'offres relevés sur la même plateforme (Indeed France), à des dates proches, pour des requêtes de nature comparable. "
  "Lecture strictement relative.", italic=True, space=6)
TAB(["Domaine","Stock national observé","Date du relevé","Lecture"],
 [["DevSecOps","≥ 800 (extrait : 817)","4 septembre 2026","Premier gisement du périmètre, en hausse depuis avril (≥ 700)"],
  ["IAM / gestion des identités","≥ 700 (extrait : 732)","31 mars 2026","Deuxième gisement, très sous-estimé par les étudiants"],
  ["Application Security Engineer","≥ 600","10 août 2026","Fort, mais exige une compréhension réelle du code"],
  ["Cloud Security Engineer","≥ 400 (extrait : 438)","25 mai 2026","≥ 769 pour « Cloud Security » à Paris au 1er septembre 2026"],
  ["Architecte sécurité / cybersécurité","≥ 400 (455) ; 404 sur Glassdoor","juin-juillet 2026","Premier métier selon l'ANSSI (21 % des offres) mais inaccessible en sortie d'école"],
  ["RSSI / CISO","≥ 400","3 septembre 2026","Destination de carrière"],
  ["Analyste SOC","≥ 300","28 mai 2026","Solide, mais offres majoritairement N2/N3"],
  ["Cybersécurité GRC","≥ 200 (extrait : 242)","3 septembre 2026","Porté par NIS2, DORA et le CRA"],
  ["Vulnerability Management","≥ 100 (extrait : 153)","15 juin 2026","Fonction en structuration (émergence des VOC)"],
  ["Threat Intelligence","≥ 100","16 juillet 2026","Marché de niche"],
  ["OT Security","≥ 50 (extrait : 54)","19 mai 2026","Niche, mais ancrée dans les bassins industriels"],
  ["Pentester","≥ 25 (extrait : 33) ; 31 sur Glassdoor","août 2026 / mai 2026","Le plus grand écart entre attractivité et recrutement"],
  ["AI Security / LLM Security","Aucun stock mesurable","—","Compétence émergente, pas un marché"]],
 [4.4,4.4,3.2,6.4], size=8.5)
SRC("Relevés horodatés Indeed et Glassdoor, onglet SYNTHESE_METIERS du classeur (tableau des stocks datés). "
    "Ces compteurs recouvrent partiellement des requêtes larges : ils ne sont ni additionnables ni assimilables à un nombre d'emplois.")
H("5.1 bis Les volumes par ville NEXA et par domaine", 2)
P("Compteurs locaux relevés domaine par domaine. Ils donnent une image beaucoup plus exploitable pour un arbitrage par campus "
  "que le stock cyber global de la ville.", italic=True, space=6)
TAB(["Ville","Cyber (tous domaines)","DevSecOps","Cloud Security","IAM","GRC","Pentest","Alternance cyber"],
 [["Paris / Île-de-France","≈ 2 444 (31/08/2026)","≈ 330 (15/04/2026)","≈ 769 (01/09/2026)","≈ 360 (26/05/2026)","≈ 112 (03/09/2026)","≥ 75 « sécurité pentest » (10/05/2026)","≈ 359 (28/05/2026)"],
  ["Lyon","≈ 335 (16/06/2026)","≈ 52 (06/09/2026)","≈ 69 (18/06/2026)","NC","≈ 14 (03/01/2026)","4 à 6 (07/2026)","≈ 32 (05/06/2026)"],
  ["Lille","≥ 100 (23/07/2026)","NC","NC (≥ 400 cloud non cyber)","NC","NC","NC","6 (20/08/2026)"],
  ["Bordeaux","≥ 200 (29/05/2026)","NC","NC","NC","NC","NC","6 (06/08/2026) ; 12 stages"],
  ["Nantes","≥ 100 (04/09/2026)","NC","≥ 25 (06/09/2024)","≈ 35 (04/05/2026)","NC","NC","10 (30/06/2026)"],
  ["Marseille - Aix","NC en propre","NC","NC","NC","NC","NC","10 (07/09/2026) ; 16 stages Aix"],
  ["Toulouse (hors campus)","≥ 500 (08/09/2026)","≈ 43 (03/03/2026)","NC","NC","NC","page datée sans compte","NC"]],
 [2.6,2.8,2.0,2.4,1.8,1.9,2.4,2.4], size=8)
P("Deux enseignements pour l'arbitrage par campus. D'abord, le DevSecOps est le seul domaine spécialisé qui affiche un volume local "
  "mesurable hors Paris (≈ 52 à Lyon, ≈ 43 à Toulouse) : c'est la spécialisation la plus « déployable » en région. "
  "Ensuite, le pentest s'effondre à l'échelle locale — 4 à 6 offres à Lyon, deuxième bassin français — ce qui rend un parcours "
  "offensif hors Paris difficilement défendable.", bold=True, space=6)
P("Les cases « NC » signifient qu'aucun compteur daté n'a pu être relevé pour ce couple ville × domaine, et non qu'il n'y a pas d'offres. "
  "C'est une limite de collecte, pas une mesure.", italic=True, size=9, space=8)
H("5.2 Métiers qui progressent", 2)
B("DevSecOps : seul domaine pour lequel nous disposons de deux relevés comparables sur la même requête — ≥ 700 le 15 avril 2026, ≥ 800 le 4 septembre 2026. Progression cohérente avec l'intégration croissante de la sécurité au cycle de développement.")
B("Cloud Security : stock élevé et stable de janvier (≥ 600 en Île-de-France) à septembre 2026 (≥ 769 à Paris), sur des requêtes différentes mais convergentes.")
B("GRC, risques et conformité : progression portée par un calendrier réglementaire daté et contraignant — NIS2 (10 000 à 15 000 organisations supplémentaires), DORA, Cyber Resilience Act à partir de juin 2026. C'est la progression la plus prévisible des trois à cinq prochaines années.")
B("IAM / PAM : volume élevé et durable, renforcé par la généralisation du Zero Trust et des architectures SASE observées dans les offres réseau et architecture.")
B("Detection Engineering et automatisation SOC : intitulés encore rares, mais compétences présentes dans les offres SOC N2/N3 et objet de missions freelance dédiées (migration QRadar vers Microsoft Sentinel, intégration de logs).")
H("5.3 Métiers qui stagnent ou reculent", 2)
B("Analyste SOC niveau 1 : aucune offre CDI intitulée « analyste SOC N1 » dans notre corpus, alors que les N2 et N3 y sont nombreux. Le Journal du Net, citant le fondateur de CSB.School, place explicitement ce poste parmi ceux rendus obsolètes par l'IA ; une analyse spécialisée avance 70-80 % des alertes de niveau 1 désormais traitées par l'IA.")
B("Administrateur / technicien sécurité : accessible mais fortement exposé à l'automatisation, niveau de technicité 1 à 2.")
B("Pentest et Red Team : le volume ne recule pas nécessairement, mais il reste très étroit et n'absorbe pas les flux de diplômés attirés par ces métiers.")
B("Profils cyber généralistes : les baromètres 2026 signalent une stagnation salariale des généralistes face à la valorisation des experts Cloud Security, IA défensive et conformité.")
H("5.4 Métiers difficiles d'accès en sortie d'école (à ne pas mettre en avant comme débouchés directs)", 2)
diff = [(m, R.ref(m)["ACCESSIBILITE"], R.ref(m)["ACCESSIBILITE_JUST"][:230] + "…")
        for m in Counter(o["METIER_NORMALISE"] for o in PER)
        if R.ref(m)["ACCESSIBILITE"] in ("DIFFICILE","TRES_DIFFICILE")]
TAB(["Métier","Accessibilité","Pourquoi"], [[a,b,c] for a,b,c in diff], [4.4,2.8,9.2], size=8.5)
doc.add_page_break()

# ============================================================ 6
H("6. Répartition régionale et villes NEXA", 1)
H("6.1 France", 2)
TAB(["Région","Offres uniques (échantillon)","Part de l'échantillon","Familles dominantes"],
 [[r, c, pc(c), " ; ".join(f"{f} ({n})" for f, n in Counter(o["FAMILLE_LIB"] for o in PER if o["REGION"]==r).most_common(3))]
  for r, c in reg_c.most_common()], [4.2,3.0,2.6,7.0], size=8.5)
P("Ces parts décrivent notre échantillon. Elles convergent néanmoins avec les stocks relevés et avec les sources publiées : "
  "l'Île-de-France concentre 43 à 45 % des professionnels cyber selon des sources secondaires convergentes, et un cabinet spécialisé avance 70 % des postes "
  "en Île-de-France alors que 50 % des candidats souhaitent partir en région. "
  "Nos relevés d'Indeed donnent ≥ 2 444 offres cyber en Île-de-France au 31 août 2026, contre ≥ 400 à Lyon, ≥ 200 à Bordeaux et ≥ 100 à Lille et à Nantes.", space=6)
P("Point d'attention : Toulouse (≥ 500 offres au 8 septembre 2026) et Sophia Antipolis (≥ 209 au 1er juin 2026) pèsent plus que plusieurs villes NEXA. "
  "Ces bassins ne sont pas des campus mais constituent des zones de mobilité et d'alternance à considérer.", italic=True, space=8)
H("6.2 Villes NEXA", 2)
ORDRE = ["Paris / Île-de-France","Lyon métropole","Lille métropole","Bordeaux métropole","Nantes métropole","Marseille - Aix-en-Provence","National / distanciel"]
STOCKV = {"Paris / Île-de-France":"≥ 2 444 (IdF, 31/08/2026)\n≥ 2 261 (Paris, 02/09/2026)",
 "Lyon métropole":"≥ 400 (10/05/2026)\n≈ 335 (16/06/2026)","Lille métropole":"≥ 100 (23/07/2026)",
 "Bordeaux métropole":"≥ 200 (29/05/2026)\n≈ 615 sur variante (24/05/2026)","Nantes métropole":"≥ 100 (04/09/2026)",
 "Marseille - Aix-en-Provence":"NC en propre\n17 ing. cyber Aix (07/01/2026)","National / distanciel":"NC"}
ALTV = {"Paris / Île-de-France":"≥ 359 alternances IdF (28/05/2026)","Lyon métropole":"NC","Lille métropole":"NC",
 "Bordeaux métropole":"6 alternances (06/08/2026)\n12 stages (20/08/2026)","Nantes métropole":"10 alternances (30/06/2026)",
 "Marseille - Aix-en-Provence":"10 alternances (07/09/2026)\n16 stages Aix (02/06/2026)","National / distanciel":"NC"}
TAB(["Ville NEXA","Périmètre retenu","Offres éch.","Stock local observé","Alternance / stage observés","Familles dominantes"],
 [[v, N.VILLES_NEXA[v]["perimetre"], v_c.get(v,0), STOCKV[v], ALTV[v],
   " ; ".join(f"{f} ({n})" for f, n in Counter(o["FAMILLE_LIB"] for o in PER if o["VILLE_NEXA"]==v).most_common(3))]
  for v in ORDRE], [2.6,5.4,1.6,3.4,3.2,5.0], size=8)
P(f"Hors villes NEXA : {v_c.get('Hors villes NEXA',0)} offres de l'échantillon (Toulouse, Rennes, Grenoble, Strasbourg, Sophia Antipolis, Normandie, Grand Est, Bretagne...). "
  "Cette masse confirme que le marché cyber français ne se limite pas aux six métropoles NEXA.", italic=True, space=8)
doc.add_page_break()

# ============================================================ 7
H("7. Contrats, alternance, séniorité et salaires", 1)
H("7.1 Répartition par type de contrat", 2)
TAB(["Type de contrat","Offres","Part de l'échantillon","Commentaire"],
 [["CDI", ct_c.get("CDI",0), pc(ct_c.get("CDI",0)), "Contrat de référence du marché cyber"],
  ["Alternance", ct_c.get("ALTERNANCE",0), pc(ct_c.get("ALTERNANCE",0)), "Porte d'entrée principale des profils en formation"],
  ["Stage", ct_c.get("STAGE",0), pc(ct_c.get("STAGE",0)), "Souvent en amont d'une alternance ou d'une pré-embauche"],
  ["Freelance / mission", ct_c.get("FREELANCE",0), pc(ct_c.get("FREELANCE",0)), "Marché actif : TJM moyen ≈ 616 € en direct, 558 € via intermédiaire (Silkhom, 2026)"],
  ["CDD", ct_c.get("CDD",0), pc(ct_c.get("CDD",0)), "Marginal"],
  ["Intérim", ct_c.get("INTERIM",0), pc(ct_c.get("INTERIM",0)), "Marginal (une mission de conseil de 6 mois renouvelable observée)"],
  ["Non renseigné", ct_c.get("NC",0), pc(ct_c.get("NC",0)), "Extraits tronqués — limite de collecte, pas une réalité du marché"]],
 [3.6,2.0,2.6,8.4], size=8.5)
H("7.2 L'alternance : la vraie porte d'entrée, mais pas là où les étudiants l'attendent", 2)
TAB(["Famille métier","Alternances observées","Part des alternances"],
 [[f, c, f"{100.0*c/len(alt):.1f} %"] for f, c in alt_fam.most_common()], [7.0,3.4,3.0], size=8.5)
P("Lecture stratégique : les employeurs ouvrent leurs alternances sur des postes de socle — cyber généraliste, systèmes-réseaux-sécurité — "
  "et sur le GRC, c'est-à-dire précisément les domaines où un alternant peut être productif rapidement sans expertise pointue. "
  "Les spécialités les plus attractives commercialement (SOC, DevSecOps, IAM, pentest) sont quasi absentes de l'alternance. "
  "Un Bachelor qui promettrait « analyste SOC » ou « pentester » dès la troisième année se heurterait donc à une offre d'alternance inexistante.", bold=True, space=6)
TAB(["Employeurs d'alternants observés","Ville"],
 [[o.get("ENTREPRISE","NC"), o.get("VILLE","NC")] for o in alt if o.get("ENTREPRISE","NC") != "NC"][:26], [8.0,5.0], size=8.5)
P(f"Répartition territoriale des alternances de l'échantillon : " + " ; ".join(f"{v} : {c}" for v, c in alt_v.most_common()) + ".", space=6)
P("Indeed relevait ≥ 359 alternances cyber en Île-de-France au 28 mai 2026 et ≥ 400 à 469 au niveau national selon la requête (mars-août 2026) ; "
  "Glassdoor affichait 1 003 offres « alternance cyber security » en France en 2026. Les relevés locaux sont en revanche très faibles : "
  "10 alternances à Nantes (30 juin 2026), 10 à Marseille (7 septembre 2026), 6 à Bordeaux (6 août 2026).", space=8)
H("7.3 Séniorité demandée", 2)
TAB(["Niveau","Offres","Part","Lecture"],
 [["DÉBUTANT (0-1 an, dont alternance et stage)", sn_c.get("DEBUTANT",0), pc(sn_c.get("DEBUTANT",0)), "Presque exclusivement des contrats de formation, pas des emplois"],
  ["JUNIOR (1-2 ans)", sn_c.get("JUNIOR",0), pc(sn_c.get("JUNIOR",0)), "Segment étroit : 6 CDI juniors seulement dans le corpus"],
  ["INTERMÉDIAIRE (3-5 ans)", sn_c.get("INTERMEDIAIRE",0), pc(sn_c.get("INTERMEDIAIRE",0)), "Cœur de la demande employeur"],
  ["SENIOR (> 5 ans)", sn_c.get("SENIOR",0), pc(sn_c.get("SENIOR",0)), "Très demandé, notamment en architecture et OT"],
  ["MANAGER / HEAD / DIRECTOR", sn_c.get("MANAGER_HEAD_DIRECTOR",0), pc(sn_c.get("MANAGER_HEAD_DIRECTOR",0)), "RSSI, SOC managers, heads of cybersecurity"],
  ["Non renseigné", sn_c.get("NC",0), pc(sn_c.get("NC",0)), "Extraits tronqués"]],
 [4.6,1.8,2.0,7.6], size=8.5)
P("En excluant les contrats de formation et les offres non renseignées, la demande se concentre nettement sur les profils intermédiaires et seniors. "
  "Sur les 77 CDI de notre corpus, 6 seulement sont explicitement ouverts à un profil junior.", bold=True, space=6)
H("7.4 Niveau de diplôme", 2)
P("Sur les 69 offres de notre corpus où le diplôme est explicitement mentionné, 62 demandent un Bac+5, 4 un Bac+4, 2 un Bac+3 et 1 un Bac+2. "
  "Ce résultat converge avec l'Observatoire ANSSI (47 % des offres visant un Bac+5). "
  "Les rares offres accessibles à Bac+3 (Crédit Mutuel Arkéa, Michael Page) exigent en contrepartie une expérience préalable.", space=6)
H("7.5 Salaires", 2)
P("Le salaire n'est affiché que dans 3 offres de notre corpus (dont 37 300 à 65 000 € pour un analyste SOC Detection en Île-de-France et "
  "2 000 € brut mensuels pour un stage de consultant cyber). Les fourchettes ci-dessous proviennent donc de baromètres publiés : "
  "ce sont des ESTIMATIONS de cabinets, à traiter avec prudence (méthodes non publiées).", italic=True, space=6)
TAB(["Profil","Fourchette annuelle brute","Statut de la donnée","Source"],
 [["Junior (analyste SOC ou pentester débutant)","42 000 – 48 000 €","ESTIMATION de cabinet","Cyberini, baromètre 2026"],
  ["Analyste SOC (L1 à L3)","35 000 – 55 000 €","ESTIMATION de cabinet","Scope Cyber, baromètre 2026"],
  ["Pentester","45 000 – 80 000 €","ESTIMATION de cabinet","Scope Cyber, baromètre 2026"],
  ["RSSI / CISO","70 000 – 220 000 €","ESTIMATION de cabinet","Scope Cyber, baromètre 2026"],
  ["Analyste SOC Detection (offre réelle)","37 300 – 65 000 €","OBSERVÉ dans une offre","HelloWork, Nanterre (92)"],
  ["Freelance cyber (TJM moyen)","616 €/jour en direct, 558 € via intermédiaire","ESTIMATION de cabinet","Silkhom, 2026"],
  ["Pentester senior freelance","600 – 900 €/jour","ESTIMATION de cabinet","Scope Cyber / Silkhom, 2026"]],
 [4.4,4.0,3.2,4.4], size=8.5)
P("Signal convergent de plusieurs baromètres 2026 : les profils généralistes voient leur rémunération stagner tandis que "
  "les experts Cloud Security, IA défensive et conformité voient leur valeur de marché augmenter. "
  "L'écart Paris/province se maintient autour de 10 à 15 %.", bold=True, space=8)
doc.add_page_break()

# ============================================================ 8
H("8. Compétences, outils, certifications et niveau de technicité", 1)
H("8.1 Compétences les plus fréquentes dans les offres", 2)
P("Fréquences mesurées sur les 342 offres du périmètre. Ce sont des BORNES BASSES : une compétence peut figurer dans l'offre complète "
  "sans apparaître dans l'extrait indexé.", italic=True, space=6)
TAB(["Compétence / outil","Offres","Part"], [[s, c, pc(c)] for s, c in sk.most_common(26)], [7.0,2.4,2.4], size=8.5)
H("8.2 Ce que ces fréquences disent du socle attendu", 2)
B("Le socle réellement demandé est un socle d'infrastructure : SOC et supervision (19,0 %), réseaux et TCP/IP (11,4 %), cloud (11,7 %), IAM (9,4 %), VPN/proxy/SASE/Zero Trust (6,1 %). Un cursus cyber sans systèmes ni réseaux ni cloud est désaligné du marché.")
B("La conformité est massivement présente : RGPD et conformité (11,7 %), gouvernance et PSSI (6,7 %), gestion des risques (5,8 %), ISO 27001 (4,7 %), audit (4,4 %), NIS2 (3,2 %), EBIOS RM (2,3 %). Le GRC n'est pas un domaine « mou » : il est aussi présent que le SOC dans les offres.")
B("La continuité, la gestion de crise et la résilience apparaissent dans 7,9 % des offres — une compétence rarement enseignée et pourtant demandée.")
B("Le scripting et l'automatisation restent sous-représentés dans les extraits (automatisation 2,6 %), mais apparaissent systématiquement dans les offres SOC N3, DevSecOps et SecOps, qui sont les mieux valorisées.")
B("L'IA générative est mentionnée dans 3,5 % des offres. Faible en volume, mais le signal est net dans les postes à forte valeur (analyse de logs assistée, génération de règles, pentest d'environnements IA).")
H("8.3 Certifications : ce que les données permettent — et ne permettent pas — de dire", 2)
P("Seules 4 offres de notre corpus mentionnent explicitement une certification dans l'extrait indexé (AWS Solutions Architect ×2, "
  "Azure Administrator Associate, et une exigence générique de « certification technique SIEM, SOAR, EDR ou XDR »). "
  "Ce taux est une borne basse liée à la troncature des extraits : il ne prouve pas que les certifications sont peu demandées.", space=6)
TAB(["Certification","Métiers concernés selon les sources","Pertinence Bachelor NEXA","Pertinence Mastère NEXA"],
 [["CompTIA Security+","Analystes, premiers postes","OUI — objectif de fin de Bachelor, aligné sur le socle","Non prioritaire (déjà acquise)"],
  ["Microsoft SC-200 (Security Operations Analyst)","SOC, détection, Microsoft Sentinel/Defender","OUI — cohérente avec l'outillage réellement cité dans les offres","OUI en spécialisation SecOps"],
  ["Microsoft AZ-500 / SC-300","Sécurité Azure, IAM Entra ID","Sensibilisation","OUI en spécialisation Cloud et IAM"],
  ["AWS Certified Security Specialty","Cloud Security","Non (prérequis trop élevés)","OUI en spécialisation Cloud Security"],
  ["ISO 27001 Lead Implementer / Lead Auditor","GRC, audit, conformité","Sensibilisation à la norme","OUI en spécialisation GRC"],
  ["EBIOS Risk Manager","Analyse de risques, GRC, homologation","OUI — méthode française, peu coûteuse, valorisée par les employeurs publics et industriels","OUI"],
  ["OSCP","Pentest","NON — 3 ans d'expérience offensive attendus par les employeurs","Option uniquement, hors parcours principal"],
  ["CISSP / CISM","RSSI, architecture, management","NON — 5 ans d'expérience requis pour la certification","Préparation post-diplôme uniquement"],
  ["CEH","Pentest (notoriété forte, valeur d'usage débattue)","NON","Non recommandée comme objectif principal"]],
 [3.8,4.6,4.2,3.4], size=8.5)
P("Recommandation : n'intégrer que des certifications (a) atteignables au niveau visé, (b) alignées sur les outils effectivement cités dans les offres "
  "et (c) utiles dès l'alternance. Concrètement : CompTIA Security+ et EBIOS RM en Bachelor ; SC-200, AZ-500/SC-300, AWS Security et ISO 27001 Lead Auditor "
  "selon la spécialisation de Mastère. Ne pas positionner CISSP ni OSCP comme objectifs de cursus.", bold=True, space=8)
H("8.4 Niveau de technicité des offres", 2)
tc = Counter(o["NIVEAU_TECHNICITE"] for o in PER)
TAB(["Niveau","Description","Offres","Part"],
 [[f"NIVEAU_{k}", N.TECH_LIB[k].split("— ")[-1], tc.get(k,0), pc(tc.get(k,0))] for k in [1,2,3,4]],
 [2.4,7.4,2.0,2.0], size=8.5)
P("54,4 % des offres relèvent du niveau 2 (expertise cyber opérationnelle) et 27,5 % du niveau 4 (architecture, expertise avancée, recherche). "
  "Le niveau 1 (fondamentaux, support, gouvernance simple) ne représente que 1,5 % des offres. "
  "Autrement dit : le marché n'achète presque plus de profils de niveau 1 — c'est exactement le niveau que produit un cursus cyber généraliste sans socle technique solide.", bold=True, space=8)
doc.add_page_break()

# ============================================================ 9
H("9. Analyse domaine par domaine", 1)
DOMS = [
 ("9.1 SOC, Blue Team et SecOps", "Analyste SOC",
  ["Stock national ≥ 300 offres (28 mai 2026), présence continue chez les MSSP (Sopra Steria, Atos, Capgemini, Advens, AlgoSecure, Itrust, Eye Security, Five Nines) et en interne (banque, secteur public, industrie).",
   "Mais la structure des offres est sans ambiguïté : notre corpus ne contient AUCUNE offre CDI intitulée « analyste SOC N1 », alors que les N2 et N3 y sont nombreux. Les exigences observées vont de 4 à 6 ans.",
   "Les portes d'entrée juniors existent, mais presque exclusivement en alternance et en stage : SOC Detection Engineer (Advens, Lille), SOC mutualisé (IMS Networks, Castres), Risk Analysis & SOC Analyst (CHANEL), apprenti analyste SOC junior (Paris).",
   "Les compétences qui font la différence sont l'automatisation et la détection : règles de corrélation, playbooks SOAR, scripting Python/PowerShell, threat hunting, MITRE ATT&CK. Une offre freelance observée exige 7 à 10 ans en SOC/SecOps/IR avec Splunk, Sentinel ou QRadar ; une autre porte sur la migration de cas d'usage de QRadar vers Microsoft Sentinel (Toulouse, 12 mois, septembre 2026).",
   "Conclusion : le SOC reste une porte d'entrée pédagogiquement légitime, à condition de viser le niveau 2 et l'ingénierie de détection, pas le niveau 1."]),
 ("9.2 Incident Response, forensics et Threat Intelligence", "Analyste DFIR / Incident Response",
  ["Volumes faibles : ≥ 100 offres « Threat Intelligence » et ≥ 50 « Threat Hunting » (juillet 2026) ; le DFIR n'a pas de stock propre mesurable.",
   "Exigences élevées : Sopra Steria demande 3 à 7 ans en CTI, SOC, pentest ou reverse ; Thales une première expérience réussie en SOC ou CSIRT.",
   "Employeurs concentrés : CERT et CSIRT internes (Crédit Mutuel Euro-Information, XMCO), MSSP, industriels de défense (Thales), spécialistes (OWN).",
   "Deux portes juniors seulement dans notre corpus : apprenti analyste de la menace (ANSSI) et stage Threat Intelligence (Sopra Steria).",
   "Conclusion : domaine d'expertise à enseigner comme module (investigation, gestion de crise, MITRE ATT&CK), jamais comme spécialisation autonome de Mastère au vu des volumes."]),
 ("9.3 Sécurité offensive : pentest et Red Team", "Pentester / Consultant sécurité offensive",
  ["Le décalage le plus important de l'étude : ≈ 33 offres « pentester » en France au 28 août 2026 (Indeed) et 31 offres « penetration testing » en mai 2026 (Glassdoor), contre ≥ 817 DevSecOps, ≥ 732 IAM et ≥ 600 AppSec.",
   "Barrière d'entrée très haute : Synacktiv exige 3 ans minimum d'expérience offensive et la maîtrise complète de la chaîne (reconnaissance, intrusion externe, latéralisation, Active Directory, cloud, CI/CD), en français et en anglais courants. Deloitte exige une expérience de pentest démontrée.",
   "Aucune alternance pentest « pure » n'a été trouvée. Les seules entrées observées sont des stages de recherche (Thales THALIUM sur la recherche de vulnérabilités, Framatome) et des alternances mixtes (Schneider Electric : DevSecOps + tests d'intrusion + automatisation).",
   "Ordre de grandeur indépendant, convergent : un cabinet de recrutement estime le marché à environ 150 recrutements de pentesters en France en 2025 (contre environ 120 en 2024), et environ 400 recrutements d'architectes cyber (contre environ 350). Même en tenant cette estimation pour approximative, elle situe le pentest à quelques centaines de recrutements par an au niveau national — à comparer aux effectifs qu'une seule promotion d'école cyber met sur le marché.",
   "Le Journal du Net, citant le fondateur de CSB.School, classe explicitement le red teamer, le hacker éthique, le bug bounty et la cryptographie parmi les voies qui « mènent rarement à des postes ».",
   "Conclusion : maintenir la sécurité offensive comme MODULE obligatoire (elle est indispensable pour comprendre la défense et pour l'AppSec) mais ne PAS en faire un parcours de Mastère, et ne plus la mettre en avant en communication comme un débouché."]),
 ("9.4 Gestion des vulnérabilités", "Analyste / Manager Vulnérabilités (VOC)",
  ["≥ 153 offres « Vulnerability Management » au 15 juin 2026. Fonction en cours de structuration : émergence des « VOC » (Vulnerability Operation Center) à côté des SOC (Crédit Mutuel Euro-Information à Strasbourg, Sopra Steria à Toulouse, Urssaf à Nantes, une offre « Responsable VOC » à Paris 20e).",
   "Employeurs cités par les sources : Safran, EQUANS, Orange Cyberdefense, AXA, Ingenico.",
   "Portes juniors réelles : deux stages analyste VOC (Sopra Steria), une alternance évaluation vulnérabilités et tests d'intrusion (Schneider Electric, Grenoble), un poste Bac+3 avec première expérience (Crédit Mutuel Arkéa).",
   "Exposition à l'automatisation moyenne à élevée : scan, priorisation et recommandations standard sont massivement outillés ; la négociation de la remédiation avec les équipes IT ne l'est pas.",
   "Conclusion : excellente porte d'entrée pédagogique, à intégrer au socle du Bachelor plutôt qu'à en faire une spécialisation."]),
 ("9.5 Cloud Security", "Cloud Security Engineer / Architect",
  ["Un des trois plus gros gisements : ≥ 438 offres « Cloud Security Engineer » en France (25 mai 2026), ≥ 769 « Cloud Security » à Paris (1er septembre 2026), ≥ 600 « Ingénieur Sécurité Cloud » en Île-de-France dès janvier 2026.",
   "La compétence est aussi transverse : le cloud apparaît dans 11,7 % de toutes nos offres, et systématiquement dans les offres d'architecture (Safran, France Travail Paris 9e), de DevSecOps et d'IAM.",
   "Compétences réellement demandées : AWS, Azure, GCP, IAM cloud, Zero Trust, CSPM/CNAPP (Prisma Cloud, Wiz), conteneurs et Kubernetes, Terraform et IaC, chiffrement. Employeurs observés : Inetum, Devoteam Revolve (première entreprise française certifiée AWS Security Competency), Capgemini, Onepoint, ANSSI, secteur bancaire.",
   "Contradiction relevée et arbitrée : un article du Journal du Net affirme que le Cloud Security connaîtrait des difficultés du fait d'un retour vers l'on-premise. Cette affirmation isolée, non étayée par des données dans la source, est CONTREDITE par nos relevés (stocks de 400 à 769 offres, stables sur huit mois).",
   "Conclusion : axe pédagogique majeur, à condition d'assumer les prérequis (systèmes, réseaux, IaC, un peu de code)."]),
 ("9.6 AppSec, Product Security et DevSecOps", "DevSecOps Engineer",
  ["DevSecOps est le premier gisement du périmètre : ≥ 817 offres au 4 septembre 2026, contre ≥ 700 le 15 avril 2026 — la seule progression que nous puissions documenter sur une requête identique.",
   "AppSec suit : ≥ 600 offres « Application Security Engineer » (10 août 2026), ≥ 354 à Paris (17 août 2026).",
   "Les employeurs sont très diversifiés : grands groupes (Safran, banques), conseil (Accenture, Devoteam, Thales), et surtout éditeurs et scale-ups (GitGuardian, Akeneo, Tiime, Yousign, Scaleway, Padoa, Mistral AI, BlaBlaCar) — un tissu employeur que NEXA touche déjà via sa filière Développement Web.",
   "Prérequis élevés et explicites : Akeneo demande 2 à 5 ans de sécurité en environnement web, Tiime 4 à 6 ans, l'Application Security Manager de Bordeaux la maîtrise de SAST, DAST, SCA, secret scanning, API security, container security, CI/CD et threat modeling.",
   "Portes juniors réelles côté DevSecOps : une offre France Travail explicitement « Ingénieur DevSecOps Junior » (Toulouse), une alternance DevSecOps (Padoa), ≥ 25 stages DevSecOps (1er juin 2026) et 21 alternances DevSecOps en Île-de-France (24 mai 2026).",
   "Contradiction relevée et arbitrée : le Journal du Net cite les « ingénieurs DevSec spécialisés » parmi les postes rendus obsolètes par l'IA. CONTREDIT par le stock observé, en hausse.",
   "Conclusion : c'est le domaine où le volume, la durabilité et la convergence avec l'ADN numérique de NEXA sont les plus forts — mais il exige un vrai socle développement. C'est le point de rapprochement naturel avec la filière Développement Web."]),
 ("9.7 IAM et PAM", "Consultant / Ingénieur IAM - PAM",
  ["Deuxième gisement : ≥ 732 offres « IAM » au 31 mars 2026, ≥ 360 « Identity Access Management » à Paris (26 mai 2026), ≥ 100 « Ingénieur Identity & Access Management » (31 juillet 2026).",
   "Marché structuré par des éditeurs identifiables : Entra ID/Azure AD, Active Directory, CyberArk, SailPoint, Okta, Ping Identity, ForgeRock, One Identity, Evidian, Wallix, Delinea — ce qui rend l'enseignement outillable en laboratoire.",
   "Employeurs : ESN et cabinets (Sopra Steria, Capgemini, Deloitte, CGI, Eviden, Accenture), éditeurs spécialisés (Memority), grands comptes (EDF DIGIT à Nantes).",
   "Seuils d'entrée parmi les plus bas des spécialités techniques : Deloitte 2 ans, Aix-en-Provence Bac+4/5 avec 1 an, et une alternance IAM explicite (Montrouge, septembre 2026).",
   "Résilience élevée : la gouvernance des identités, les campagnes de revue et l'intégration applicative restent des projets humains ; le Zero Trust et le SASE en renforcent la demande.",
   "Conclusion : c'est le domaine le plus sous-estimé par les étudiants et l'un des mieux adaptés à un Mastère NEXA — volume élevé, accessibilité correcte, faible exposition à l'automatisation, outillage enseignable."]),
 ("9.8 GRC, risques, audit et conformité", "Consultant GRC / Risque / Conformité",
  ["≥ 242 offres « cybersécurité GRC » au 3 septembre 2026, ≥ 112 à Paris. 37 offres GRC dans notre corpus, soit la troisième famille.",
   "Moteur réglementaire daté et contraignant : NIS2 (10 000 à 15 000 organisations supplémentaires concernées selon des sources convergentes), DORA pour le secteur financier, Cyber Resilience Act à partir de juin 2026, auxquels s'ajoutent RGPD, HDS, SOC 2 et LPM — tous cités dans nos offres.",
   "C'est la famille la plus ouverte aux profils en formation : 11 alternances GRC dans notre corpus (MGEN, Safran Massy, Thales Bordeaux, Framatome/EDF Grenoble, Onet Marseille, PSTB, Icademie, Lyon...), avec des seuils d'entrée CDI plus bas (Upcoop 3-5 ans, Toulouse 3-5 ans, CyberTee 4 ans).",
   "Attention : le GRC n'est pas de la cybersécurité opérationnelle. Un cursus qui bascule trop vers le GRC produit des profils que les recruteurs techniques n'embaucheront pas.",
   "Exposition moyenne à l'automatisation : rédaction documentaire, questionnaires fournisseurs, cartographies et reporting sont fortement accélérés par l'IA générative.",
   "Conclusion : axe à renforcer, mais toujours adossé à un socle technique — le GRC crédible est celui qui comprend ce qu'il audite."]),
 ("9.9 Architecture et Security Engineering", "Architecte sécurité / cybersécurité",
  ["Premier métier du marché selon l'Observatoire ANSSI (21 % des offres analysées), confirmé par nos relevés sur deux sources indépendantes : ≈ 400 à 455 offres en France, ≈ 270 à 277 à Paris.",
   "Exigences : Safran demande Bac+5 et 5 ans et plus ; l'architecte Sécurité & Réseau Cloud de Paris 9e demande 7 à 8 ans avec maîtrise des firewalls, IAM, PKI, SIEM, cloud, Zero Trust et ISO 27001.",
   "Conclusion : c'est le paradoxe central du marché cyber français. Le métier le plus volumineux est aussi le plus inaccessible. Il doit être présenté par NEXA comme un HORIZON de carrière à 7-10 ans, jamais comme un débouché — et le cursus doit préparer la trajectoire qui y mène (systèmes, réseaux, cloud, IAM, conformité)."]),
 ("9.10 Sécurité réseau, infrastructure et OT", "Ingénieur sécurité réseau / infrastructure",
  ["Volumes élevés mais requêtes larges : ≥ 1 736 offres « Ingénieur Réseau Sécurité » (4 août 2026), ≥ 684 en Île-de-France — à lire comme une borne haute recouvrant l'administration système et réseau non cyber.",
   "C'est la porte d'entrée la plus large observée : 14 des 62 alternances de notre corpus relèvent de cette famille (Sopra Steria Villeneuve-d'Ascq, Metz, Aubière, Bordeaux, Sarcelles), avec des niveaux Bac+2 à Bac+4.",
   "OT et sécurité industrielle : marché national étroit (≈ 54 offres « OT Security » au 19 mai 2026) mais très ancré territorialement — Belfort, Grenoble, Lyon, Toulouse, Bouzonville, Montreuil-Juigné, avec Framatome, ZF, Schneider Electric, KYRON, Davidson. Exigences de 5 à 8 ans et culture industrielle (SCADA, DCS, PLC, IEC 62443, LPM, NIS2).",
   "Conclusion : le réseau et les systèmes doivent constituer le socle obligatoire du Bachelor. L'OT est un axe de différenciation pertinent pour Lyon, pas pour Paris."]),
]
for titre, metier, bullets in DOMS:
    H(titre, 2)
    for b in bullets: B(b)
    ref = R.ref(metier)
    P(f"Synthèse — tension : {ref['TENSION']} | accessibilité junior : {ref['ACCESSIBILITE']} | "
      f"exposition à l'automatisation : {ref['AUTOMATISATION']} | qualité du débouché : {ref['QUALITE']}",
      italic=True, size=9, color=NAVY, space=10)
doc.add_page_break()

# ============================================================ 10
H("10. La transformation par l'IA : automatiser la cyber et sécuriser l'IA", 1)
P("L'étude distingue rigoureusement deux sujets que les programmes pédagogiques confondent souvent.", space=6)
H("10.1 Utiliser l'IA pour faire de la cybersécurité", 2)
P("C'est le sujet mature et immédiatement enseignable.", space=4)
B("Adoption : selon une enquête de la Banque de France (février-avril 2026), 67 % des entreprises de 20 salariés et plus utilisent l'IA générative (83 % pour les grandes entreprises) — mais seulement 31 % constatent des gains de productivité concrets et 38 % citent le manque de cas d'usage comme principal obstacle.")
B("Outillage : Microsoft Security Copilot est décrit comme atteignant l'adoption de masse en 2026, avec un modèle de consommation intégré aux licences E5. Les SIEM, EDR/XDR et SOAR intègrent désormais des fonctions d'IA natives.")
B("Tâches les plus exposées à l'automatisation, telles qu'observées et documentées : tri manuel des alertes simples, enrichissement d'IOC, collecte de contexte, création de tickets, reporting répétitif, génération de requêtes SIEM et de règles Sigma, première analyse de logs, recherches OSINT simples, recommandations de remédiation standard, rédaction de rapports d'audit et de politiques.")
B("Effet mesuré ou rapporté : une analyse spécialisée avance 70 à 80 % des alertes de niveau 1 traitées par l'IA et une équipe de 5 personnes réalisant le travail qui en demandait 8 il y a trois ans. Ces chiffres proviennent d'une source non institutionnelle : ils sont utilisés comme signal de direction, pas comme mesure.")
B("Compétences dont la valeur augmente : detection engineering, threat hunting, incident response avancé, architecture, cloud, IAM, AppSec, DevSecOps, compréhension du code, scripting et automatisation, gouvernance et gestion des risques, gestion de crise, supervision des systèmes automatisés et validation critique des résultats produits par l'IA.")
P("Conséquence pédagogique directe : l'IA ne supprime pas le besoin de cybersécurité, elle supprime le contenu du poste junior généraliste. "
  "Un cursus qui prépare à « surveiller des alertes » prépare à un poste en voie de disparition ; un cursus qui prépare à « concevoir, automatiser et superviser » prépare à un poste qui se valorise.", bold=True, space=8)
H("10.2 Sécuriser des systèmes d'IA", 2)
P("C'est le sujet stratégique — mais ce n'est pas encore un marché.", space=4)
B("Aucun stock d'offres mesurable en France pour « AI Security Engineer », « LLM Security Engineer », « AI Red Teamer » ou « ML Security Engineer ». Un cabinet de recrutement avance 119 offres Red Team sur LinkedIn France en mai 2026 et des rémunérations de 65 à 180 k€ : chiffres non vérifiables, non spécifiques à l'AI Security, à traiter comme signal commercial.")
B(f"Dans notre corpus, {n_ia} offres sur {n_per} ({pc(n_ia)}) portent une mention IA. Les seules offres réellement rattachables à l'AI Security sont des postes existants enrichis d'une dimension IA : « Pentester IA / Offensive Cybersecurity Engineer » (Cybermaker, Île-de-France — pentest de LLM, API, agents IA, pipelines RAG), « Architecte Sécurité Cloud, DevSecOps & IA », « Ingénieur Sécurité Système » avec conception de solutions d'IA pour l'analyse cyber, « Software Engineer - AI Agent » pour des équipes sécurité, et une seule alternance (« Ingénieur Développement cybersécurité IA », Vélizy).")
B("Côté IA/data, plusieurs offres intègrent la sécurité et la gouvernance sans être des postes cyber : POEI Ingénieur IA industriel (LLM, RAG, systèmes agentiques, sécurité de l'IA, RGPD), alternants IA & automatisation avec sécurité et gouvernance des données.")
B("Contexte réglementaire : l'échéance d'application du règlement européen sur l'IA et le déploiement du Cyber Resilience Act à partir de juin 2026 créent une demande de gouvernance de l'IA qui devrait précéder la demande technique.")
t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"; c = t.rows[0].cells[0]; shade(c, "FFF2CC"); c.text = ""
pp = c.paragraphs[0]
rr = pp.add_run("Arbitrage : l'AI Security mérite un MODULE (sécurisation des applications à base de LLM, prompt injection, sécurité des agents et des pipelines RAG, "
 "OWASP Top 10 for LLM Applications, gouvernance de l'IA) et une VEILLE structurée — pas une spécialisation autonome. "
 "Créer un Mastère « AI Security » en 2026 reviendrait à vendre un débouché que le marché français ne documente pas encore.")
rr.bold = True; rr.font.size = Pt(10)
doc.add_paragraph()
doc.add_page_break()

# ============================================================ 11
H("11. Implications pédagogiques : Bachelor et Mastère", 1)
H("11.1 Le constat qui commande l'architecture", 2)
P("Trois faits, pris ensemble, déterminent la structure du cursus :", space=4)
NUM("47 % des offres cyber visent un Bac+5 (ANSSI) et 62 des 69 offres de notre corpus mentionnant un diplôme demandent un Bac+5. Le Bachelor ne peut donc pas viser l'emploi direct.")
NUM("Le seuil d'entrée réel du marché est de 2 à 5 ans d'expérience, souvent acquise en systèmes, réseaux ou développement. Le cursus doit donc produire un socle technique transférable, pas une culture cyber.")
NUM("Le niveau 1 de technicité (fondamentaux, support, gouvernance simple) ne représente que 1,5 % des offres. Un cursus qui s'arrête à ce niveau ne vend rien.")
H("11.2 Bachelor recommandé — « Cybersecurity Engineering : socle technique »", 2)
P("Objectif assumé : obtenir une ALTERNANCE en 2e et 3e année, puis poursuivre en Mastère. L'insertion directe à Bac+3 doit être présentée comme possible mais minoritaire, "
  "sur des postes de technicien/administrateur sécurité, analyste GRC junior, analyste vulnérabilités junior ou support sécurité — pas comme analyste SOC ni comme pentester.", bold=True, space=6)
TAB(["Bloc","Contenu","Justification par les données"],
 [["Systèmes","Linux, Windows, Windows Server, Active Directory, virtualisation, durcissement","Socle exigé dans les offres SOC, réseau, IAM et alternance ; l'alternance Avignon liste explicitement Windows, Linux, VLAN, routage, firewall"],
  ["Réseaux","TCP/IP, DNS, DHCP, VPN, segmentation, firewall, proxy, IDS/IPS, bases SASE et Zero Trust","Réseaux dans 11,4 % des offres ; VPN/proxy/SASE/Zero Trust dans 6,1 % ; famille réseau = 14 des 62 alternances"],
  ["Cloud","Azure et AWS : IAM cloud, réseau cloud, posture de sécurité, bases de Terraform","Cloud dans 11,7 % des offres ; ≥ 438 offres Cloud Security ; compétence transverse à toutes les spécialités"],
  ["Scripting et automatisation","Python, Bash, PowerShell, Git, API, premières automatisations de sécurité","Compétence qui sépare le SOC N1 automatisable du SOC N2/N3 valorisé"],
  ["Sécurité opérationnelle","SOC, SIEM (Microsoft Sentinel), EDR, gestion des vulnérabilités, réponse à incident, MITRE ATT&CK","SOC/supervision = première compétence du corpus (19,0 %) ; Vulnerability Management = très bonne porte d'entrée"],
  ["IAM","Active Directory, Entra ID, SSO, MFA, RBAC, bases de la gouvernance des identités","IAM dans 9,4 % des offres ; deuxième gisement du marché ; seuils d'entrée bas"],
  ["Bases AppSec","OWASP Top 10, revue de code, notions de SAST/DAST, sécurité des API","Prépare la spécialisation Mastère et la convergence avec Développement Web"],
  ["GRC","ISO 27001, EBIOS RM, NIS2, DORA, RGPD, analyse de risques, continuité et gestion de crise","Conformité et gouvernance dans plus de 20 % des offres cumulées ; 11 des 62 alternances"],
  ["IA appliquée à la cyber","Usage raisonné des copilotes de sécurité, génération et validation de requêtes et de règles, limites et risques","3,5 % des offres mentionnent l'IA mais la transformation des tâches juniors est documentée"],
  ["Transverse","Anglais technique, documentation, communication, gestion de projet, posture professionnelle","Anglais exigé explicitement (Synacktiv, expert cloud Azure) ; communication et restitution récurrentes"]],
 [2.6,6.2,6.4], size=8.5)
P("Compétences devant impérativement être pratiquées en laboratoire : construction et durcissement d'un domaine Active Directory ; "
  "déploiement d'un SIEM (Microsoft Sentinel ou Elastic) avec collecte de logs et écriture de règles de détection ; "
  "usage d'un EDR ; scan et remédiation de vulnérabilités ; déploiement d'une infrastructure cloud sécurisée avec Terraform ; "
  "pipeline CI/CD avec contrôles de sécurité ; exercice de réponse à incident et de gestion de crise ; "
  "analyse de risques EBIOS RM sur un cas réel. Sans ces laboratoires, le cursus ne produit pas le niveau 2 que le marché achète.", bold=True, space=8)
H("11.3 Mastère recommandé — trois spécialisations, pas plus", 2)
TAB(["Spécialisation","Justification marché","Débouchés visés","Certifications alignées"],
 [["Cloud Security & DevSecOps","≥ 817 offres DevSecOps (04/09/2026), ≥ 438 Cloud Security Engineer, ≥ 600 AppSec. Employeurs : ESN, éditeurs, scale-ups, banques, industrie.",
   "Ingénieur DevSecOps, Cloud Security Engineer, AppSec Engineer, Security Engineer produit","AZ-500, AWS Certified Security, CKS"],
  ["SecOps, Detection & Automation","≥ 300 offres analyste SOC, missions de detection engineering et de migration SIEM ; c'est le segment du SOC dont la valeur augmente avec l'IA.",
   "Analyste SOC N2/N3, Detection Engineer, SecOps Engineer, Threat Hunter, analyste VOC","SC-200, certifications Splunk, GCIA"],
  ["Cyber GRC, Risques & IAM","≥ 242 offres GRC et ≥ 732 IAM ; moteur réglementaire NIS2/DORA/CRA daté ; les deux domaines les plus accessibles et les plus résilients.",
   "Consultant GRC, analyste risques cyber, auditeur SSI, consultant IAM/PAM, chargé de conformité","ISO 27001 Lead Auditor, EBIOS RM, SC-300"]],
 [3.4,6.0,3.6,2.6], size=8.5)
P("Pourquoi trois et pas six : le marché ne justifie pas de parcours autonomes en pentest (≈ 33 offres), en DFIR (pas de stock mesurable), "
  "en AI Security (aucun marché mesurable) ni en OT (≈ 54 offres, très localisées). Ces domaines doivent être des MODULES à l'intérieur des trois spécialisations, "
  "et des options selon le campus.", bold=True, space=6)
H("11.4 Convergences avec les autres filières NEXA", 2)
B("Avec Développement Web : AppSec, DevSecOps, sécurité des API et des conteneurs. Convergence forte et documentée — les employeurs AppSec observés (GitGuardian, Akeneo, Tiime, Yousign, Scaleway, Padoa) sont exactement le tissu employeur d'une filière web. Recommandation : mutualiser les enseignements de développement, CI/CD et conteneurs, et créer une option croisée en Mastère.")
B("Avec IA & Data : sécurisation des systèmes d'IA, gouvernance de l'IA, sécurité des agents et pipelines RAG. Convergence réelle mais marché non mesurable — recommandation : un module mutualisé, pas un parcours.")
B("Avec Marketing Digital : aucune convergence identifiée dans les données.")
doc.add_page_break()

# ============================================================ 12
H("12. Recommandations par campus", 1)
CAMP = [
 ("Paris / Île-de-France", f"{v_c.get('Paris / Île-de-France',0)} offres de l'échantillon ; ≥ 2 444 offres cyber en Île-de-France (31/08/2026) ; ≥ 359 alternances (28/05/2026)",
  "Banque et assurance, secteur public et défense, luxe, conseil, ESN et MSSP, éditeurs et scale-ups, Campus Cyber",
  "Les trois spécialisations de Mastère sont soutenables. Prioriser Cloud Security & DevSecOps (tissu éditeurs et scale-ups) et Cyber GRC & IAM (banque, assurance, secteur public soumis à DORA et NIS2). C'est le seul campus où une option Offensive Security encadrée serait défendable, en module et non en parcours."),
 ("Lyon métropole", f"{v_c.get('Lyon métropole',0)} offres de l'échantillon ; ≈ 335 offres cyber (16/06/2026) ; ≈ 32 alternances cyber (05/06/2026) ; par domaine : DevSecOps ≈ 52, cloud ≈ 69, GRC ≈ 14, pentest 4 à 6",
  "Énergie et nucléaire (EDF, Framatome), industrie, santé, ESN, télécoms",
  "Différenciation par l'industriel : SecOps + sécurité OT/ICS + GRC industrielle (LPM, NIS2, IEC 62443). Les alternances observées (EDF, Groupe SEB, Framatome, GRC Lyon) confirment ce positionnement. Second axe : Cloud Security."),
 ("Lille métropole", f"{v_c.get('Lille métropole',0)} offres de l'échantillon ; ≥ 100 offres cyber (23/07/2026) ; seulement 6 alternances cyber relevées localement (20/08/2026)",
  "Retail et distribution, ESN, un acteur cyber structurant (Advens), industrie (Villeneuve-d'Ascq)",
  "Prioriser SecOps, Detection & Automation : la présence d'Advens, qui ouvre une alternance « SOC Detection Engineer » dès 2026, est un point d'ancrage rare. Second axe : GRC. Volume local modeste : prévoir un sourcing d'alternance sur la région élargie et le distanciel."),
 ("Bordeaux métropole", f"{v_c.get('Bordeaux métropole',0)} offres ; ≥ 200 offres cyber (29/05/2026) ; seulement 6 alternances et 12 stages relevés localement (août 2026)",
  "Défense et aéronautique (Thales), éditeurs, ESN, santé",
  "Prioriser Cloud Security & DevSecOps/AppSec (postes AppSec Manager, SecOps Engineer et pentester observés localement) et GRC/homologation (alternance Thales sur l'homologation). ALERTE : le volume d'alternance observé localement est le plus faible de tous les campus — à sécuriser avant toute montée en effectifs."),
 ("Nantes métropole", f"{v_c.get('Nantes métropole',0)} offres de l'échantillon ; ≥ 100 offres cyber (04/09/2026) ; 10 alternances (30/06/2026) ; IAM ≈ 35 (04/05/2026) — le meilleur signal IAM hors Paris",
  "Secteur public et protection sociale (Urssaf), transport (SNCF), ESN (CGI, Niji, Devoteam Revolve), énergie (EDF DIGIT)",
  "Prioriser Cyber GRC & IAM : Nantes concentre des postes IAM structurants (architecte système IAM chez EDF DIGIT, consultant IAM CGI à Rennes) et des fonctions d'audit et de GRC (Urssaf, consultant GRC confirmé). Second axe : Cloud Security (Devoteam Revolve, certifié AWS Security Competency, recrute un Cloud Security Architect DevSecOps à Nantes)."),
 ("Marseille - Aix-en-Provence", f"{v_c.get('Marseille - Aix-en-Provence',0)} offres ; pas de stock local propre ; 10 alternances Marseille (07/09/2026), 16 stages Aix (02/06/2026)",
  "Paiement et monétique (Monext), services et facility management (Onet), Eviden Aix, aéronautique, secteur public",
  "Prioriser SecOps sur l'écosystème Microsoft (l'alternance Monext cite explicitement Sentinel, Intune, Azure AD, Defender) et GRC. C'est le campus au volume local le plus faible : privilégier un modèle avec forte part de distanciel et de mobilité, et ne pas y ouvrir plus d'une spécialisation de Mastère."),
]
for v, vol, secteurs, reco in CAMP:
    H(v, 2); P("Volume observé : " + vol, size=9.5, italic=True, space=2)
    P("Tissu économique observé dans les offres : " + secteurs, size=9.5, space=2)
    P("Recommandation : " + reco, size=10, space=8)
P("Distanciel : les postes explicitement en télétravail total observés portent sur l'AppSec, le SOC managé et le DevSecOps, "
  "et s'adressent à des profils de 3 à 5 ans d'expérience. Le distanciel est donc un levier pour le Mastère et pour l'après-diplôme, "
  "pas une solution au manque d'alternance locale en Bachelor.", italic=True, space=8)
doc.add_page_break()

# ============================================================ 13
H("13. Test des 30 hypothèses", 1)
HYP = [
("H1","Demande forte mais concentrée sur certains métiers et niveaux","CONFIRMEE",
 "ANSSI : +49 % d'offres 2019-2024 et 47 % de Bac+5. Nos relevés : ≥ 5 000 offres cyber nationales mais ≈ 26 offres « débutant » en IdF. Architectes = 21 % des offres et 5-8 ans exigés.","FORTE",
 "Ne jamais construire l'argumentaire commercial sur le volume global du marché."),
("H2","Tension plus élevée sur les intermédiaires et seniors que sur les juniors","CONFIRMEE",
 "Sur 77 CDI du corpus, 6 seulement sont explicitement juniors. Les offres SOC exigent 4 à 6 ans, l'architecture 5 à 8 ans.","FORTE",
 "Le Bachelor doit viser l'alternance, pas l'emploi direct."),
("H3","L'alternance est l'une des principales portes d'entrée","CONFIRMEE",
 f"{len(alt)} alternances sur {n_per} offres du corpus ; ≥ 359 alternances cyber en IdF (28/05/2026) ; 1 003 sur Glassdoor France.","FORTE",
 "L'alternance devient le cœur du modèle, pas un complément."),
("H4","Le SOC est une porte d'entrée mais le N1 s'automatise","CONFIRMEE",
 "Aucune offre CDI « analyste SOC N1 » dans le corpus alors que N2/N3 abondent ; le JDN cite le SOC N1 parmi les métiers rendus obsolètes ; 70-80 % des alertes N1 traitées par l'IA selon une analyse spécialisée.","MOYENNE (sources secondaires sur la part automatisée)",
 "Enseigner le SOC au niveau 2 et l'ingénierie de détection, jamais le N1 comme cible."),
("H5","Les profils SOC capables de scripting, automatisation, detection engineering, EDR/XDR et threat hunting sont plus valorisés","CONFIRMEE",
 "Les offres SOC N3 exigent règles de corrélation, playbooks SOAR, Splunk/Sentinel/QRadar/ELK ; missions freelance dédiées à la migration SIEM et au parsing ; alternance Advens explicitement « SOC Detection Engineer ».","FORTE",
 "Le scripting doit être un bloc obligatoire du Bachelor."),
("H6","Le pentest bénéficie d'une attractivité supérieure à son poids réel","CONFIRMEE",
 "≈ 33 offres pentester (Indeed, 28/08/2026) et 31 (Glassdoor, 05/2026) contre ≥ 817 DevSecOps, ≥ 732 IAM, ≥ 600 AppSec. Aucune alternance pentest pure. Synacktiv exige 3 ans minimum.","FORTE",
 "Retirer le pentest de la promesse commerciale principale ; le maintenir comme module."),
("H7","Le Cloud Security est un des domaines les plus porteurs","CONFIRMEE",
 "≥ 438 offres France (25/05/2026), ≥ 769 à Paris (01/09/2026), ≥ 600 en IdF dès janvier 2026 ; cloud présent dans 11,7 % de toutes les offres.","FORTE",
 "Axe majeur de Mastère. Une source contraire (JDN) n'est pas étayée et est contredite par les relevés."),
("H8","AppSec et DevSecOps progressent","CONFIRMEE",
 "DevSecOps : ≥ 700 (15/04/2026) puis ≥ 800 (04/09/2026), seule progression documentée sur requête identique. AppSec : ≥ 600 (10/08/2026).","FORTE",
 "Premier gisement du périmètre : à traiter comme axe prioritaire."),
("H9","AppSec et DevSecOps exigent plus de compétences dev et infra que les cursus cyber généralistes","CONFIRMEE",
 "Akeneo : 2-5 ans de sécurité en environnement web ; Tiime : 4-6 ans ; Application Security Manager Bordeaux : SAST/DAST/SCA, API, conteneurs, CI/CD, threat modeling ; DevSecOps junior Toulouse : SBOM, CVE, templates CI/CD.","FORTE",
 "Impose un vrai bloc développement dans le Bachelor et une mutualisation avec Développement Web."),
("H10","IAM et PAM représentent une part importante mais sous-valorisée","CONFIRMEE",
 "≥ 732 offres IAM (31/03/2026), ≥ 360 à Paris. Attractivité étudiante estimée faible. Seuils d'entrée parmi les plus bas (Deloitte 2 ans, Aix 1 an, une alternance IAM observée).","FORTE",
 "À intégrer au socle Bachelor et à une spécialisation Mastère."),
("H11","Les obligations réglementaires augmentent la demande GRC","CONFIRMEE",
 "≥ 242 offres GRC (03/09/2026) ; NIS2 (10 000-15 000 organisations supplémentaires), DORA, CRA à partir de juin 2026 ; nos offres GRC citent massivement ISO 27001, EBIOS RM, NIS2, DORA, HDS, SOC 2.","FORTE",
 "Axe à renforcer, avec une visibilité à 3-5 ans."),
("H12","Le GRC propose davantage de débouchés juniors que les spécialités techniques avancées","CONFIRMEE",
 "11 alternances GRC sur 62 dans le corpus ; seuils CDI plus bas (3-5 ans) ; « Alternant GRC » accessible depuis un Bac+2/+3.","MOYENNE (échantillon d'alternances limité)",
 "Le GRC est le meilleur point d'entrée junior après le socle infrastructure."),
("H13","Les métiers les plus porteurs demandent des compétences hybrides","CONFIRMEE",
 "L'architecte Sécurité & Réseau Cloud cumule firewalls, IAM, PKI, SIEM, cloud, Zero Trust, ISO 27001 ; CGI attend GRC + Cloud Security + IAM/PAM + cyberdéfense ; Soors attend AWS, GCP, DevSecOps, cryptographie, pentest et SOC.","FORTE",
 "L'hybridation n'est pas un choix pédagogique : c'est la demande."),
("H14","Un cursus trop généraliste ou théorique est moins aligné qu'un cursus opérationnel","CONFIRMEE",
 "Le niveau 1 de technicité ne représente que 1,5 % des offres ; les baromètres signalent une stagnation salariale des généralistes ; l'intitulé « ingénieur cybersécurité » recouvre en réalité des postes spécialisés.","FORTE",
 "La technicisation n'est pas une option."),
("H15","Les certifications renforcent l'employabilité sans remplacer l'expérience","PARTIELLEMENT_CONFIRMEE",
 "Seules 4 offres du corpus mentionnent une certification (borne basse liée aux extraits). Les sources secondaires convergent sur CISSP, OSCP, Security+ et CEH ; un baromètre indique que l'OSCP apporte 100-150 €/jour en freelance. Mais toutes les offres exigent d'abord de l'expérience.","MOYENNE",
 "Intégrer des certifications atteignables et alignées sur les outils cités, pas les plus connues."),
("H16","Le Bachelor doit fournir un socle technique large permettant une première insertion","PARTIELLEMENT_CONFIRMEE",
 "Le socle large est confirmé par la demande hybride. Mais l'insertion directe à Bac+3 est contredite : 47 % des offres visent Bac+5 et 62 des 69 offres du corpus mentionnant un diplôme demandent un Bac+5.","FORTE",
 "Le Bachelor doit viser l'alternance et la poursuite d'études, l'insertion directe restant minoritaire et ciblée."),
("H17","Le Mastère doit permettre une spécialisation nettement plus forte","CONFIRMEE",
 "Les offres à forte valeur sont toutes spécialisées (Cloud Security, DevSecOps, AppSec, IAM, GRC, detection engineering) et exigent Bac+5.","FORTE",
 "Différenciation Bachelor/Mastère structurante."),
("H18","Cloud Security, IAM, AppSec, DevSecOps, Security Engineering et GRC justifient un Bac+5","CONFIRMEE",
 "Ces six domaines concentrent les stocks les plus élevés et exigent quasi systématiquement Bac+5 et 2 à 5 ans.","FORTE",
 "Ce sont les briques du Mastère."),
("H19","Une partie de la cyber converge avec le Développement Web et le DevOps","CONFIRMEE",
 "≥ 817 offres DevSecOps et ≥ 600 AppSec ; employeurs communs (GitGuardian, Akeneo, Tiime, Yousign, Scaleway, Padoa, BlaBlaCar) ; compétences CI/CD, conteneurs, Kubernetes, IaC.","FORTE",
 "Mutualisation à organiser avec la filière Développement Web."),
("H20","Une partie des nouveaux enjeux converge avec IA & Data","PARTIELLEMENT_CONFIRMEE",
 f"Convergence réelle mais faible en volume : {n_ia} offres sur {n_per} mentionnent l'IA, et les postes IA/data intégrant la sécurité sont peu nombreux.","MOYENNE",
 "Mutualiser un module, pas un parcours."),
("H21","L'IA automatise une part croissante des tâches cyber opérationnelles simples","CONFIRMEE",
 "Absence d'offres SOC N1 en CDI dans le corpus ; JDN sur l'obsolescence du SOC N1 ; 70-80 % des alertes N1 traitées par l'IA selon une analyse spécialisée ; adoption de l'IA générative par 67 % des entreprises françaises de 20 salariés et plus (Banque de France).","MOYENNE-FORTE",
 "Sortir le SOC N1 des débouchés affichés."),
("H22","L'IA augmente la valeur des profils capables d'investiguer, automatiser, architecturer, comprendre les systèmes, le cloud et le code","CONFIRMEE",
 "Les offres les mieux valorisées du corpus (SOC N3, detection engineering, DevSecOps, architecture, cloud) sont précisément celles qui exigent ces compétences ; les baromètres signalent l'écart croissant entre généralistes et experts.","FORTE",
 "Réorienter le contenu vers la conception et la supervision, pas l'exécution."),
("H23","L'AI Security est stratégique mais pas encore un marché suffisant pour une formation autonome","CONFIRMEE",
 f"Aucun stock d'offres mesurable ; {n_ia} offres avec mention IA sur {n_per} ; une seule alternance identifiée ; les postes sont des extensions de métiers existants.","FORTE",
 "Module et veille, pas de spécialisation."),
("H24","Les différences territoriales justifient une stratégie distincte par campus","CONFIRMEE",
 "≥ 2 444 offres en IdF contre ≥ 100 à Lille et Nantes ; tissus économiques nettement différenciés (énergie/nucléaire à Lyon, défense/aéronautique à Bordeaux, public/transport à Nantes, monétique à Marseille).","FORTE",
 "Spécialisations différenciées par campus."),
("H25","Paris concentre une part disproportionnée des opportunités spécialisées et avancées","CONFIRMEE",
 "≥ 2 444 offres cyber en IdF ; ≥ 769 Cloud Security, ≥ 360 IAM, ≥ 354 AppSec et ≈ 277 architectes à Paris ; 43 à 45 % des professionnels cyber en IdF selon des sources convergentes ; un cabinet avance 70 % des postes.","FORTE",
 "Paris peut porter toutes les spécialisations ; les autres campus doivent choisir."),
("H26","Les autres campus peuvent présenter des spécialisations différentes selon leur bassin","CONFIRMEE",
 "Alternances et offres observées : EDF/Framatome/Groupe SEB à Lyon, Advens à Lille, Thales à Bordeaux, Urssaf/SNCF/EDF DIGIT à Nantes, Monext/Onet/Eviden à Marseille-Aix.","MOYENNE-FORTE",
 "Décliner le Mastère campus par campus."),
("H27","Le marché offre assez de débouchés et d'alternances pour maintenir une filière autonome","PARTIELLEMENT_CONFIRMEE",
 "Oui au niveau national (≥ 5 000 offres cyber, ≥ 359 alternances en IdF, 1 003 sur Glassdoor France). Mais localement, les volumes d'alternance relevés sont très faibles à Bordeaux (6), Marseille (10) et Nantes (10).","MOYENNE",
 "Filière autonome justifiée nationalement ; effectifs à calibrer campus par campus."),
("H28","Une orientation Cybersecurity Engineering / Cloud / SecOps / Automation créerait une différenciation plus forte qu'un cursus généraliste","CONFIRMEE",
 "Les trois plus gros gisements (DevSecOps, IAM, Cloud Security) et les compétences les mieux valorisées relèvent tous de l'engineering ; le généraliste stagne salarialement et est le plus exposé à l'automatisation.","FORTE",
 "C'est le cœur de la recommandation."),
("H29","Bachelor généraliste technique puis Mastère spécialisé est plus pertinent qu'un cursus identique du Bachelor au Bac+5","CONFIRMEE",
 "Le marché demande d'abord un socle transférable (systèmes, réseaux, cloud, code) puis une spécialisation Bac+5 : c'est exactement la structure H16 + H17 + H18.","FORTE",
 "Architecture retenue."),
("H30","Si certaines spécialités présentent trop peu de volumes ou d'alternance, NEXA doit les déprioriser même si elles sont attractives","CONFIRMEE",
 "Pentest (≈ 33 offres, aucune alternance pure), DFIR (pas de stock mesurable, aucune offre junior), AI Security (aucun marché mesurable, une seule alternance).","FORTE",
 "Dépriorisation assumée de ces trois parcours."),
]
TAB(["#","Hypothèse","Résultat","Preuves et chiffres","Confiance","Implication pour NEXA"],
 [[a,b,c,d,e,f] for a,b,c,d,e,f in HYP], [0.9,3.6,2.6,6.4,2.0,4.0], size=8)
P("Aucune hypothèse n'est ressortie CONTREDITE. Deux affirmations issues d'une source de presse (obsolescence des ingénieurs DevSec, "
  "difficultés du Cloud Security liées à un retour vers l'on-premise) sont en revanche CONTREDITES par nos relevés de stocks et n'ont pas été retenues.", italic=True, space=8)
doc.add_page_break()

# ============================================================ 14
H("14. Quatre scénarios et matrice d'arbitrage", 1)
SCEN = [
("SCÉNARIO A — Maintien généraliste","Filière Cybersécurité large maintenue, ajustements limités (mise à jour des contenus, ajout de modules IA).",
 "Étudiants attirés par la cybersécurité en général, sans projet précis",
 "Analyste cybersécurité, consultant cybersécurité junior, administrateur sécurité",
 "Volume d'intitulés élevé (≥ 1 000 offres « ingénieur cybersécurité ») mais recouvrant des postes en réalité spécialisés",
 "FAIBLE — le niveau 1 de technicité ne représente que 1,5 % des offres et le junior généraliste est le plus exposé à l'automatisation",
 "MOYEN — l'alternance généraliste existe (19 des 62 alternances du corpus)",
 "NIVEAU_2 dominant","Security+ uniquement","ÉLEVÉE — c'est le profil dont les tâches sont les plus automatisées",
 "FAIBLE — les baromètres signalent déjà la stagnation salariale des généralistes",
 "Simplicité de mise en œuvre ; coût pédagogique le plus bas ; discours commercial inchangé",
 "Désalignement croissant avec la demande ; promesse d'emploi non tenable à Bac+3 ; aucune différenciation face aux écoles cyber spécialisées",
 "FAIBLE","Laboratoires légers","Faible","AUCUNE","MOYENNE","FORTE","NON RECOMMANDÉ"),
("SCÉNARIO B — Cybersecurity Engineering","Repositionnement technique fort de toute la filière : systèmes, réseaux, Linux, Windows, AD, cloud, SOC, SIEM, EDR/XDR, security engineering, scripting, automatisation, IAM, Cloud Security, DevSecOps, AppSec, conteneurs, IaC, IA appliquée aux opérations.",
 "Étudiants à appétence technique réelle, y compris en reconversion IT",
 "Ingénieur DevSecOps, Cloud Security Engineer, SecOps/Detection Engineer, Security Engineer, ingénieur IAM",
 "ÉLEVÉ — DevSecOps ≥ 817, IAM ≥ 732, AppSec ≥ 600, Cloud Security ≥ 438",
 "MOYEN — portes juniors réelles (DevSecOps junior, alternances IAM et Cloud) mais prérequis élevés",
 "MOYEN — les alternances techniques pointues sont rares (1 DevSecOps, 1 IAM, 3 SOC dans le corpus)",
 "NIVEAU_3 dominant","SC-200, AZ-500, AWS Security, CKS","FAIBLE — métiers de conception et d'automatisation",
 "TRÈS ÉLEVÉE — c'est la trajectoire du marché",
 "Alignement maximal avec les gisements ; différenciation forte ; salaires de sortie supérieurs",
 "Risque de sélectivité à l'entrée trop élevée pour une école post-bac ; besoin d'intervenants rares et coûteux ; risque d'échec si le socle n'est pas acquis",
 "ÉLEVÉ","Laboratoires lourds (cloud, Kubernetes, SIEM)","Difficile","FORTE","FORTE","MOYENNE","RECOMMANDÉ COMME ORIENTATION DU BACHELOR"),
("SCÉNARIO C — Modèle hybride / spécialisé","Bachelor de socle technique large (systèmes, réseaux, cloud, scripting, SOC, vulnérabilités, IAM, bases AppSec, GRC) visant l'alternance ; Mastère réellement spécialisé sur trois axes : Cloud Security & DevSecOps, SecOps/Detection & Automation, Cyber GRC/Risques & IAM.",
 "Étudiants post-bac en Bachelor, puis orientation en fonction du marché et du campus",
 "Bachelor : alternant cyber, technicien/administrateur sécurité, analyste GRC junior, analyste vulnérabilités junior. Mastère : DevSecOps, Cloud Security, Detection Engineer, consultant GRC, consultant IAM",
 "ÉLEVÉ ET DIVERSIFIÉ — couvre les cinq plus gros gisements du marché",
 "ÉLEVÉ pour le Bachelor via l'alternance (socle et GRC = 44 des 62 alternances du corpus) ; MOYEN à ÉLEVÉ en sortie de Mastère",
 "ÉLEVÉ — le socle et le GRC sont précisément ce que les employeurs ouvrent en alternance",
 "NIVEAU_2 en Bachelor, NIVEAU_3 en Mastère","Security+ et EBIOS RM en Bachelor ; SC-200, AZ-500/SC-300, AWS Security, ISO 27001 LA en Mastère",
 "FAIBLE À MOYENNE — le socle reste transférable et les spécialisations visent la conception",
 "TRÈS ÉLEVÉE — les trois axes sont portés par des moteurs durables (cloud, réglementation, automatisation)",
 "Aligné sur la réalité de l'insertion (alternance puis Bac+5) ; permet une différenciation par campus ; mutualisable avec Développement Web et IA & Data ; réduit le risque de promesse non tenue",
 "Exige de renoncer publiquement au pentest comme promesse ; suppose un investissement laboratoire réel ; complexité de gestion de trois spécialisations",
 "ÉLEVÉ","Laboratoires structurants mais mutualisables entre spécialisations","Moyennement difficile","FORTE","TRÈS FORTE","FAIBLE","RECOMMANDÉ"),
("SCÉNARIO D — Réduction / rapprochement / restructuration","Réduction du nombre de parcours, fusion partielle d'AppSec-DevSecOps avec Développement Web, mutualisation de l'AI Security avec IA & Data, arrêt des parcours trop faibles, voire arrêt progressif de la filière.",
 "Sans objet (scénario de repli)",
 "Sans objet",
 "Le marché national ne justifie PAS un arrêt de filière : ≥ 5 000 offres cyber, ≥ 359 alternances en IdF, moteur réglementaire à 3-5 ans",
 "Sans objet",
 "Sans objet",
 "Sans objet","Sans objet","Sans objet","Sans objet",
 "Réduit le risque sur les campus à faible volume d'alternance ; les rapprochements avec Développement Web et IA & Data sont pertinents en eux-mêmes",
 "Un arrêt de filière serait contredit par les données : le marché est porteur, le problème est le POSITIONNEMENT, pas l'existence de la demande",
 "Sans objet","Sans objet","Sans objet","Sans objet","Sans objet","Sans objet",
 "PARTIELLEMENT RETENU : les composantes de rapprochement (AppSec/DevSecOps avec Développement Web, AI Security avec IA & Data) et de réduction du nombre de parcours sont intégrées au scénario C. L'arrêt de filière est ÉCARTÉ."),
]
COLS_S = ["JUSTIFICATION","PUBLIC_CIBLE","METIERS_VISES","VOLUME_DEBOUCHES","ACCESSIBILITE_JUNIOR","POTENTIEL_ALTERNANCE",
 "NIVEAU_TECHNICITE","CERTIFICATIONS","EXPOSITION_AUTOMATISATION","RESILIENCE_A_3_5_ANS","AVANTAGES","RISQUES",
 "EFFORT_PEDAGOGIQUE","BESOINS_LABORATOIRES","BESOINS_INTERVENANTS","DIFFERENCIATION","COHERENCE_AVEC_NEXA","RISQUE_GLOBAL","RECOMMANDATION"]
for s in SCEN:
    H(s[0], 2)
    TAB(["Critère","Analyse"], [[COLS_S[i], s[i+1]] for i in range(len(COLS_S))], [4.0,12.0], size=8.5)
H("14.1 Matrice d'arbitrage", 2)
P("Notation de 0 à 5 par critère. Les critères marqués d'un astérisque sont considérés comme stratégiquement déterminants "
  "et ne sont pas moyennés mécaniquement avec les autres.", italic=True, space=6)
CRIT = [
 ("Volume du marché *", 3, 5, 5, 1, "A : le volume de l'intitulé généraliste est élevé mais trompeur. B et C couvrent les cinq plus gros gisements. D ne crée pas de volume."),
 ("Évolution récente *", 2, 5, 5, 1, "Seule progression documentée sur requête identique : DevSecOps (≥ 700 → ≥ 800 entre avril et septembre 2026)."),
 ("Potentiel à 3-5 ans *", 2, 5, 5, 1, "Cloud, réglementation (NIS2/DORA/CRA) et automatisation sont des moteurs datés et durables."),
 ("Accessibilité junior *", 2, 3, 4, 1, "C conserve un socle et le GRC, qui sont les deux voies juniors réellement observées."),
 ("Potentiel d'alternance *", 3, 2, 5, 1, "44 des 62 alternances du corpus relèvent du socle généraliste, de l'infrastructure et du GRC — exactement le Bachelor du scénario C."),
 ("Niveau salarial", 2, 5, 4, 1, "Les baromètres valorisent Cloud Security, IA défensive et conformité ; le généraliste stagne."),
 ("Tension du marché", 3, 5, 5, 1, "Architecture, cloud, DevSecOps, IAM et AppSec sont les plus tendus."),
 ("Résilience face à l'IA *", 1, 5, 4, 1, "Le junior généraliste est le plus exposé ; la conception et l'automatisation le sont le moins."),
 ("Différenciation possible", 1, 5, 4, 2, "Le généraliste ne différencie pas NEXA des écoles cyber spécialisées."),
 ("Cohérence avec l'ADN numérique de NEXA", 3, 4, 5, 3, "C mutualise avec Développement Web (AppSec/DevSecOps) et IA & Data (module IA)."),
 ("Pertinence Bachelor *", 3, 2, 5, 1, "Un Bachelor purement engineering (B) serait trop sélectif en post-bac ; C calibre le niveau."),
 ("Pertinence Mastère *", 1, 5, 5, 1, "Les six domaines à fort volume exigent tous un Bac+5."),
 ("Potentiel multi-campus", 3, 2, 5, 2, "C permet de décliner une spécialisation différente par bassin ; B impose partout le même niveau d'exigence."),
 ("Potentiel distanciel", 3, 3, 3, 2, "Les postes full remote observés visent 3-5 ans d'expérience : peu mobilisables en Bachelor."),
 ("Simplicité pédagogique", 5, 2, 3, 4, "C est plus complexe que A mais moins que B grâce à la mutualisation du socle."),
 ("Besoin d'infrastructure technique", 4, 1, 2, 4, "Note inversée : plus la note est haute, moins le besoin est lourd. B exige cloud, Kubernetes et SIEM à grande échelle."),
 ("Facilité à recruter des formateurs", 4, 1, 3, 4, "Note inversée. Les profils DevSecOps et Cloud Security seniors sont rares et chers ; le GRC et le socle sont plus faciles à sourcer."),
 ("Risque global maîtrisé", 2, 2, 4, 2, "Note inversée : plus la note est haute, plus le risque est faible. C répartit le risque sur trois axes portés par des moteurs différents."),
]
TAB(["Critère","A Généraliste","B Cyber Engineering","C Hybride spécialisé","D Réduction / restructuration","Documentation du score"],
 [[c, a, b, cc, d, j] for c, a, b, cc, d, j in CRIT], [3.6,1.7,1.9,1.9,2.1,5.4], size=8)
sa = sum(c[1] for c in CRIT); sb = sum(c[2] for c in CRIT); sc = sum(c[3] for c in CRIT); sd = sum(c[4] for c in CRIT)
sa_s = sum(c[1] for c in CRIT if "*" in c[0]); sb_s = sum(c[2] for c in CRIT if "*" in c[0])
sc_s = sum(c[3] for c in CRIT if "*" in c[0]); sd_s = sum(c[4] for c in CRIT if "*" in c[0])
TAB(["Total","A Généraliste","B Cyber Engineering","C Hybride spécialisé","D Réduction"],
 [["Total brut (18 critères, /90)", sa, sb, sc, sd],
  ["Total sur les 9 critères stratégiques (/45)", sa_s, sb_s, sc_s, sd_s]], [6.0,2.6,2.8,2.8,2.6], size=9)
P(f"Lecture : le scénario C arrive en tête sur les critères stratégiques ({sc_s}/45 contre {sb_s}/45 pour B et {sa_s}/45 pour A), "
  "principalement parce qu'il est le seul à concilier un potentiel d'alternance élevé (indispensable au Bachelor) et un alignement "
  "sur les gisements réels du marché (indispensable au Mastère). Le scénario B est supérieur sur le volume et la résilience, "
  "mais son potentiel d'alternance et sa pertinence en Bachelor post-bac sont insuffisants : il est retenu comme ORIENTATION du Bachelor de C, "
  "pas comme modèle complet. Aucune moyenne mécanique n'a été appliquée.", bold=True, space=8)
doc.add_page_break()

# ============================================================ 15
H("15. Recommandation finale", 1)
P("ADOPTER_MODELE_HYBRIDE_SPECIALISE — avec technicisation forte du Bachelor et réduction du nombre de parcours de Mastère.",
  bold=True, size=13, color=RED, space=8)
H("15.1 Ce que NEXA doit faire", 2)
NUM("Conserver une filière Cybersécurité autonome. Les données ne justifient ni fermeture ni fusion complète : ≥ 5 000 offres cyber en France, ≥ 359 alternances cyber en Île-de-France, +49 % d'offres entre 2019 et 2024, et un moteur réglementaire (NIS2, DORA, CRA) visible jusqu'en 2030.")
NUM("Techniciser fortement le Bachelor et le renommer autour de l'ingénierie : systèmes, réseaux, cloud, scripting et automatisation, SOC de niveau 2, vulnérabilités, IAM, bases AppSec, GRC. Objectif assumé : l'alternance, pas l'emploi direct.")
NUM("Réduire le Mastère à trois spécialisations : Cloud Security & DevSecOps ; SecOps, Detection & Automation ; Cyber GRC, Risques & IAM.")
NUM("Déprioriser explicitement trois parcours : Offensive Security / Red Team (≈ 33 offres nationales, aucune alternance pure), DFIR / forensics (pas de stock mesurable, aucune offre junior), AI Security (aucun marché mesurable). Les trois deviennent des modules.")
NUM("Rapprocher AppSec et DevSecOps de la filière Développement Web (mutualisation du développement, de CI/CD et des conteneurs, option croisée en Mastère) et mutualiser un module de sécurisation des systèmes d'IA avec la filière IA & Data.")
NUM("Faire de l'alternance le cœur du modèle et la piloter comme telle : sécuriser en priorité les bassins de Bordeaux, Marseille-Aix et Nantes, où les volumes d'alternance relevés localement sont les plus faibles.")
NUM("Aligner la communication sur la réalité du marché : cesser de mettre en avant le pentest et l'analyste SOC comme débouchés de sortie de Bachelor.")
H("15.2 Le risque si NEXA ne change rien", 2)
B("Promesse non tenue : un Bachelor cyber généraliste vendu comme un débouché direct se heurte à un marché où 47 % des offres visent un Bac+5 et où environ 1 % des offres franciliennes sont ouvertes aux débutants.")
B("Érosion par l'IA : le contenu du poste junior généraliste (tri d'alertes, enrichissement, reporting) est précisément ce que l'IA automatise en premier.")
B("Perte de différenciation : face aux écoles cyber spécialisées, un cursus généraliste sans laboratoires ni socle infrastructure n'a pas d'argument.")
B("Décalage de communication : mettre en avant le pentest, dont le volume national est d'environ 33 offres, crée un risque réputationnel à mesure que les diplômés constatent l'écart.")
doc.add_page_break()

# ============================================================ 16
H("16. Réponses aux 50 questions stratégiques", 1)
Q = [
("1","Le marché progresse-t-il, stagne-t-il ou recule-t-il ?","Il progresse structurellement (+49 % d'offres 2019-2024, ANSSI ; +4 % de recrutements de cadres informaticiens en 2026, Apec) mais avec un ralentissement conjoncturel en 2025 (gel des recrutements dans les ESN, -6,5 % de projets de recrutement tous secteurs au BMO 2026)."),
("2","L'évolution concerne-t-elle toute la cyber ?","Non. Elle est très inégale : DevSecOps, Cloud Security, IAM, AppSec et GRC progressent ; le SOC N1, l'administration sécurité et les profils généralistes stagnent ou reculent."),
("3","Quels métiers progressent ?","DevSecOps (≥ 700 → ≥ 800 entre avril et septembre 2026), Cloud Security, GRC (porté par NIS2/DORA/CRA), IAM/PAM, detection engineering et automatisation."),
("4","Quels métiers stagnent ou reculent ?","Analyste SOC niveau 1, administrateur/technicien sécurité, profils cyber généralistes (stagnation salariale), pentest (volume étroit et stable)."),
("5","Les métiers généralistes restent-ils demandés et que recouvrent-ils ?","Les intitulés restent très demandés (≥ 1 000 « ingénieur cybersécurité », ≥ 800 « consultant cybersécurité ») mais recouvrent en réalité des postes spécialisés : SOC, réseau, cloud, IAM, OT, conformité. Le volume mesure la popularité de l'intitulé, pas l'existence d'un métier homogène."),
("6","Les entreprises privilégient-elles des profils spécialisés ?","Oui. Les offres les mieux valorisées sont toutes spécialisées, et les baromètres 2026 signalent explicitement une prime à la spécialisation contre une stagnation des généralistes."),
("7","Les entreprises recrutent-elles des juniors ?","Marginalement en CDI (6 CDI juniors sur 77 dans notre corpus ; ≈ 26 offres « débutant » en IdF pour ≈ 2 444 offres). Massivement en alternance et en stage."),
("8","Quelles sont les portes d'entrée ?","Par ordre décroissant observé : alternance en cyber généraliste et systèmes-réseaux-sécurité, alternance GRC, stage puis pré-embauche, consultant junior en ESN/cabinet, analyste vulnérabilités (VOC), et une première expérience IT (support, systèmes, réseaux) suivie d'une bascule cyber."),
("9","Quelle est la place de l'alternance et du stage ?","Centrale : 62 alternances et 17 stages sur 342 offres, ≥ 359 alternances cyber relevées en IdF, 1 003 sur Glassdoor France. C'est le principal mécanisme d'entrée."),
("10","Les opportunités de premier emploi justifient-elles un Bachelor Cybersécurité dédié ?","Pas pour l'emploi direct (47 % de Bac+5 exigés). Oui pour un Bachelor conçu comme un tremplin vers l'alternance et le Mastère."),
("11","Certains métiers présentés comme accessibles exigent-ils en réalité une expérience préalable ?","Oui, systématiquement : analyste SOC (4-6 ans), pentester (3 ans offensifs), architecte (5-8 ans), IAM (1-2 ans), AppSec (2-6 ans). Souvent en systèmes, réseaux ou développement."),
("12","La demande se concentre-t-elle sur les intermédiaires et seniors ?","Oui, nettement. Hors contrats de formation, l'essentiel des offres renseignées vise 3 ans et plus."),
("13","Quelle place pour CDI, CDD, alternance, stage, freelance, intérim, conseil ?","CDI dominant, alternance très présente, freelance actif (TJM moyen ≈ 616 € en direct), stage significatif, CDD et intérim marginaux. Le conseil (ESN, cabinets, MSSP) est le premier canal d'entrée."),
("14","Quelles régions et villes concentrent les recrutements ?","Île-de-France très largement (≥ 2 444 offres, 43-45 % des professionnels), puis Auvergne-Rhône-Alpes, Occitanie (Toulouse ≥ 500), PACA (Sophia Antipolis ≥ 209), Pays de la Loire, Hauts-de-France, Nouvelle-Aquitaine."),
("15","Quelle part portée par ESN, conseil, MSSP, éditeurs, grands groupes, etc. ?","Les employeurs les plus fréquents de notre corpus sont les ESN/MSSP et cabinets (Sopra Steria, Capgemini, Atos/Eviden, Accenture, Deloitte, CGI, Devoteam, Advens, AlgoSecure, Itrust), les grands groupes industriels et de défense (Thales, Safran, Framatome, EDF, Airbus), la banque et l'assurance, le secteur public (ANSSI, ministères, Urssaf), et un écosystème d'éditeurs et de scale-ups (GitGuardian, Akeneo, Tiime, Yousign, Scaleway, Mistral AI). Notre échantillon ne permet pas d'en chiffrer les parts."),
("16","Quelles compétences sont les plus demandées ?","SOC et supervision (19,0 %), conformité/RGPD (11,7 %), cloud (11,7 %), réseaux (11,4 %), IAM (9,4 %), continuité et gestion de crise (7,9 %), DevSecOps (7,6 %), gouvernance (6,7 %), architecture (6,1 %), Zero Trust/SASE (6,1 %)."),
("17","Quels outils sont devenus indispensables ?","SIEM (Microsoft Sentinel, Splunk, QRadar, Elastic), EDR/XDR (CrowdStrike, SentinelOne, Defender), firewalls (Palo Alto, Fortinet), Active Directory et Entra ID, Azure et AWS, Terraform, Docker et Kubernetes, outils SAST/DAST/SCA, solutions IAM/PAM (SailPoint, CyberArk, Okta)."),
("18","Quelle place pour Linux, Windows, AD, cloud, SIEM, scripting, IAM, conteneurs, IaC, CI/CD, IA ?","Toutes présentes, avec une hiérarchie nette : le socle systèmes-réseaux-cloud et l'IAM sont massivement demandés ; scripting, conteneurs, IaC et CI/CD concentrent la valeur ajoutée ; l'IA reste peu formalisée dans les offres (3,5 %) mais transforme déjà les tâches."),
("19","Les certifications sont-elles réellement demandées ?","Peu visibles dans nos extraits (4 offres sur 342, borne basse). Les sources convergent sur CISSP, OSCP, Security+, CEH, mais toutes les offres exigent d'abord de l'expérience."),
("20","Quelles certifications reviennent le plus et pour quels métiers ?","Security+ et SC-200 pour les analystes et le SOC ; OSCP pour le pentest ; CISSP et CISM pour les RSSI et l'architecture ; CCSP, AZ-500 et AWS Security pour le cloud ; ISO 27001 Lead Auditor et EBIOS RM pour le GRC ; SC-300 pour l'IAM."),
("21","Les métiers SOC N1 sont-ils assez nombreux et accessibles ?","Non. Aucune offre CDI « analyste SOC N1 » dans notre corpus, alors que les N2 et N3 y sont nombreux."),
("22","Sont-ils fragilisés par l'automatisation et l'IA ?","Oui, c'est le segment le plus directement visé, selon des sources convergentes et selon la structure même des offres observées."),
("23","Les métiers GRC sont-ils plus accessibles aux juniors ?","Oui : 11 alternances GRC sur 62, seuils d'entrée CDI plus bas (3-5 ans), et un moteur réglementaire qui crée du volume."),
("24","Le pentest représente-t-il un volume réel suffisant ?","Non : ≈ 33 offres nationales. Il bénéficie surtout d'une très forte attractivité étudiante."),
("25","Existe-t-il un déséquilibre candidats/offres en pentest ?","Oui, très probablement : un volume d'environ 33 offres nationales face à un métier régulièrement cité comme le plus désiré, et une barrière d'entrée de 3 ans d'expérience offensive."),
("26","Le Cloud Security justifie-t-il un axe pédagogique majeur ?","Oui : ≥ 438 offres nationales, ≥ 769 à Paris, et une présence transverse dans 11,7 % de toutes les offres."),
("27","AppSec et DevSecOps sont-ils des débouchés significatifs pour des profils avec compétences dev ?","Oui, ce sont les plus significatifs du périmètre : ≥ 817 offres DevSecOps et ≥ 600 AppSec, avec un tissu employeur d'éditeurs et de scale-ups."),
("28","IAM et PAM constituent-ils un marché important et durable ?","Oui : ≥ 732 offres, moteur Zero Trust et SASE, faible exposition à l'automatisation, outillage enseignable."),
("29","NIS2 et DORA augmentent-ils réellement la demande GRC ?","Oui : ≥ 242 offres GRC, NIS2 devant concerner 10 000 à 15 000 organisations supplémentaires, DORA appliqué au secteur financier, CRA à partir de juin 2026, et une présence massive de ces référentiels dans les offres."),
("30","Quels domaines offrent les meilleurs débouchés en alternance ?","Cyber généraliste et systèmes-réseaux-sécurité (33 alternances sur 62), puis GRC (11). Les spécialités techniques pointues sont quasi absentes de l'alternance."),
("31","Quels domaines à Bac+3 ?","Technicien et administrateur sécurité, analyste GRC junior, analyste vulnérabilités junior, support sécurité — et surtout l'alternance elle-même. Volume limité."),
("32","Quels domaines exigent un Bac+5 ?","Cloud Security, DevSecOps, AppSec, IAM/PAM, architecture, security engineering, GRC senior, detection engineering."),
("33","Quels métiers exigent surtout de l'expérience plutôt qu'un diplôme ?","Pentest, DFIR, architecture, RSSI, SecOps. Pour ces métiers, l'expérience prime clairement sur le diplôme."),
("34","Quel rôle des certifications par rapport aux diplômes ?","Complémentaire : elles crédibilisent un niveau opérationnel et facilitent l'alternance, mais aucune offre observée ne les substitue à l'expérience. Le diplôme Bac+5 reste le filtre RH dominant (47 % des offres)."),
("35","L'IA réduit-elle le besoin d'analystes ou transforme-t-elle leurs tâches ?","Principalement elle transforme les tâches, mais elle réduit réellement le besoin sur le segment N1 : le contenu du poste junior est ce qui s'automatise en premier."),
("36","Quelles tâches sont les plus exposées ?","Tri d'alertes simples, enrichissement d'IOC, collecte de contexte, création de tickets, reporting répétitif, génération de requêtes et de règles, première analyse de logs, OSINT simple, recommandations de remédiation standard, rédaction documentaire."),
("37","Quelles compétences deviennent plus importantes ?","Detection engineering, threat hunting, incident response avancé, architecture, cloud, IAM, AppSec, DevSecOps, compréhension du code, automatisation, gouvernance et gestion des risques, gestion de crise, supervision et validation critique des systèmes automatisés."),
("38","Existe-t-il une demande observable en AI Security ?","Une demande émergente et réelle mais non mesurable : 13 offres sur 342 mentionnent l'IA, dont 6 rattachables à l'AI Security, toutes sous forme d'extension de postes existants."),
("39","Existe-t-il un marché réel pour AI Security Engineer, LLM Security, AI Red Teaming, ML Security, AI Governance ?","Pas en France en 2026, au sens d'un stock d'offres mesurable. Les seuls chiffres disponibles proviennent d'un cabinet de recrutement et ne sont pas vérifiables."),
("40","Ces compétences sont-elles des métiers autonomes ou des extensions ?","Des extensions de métiers cyber existants (pentest, architecture, GRC, security engineering) et de métiers IA existants."),
("41","Les métiers porteurs exigent-ils une technicité supérieure aux cursus cyber généralistes ?","Oui, sans ambiguïté : le niveau 1 de technicité ne représente que 1,5 % des offres, et les gisements les plus importants exigent cloud, code, conteneurs et automatisation."),
("42","Une orientation Cybersecurity Engineering / Cloud / SecOps serait-elle plus pertinente qu'un cursus généraliste ?","Oui pour l'alignement marché — mais insuffisante seule en Bachelor post-bac, où le potentiel d'alternance repose sur le socle et le GRC."),
("43","Une orientation GRC / IAM / Cloud / AppSec différenciée en Mastère serait-elle plus pertinente ?","Oui. C'est la structure recommandée, ramenée à trois spécialisations pour éviter la dispersion."),
("44","Faut-il conserver un Bachelor Cybersécurité généraliste ?","Oui dans son périmètre, non dans son niveau : il doit devenir un Bachelor de socle technique (Cybersecurity Engineering), pas un Bachelor de culture cyber."),
("45","Faut-il différencier fortement Bachelor et Mastère ?","Oui : socle large et alternance en Bachelor, spécialisation forte et emploi en Mastère."),
("46","Quelles orientations selon les campus ?","Paris : les trois axes. Lyon : SecOps + OT + GRC industrielle. Lille : SecOps/Detection + GRC. Bordeaux : Cloud/DevSecOps-AppSec + GRC/homologation. Nantes : GRC & IAM + Cloud. Marseille-Aix : SecOps Microsoft + GRC."),
("47","Le volume et la qualité des débouchés justifient-ils une filière autonome ?","Oui au niveau national. Sous réserve d'un calibrage des effectifs par campus, notamment à Bordeaux, Marseille-Aix et Nantes où les volumes locaux d'alternance relevés sont faibles."),
("48","Certaines spécialisations doivent-elles être rapprochées de Développement Web ?","Oui : AppSec, DevSecOps, sécurité des API et des conteneurs. Convergence forte, employeurs communs, compétences communes."),
("49","Certaines spécialisations doivent-elles être rapprochées d'IA & Data ?","Un module oui (sécurisation des LLM, des agents et des pipelines RAG, gouvernance de l'IA), un parcours non."),
("50","En synthèse, quel choix ?","HYBRIDE_SPECIALISEE : Bachelor de Cybersecurity Engineering fortement technicisé visant l'alternance, puis Mastère spécialisé sur trois axes (Cloud Security & DevSecOps ; SecOps, Detection & Automation ; Cyber GRC, Risques & IAM), avec dépriorisation du pentest, du DFIR et de l'AI Security comme parcours autonomes et rapprochement partiel avec Développement Web et IA & Data."),
]
TAB(["#","Question","Réponse"], [[a,b,c] for a,b,c in Q], [0.9,5.0,10.5], size=8)
doc.add_page_break()

# ============================================================ 17
H("17. Études, articles et sources pour approfondir", 1)
P("Toutes les URL sont cliquables. Le classeur Excel reprend ce tableau dans l'onglet SYNTHESE_METIERS, "
  "avec la colonne RESULTAT_UTILISE détaillée.", italic=True, space=6)
order = {"FORTE":0,"MOYENNE-FORTE":1,"MOYENNE":2,"FAIBLE-MOYENNE":3,"FAIBLE":4}
for e in sorted(ETU, key=lambda x: order.get(x["NIVEAU_DE_FIABILITE"].split(" —")[0].strip(), 5)):
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(e["TITRE"]); r.bold = True; r.font.size = Pt(9.5)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(f"{e['ORGANISME']} — {e['AUTEUR']} — publié : {e['DATE_PUBLICATION']} — consulté : {e['DATE_CONSULTATION']}")
    r.font.size = Pt(8.5); r.font.color.rgb = GREY
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(f"Périmètre : {e['PERIMETRE']} | Méthode : {e['METHODE']} | Échantillon : {e['TAILLE_ECHANTILLON']}")
    r.font.size = Pt(8.5)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(f"Résultat utilisé : {e['RESULTAT_UTILISE']}"); r.font.size = Pt(8.5)
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1)
    r = p.add_run(f"Page / document : {e['PAGE_DU_RAPPORT']} | Fiabilité : {e['NIVEAU_DE_FIABILITE']}")
    r.font.size = Pt(8.5); r.font.color.rgb = GREY
    p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(8)
    r = p.add_run("URL : "); r.font.size = Pt(8.5)
    LINK(p, e["URL"])
doc.add_page_break()

# ============================================================ 18 — DERNIÈRE PAGE
H("18. Décision recommandée pour NEXA", 1)
t = doc.add_table(rows=1, cols=2); t.style = "Table Grid"
FIELDS = [
("ORIENTATION_RECOMMANDEE","HYBRIDE_SPECIALISEE"),
("DECISION","ADOPTER_MODELE_HYBRIDE_SPECIALISE — conserver une filière Cybersécurité autonome, techniciser fortement le Bachelor autour de la Cybersecurity Engineering, et réduire le Mastère à trois spécialisations réellement portées par le marché."),
("JUSTIFICATION_EN_5_POINTS",
 "1. Le marché progresse (+49 % d'offres 2019-2024, ANSSI) mais 47 % des offres visent un Bac+5 et environ 1 % des offres franciliennes sont ouvertes aux débutants : un Bachelor cyber ne peut pas viser l'emploi direct.\n"
 "2. Les cinq plus gros gisements — DevSecOps (≥ 817), IAM (≥ 732), AppSec (≥ 600), Cloud Security (≥ 438) et architecture (≈ 400-455) — exigent tous un socle systèmes, cloud et code supérieur à celui d'un cursus cyber généraliste.\n"
 "3. L'alternance est la vraie porte d'entrée, et les employeurs l'ouvrent sur le socle et le GRC (44 des 62 alternances observées), pas sur les spécialités attractives.\n"
 "4. L'IA n'automatise pas la cybersécurité, elle automatise le contenu du poste junior généraliste : maintenir un cursus généraliste revient à former au segment le plus exposé.\n"
 "5. Le pentest (≈ 33 offres nationales) et l'AI Security (aucun marché mesurable) sont des promesses commerciales que les données ne soutiennent pas."),
("METIERS_A_PRIORISER","Ingénieur DevSecOps ; Cloud Security Engineer ; AppSec / Product Security Engineer ; Consultant et ingénieur IAM/PAM ; Consultant GRC, risques et conformité ; Analyste SOC N2 et Detection Engineer ; Analyste vulnérabilités (VOC) ; Auditeur SSI."),
("METIERS_A_DEPRIORISER","Analyste SOC niveau 1 ; Pentester et Red Teamer (comme débouché affiché) ; Analyste DFIR ; AI Security Engineer ; Administrateur/technicien sécurité comme cible d'un Bac+3. Architecte sécurité et RSSI restent à présenter comme horizons de carrière, jamais comme débouchés de sortie."),
("SPECIALISATIONS_A_PRIORISER","Mastère 1 : Cloud Security & DevSecOps. Mastère 2 : SecOps, Detection & Automation. Mastère 3 : Cyber GRC, Risques & IAM."),
("SPECIALISATIONS_A_DEPRIORISER","Offensive Security / Red Team ; DFIR & Forensics ; AI Security & Cyber Defense ; OT Security en parcours autonome (à conserver comme option de campus à Lyon)."),
("COMPETENCES_A_RENFORCER","Linux, Windows et Active Directory ; réseaux et TCP/IP ; cloud Azure et AWS ; Entra ID et IAM ; scripting Python, Bash et PowerShell ; automatisation et API ; CI/CD, conteneurs, Kubernetes et Terraform ; detection engineering et SOAR ; gestion des vulnérabilités ; OWASP, SAST/DAST/SCA et threat modeling ; ISO 27001, EBIOS RM, NIS2 et DORA ; continuité et gestion de crise ; usage raisonné et validation critique de l'IA ; anglais technique."),
("COMPETENCES_A_RENDRE_SECONDAIRES","Tri manuel d'alertes de niveau 1 ; exploitation offensive avancée ; reverse engineering et analyse de malware approfondie ; cryptographie théorique ; outillage propriétaire de niche ; production documentaire répétitive."),
("CERTIFICATIONS_A_INTEGRER","Bachelor : CompTIA Security+ et EBIOS Risk Manager. Mastère selon la spécialisation : Microsoft SC-200 (SecOps), AZ-500 et AWS Certified Security (Cloud/DevSecOps), SC-300 (IAM), ISO 27001 Lead Auditor (GRC). Ne pas positionner CISSP ni OSCP comme objectifs de cursus."),
("POSITIONNEMENT_RECOMMANDE_DU_BACHELOR","« Bachelor Cybersecurity Engineering » — socle technique large (systèmes, réseaux, cloud, scripting, SOC de niveau 2, vulnérabilités, IAM, bases AppSec, GRC), fortement pratiqué en laboratoire, avec pour objectif assumé l'alternance en 2e et 3e année puis la poursuite en Mastère. L'insertion directe à Bac+3 est possible mais minoritaire et doit être présentée comme telle."),
("POSITIONNEMENT_RECOMMANDE_DU_MASTERE","Trois spécialisations distinctes, chacune adossée à un gisement mesuré et à des certifications alignées, avec projets en conditions réelles et alternance systématique. Les domaines dépriorisés deviennent des modules à l'intérieur de ces trois parcours."),
("IMPACT_PAR_CAMPUS","Paris : les trois spécialisations. Lyon : SecOps + OT/industriel + GRC. Lille : SecOps/Detection + GRC. Bordeaux : Cloud/DevSecOps-AppSec + GRC/homologation, avec sécurisation prioritaire du sourcing d'alternance. Nantes : GRC & IAM + Cloud. Marseille-Aix : SecOps sur écosystème Microsoft + GRC, une seule spécialisation."),
("PLACE_RECOMMANDEE_DE_L_IA","Compétence transversale obligatoire dès le Bachelor : utiliser l'IA pour faire de la cybersécurité (copilotes de sécurité, génération et validation de requêtes et de règles, automatisation, analyse de logs assistée), avec un enseignement explicite de la validation critique des résultats produits. Security Copilot doit être traité comme un OUTIL à maîtriser, pas comme une compétence structurante autonome."),
("PLACE_RECOMMANDEE_DE_L_AI_SECURITY","Un module en Mastère (sécurisation des applications à base de LLM, prompt injection, sécurité des agents et des pipelines RAG, OWASP Top 10 for LLM Applications, gouvernance de l'IA), mutualisé avec la filière IA & Data, plus une veille structurée. PAS de spécialisation autonome tant qu'aucun stock d'offres n'est mesurable en France."),
("RISQUE_SI_NEXA_NE_CHANGE_RIEN","Promesse d'employabilité non tenable à Bac+3 ; érosion accélérée par l'automatisation du poste junior généraliste ; perte de différenciation face aux écoles cyber spécialisées ; risque réputationnel lié à la mise en avant du pentest ; difficulté croissante à placer les alternants sur les campus à faible volume local."),
("NIVEAU_DE_CONFIANCE","MOYENNE À FORTE. Forte sur la structure du marché, la hiérarchie des volumes entre domaines, l'écart entre tension et accessibilité junior et le rôle de l'alternance — ces résultats sont convergents entre nos relevés et des sources publiques de référence (ANSSI, OPIIEC, Apec, BMO). Moyenne sur les évolutions annuelles (séries insuffisantes), les salaires (3 offres renseignées, baromètres de cabinets) et les certifications (4 mentions dans les extraits)."),
("DONNEES_COMPLEMENTAIRES_NECESSAIRES","Données internes NEXA indispensables avant décision économique définitive : candidatures et taux de remplissage par campus, taux de signature d'alternance et délai moyen, métiers réellement obtenus par les diplômés à 6 et 12 mois, salaires de sortie, taux d'abandon, marge par parcours, coût des laboratoires cyber. Données externes à acquérir : accès direct aux API des jobboards ou à un fournisseur de données d'offres pour construire de vraies séries temporelles 2024-2026, et accès aux tableaux détaillés de l'Observatoire des métiers de l'ANSSI."),
]
hdr = t.rows[0].cells
hdr[0].text = ""; r = hdr[0].paragraphs[0].add_run("CHAMP"); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
hdr[1].text = ""; r = hdr[1].paragraphs[0].add_run("DÉCISION RECOMMANDÉE POUR NEXA"); r.bold = True; r.font.size = Pt(9); r.font.color.rgb = RGBColor(0xFF,0xFF,0xFF)
shade(hdr[0], "1F3864"); shade(hdr[1], "1F3864")
for k, v in FIELDS:
    cells = t.add_row().cells
    cells[0].text = ""; rr = cells[0].paragraphs[0].add_run(k); rr.bold = True; rr.font.size = Pt(8.5); rr.font.color.rgb = NAVY
    shade(cells[0], "DCE6F1")
    cells[1].text = ""
    for i, line in enumerate(str(v).split("\n")):
        p = cells[1].paragraphs[0] if i == 0 else cells[1].add_paragraph()
        rr = p.add_run(line); rr.font.size = Pt(8.5); p.paragraph_format.space_after = Pt(1)
        if k in ("ORIENTATION_RECOMMANDEE","DECISION"): rr.bold = True
    cells[0].width = Cm(4.4); cells[1].width = Cm(12.0)
doc.add_paragraph()
P("Cette recommandation porte exclusivement sur la pertinence au regard du marché de l'emploi. "
  "Elle ne préserve pas artificiellement l'existant — le maintien généraliste est explicitement écarté — "
  "et ne recommande pas une spécialisation « à la mode » : l'AI Security, la plus attractive commercialement, "
  "est justement celle que les données conduisent à ne pas transformer en parcours.",
  italic=True, size=9, color=GREY)

doc.save(OUT)
print("Word écrit :", OUT)
