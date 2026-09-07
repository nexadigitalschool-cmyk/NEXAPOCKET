#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests d'hypothèses H1-H18, indicateurs dérivés (tension, qualité du débouché) et scénarios."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "collecte_mkt")
D = json.load(open(os.path.join(BASE, "mkt_consolide.json"), encoding="utf-8"))

# --------------------------------------------------------------- INDICATEURS
# Tension et qualité du débouché : notation experte documentée, croisant
# volume échantillon + volume jobboard daté + accessibilité junior + alternance
# + technicité + salaire + exposition automatisation + pérennité.
FAMILLE_INDIC = {
  # famille: (tension, qualité_debouche, exposition_automatisation, perennite_3_5_ans, justification)
  "ACQUISITION_PERFORMANCE": ("EN_TENSION", "TRES_FAVORABLE", "MOYENNE", "FORTE",
    "85 offres uniques (17,2 % de l'échantillon, 1re famille spécialisée) ; stocks Indeed Growth Marketing France 1 842 (08/2026) et Île-de-France 1 295 (09/2026) ; marché publicitaire digital +11 % en 2025 et +12 % au S1 2026 (SRI/UDECAM/Oliver Wyman) qui finance directement ces postes ; salaires en progression (Growth senior 80-90 k€) ; technicité 2,09 ; accès junior limité (17,6 %) mais alternance réelle (14,1 %)."),
  "CRM_LIFECYCLE": ("EN_TENSION", "TRES_FAVORABLE", "FAIBLE", "FORTE",
    "36 offres uniques ; stocks Indeed CRM Manager France 2 000+ (09/2026) et Paris 800+ ; HelloWork CRM manager 100+ et Chargé de CRM 90+ ; technicité 2,50 (2e rang) ; compétence CRM citée dans 11,5 % de l'ensemble des offres du périmètre, 2e compétence la plus demandée ; faible exposition à l'automatisation (architecture, données, cycle de vie) ; accès junior 30,6 % via alternance CRM."),
  "DATA_ANALYTICS_CRO": ("EN_TENSION", "FAVORABLE", "FAIBLE", "FORTE",
    "31 offres uniques ; technicité 2,45 ; exigences fréquentes Bac+5 et 4-5 ans (Web Analyst, Senior Digital Analyst) ; SQL, BigQuery, GA4, GTM, Looker Studio explicitement demandés ; MAIS accessibilité junior faible (16,1 %) et alternance quasi nulle (3,2 %) : débouché de Mastère, pas de Bachelor."),
  "MARTECH_MARKETING_OPS": ("EN_TENSION", "FAVORABLE", "FAIBLE", "FORTE",
    "17 offres uniques seulement mais technicité la plus élevée (2,82) ; 0 % d'alternance et 11,8 % de juniors : marché de profils expérimentés (RevOps, Marketing Ops, CDP) ; volumes faibles en valeur absolue — ne peut pas porter seul une filière ; débouché de spécialisation Bac+5 ou d'évolution à 3-5 ans."),
  "SEO_SEA": ("EN_TENSION", "FAVORABLE", "MOYENNE", "MOYENNE",
    "51 offres uniques (2e famille spécialisée) ; stocks Indeed SEO Manager France 318 (08/2026), SEO Manager Paris 200+, HelloWork SEO 1 521 (07/2026) ; salaires en hausse (SEO manager confirmé 47 855 € médian, +4,2 % sur un an — Observatoire Seobooster) ; MAIS transformation forte du Search par l'IA générative : apparition documentée du GEO/AEO dans 7 offres du périmètre et dans des intitulés réels (SEO SEA GEO AI Visibility Manager, Consultant SEO/GEO) ; pérennité conditionnée à la montée en GEO/AEO."),
  "ECOMMERCE": ("EQUILIBRE", "FAVORABLE", "MOYENNE", "FORTE",
    "28 offres uniques ; filière e-commerce à 196,4 Md€ en 2025 (+7 %) et 234 000 emplois (+9 %) selon la Fevad ; technicité 2,11 ; alternance 14,3 % ; débouchés répartis sur tout le territoire (marques, retail, marketplaces)."),
  "COEUR_GENERALISTE": ("EQUILIBRE", "MOYEN", "FORTE", "MOYENNE",
    "111 offres uniques — 1re famille en volume (22,4 % du périmètre) et de loin le premier gisement d'alternance (40,5 %) et de débutants (47,7 %) ; MAIS technicité la plus faible du périmètre après le social media (1,42) : les tâches décrites (publication, mise à jour de contenus, emailing simple, coordination) sont celles que les études identifient comme les plus automatisables ; marché d'entrée, pas marché de carrière."),
  "CONTENT_BRAND": ("RALENTISSEMENT", "MOYEN", "FORTE", "MOYENNE",
    "29 offres uniques ; technicité 1,66 ; production de contenus génériques directement exposée à l'IA générative (76 % des marketeurs déclarent utiliser l'IA générative pour la création de contenu) ; se maintient sur la partie stratégie éditoriale, brand content et influence, pas sur la production."),
  "SOCIAL_MEDIA": ("SATURE", "FRAGILE", "TRES_FORTE", "FAIBLE",
    "39 offres uniques mais technicité la plus faible du périmètre (1,03) ; 25,6 % d'alternance et 38,5 % de débutants/juniors : forte concurrence à l'entrée ; France Travail recense 317 offres de community manager en 2026 ; saturation documentée (Journal du CM, VISIPLUS) ; 52 % des annonceurs prévoient de réduire leur budget média 2026 ; tâches (publication, déclinaisons, veille) parmi les plus automatisables."),
  "PRODUCT_MARKETING": ("EQUILIBRE", "FAVORABLE", "FAIBLE", "FORTE",
    "9 offres uniques seulement, toutes en CDI, 0 % d'alternance et 0 % de junior : métier d'expérience (3 à 10 ans exigés), très concentré à Paris et dans le B2B SaaS ; débouché de Mastère et d'évolution, jamais de sortie de Bachelor."),
  "METIER_IA_EMERGENT": ("DONNEES_INSUFFISANTES", "MOYEN", "FAIBLE", "MOYENNE",
    "10 offres uniques (2,0 % du périmètre) : le marché existe et est observable (Consultant SEO/GEO, SEO SEA GEO AI Visibility Manager, AI Content Manager, Community Manager spécialiste Agents IA & GEO/SEO, Growth Manager IA, RevOps AI Data & Automation) mais reste marginal en volume ; 0 % d'alternance ; ne peut pas constituer une filière ni un parcours autonome à ce stade."),
  "METIER_ADJACENT": ("EQUILIBRE", "MOYEN", "MOYENNE", "MOYENNE",
    "49 offres (marketing généraliste, chef de produit, business developer) : débouchés réels pour des diplômés marketing mais qui ne relèvent pas du marketing digital au sens strict ; ne doivent pas être comptés comme débouchés directs de la filière."),
}

# --------------------------------------------------------------- HYPOTHÈSES
def f(nom): return D["par_famille"].get(nom, {})
def m(nom): return D["par_metier"].get(nom, {})
NAT = D["national"]
NP = NAT["n"]

spec = ["ACQUISITION_PERFORMANCE","SEO_SEA","CRM_LIFECYCLE","DATA_ANALYTICS_CRO",
        "ECOMMERCE","MARTECH_MARKETING_OPS","PRODUCT_MARKETING"]
n_spec = sum(f(x).get("n",0) for x in spec)
n_gen = f("COEUR_GENERALISTE").get("n",0)
n_socont = f("SOCIAL_MEDIA").get("n",0) + f("CONTENT_BRAND").get("n",0)

HYPOTHESES = [
 ("H1", "Les métiers généralistes du Marketing Digital progressent moins vite que les métiers spécialisés.",
  "PARTIELLEMENT_CONFIRMEE",
  f"Les familles spécialisées totalisent {n_spec} offres uniques ({round(100*n_spec/NP,1)} %) contre {n_gen} pour le cœur généraliste ({round(100*n_gen/NP,1)} %) : le marché est majoritairement spécialisé. Mais l'échantillon est un stock à une date, pas un flux : il établit une STRUCTURE, pas une VITESSE de progression.",
  f"Spécialisés {n_spec} vs généralistes {n_gen} offres uniques ; technicité moyenne 2,15 (spécialisés) vs 1,42 (généralistes)",
  "Échantillon 495 offres uniques dans le périmètre (Indeed, WTTJ, HelloWork, France Travail, 2026-09-07) ; Apec Les métiers cadres porteurs 2026",
  "Les séries historiques comparables 2024/2025/2026 par métier n'ont pas pu être reconstituées (pages de liste indexées à des dates hétérogènes, libellés de requête différents) : la progression relative n'est donc PAS démontrée quantitativement.",
  "MOYENNE",
  "NEXA ne peut pas justifier un cursus centré sur le généraliste par la structure du marché, mais ne peut pas non plus affirmer que le généraliste recule."),

 ("H2", "La demande se déplace vers Growth, Acquisition, Performance, CRM, Lifecycle, e-commerce, Analytics, Data Marketing, CRO, Marketing Automation, MarTech.",
  "CONFIRMEE",
  f"Ces familles concentrent {n_spec} des {NP} offres uniques du périmètre ({round(100*n_spec/NP,1)} %). Acquisition/Performance est la 1re famille spécialisée (85 offres) devant SEO/SEA (51), CRM/Lifecycle (36), Data/Analytics/CRO (31), e-commerce (28), MarTech/MarketingOps (17), Product Marketing (9). Les stocks datés confirment : Growth Marketing France 1 842 offres (Indeed, 08/2026), CRM Manager France 2 000+ (09/2026), Marketing Automation 759 (05/2026).",
  f"{n_spec} offres spécialisées / {NP} ; Growth Marketing 1 842 (Indeed 08/2026) ; CRM Manager 2 000+ (Indeed 09/2026) ; Marketing Automation 759 (Indeed 05/2026)",
  "Échantillon offres 2026 ; stocks Indeed/HelloWork datés ; SRI-UDECAM-Oliver Wyman 36e Observatoire e-pub S1 2026 ; Fevad Chiffres clés 2026",
  "Le volume absolu de MarTech/RevOps (17 offres) et de Product Marketing (9) reste faible : le déplacement est réel mais très inégal selon les spécialités.",
  "FORTE",
  "Une filière NEXA doit être organisée autour de ces familles, avec une hiérarchie : Acquisition/Growth et CRM/Data d'abord, MarTech et Product Marketing en modules et non en parcours autonomes."),

 ("H3", "Les compétences techniques et analytiques prennent davantage de valeur dans les métiers marketing.",
  "CONFIRMEE",
  "La technicité moyenne croît régulièrement avec la spécialisation : MarTech/MarketingOps 2,82, CRM/Lifecycle 2,50, Data/Analytics/CRO 2,45, e-commerce 2,11, Acquisition/Performance 2,09, SEO/SEA 2,00, Content 1,66, Cœur généraliste 1,42, Social Media 1,03. Les offres de niveau 3-4 (performance/data/automation et MarTech/systèmes) représentent 51 offres du périmètre. Les salaires suivent : SEO manager confirmé 47 855 € médian (+4,2 % sur un an), Growth senior 80-90 k€, contre 20-30 k€ pour des postes de webmarketing/communication digitale généralistes observés dans l'échantillon.",
  "Technicité moyenne par famille de 1,03 à 2,82 ; 51 offres de niveau 3-4 ; SEO manager 47 855 € (+4,2 %/an, Seobooster 2026)",
  "Échantillon 495 offres ; Observatoire Salaires SEO et Marketing France 2026 (Seobooster) ; Licorne Society 2026 ; Apec Impact de l'IA sur les compétences commercial-marketing 2026",
  "Aucune : la corrélation technicité / séniorité / salaire est constante dans toutes les familles observées.",
  "FORTE",
  "Le socle technique (GA4, GTM, tracking, CRM, automation, SQL, dashboards) doit devenir obligatoire et non optionnel, dès le Bachelor."),

 ("H4", "Les métiers centrés sur le Community Management, la production simple de contenus, l'exécution opérationnelle et la communication digitale généraliste présentent un marché plus saturé.",
  "CONFIRMEE",
  f"Social Media : {f('SOCIAL_MEDIA').get('n')} offres, technicité 1,03 (la plus faible), 38,5 % de débutants/juniors et 25,6 % d'alternance — forte pression concurrentielle à l'entrée. Content/Brand : {f('CONTENT_BRAND').get('n')} offres, technicité 1,66. Le Cœur généraliste affiche 47,7 % de débutants/juniors pour une technicité de 1,42. France Travail ne recense que 317 offres de community manager en 2026, pour un vivier de candidats très large. 52 % des annonceurs prévoient de réduire leur budget média 2026.",
  "Social Media technicité 1,03 ; 317 offres CM (France Travail 2026) ; 52 % des annonceurs réduisent leur budget média 2026",
  "Échantillon ; France Travail offres community manager 2026 ; VISIPLUS academy 2026 ; Journal du Community Manager",
  "Le stock Indeed Community Manager France reste élevé (1 371 offres, 09/2026) : il ne s'agit pas d'une disparition du métier mais d'un déséquilibre offre/demande de candidats et d'un appauvrissement du contenu des postes.",
  "FORTE",
  "NEXA ne doit plus faire du Community Management / Social Media une spécialisation d'arrivée, mais une compétence de socle intégrée à des postes plus larges."),

 ("H5", "Les entreprises recrutent proportionnellement moins de juniors en CDI et utilisent davantage l'alternance comme voie d'entrée.",
  "PARTIELLEMENT_CONFIRMEE",
  f"L'alternance représente {NAT['contrats_pct'].get('ALTERNANCE')} % des offres du périmètre (103 offres) contre {NAT['contrats_pct'].get('CDI')} % de CDI, et 25,5 % des offres sont explicitement de niveau débutant. Les volumes d'alternance sont massifs : 1 177 offres alternance marketing digital sur HelloWork (08/2026), plus de 1 000 sur Indeed (09/2026), 1 254 en Île-de-France (06/2026), 375 en alternance community manager, 459 en alternance chargé de marketing. À l'inverse, les CDI juniors purs sont rares dans les familles techniques.",
  "103 offres en alternance (20,8 %) ; 1 177 alternances marketing digital (HelloWork 08/2026) ; 1 254 en IDF (Indeed 06/2026)",
  "Échantillon ; stocks HelloWork et Indeed datés 2026",
  "30,1 % des offres de l'échantillon n'indiquent pas le type de contrat dans les extraits indexés : la part réelle de CDI est mécaniquement sous-estimée. La substitution CDI junior → alternance n'est donc pas démontrée, seule l'abondance de l'alternance l'est.",
  "MOYENNE",
  "L'alternance est la voie d'entrée dominante et sécurise le modèle Bachelor de NEXA — c'est l'actif le plus solide de la filière."),

 ("H6", "Certaines spécialités offrent significativement davantage de débouchés aux juniors que d'autres.",
  "CONFIRMEE",
  "L'écart est massif et systématique. Part de débutants+juniors : Cœur généraliste 47,7 %, Social Media 38,5 %, CRM/Lifecycle 30,6 %, e-commerce 21,4 %, Content 20,7 %, Acquisition/Performance 17,6 %, SEO/SEA 17,6 %, Data/Analytics/CRO 16,1 %, MarTech/MarketingOps 11,8 %, Product Marketing 0 %, Métiers IA émergents 0 %. Part d'alternance : généraliste 40,5 %, social 25,6 %, CRM 16,7 %, e-commerce 14,3 %, acquisition 14,1 %, SEO/SEA 11,8 %, data 3,2 %, MarTech 0 %, Product Marketing 0 %, IA émergents 0 %.",
  "Débutants+juniors de 47,7 % (généraliste) à 0 % (Product Marketing, IA émergents) ; alternance de 40,5 % à 0 %",
  "Échantillon 495 offres uniques",
  "Aucune : la relation est monotone et inverse à la technicité.",
  "FORTE",
  "POINT CENTRAL POUR NEXA : les métiers les plus porteurs en valeur sont ceux qui recrutent le MOINS de juniors. Un Bachelor exclusivement technique n'aurait pas de débouché ni d'alternance."),

 ("H7", "L'IA automatise une part croissante des tâches opérationnelles simples du marketing.",
  "CONFIRMEE",
  "Convergence de sources : 75 % des marketeurs déclarent utiliser l'IA générative dans leur travail quotidien et 76 % pour la création de contenu ; 88 % des équipes marketing déclarent utiliser l'IA au quotidien ; 82 % des entreprises e-commerce utilisaient déjà l'IA générative en 2025 (Fevad). L'Apec constate que l'IA automatise de nombreuses tâches et redéploie la valeur ajoutée des cadres commercial-marketing vers l'analyse, la personnalisation et la stratégie de la relation client. Les tâches concernées (rédaction générique, déclinaisons publicitaires, publication, reporting manuel, recherche de mots-clés basique) sont précisément celles décrites dans les offres de niveau de technicité 1, soit 136 offres de l'échantillon (27,5 %).",
  "75-88 % d'usage déclaré de l'IA générative en marketing ; 82 % des e-commerçants (Fevad 2025) ; 136 offres de technicité 1 dans l'échantillon",
  "Apec L'intelligence artificielle en commercial-marketing 2026 ; Fevad Chiffres clés 2026 ; compilations sectorielles 2026",
  "Les taux d'usage déclaré proviennent en partie de sources secondaires de fiabilité faible ; ils convergent toutefois avec l'analyse Apec, de fiabilité forte.",
  "FORTE",
  "Les compétences d'exécution simple ne peuvent plus constituer le cœur de la proposition de valeur pédagogique de NEXA."),

 ("H8", "L'IA ne supprime pas les métiers marketing mais augmente la valeur des profils capables d'analyser, expérimenter, piloter, automatiser, intégrer des outils, travailler avec la donnée et comprendre le business.",
  "CONFIRMEE",
  "Le marché de l'emploi marketing ne recule pas : la filière marketing digital française représente 14,4 Md€ de revenus directs et environ 310 000 emplois, avec une croissance cinq fois supérieure à celle du PIB (Alliance Digitale / EY) ; le marché publicitaire digital progresse de 11 % en 2025 et 12 % au S1 2026 ; l'Apec prévoit 305 800 recrutements de cadres en 2026 (+4 % vs 2025), la fonction commercial-marketing figurant parmi les trois fonctions concentrant plus de la moitié des recrutements. Parallèlement, l'Apec identifie explicitement le redéploiement de la valeur ajoutée vers l'analyse, la personnalisation et la stratégie, et deux compétences émergentes : la maîtrise des outils génératifs et la capacité à les intégrer dans des processus métier. Dans l'échantillon, 86 % des marketeurs retravaillent systématiquement les contenus générés par l'IA et 92 % imposent une validation humaine.",
  "310 000 emplois et 14,4 Md€ (Alliance Digitale/EY) ; +11 % pub digitale 2025 ; 305 800 recrutements cadres 2026 (+4 %) ; 86 % de retouche humaine des contenus IA",
  "Alliance Digitale / EY 2025 ; SRI-UDECAM-Oliver Wyman 2026 ; Apec 2026 ; Fevad 2026",
  "L'enquête BMO 2026 de France Travail signale à l'inverse un recul de 6,5 % des intentions de recrutement tous métiers confondus : le marketing digital évolue donc mieux que la moyenne du marché du travail, mais dans un contexte macro-économique dégradé.",
  "FORTE",
  "La question n'est pas de savoir si NEXA doit maintenir une offre marketing, mais à quel niveau de technicité elle doit la positionner."),

 ("H9", "Le concept de marketeur augmenté par l'IA possède une réalité observable dans les compétences demandées, même si l'intitulé n'est pas utilisé.",
  "PARTIELLEMENT_CONFIRMEE",
  "Réalité observable mais TRÈS MINORITAIRE, et c'est le résultat le plus important de l'étude. Seules 2,4 % des offres du périmètre mentionnent explicitement l'IA (12 offres sur 495). Ce chiffre converge remarquablement avec la mesure indépendante de l'Apec : les offres mentionnant l'IA ne représentent que 2 % des offres de la fonction commercial-marketing. Des intitulés réels existent bien (Consultant SEO/GEO, SEO SEA GEO AI Visibility Manager E-commerce, AI Content Manager, Community Manager spécialiste Agents IA & GEO/SEO, Growth Manager IA, RevOps Manager AI Data & Automation) : 10 offres, soit 2,0 % du périmètre. La dynamique est réelle — les offres de la fonction commerciale mentionnant l'IA ont progressé de 62 % entre 2022 et 2025 (Apec) — mais le niveau reste faible.",
  "12 offres mentionnant explicitement l'IA (2,4 %) ; 10 métiers IA émergents (2,0 %) ; Apec : 2 % des offres commercial-marketing, +62 % entre 2022 et 2025",
  "Échantillon 495 offres ; Apec L'intelligence artificielle en commercial-marketing (mars 2026)",
  "CONTRADICTION MAJEURE À SIGNALER : la recherche ciblée sur les offres mentionnant agents IA, no-code, Make, n8n et Zapier fait remonter 8 offres dont 6 sont des postes TECH/PRODUIT (Product Builder IA, Ingénieur IA & Automatisation, Agent Builder GenAI, Développeur intégrations API & agents MCP) et non des postes marketing. Le marché de l'orchestration d'agents IA existe en France en 2026 mais il est aujourd'hui capté par des profils techniques, pas par des marketeurs. Par ailleurs les extraits indexés ne restituent qu'une partie du contenu des offres : 2,4 % est une borne basse.",
  "MOYENNE",
  "NEXA ne peut PAS fonder un parcours entier sur le marketeur augmenté par l'IA : la demande employeur ne le justifie pas encore. L'IA doit être une couche de compétences transversale et obligatoire, pas une spécialisation affichée."),

 ("H10", "Un cursus Marketing Digital principalement généraliste est moins aligné avec les besoins futurs qu'un cursus plus spécialisé et technique.",
  "CONFIRMEE",
  "Le cœur généraliste cumule les trois signaux de fragilité : technicité la plus faible du périmètre après le social media (1,42), exposition la plus forte à l'automatisation (tâches de niveau 1), et salaires les plus bas observés (offres à 20-30 k€ pour des postes de webmarketing et communication digitale). Les familles techniques concentrent 51,9 % du marché, les salaires en progression et la pérennité la plus forte.",
  "Technicité généraliste 1,42 vs 2,09-2,82 pour les familles techniques ; 51,9 % du marché spécialisé",
  "Échantillon ; études salariales 2026 ; Apec 2026",
  "Le généraliste reste le premier gisement d'alternance (40,5 %) et de débutants (47,7 %) : il est mal aligné avec les besoins de CARRIÈRE mais bien aligné avec les besoins d'ENTRÉE sur le marché.",
  "FORTE",
  "Le généraliste doit être un point de départ, jamais un point d'arrivée. Un Mastère généraliste n'est pas défendable."),

 ("H11", "Malgré la spécialisation du marché, un socle généraliste reste pertinent en Bachelor.",
  "CONFIRMEE",
  "Le cœur généraliste est la 1re famille en volume (111 offres, 22,4 %), la 1re en alternance (40,5 %) et la 1re en accessibilité débutant (47,7 %). Les volumes de marché confirment : plus de 1 000 offres d'alternance marketing digital sur Indeed (09/2026), 1 254 en Île-de-France (06/2026), 1 177 sur HelloWork (08/2026). À l'inverse, les familles les plus techniques n'offrent presque aucune alternance (Data 3,2 %, MarTech 0 %, Product Marketing 0 %, IA émergents 0 %).",
  "111 offres généralistes ; 40,5 % d'alternance ; 1 177 à 1 254 offres d'alternance marketing digital sur les jobboards en 2026",
  "Échantillon ; stocks HelloWork et Indeed datés",
  "Aucune contradiction : c'est le constat le plus robuste de l'étude.",
  "FORTE",
  "Sans socle généraliste, le Bachelor NEXA perdrait l'accès à l'alternance, donc son modèle économique et son taux de placement."),

 ("H12", "Les besoins en Growth, CRM, Data Marketing, Marketing Automation et MarTech justifient davantage une formation Bac+5.",
  "CONFIRMEE",
  "Ces familles exigent systématiquement de l'expérience et un niveau Bac+5 : Data/Analytics 16,1 % de juniors et 3,2 % d'alternance, MarTech 11,8 % de juniors et 0 % d'alternance, Product Marketing 0 % de juniors. Les offres exigent 3 à 10 ans (Web Analyst 5 ans minimum, Marketing Automation Manager 6 ans, CRM Lead 7 ans, Head of Growth 8 ans, Head of Marketing 10-15 ans) et mentionnent explicitement Bac+5. Les salaires correspondants sont les plus élevés du périmètre.",
  "MarTech 0 % alternance / 11,8 % juniors ; exigences 3 à 15 ans ; Bac+5 explicite dans les offres CRM, Data, Product Marketing",
  "Échantillon 495 offres ; études salariales 2026",
  "Le volume absolu de MarTech (17) et de Product Marketing (9) est faible : ces spécialités justifient des MODULES de Mastère, pas des parcours autonomes à effectifs importants.",
  "FORTE",
  "Le Mastère NEXA doit être spécialisé et technique ; c'est là que se situe la valeur différenciante."),

 ("H13", "Une partie des métiers du Marketing Digital converge avec la Data.",
  "CONFIRMEE",
  "31 offres Data/Analytics/CRO dans le périmètre marketing, avec des compétences explicitement data : SQL, BigQuery, Looker Studio, Power BI, data layer, CDP. Des intitulés hybrides sont observés (Senior Data Analyst SEO chez Havas, Lead Marketing Data Analyst chez Doctolib, Marketing Data Analyst chez Groupe Positive, Data Analyst Marketing chez Laforêt, Expert technique Customer Data Platform). La compétence CRM est la 2e la plus demandée de tout le périmètre (11,5 %).",
  "31 offres Data/Analytics/CRO ; technicité 2,45 ; intitulés hybrides data+marketing observés chez Havas, Doctolib, Laforêt, Groupe Positive",
  "Échantillon 495 offres",
  "Les postes de Data Analyst sans finalité marketing ont été exclus du périmètre : la convergence est réelle mais ne signifie pas fusion des métiers.",
  "FORTE",
  "Une passerelle et des modules communs avec la filière IA & Data de NEXA sont justifiés — sans fusion des filières."),

 ("H14", "Une partie des métiers du Marketing Digital converge avec les fonctions commerciales et Revenue Operations.",
  "CONFIRMEE",
  "17 offres MarTech/Marketing Ops/RevOps observées, dont des intitulés explicitement transverses marketing-vente : RevOps & CRM Manager, CRM/SalesOps Manager, Consultant RevOps/Sales Ops, Senior RevOps Manager (collaboration Marketing, Sales et Customer Care), Director Revenue Operations EMEA (marketing, sales, customer success). L'Apec rattache d'ailleurs le marketing à la fonction commercial-marketing, qui représentait 20 % des offres cadres en 2024.",
  "17 offres MarTech/RevOps ; intitulés transverses CRM/SalesOps ; Apec : fonction commercial-marketing = 20 % des offres cadres 2024",
  "Échantillon ; Apec Les métiers cadres de la fonction Commercial, commerce, ventes",
  "Le volume reste faible (3,4 % du périmètre) et ces postes exigent 3 à 5 ans d'expérience : convergence stratégique, pas débouché de sortie d'école.",
  "MOYENNE",
  "Un module RevOps / pilotage de la performance commerciale a du sens en Mastère ; une fusion avec une filière Business ne se justifie pas."),

 ("H15", "Les différences territoriales justifient une stratégie distincte selon les campus NEXA.",
  "CONFIRMEE",
  "L'Île-de-France concentre 262 des 495 offres du périmètre (52,9 %), devant Auvergne-Rhône-Alpes (64), Nouvelle-Aquitaine (35), PACA (31), Hauts-de-France (26), Occitanie (20) et Pays de la Loire (20). Les stocks Indeed confirment la hiérarchie : Paris 2 000+ offres Digital Marketing, Île-de-France 3 000+, Lyon 258-317, Lille 113, Marseille 92, Bordeaux 90, Nantes 82. Les métiers spécialisés (RevOps, Product Marketing, MarTech, Paid Media en agence) sont presque exclusivement parisiens ; en régions dominent le généraliste, l'e-commerce, le SEO/SEA et le CRM.",
  "IDF 52,9 % de l'échantillon ; stocks Indeed : Paris 2 000+, Lyon 258-317, Lille 113, Marseille 92, Bordeaux 90, Nantes 82",
  "Échantillon ; stocks Indeed datés 2026 ; Alliance Digitale/EY (près de la moitié des emplois hors IDF)",
  "L'étude Alliance Digitale/EY indique que près de la moitié des 310 000 emplois de la filière sont hors Île-de-France : la concentration observée sur les jobboards surestime probablement le poids francilien pour les postes les plus qualifiés.",
  "FORTE",
  "Les spécialisations Mastère les plus techniques ne sont soutenables qu'à Paris et Lyon ; les autres campus doivent s'appuyer sur le socle généraliste, l'e-commerce, le SEO/SEA et le CRM."),

 ("H16", "Le marché offre suffisamment de débouchés et d'alternances pour maintenir une filière Marketing Digital autonome chez NEXA.",
  "CONFIRMEE",
  "Volume d'offres : 4 000+ offres Marketing Digital sur Indeed France (07/2026), 2 568 sur HelloWork (07/2026), 4 015 sur la requête SEO/SEA/SMO/Marketing Digital (09/2026). Volume d'alternance : 1 177 offres HelloWork (08/2026), plus de 1 000 sur Indeed (09/2026), 1 254 en Île-de-France (06/2026), 459 en alternance chargé de marketing, 375 en alternance community manager. Poids macro-économique : 310 000 emplois et 14,4 Md€ de revenus directs, croissance cinq fois supérieure au PIB. Aucun signal de contraction structurelle.",
  "4 000+ offres Indeed France ; 2 568 HelloWork ; 1 177 alternances ; 310 000 emplois de filière",
  "Stocks Indeed et HelloWork datés 2026 ; Alliance Digitale/EY 2025 ; Apec 2026 ; Fevad 2026",
  "Les comptes de jobboards ne sont pas dédoublonnés entre eux et recouvrent des périmètres lexicaux larges : ils ne peuvent pas être additionnés. Ils établissent un ordre de grandeur, pas un nombre d'emplois.",
  "FORTE",
  "La fermeture de la filière n'est pas justifiée par le marché de l'emploi."),

 ("H17", "Une filière Marketing Digital plus technique créerait une différenciation plus forte pour NEXA qu'une offre généraliste comparable à celle de nombreuses écoles.",
  "PARTIELLEMENT_CONFIRMEE",
  "Côté marché, la différenciation technique est cohérente : 51,9 % des offres sont spécialisées, la technicité et les salaires progressent avec la spécialisation, et NEXA dispose déjà des filières Développement Web et IA & Data qui rendent crédible un positionnement MarTech / Data Marketing — ce qu'une école de commerce généraliste ne peut pas revendiquer. L'échantillon montre aussi une demande de profils hybrides (Senior Data Analyst SEO, Marketing Data Analyst, RevOps AI Data & Automation).",
  "51,9 % d'offres spécialisées ; technicité 2,45-2,82 sur les familles data/MarTech ; intitulés hybrides observés",
  "Échantillon ; positionnement de l'offre NEXA (4 filières)",
  "Aucune donnée concurrentielle sur l'offre de formation française n'a été collectée dans cette étude : l'avantage différenciant est déduit de la structure du marché de l'emploi et du portefeuille NEXA, il n'est pas mesuré sur le marché de la formation.",
  "MOYENNE",
  "La technicisation est un axe de différenciation crédible, à valider par une analyse concurrentielle des programmes que cette étude n'a pas réalisée."),

 ("H18", "Si les métiers généralistes sont saturés et si les spécialisations ne présentent pas suffisamment de volumes accessibles aux diplômés NEXA, une réduction ou fermeture progressive de la filière peut être rationnelle.",
  "NON_CONFIRMEE",
  "Les deux conditions ne sont pas réunies. Le généraliste n'est pas saturé au sens d'un effondrement des débouchés : il reste la 1re famille en volume (111 offres) et le 1er gisement d'alternance (40,5 %, plus de 1 000 offres d'alternance sur le marché). Les spécialisations présentent des volumes réels et croissants (Growth Marketing 1 842 offres, CRM Manager 2 000+, Marketing Automation 759). Le secteur crée de l'emploi (310 000 emplois, croissance cinq fois supérieure au PIB ; e-commerce +9 % d'emplois en 2025).",
  "111 offres généralistes et 1 000+ alternances ; Growth 1 842, CRM 2 000+, Marketing Automation 759 ; +9 % d'emplois e-commerce",
  "Échantillon ; stocks Indeed/HelloWork ; Alliance Digitale/EY ; Fevad 2026",
  "Le seul segment qui remplit les critères de fragilité est le Social Media / Community Management pur (technicité 1,03, saturation documentée, 52 % des annonceurs réduisant leur budget média) : c'est une spécialisation à supprimer, pas une filière à fermer.",
  "FORTE",
  "La fermeture progressive de la filière n'est pas rationnelle au regard du marché de l'emploi. La réduction doit porter sur les PARCOURS social media / communication digitale, pas sur la filière."),
]

# --------------------------------------------------------------- SCÉNARIOS
SCENARIOS = {
 "A_MAINTIEN_GENERALISTE": {
  "titre": "Scénario A — Maintien d'une filière Marketing Digital généraliste",
  "justification": "S'appuie sur la famille la plus volumineuse (111 offres, 22,4 % du périmètre) et sur le premier gisement d'alternance du marché (40,5 % des offres généralistes, plus de 1 000 offres d'alternance marketing digital référencées en 2026).",
  "public_cible": "Bacheliers et Bac+2 cherchant une entrée polyvalente dans le digital.",
  "metiers_vises": "Chargé de marketing digital, assistant marketing digital, chef de projet digital, community manager, chargé de communication digitale.",
  "volume_debouches": "Élevé à l'entrée (111 offres dans l'échantillon, 4 000+ offres Indeed France), faible en progression de carrière.",
  "accessibilite_junior": "Très forte (47,7 % de débutants et juniors).",
  "potentiel_alternance": "Très fort (40,5 %, le plus élevé de toutes les familles).",
  "competences": "Fondamentaux marketing, réseaux sociaux, contenu, emailing, gestion de projet, notions SEO/SEA.",
  "niveau_technicite": "1,42 sur 4 — le plus faible du périmètre après le social media.",
  "exposition_ia": "FORTE — les tâches décrites (publication, mise à jour de contenus, rédaction générique, reporting manuel) sont celles que 75 à 88 % des marketeurs déclarent déjà automatiser avec l'IA générative.",
  "resilience_3_5_ans": "FAIBLE.",
  "potentiel_national": "Fort — présent sur tous les territoires.",
  "potentiel_par_ville": "Viable sur les 6 campus.",
  "avantages": "Modèle d'alternance sécurisé, recrutement étudiant facile, coût pédagogique bas, employabilité immédiate à l'entrée.",
  "risques": "Aucune différenciation face aux dizaines d'écoles proposant la même offre ; valeur du diplôme érodée par l'automatisation des tâches enseignées ; salaires de sortie faibles (20-30 k€ observés) ; pas de justification d'un Bac+5.",
  "effort_pedagogique": "Faible.",
  "differenciation": "Nulle.",
  "coherence_avec_nexa": "Faible — n'exploite pas l'ADN technique de NEXA (Développement Web, IA & Data, Cybersécurité).",
  "confiance": "FORTE",
  "recommandation": "À REJETER comme positionnement d'ensemble ; à conserver uniquement comme socle de première année."},

 "B_TECHNICISATION": {
  "titre": "Scénario B — Technicisation forte (Marketing Technology & Growth)",
  "justification": "S'appuie sur les 51,9 % d'offres spécialisées, sur la corrélation technicité/salaire/pérennité, et sur la complémentarité avec les filières Développement Web et IA & Data de NEXA.",
  "public_cible": "Profils à appétence analytique et technique, du Bachelor au Mastère.",
  "metiers_vises": "Growth marketer, traffic manager, consultant SEA/SEO, CRM manager, marketing automation manager, web analyst, marketing data analyst, marketing ops, RevOps.",
  "volume_debouches": "Élevé en cumul (257 offres spécialisées dans l'échantillon ; Growth Marketing 1 842 offres, CRM Manager 2 000+, Marketing Automation 759 sur Indeed en 2026).",
  "accessibilite_junior": "FAIBLE — 11,8 % de juniors en MarTech, 16,1 % en Data, 17,6 % en Acquisition et en SEO/SEA.",
  "potentiel_alternance": "FAIBLE à MOYEN — 0 % en MarTech et Product Marketing, 3,2 % en Data, 11,8 % en SEO/SEA, 14,1 % en Acquisition.",
  "competences": "GA4, GTM, tracking, attribution, CRO, CRM, marketing automation, SQL, BigQuery, dashboards, no-code, IA appliquée.",
  "niveau_technicite": "2,09 à 2,82 selon la famille.",
  "exposition_ia": "FAIBLE — ce sont les compétences dont l'Apec constate qu'elles gagnent en valeur avec l'IA.",
  "resilience_3_5_ans": "FORTE.",
  "potentiel_national": "Moyen — les postes les plus techniques sont très concentrés en Île-de-France et à Lyon.",
  "potentiel_par_ville": "Paris et Lyon uniquement pour les spécialisations les plus techniques.",
  "avantages": "Différenciation maximale, salaires de sortie supérieurs, résilience à l'automatisation, cohérence avec l'ADN NEXA.",
  "risques": "RISQUE MAJEUR : effondrement de l'alternance en Bachelor, donc du modèle économique et du taux de placement ; sélectivité du recrutement étudiant ; coût pédagogique élevé ; inadéquation avec les campus régionaux.",
  "effort_pedagogique": "Élevé.",
  "differenciation": "Très forte.",
  "coherence_avec_nexa": "Très forte.",
  "confiance": "FORTE",
  "recommandation": "À REJETER en l'état pour le Bachelor (pas d'alternance ni de débouché junior) ; PERTINENT pour le Mastère."},

 "C_HYBRIDE_SPECIALISE": {
  "titre": "Scénario C — Modèle hybride : socle généraliste technicisé en Bachelor, spécialisations techniques en Mastère",
  "justification": "Seul scénario qui réconcilie les deux résultats structurants et contradictoires de l'étude : (1) les débouchés juniors et l'alternance sont concentrés dans le généraliste (47,7 % de juniors, 40,5 % d'alternance) ; (2) la valeur, les salaires et la pérennité sont dans les familles techniques (technicité 2,09 à 2,82, 51,9 % du marché, 0 à 17 % de juniors).",
  "public_cible": "Bachelor : profils polyvalents recrutables en alternance. Mastère : spécialisation sur les métiers réellement porteurs.",
  "metiers_vises": "Bachelor : chargé de marketing digital, assistant acquisition, chargé CRM, assistant e-commerce, traffic manager junior. Mastère : growth/acquisition manager, CRM & marketing automation manager, web/marketing data analyst, e-commerce manager, marketing ops.",
  "volume_debouches": "Maximal — couvre le cœur généraliste (111 offres) ET les familles spécialisées (257 offres), soit 74,3 % du périmètre observé.",
  "accessibilite_junior": "Forte en Bachelor (socle généraliste), progressive en Mastère.",
  "potentiel_alternance": "Fort — le socle Bachelor capte les 1 000 à 1 250 offres d'alternance marketing digital du marché ; le Mastère capte l'alternance CRM (16,7 %), e-commerce (14,3 %) et acquisition (14,1 %).",
  "competences": "Bachelor : fondamentaux marketing, acquisition, SEO, SEA, paid social, contenu, e-commerce, CRM, GA4, GTM, Excel/Sheets, introduction SQL, no-code, IA générative encadrée, gestion de projet, business. Mastère : growth, attribution, CRO, tracking avancé, CRM/CDP, marketing automation, SQL/BigQuery, dashboards, MarTech, pilotage budgétaire, RGPD.",
  "niveau_technicite": "Bachelor cible 2 ; Mastère cible 3 à 4.",
  "exposition_ia": "MOYENNE en Bachelor (compensée par l'obligation du socle technique et de l'IA encadrée), FAIBLE en Mastère.",
  "resilience_3_5_ans": "FORTE.",
  "potentiel_national": "Fort — le socle est déployable sur les 6 campus, les spécialisations sont modulables par territoire.",
  "potentiel_par_ville": "Bachelor sur les 6 campus ; Mastère Growth/Performance et CRM/Data à Paris et Lyon ; Mastère e-commerce à Bordeaux, Nantes et Lille ; distanciel national pour les spécialisations à faible volume local.",
  "avantages": "Sécurise l'alternance et le placement en Bachelor ; capte la valeur et la différenciation en Mastère ; justifie réellement le passage au Bac+5 ; permet des passerelles avec IA & Data et Développement Web.",
  "risques": "Complexité de pilotage pédagogique ; risque d'un socle Bachelor trop dilué si la technicisation n'est pas rendue obligatoire ; nécessité de recruter des intervenants techniques sur les campus régionaux.",
  "effort_pedagogique": "Moyen à élevé.",
  "differenciation": "Forte — un Bachelor généraliste RÉELLEMENT technicisé (GA4, GTM, CRM, SQL) est déjà différenciant face aux écoles de commerce.",
  "coherence_avec_nexa": "Très forte.",
  "confiance": "FORTE",
  "recommandation": "À RETENIR."},

 "D_REDUCTION_FUSION_FERMETURE": {
  "titre": "Scénario D — Réduction, fusion ou fermeture progressive",
  "justification": "Scénario testé explicitement. Les conditions qui le justifieraient (insuffisance durable des débouchés, saturation généralisée, faible accès junior, faibles volumes d'alternance, automatisation massive, différenciation impossible) ne sont PAS réunies.",
  "public_cible": "Sans objet.",
  "metiers_vises": "Sans objet.",
  "volume_debouches": "Le marché ne se contracte pas : 310 000 emplois de filière, croissance cinq fois supérieure au PIB (Alliance Digitale/EY), marché publicitaire digital +11 % en 2025 et +12 % au S1 2026, e-commerce +9 % d'emplois en 2025, 305 800 recrutements de cadres prévus en 2026 (+4 %).",
  "accessibilite_junior": "Sans objet.",
  "potentiel_alternance": "Le volume d'alternance (1 000 à 1 250 offres marketing digital) contredit frontalement l'hypothèse de fermeture.",
  "competences": "Sans objet.",
  "niveau_technicite": "Sans objet.",
  "exposition_ia": "L'automatisation transforme les tâches sans supprimer les postes : 86 % des marketeurs retravaillent systématiquement les contenus générés par l'IA, 92 % imposent une validation humaine.",
  "resilience_3_5_ans": "Sans objet.",
  "potentiel_national": "Sans objet.",
  "potentiel_par_ville": "Sans objet.",
  "avantages": "Réallocation de ressources vers IA & Data et Cybersécurité.",
  "risques": "Perte d'un marché en croissance, d'un vivier d'alternance considérable et d'une porte d'entrée majeure vers l'école ; décision non justifiée par les données.",
  "effort_pedagogique": "Sans objet.",
  "differenciation": "Sans objet.",
  "coherence_avec_nexa": "Faible.",
  "confiance": "FORTE",
  "recommandation": "À REJETER pour la filière. Les variantes partielles suivantes sont en revanche justifiées : ARRÊT DU PARCOURS SOCIAL MEDIA / COMMUNITY MANAGEMENT AUTONOME (technicité 1,03, saturation documentée, 52 % des annonceurs réduisant leur budget média) et RÉDUCTION DU NOMBRE DE PARCOURS au profit de 2 à 3 spécialisations de Mastère à forte technicité."},
}

# --------------------------------------------------------------- MATRICE
# Notes 0-5, documentées. Pondération explicite (les critères stratégiques pèsent double).
CRITERES = [
 ("Volume du marché",                      2, {"GENERALISTE":4,"TECHNIQUE":4,"HYBRIDE_SPECIALISEE":5,"REDUCTION_FUSION_FERMETURE":0},
  "Généraliste 111 offres / Techniques 257 / Hybride couvre les deux (368 offres, 74,3 % du périmètre) / Fermeture renonce à tout."),
 ("Évolution récente",                     1, {"GENERALISTE":2,"TECHNIQUE":4,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "Marché publicitaire digital +11 % (2025) et +12 % (S1 2026), e-commerce +7 % et +9 % d'emplois : la croissance porte l'acquisition, le CRM et l'e-commerce, pas l'exécution généraliste."),
 ("Potentiel à 3-5 ans",                   2, {"GENERALISTE":2,"TECHNIQUE":5,"HYBRIDE_SPECIALISEE":5,"REDUCTION_FUSION_FERMETURE":0},
  "Les compétences analytiques, CRM, data et automation sont celles que l'Apec identifie comme gagnant en valeur avec l'IA ; l'exécution simple perd de la valeur."),
 ("Accessibilité junior",                  2, {"GENERALISTE":5,"TECHNIQUE":1,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "Débutants+juniors : généraliste 47,7 %, MarTech 11,8 %, Data 16,1 %, Product Marketing 0 %. Critère décisif pour une école."),
 ("Alternance",                            2, {"GENERALISTE":5,"TECHNIQUE":1,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "Alternance : généraliste 40,5 %, MarTech 0 %, Data 3,2 %. Plus de 1 000 offres d'alternance marketing digital sur le marché. Critère décisif pour le modèle économique NEXA."),
 ("Niveau de salaire",                     1, {"GENERALISTE":2,"TECHNIQUE":5,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "Postes généralistes observés à 20-30 k€ ; SEO manager confirmé 47 855 € (+4,2 %/an) ; Growth senior 80-90 k€ ; Traffic manager senior >60 k€."),
 ("Tension du marché",                     1, {"GENERALISTE":2,"TECHNIQUE":4,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "Acquisition, CRM, Data et MarTech en tension ; généraliste à l'équilibre ; social media saturé."),
 ("Résilience face à l'IA",                2, {"GENERALISTE":1,"TECHNIQUE":5,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "136 offres de technicité 1 dans l'échantillon décrivent des tâches directement automatisables ; les offres de technicité 3-4 décrivent des compétences valorisées par l'IA."),
 ("Différenciation possible",              2, {"GENERALISTE":1,"TECHNIQUE":5,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "Une offre généraliste est indifférenciable ; un positionnement MarTech/Data Marketing est crédible pour NEXA du fait de ses filières Développement Web et IA & Data."),
 ("Cohérence avec l'ADN digital de NEXA",  1, {"GENERALISTE":2,"TECHNIQUE":5,"HYBRIDE_SPECIALISEE":5,"REDUCTION_FUSION_FERMETURE":1},
  "NEXA est une école du numérique : le positionnement technique est cohérent avec les trois autres filières et rend les passerelles possibles."),
 ("Pertinence Bachelor",                   2, {"GENERALISTE":4,"TECHNIQUE":1,"HYBRIDE_SPECIALISEE":5,"REDUCTION_FUSION_FERMETURE":0},
  "Un Bachelor purement technique n'a ni alternance (0-3 % en MarTech/Data) ni débouché junior ; un Bachelor purement généraliste n'a pas de valeur durable. Le socle technicisé est la seule réponse."),
 ("Pertinence Mastère",                    2, {"GENERALISTE":1,"TECHNIQUE":5,"HYBRIDE_SPECIALISEE":5,"REDUCTION_FUSION_FERMETURE":0},
  "Les métiers exigeant Bac+5 et 3 à 10 ans (CRM manager, marketing automation, web analyst, growth, product marketing, RevOps) justifient un Mastère spécialisé, jamais un Mastère généraliste."),
 ("Potentiel multi-campus",                1, {"GENERALISTE":5,"TECHNIQUE":2,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":0},
  "Stocks Indeed : Paris 2 000+, Lyon 258-317, Lille 113, Marseille 92, Bordeaux 90, Nantes 82. Les spécialisations les plus techniques ne sont soutenables qu'à Paris et Lyon."),
 ("Simplicité pédagogique (inverse du coût)",1,{"GENERALISTE":5,"TECHNIQUE":2,"HYBRIDE_SPECIALISEE":3,"REDUCTION_FUSION_FERMETURE":4},
  "Le socle technicisé et les spécialisations exigent des intervenants experts (tracking, CRM, SQL) et des environnements outillés."),
 ("Maîtrise du risque",                    1, {"GENERALISTE":2,"TECHNIQUE":2,"HYBRIDE_SPECIALISEE":4,"REDUCTION_FUSION_FERMETURE":1},
  "Le généraliste porte un risque d'obsolescence, le technique un risque de placement et d'alternance, l'hybride répartit les deux, la fermeture détruit un actif en croissance."),
]
OPTIONS = ["GENERALISTE", "TECHNIQUE", "HYBRIDE_SPECIALISEE", "REDUCTION_FUSION_FERMETURE"]

def scores():
    tot = {o: 0 for o in OPTIONS}; pmax = 0
    for _, poids, notes, _ in CRITERES:
        pmax += 5 * poids
        for o in OPTIONS: tot[o] += notes[o] * poids
    return tot, pmax

if __name__ == "__main__":
    t, pmax = scores()
    print("=== MATRICE D'ARBITRAGE (pondérée, max %d) ===" % pmax)
    for o, v in sorted(t.items(), key=lambda x: -x[1]):
        print(f"{v:4d} / {pmax}   ({round(100*v/pmax)} %)   {o}")
    print()
    print("=== HYPOTHÈSES ===")
    for h in HYPOTHESES:
        print(f"{h[0]:4s} {h[2]:26s} confiance {h[6]}")
