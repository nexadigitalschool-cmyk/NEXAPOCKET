#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Livrable 3 — NEXA_Perimetre_Metiers_Marketing_et_Plateformes_Sans_Donnees.md"""
import json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize_mkt as N

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BASE = os.path.join(ROOT, "collecte_mkt")
D = json.load(open(os.path.join(BASE, "mkt_consolide.json"), encoding="utf-8"))
OFFRES = json.load(open(os.path.join(BASE, "mkt_offres_normalisees.json"), encoding="utf-8"))
META = D["meta"]

# requêtes réellement lancées, avec le nombre d'offres retenues
req = collections.Counter(o["REQUETE"] for o in OFFRES)

L = []
A = L.append
A("# NEXA — Périmètre des métiers du Marketing Digital et plateformes sans données")
A("")
A("**Étude :** Observatoire du marché de l'emploi du marketing digital en France · **Date de collecte :** 7 septembre 2026")
A("")
A("Ce fichier constitue le **journal séparé de la collecte**. Il contient la taxonomie complète des métiers retenus "
  "et écartés (partie A) et le relevé des plateformes et chemins d'accès testés sans résultat exploitable (partie B). "
  "Ces éléments n'alourdissent volontairement pas le document de synthèse Word.")
A("")
A(f"**Volumétrie de la collecte :** {META['volume_brut']} lignes d'offres collectées · "
  f"{META['offres_uniques']} offres uniques après dédoublonnage (taux de doublons {META['taux_doublons']} %) · "
  f"{META['offres_dans_perimetre']} dans le périmètre marketing digital · "
  f"{META['offres_coeur_marketing_digital']} au cœur du marketing digital hors métiers adjacents · "
  f"{META['offres_exclues']} exclues comme faux positifs · "
  f"{META['nb_volumes']} stocks d'offres datés · {META['nb_etudes']} sources documentaires.")
A("")
A("**Statuts de dédoublonnage observés :** " + " · ".join(f"{k} : {v}" for k, v in sorted(META["statuts_doublon"].items(), key=lambda x:-x[1])))
A("")
A("---")
A("")

# ============================================================ PARTIE A
A("## PARTIE A — TAXONOMIE DES MÉTIERS")
A("")
A("### A.0 Méthode de classification")
A("")
A("Chaque intitulé brut d'offre est passé dans un jeu de **64 règles ordonnées** (des plus spécifiques aux plus "
  "générales) qui produisent trois valeurs : un métier normalisé, une famille et un niveau de technicité de base. "
  "Le niveau de technicité final est ensuite recalculé à partir des compétences réellement détectées dans le titre "
  "et l'extrait de l'offre, selon l'échelle suivante :")
A("")
A("| Niveau | Définition | Déclencheurs |")
A("|---|---|---|")
A("| 1 | Généraliste / exécution | Publication réseaux sociaux, rédaction simple, emailing simple, coordination, animation, mise à jour de contenus |")
A("| 2 | Expertise canal | SEO, SEA, Paid Social, CRM, e-commerce, content strategy, influence, plateformes publicitaires |")
A("| 3 | Performance / data / automation | GA4, GTM, tracking, attribution, CRO, CRM automation, dashboards, segmentation, no-code, agents IA |")
A("| 4 | MarTech / data / systèmes | CDP, SQL, BigQuery, data warehouse, API, gouvernance de la donnée, Python |")
A("")
A("Une offre atteint le niveau 4 dès qu'une compétence de niveau 4 est détectée ; le niveau 3 requiert deux "
  "compétences de niveau 3 (ou une seule si le métier est déjà de technicité de base 3).")
A("")
A("### A.1 Familles retenues")
A("")
A("| Famille | Offres uniques | Part du périmètre | Technicité moyenne | Alternance | Débutants + juniors |")
A("|---|---|---|---|---|---|")
for f, b in sorted(D["par_famille"].items(), key=lambda x: -x[1]["n"]):
    A(f"| `{f}` | {b['n']} | {round(100*b['n']/META['offres_dans_perimetre'],1)} % | {b['technicite_moy']} | {b['alternance_pct']} % | {b['debutant_junior_pct']} % |")
A("")
A(f"À ces familles s'ajoute `EXCLU_DU_PERIMETRE` : {META['offres_exclues']} offres écartées comme faux positifs "
  "(voir A.4).")
A("")

# --- fiches métiers
A("### A.2 Fiches métiers observés dans l'étude")
A("")
VAR_FR = {}
VAR_EN = {}
for o in OFFRES:
    m = o["METIER_NORMALISE"]
    VAR_FR.setdefault(m, set()).add(o["INTITULE_BRUT"])

OUTILS_PAR_FAMILLE = {
 "COEUR_GENERALISTE": "WordPress, CMS, Google Analytics 4, Google Tag Manager, HubSpot, Canva, suite Adobe, Google Ads, Meta Ads",
 "ACQUISITION_PERFORMANCE": "Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio",
 "SEO_SEA": "Google Search Console, Semrush, Ahrefs, Screaming Frog, Oncrawl, Majestic, Google Ads, Microsoft Ads, données structurées, Core Web Vitals",
 "SOCIAL_MEDIA": "Meta Business Suite, Instagram, TikTok, LinkedIn, YouTube, Pinterest, outils de planification éditoriale",
 "CONTENT_BRAND": "CMS, outils rédactionnels, suite Adobe, outils de montage vidéo, plateformes d'influence",
 "CRM_LIFECYCLE": "HubSpot, Salesforce et Marketing Cloud, Pardot, Braze, Klaviyo, Brevo, Adobe Campaign, ActiveCampaign, Splio, Dotdigital, Actito, Dartagnan",
 "ECOMMERCE": "Shopify, PrestaShop, Magento, marketplaces Amazon et Cdiscount, outils de gestion de flux produits, e-merchandising",
 "DATA_ANALYTICS_CRO": "Google Analytics 4, Google Tag Manager, Looker Studio, Matomo, Adobe Analytics, Amplitude, Mixpanel, Piano Analytics, SQL, BigQuery, Power BI, AB Tasty, Kameleoon, Contentsquare, Hotjar",
 "MARTECH_MARKETING_OPS": "Customer Data Platform (Adobe Experience Platform, Salesforce Data Cloud, Sitecore CDP, BlueConic, Treasure Data, Imagino), Salesforce, HubSpot, BigQuery, Databricks, APIs, Zapier, Make, n8n",
 "PRODUCT_MARKETING": "HubSpot, Salesforce, outils de recherche utilisateur, outils de go-to-market, analytics produit",
 "METIER_IA_EMERGENT": "ChatGPT, Claude, Gemini, Copilot, Midjourney, Adobe Firefly, n8n, Make, Zapier, outils GEO/AEO, agents IA, MCP",
 "METIER_ADJACENT": "CRM, outils de prospection, PipeDrive, HubSpot, outils marketing généralistes",
}
PROXIMITE = {
 "COEUR_GENERALISTE": "CENTRALE", "ACQUISITION_PERFORMANCE": "CENTRALE", "SEO_SEA": "CENTRALE",
 "SOCIAL_MEDIA": "CENTRALE", "CONTENT_BRAND": "CENTRALE", "CRM_LIFECYCLE": "CENTRALE",
 "ECOMMERCE": "CENTRALE", "DATA_ANALYTICS_CRO": "FORTE", "MARTECH_MARKETING_OPS": "FORTE",
 "PRODUCT_MARKETING": "FORTE", "METIER_IA_EMERGENT": "FORTE", "METIER_ADJACENT": "PERIPHERIQUE",
 "EXCLU_DU_PERIMETRE": "NULLE",
}
JUSTIF = {
 "METIER_ADJACENT": "Identifié et tracé, mais **non comptabilisé dans les volumes du cœur marketing digital** : "
   "débouché possible pour un diplômé marketing, sans relever du marketing digital au sens strict.",
 "EXCLU_DU_PERIMETRE": "Exclu : aucune finalité marketing identifiable dans l'offre.",
}
for m, b in sorted(D["par_metier"].items(), key=lambda x: (x[1]["famille"], -x[1]["n"])):
    fam = b["famille"]
    var = sorted(VAR_FR.get(m, []))
    fr = [v for v in var if not any(k in v.lower() for k in ("manager","specialist","analyst","growth","lead","head","content","social","product","paid","traffic","search","campaign","builder","officer"))]
    en = [v for v in var if v not in fr]
    A(f"#### {m}")
    A("")
    A(f"- **FAMILLE :** `{fam}`")
    A(f"- **INCLUS_OU_EXCLU :** {'INCLUS' if fam not in ('EXCLU_DU_PERIMETRE',) else 'EXCLU'}"
      + (" (tracé mais hors volumes du cœur)" if fam == "METIER_ADJACENT" else ""))
    A(f"- **NIVEAU_TECHNICITE :** {b['technicite_moy']} (moyenne observée sur {b['n']} offres)")
    A(f"- **PROXIMITE_AVEC_MARKETING_DIGITAL :** {PROXIMITE.get(fam,'NC')}")
    A(f"- **VARIANTES_FRANCAISES :** {' · '.join(fr[:6]) if fr else 'aucune variante française observée'}")
    A(f"- **VARIANTES_ANGLAISES :** {' · '.join(en[:6]) if en else 'aucune variante anglaise observée'}")
    A(f"- **COMPETENCES_ASSOCIEES :** {' · '.join(c for c,_ in b['competences_top'][:8]) if b['competences_top'] else 'non renseignées dans les extraits'}")
    A(f"- **OUTILS_ASSOCIES :** {OUTILS_PAR_FAMILLE.get(fam,'NC')}")
    A(f"- **JUSTIFICATION :** {JUSTIF.get(fam, 'Métier du périmètre marketing digital, retenu dans les volumes.')} "
      f"Observé sur {b['n']} offres uniques ({b['part_marche']} % du périmètre), issues de {b['sources']} plateforme(s) différente(s).")
    reqs = sorted({o["REQUETE"] for o in OFFRES if o["METIER_NORMALISE"] == m})[:4]
    A("- **REQUETES_UTILISEES :**")
    for r_ in reqs:
        A(f"  - `{r_}`")
    A("")

# --- taxonomie initiale non observée
A("### A.3 Métiers de la taxonomie initiale non observés dans la collecte")
A("")
A("Ces intitulés figuraient dans la cartographie de départ mais **aucune offre individuelle correspondante n'a été "
  "trouvée** sur les pages publiques indexées. Leur absence est un résultat en soi : elle indique que ces "
  "dénominations ne sont pas utilisées par les employeurs français, ou que leur volume est trop faible pour "
  "remonter dans les moteurs.")
A("")
A("| Intitulé recherché | Famille visée | Résultat | Lecture |")
A("|---|---|---|---|")
NON_OBS = [
 ("User Acquisition Manager","ACQUISITION_PERFORMANCE","Aucune offre isolée","Le poste existe (Performance Marketing Manager Gaming chez Voodoo mentionne l'user acquisition) mais l'intitulé n'est pas autonome en France."),
 ("Growth Hacker","ACQUISITION_PERFORMANCE","2 offres, uniquement en alternance","Intitulé résiduel, employé surtout par des organismes de formation et non par des annonceurs."),
 ("Demand Generation Manager","ACQUISITION_PERFORMANCE","Aucune offre sous cet intitulé exact","Le concept apparaît dans les descriptions (lead generation, Artur'In) mais pas dans les titres français."),
 ("Search Engine Marketing Specialist","SEO_SEA","Aucune offre","Le marché français utilise SEA, Paid Search ou Traffic Manager."),
 ("Technical SEO Specialist","SEO_SEA","Aucune offre sous cet intitulé","Le SEO technique est une compétence citée (offre SEO Manager Bagneux) et non un métier autonome."),
 ("SEO Content Manager","SEO_SEA","Aucune offre sous cet intitulé","Recouvert par Content Manager avec composante SEO."),
 ("Paid Acquisition Specialist","ACQUISITION_PERFORMANCE","Aucune offre","Recouvert par Traffic Manager et Consultant Paid Media."),
 ("Creator Partnerships Manager","CONTENT_BRAND","Aucune offre","Le marché français utilise Influence Manager ou Chef de projet influence."),
 ("Responsable Partenariats Influence","CONTENT_BRAND","Aucune offre","Idem."),
 ("Customer Marketing Manager","CRM_LIFECYCLE","Aucune offre sous cet intitulé","Recouvert par CRM Manager et Lifecycle Manager."),
 ("Loyalty Manager","CRM_LIFECYCLE","1 offre (Expert CRM, fidélisation et voix du client, Gémo)","Intitulé rare, la fidélisation est intégrée aux postes CRM."),
 ("Email Marketing Specialist","CRM_LIFECYCLE","Aucune offre autonome","L'emailing est une composante des postes CRM et Campaign Manager."),
 ("E-commerce Acquisition Manager","ECOMMERCE","Aucune offre","Recouvert par Traffic Manager E-commerce et Chargé de marketing e-commerce."),
 ("Digital Commerce Manager","ECOMMERCE","Aucune offre","Le marché français utilise E-commerce Manager."),
 ("Customer Data Analyst","DATA_ANALYTICS_CRO","Aucune offre à finalité marketing","Les Data Analyst sans finalité marketing ont été exclus du périmètre."),
 ("Web Analytics Consultant","DATA_ANALYTICS_CRO","Aucune offre sous cet intitulé","Recouvert par Web Analyst et Digital Analyst."),
 ("Tagging Specialist / Analytics Implementation Specialist","DATA_ANALYTICS_CRO","Aucune offre","Le tracking et le taggage sont des compétences, jamais des intitulés autonomes en France."),
 ("CRO Manager","DATA_ANALYTICS_CRO","Aucune offre sous cet intitulé","Le CRO n'existe pas comme métier autonome : 7 mentions au total, toujours comme composante d'un poste."),
 ("MarTech Specialist / MarTech Manager","MARTECH_MARKETING_OPS","Aucune offre sous cet intitulé","Le marché français utilise Marketing Operations, RevOps ou Expert CDP."),
 ("Marketing Automation AI Specialist","METIER_IA_EMERGENT","Aucune offre","Intitulé non employé en France en 2026."),
 ("AI Growth Specialist / AI-Powered Growth Marketer","METIER_IA_EMERGENT","Aucune offre (1 seul Growth Manager IA)","Le marché n'a pas encore stabilisé de dénomination."),
 ("Prompt Specialist appliqué au marketing","METIER_IA_EMERGENT","Aucune offre marketing","Les offres mentionnant le prompt engineering sont des postes tech/produit."),
 ("GenAI Content Specialist / AI CRM Specialist / AI Marketing Operations","METIER_IA_EMERGENT","Aucune offre","Intitulés non observés sur le marché français."),
 ("Generative Engine Optimization Specialist / Answer Engine Optimization Specialist","METIER_IA_EMERGENT","Aucune offre sous ces intitulés complets","Le marché utilise l'abréviation GEO, accolée à SEO : Consultant SEO/GEO, SEO SEA GEO AI Visibility Manager."),
 ("AI Search Specialist","METIER_IA_EMERGENT","Aucune offre","Recouvert par les intitulés SEO/GEO."),
]
for i, f_, r_, l_ in NON_OBS:
    A(f"| {i} | `{f_}` | {r_} | {l_} |")
A("")

A("### A.4 Faux positifs exclus du périmètre")
A("")
A("Les règles d'exclusion ont été appliquées **avant** toute classification métier, afin d'éviter de gonfler "
  "artificiellement les volumes.")
A("")
A("| Motif d'exclusion | Exemples réellement rencontrés | Offres |")
A("|---|---|---|")
excl = collections.Counter(o["METIER_NORMALISE"] for o in OFFRES if o["FAMILLE_METIER"] == "EXCLU_DU_PERIMETRE")
EXCL_EX = {
 "Hors périmètre — tech/produit IA": "Product Builder IA et No-Code, Product Builder IA Rennes, Alternant Ingénieur IA & Automatisation, Stage Développeur d'agents IA, Agent Builder AI/GenAI, Développeur Intégrations API & IA/Agents MCP",
 "Hors périmètre — développement/IT": "Développeur Web / Mobile, Intégrateur CRM Efficy, Consultant Odoo, Lead Developer / Référent Technique Digital CRM/ERP",
 "Hors périmètre — relation client": "Conseiller Relation Clients, Chargé de Suivi Client",
 "Hors périmètre — vente/logistique": "Préparateur/livreur e-commerce, Conseiller de vente BTS MCO, vente gestion comptoir",
 "Hors périmètre — RH/paie": "Gestionnaire carrière rémunération",
 "Hors périmètre — recrutement": "Talent Acquisition Specialist, Chargé de recrutement",
 "Hors périmètre — IT/BI": "Chef de projet informatique digital, Service Delivery Manager, Consultant BI confirmé",
}
for m, n in excl.most_common():
    A(f"| {m} | {EXCL_EX.get(m,'—')} | {n} |")
A("")
A("**Point d'analyse important.** L'exclusion des postes « tech/produit IA » est le résultat méthodologique le plus "
  "significatif de cette partie. La recherche ciblée sur les agents IA, le no-code, Make, n8n et Zapier fait "
  "remonter huit offres, dont **six sont des postes techniques ou produit** et non des postes marketing. Le marché "
  "de l'orchestration d'agents IA et de l'automatisation no-code existe bien en France en 2026, mais il est "
  "aujourd'hui capté par des profils tech, pas par des marketeurs. Ce constat est repris dans le test de "
  "l'hypothèse H9 du document de synthèse.")
A("")
A("D'autres catégories de faux positifs annoncées dans le cadrage n'ont produit aucune offre à exclure, faute "
  "d'avoir été ramenées par les requêtes : graphiste, communication institutionnelle pure, relations presse "
  "traditionnelles, événementiel sans composante digitale, support client, vendeur e-commerce en magasin.")
A("")

A("### A.5 Journal des requêtes de collecte d'offres")
A("")
A(f"{len(req)} requêtes distinctes ont produit au moins une offre individuelle retenue.")
A("")
A("| Requête | Offres retenues |")
A("|---|---|")
for r_, n in req.most_common():
    A(f"| `{r_}` | {n} |")
A("")
A("---")
A("")

# ============================================================ PARTIE B
A("## PARTIE B — PLATEFORMES ET CHEMINS D'ACCÈS SANS DONNÉES EXPLOITABLES")
A("")
A("### B.0 Contrainte technique générale")
A("")
A("**Seul l'outil de recherche web a fonctionné pendant toute la collecte.** Les accès HTTP directs aux sites "
  "(WebFetch, curl) sont bloqués par le proxy de l'environnement, et aucune clé d'API n'était disponible. "
  "Toutes les données proviennent donc des **titres, URL et extraits de pages publiques indexées par un moteur de "
  "recherche**. Cette contrainte a trois conséquences, signalées partout où elles s'appliquent dans les livrables :")
A("")
A("1. Les champs absents des extraits sont notés `NC` et n'ont jamais été déduits — d'où 30,1 % de contrats et "
  "52,9 % de niveaux de séniorité non renseignés.")
A("2. Les comptes de compétences sont des **bornes basses** : un extrait ne restitue qu'une fraction du contenu de l'offre.")
A("3. Les **séries historiques annuelles comparables n'ont pas pu être reconstituées** par métier : les pages de "
  "listes sont indexées à des dates hétérogènes et sous des libellés de requête différents.")
A("")

A("### B.1 Plateformes et chemins testés sans résultat exploitable")
A("")
SANS = [
 ("Apec — offres individuelles","https://www.apec.fr/candidat/recherche-emploi.html/emploi","2026-09-07",
  "Marketing digital, responsable marketing digital, directeur marketing digital, alternance marketing digital",
  "France, toutes régions","Offres individuelles avec entreprise, contrat, expérience, salaire",
  "Seules des **pages de résultats de recherche** ont été indexées, sans contenu d'offre exploitable. Une seule page de détail d'offre est remontée (Responsable Marketing Digital F/H, Nice), sans extrait suffisant pour renseigner les champs.",
  "Entreprise, contrat, expérience, salaire, compétences des offres cadres Apec",
  "Requêtes `site:apec.fr detail-offre`, requêtes par intitulé, requêtes par fonction",
  "**Études Apec utilisées à la place**, et elles constituent les sources les plus fiables de l'étude : L'intelligence artificielle en commercial-marketing (mars 2026), Les cadres et l'IA (mai 2026), Les métiers cadres porteurs 2026, Baromètres trimestriels 2026, référentiels métiers Marketing et Commercial.",
  "**Impact réel mais compensé.** L'absence d'offres Apec individuelles prive l'échantillon d'une vision spécifiquement cadre du marché. Les études Apec, mobilisées massivement, apportent en revanche les données d'évolution et d'impact de l'IA que l'échantillon ne pouvait pas produire."),
 ("LinkedIn Jobs","https://fr.linkedin.com/jobs","2026-09-07",
  "Marketing digital, growth, CRM, SEO, SEA, paid social","France, villes NEXA","Offres individuelles",
  "Aucune page `linkedin.com/jobs/view` exploitable n'est remontée dans les résultats indexés sur l'ensemble des requêtes lancées.",
  "Totalité des champs","Requêtes `site:fr.linkedin.com/jobs/view` avec plusieurs combinaisons de métiers et de villes",
  "Indeed, Welcome to the Jungle, HelloWork et France Travail, qui couvrent les mêmes employeurs",
  "**Faible.** LinkedIn est fortement redondant avec les autres plateformes pour les intitulés recherchés ; les employeurs identifiés (agences, scale-ups, grands groupes) sont présents dans l'échantillon via les autres sources."),
 ("Talent.com","https://fr.talent.com","2026-09-07","Marketing digital, CRM","France, plusieurs départements",
  "Offres individuelles et comptes d'offres",
  "Seules des **pages de liste par ville** sont indexées (`fr.talent.com/jobs/k-marketing-digital-l-...`), sans compte d'offres daté dans le titre ni contenu d'offre individuelle.",
  "Volumes datés et offres individuelles","Requêtes par ville et par intitulé",
  "Indeed et HelloWork pour les volumes datés","**Nul.** Talent.com est un agrégateur : ses offres proviennent des plateformes déjà couvertes."),
 ("Jooble","https://fr.jooble.org","2026-09-07","Marketing digital, consultant marketing digital, chef de produit marketing digital",
  "Nantes et autres villes","Volumes d'offres et offres individuelles",
  "Des comptes sont bien affichés mais **jugés non exploitables** : « Consultant marketing digital Nantes : 1 831 offres », « Chef produit marketing digital Nantes : 7 275 offres ». Ces valeurs relèvent d'un appariement lexical très lâche sur un agrégateur revendiquant plus de 20 000 sites sources, sans dédoublonnage.",
  "Volumes fiables","Requêtes par ville et par intitulé","Indeed et HelloWork, dont les comptes sont datés et cohérents entre eux",
  "**Nul, décision volontaire.** Retenir ces comptes aurait gravement faussé l'estimation du marché nantais. Ils sont explicitement écartés."),
 ("Meteojob, Monster, JobTeaser, Free-Work, ChooseYourBoss, LesJeudis","—","2026-09-07",
  "Marketing digital, growth, CRM, SEO","France","Offres individuelles",
  "Aucune page d'offre exploitable remontée sur les requêtes lancées.",
  "Totalité des champs","Requêtes `site:` sur chaque domaine, combinées à plusieurs intitulés",
  "Indeed, Welcome to the Jungle, HelloWork, France Travail",
  "**Faible.** Free-Work, ChooseYourBoss et LesJeudis sont orientés IT et freelance technique, donc peu pertinents pour le marketing digital ; JobTeaser aurait pu enrichir la vision stage et alternance, déjà bien couverte par Indeed et HelloWork (103 offres d'alternance dans l'échantillon)."),
 ("Sites carrières d'entreprises et ATS (Greenhouse, Workday)","—","2026-09-07",
  "Growth, paid social, CRM, product marketing","France","Offres individuelles",
  "Des pages Greenhouse sont bien remontées (WPP Media, Sony Music France, Artefact, Oliver, The Orchard) mais **sans extrait exploitable** permettant de renseigner les champs de la grille de collecte.",
  "Entreprise confirmée, contrat, expérience, compétences",
  "Requêtes `site:job-boards.greenhouse.io` combinées aux intitulés métiers",
  "Les mêmes employeurs sont présents dans l'échantillon via Welcome to the Jungle (Artefact, WPP Media/GroupM, Havas) et Indeed",
  "**Faible.** Les employeurs concernés sont couverts par ailleurs."),
 ("API France Travail (offres d'emploi v2)","https://francetravail.io","2026-09-07",
  "Ensemble des codes ROME du marketing digital","France entière","Séries d'offres datées, volumes par métier et par région",
  "**Aucune clé d'API disponible** dans l'environnement et accès HTTP direct bloqué par le proxy.",
  "Séries annuelles comparables 2024-2025-2026 par métier et par région, nombre de candidats par offre, durée de publication",
  "Aucun chemin alternatif possible sans authentification",
  "Pages d'offres individuelles France Travail indexées (39 offres collectées) et stocks de listes Indeed et HelloWork datés",
  "**Impact fort et assumé.** C'est la principale limite de l'étude : sans cette API, les **évolutions annuelles par métier ne peuvent pas être calculées**. Toutes les affirmations d'évolution du document de synthèse s'appuient donc sur des études publiées (Apec, Fevad, SRI, BMO) et jamais sur l'échantillon d'offres. Cette limite est signalée dans les hypothèses H1 et H5, dans les colonnes EVOLUTION des trois onglets Excel, et dans l'encadré de décision."),
 ("Insee — populations actives régionales","https://www.insee.fr","2026-09-07",
  "—","Régions administratives","Population active par région pour normaliser les volumes",
  "Aucune donnée précise n'a été collectée pendant l'étude.",
  "Population active régionale exacte et datée",
  "Non testé faute de temps de collecte disponible",
  "Ordres de grandeur usuels utilisés à la place",
  "**Modéré et explicitement tracé.** La colonne `OFFRES_POUR_100_000_ACTIFS` de l'onglet REGIONS_METIERS est marquée `ESTIMATION` : elle permet une comparaison relative entre régions mais ne doit pas être citée comme une donnée."),
 ("Numeum, OPCO Atlas, Grande École du Numérique, France Num, IAB France, Union des Marques, CPA","—","2026-09-07",
  "—","France","Études sectorielles complémentaires sur les métiers du marketing",
  "Non atteints : la collecte documentaire a été concentrée sur les producteurs de données les plus directement pertinents.",
  "Éclairages complémentaires sur les compétences et la formation",
  "Recherches thématiques génériques",
  "Apec, France Travail, Dares, Fevad, SRI/UDECAM/Oliver Wyman, Alliance Digitale/EY, observatoires salariaux",
  "**Faible.** Les sources mobilisées couvrent le marché du travail, le marché publicitaire, l'e-commerce, le poids économique de la filière et l'impact de l'IA — soit l'ensemble des dimensions nécessaires à la décision."),
]
for p_, url, date, met, zones, rech, res, manq, autres, remp, imp in SANS:
    A(f"#### {p_}")
    A("")
    A(f"- **PLATEFORME :** {p_}")
    A(f"- **URL :** {url}")
    A(f"- **DATE_DU_TEST :** {date}")
    A(f"- **METIERS_TESTES :** {met}")
    A(f"- **ZONES_TESTEES :** {zones}")
    A(f"- **DONNEES_RECHERCHEES :** {rech}")
    A(f"- **RESULTAT :** {res}")
    A(f"- **DONNEES_MANQUANTES :** {manq}")
    A(f"- **AUTRES_CHEMINS_TESTES :** {autres}")
    A(f"- **SOURCE_DE_REMPLACEMENT :** {remp}")
    A(f"- **IMPACT_SUR_L_ANALYSE :** {imp}")
    A("")

A("### B.2 Requêtes lancées sans offre exploitable")
A("")
jp = os.path.join(BASE, "journal.txt")
if os.path.exists(jp):
    for line in open(jp, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"): continue
        if "|" in line:
            q, r_ = line.split("|", 1)
            A(f"- `{q.strip()}`")
            A(f"  - {r_.strip()}")
A("")

A("### B.3 Comptes de volumes écartés")
A("")
A("| Compte affiché | Source | Motif de l'écartement |")
A("|---|---|---|")
A("| Consultant marketing digital Nantes : 1 831 offres | Jooble | Appariement lexical trop lâche sur un agrégateur sans dédoublonnage ; incohérent avec les 82 offres Indeed pour Nantes. |")
A("| Chef produit marketing digital Nantes : 7 275 offres | Jooble | Idem, valeur manifestement non significative. |")
A("| Fidélisation clients : 18 000+ offres | Indeed | La requête capte massivement des postes de relation client, service client et téléconseil sans finalité marketing. |")
A("| Chargé Client Fidélisation : 6 000+ offres | Indeed | Idem. |")
A("| Responsable Fidélisation Clients : 6 000+ offres | Indeed | Idem. |")
A("")
A("Les comptes **CRM Marketing Manager (800+)** et **Responsable CRM Fidélisation (1 000+)** ont en revanche été "
  "conservés, avec réserve explicite sur la largeur du périmètre lexical.")
A("")
A("---")
A("")
A("## Note finale sur la fiabilité")
A("")
A("Pour chaque résultat important des livrables, les métadonnées suivantes sont conservées : source, date, "
  "périmètre, taille d'échantillon, statut observé ou estimé, niveau de confiance. Aucune offre, aucun volume, "
  "aucune évolution et aucune URL n'a été inventé. Les valeurs absentes des extraits sont notées `NC` et n'ont "
  "jamais été complétées par déduction. Les estimations sont marquées `ESTIMATION` et leur mode de calcul est "
  "documenté à l'endroit où elles apparaissent.")

path = os.path.join(ROOT, "NEXA_Perimetre_Metiers_Marketing_et_Plateformes_Sans_Donnees.md")
open(path, "w", encoding="utf-8").write("\n".join(L))
print("Écrit :", path, "—", len(L), "lignes")
