#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Taxonomie, normalisation et dictionnaire de compétences — Marketing Digital France 2026."""
import re, unicodedata

def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def key(s):
    return re.sub(r"[^a-z0-9 ]+", " ", strip_accents((s or "").lower()))

# ---------------------------------------------------------------- FAMILLES
FAMILLES = ["COEUR_GENERALISTE", "ACQUISITION_PERFORMANCE", "SEO_SEA", "SOCIAL_MEDIA",
            "CONTENT_BRAND", "CRM_LIFECYCLE", "ECOMMERCE", "DATA_ANALYTICS_CRO",
            "MARTECH_MARKETING_OPS", "PRODUCT_MARKETING", "METIER_IA_EMERGENT",
            "METIER_ADJACENT", "EXCLU_DU_PERIMETRE"]

# Règles ordonnées : (regex sur le titre normalisé, métier normalisé, famille, technicité de base)
# L'ordre compte : les règles les plus spécifiques d'abord.
REGLES = [
    # --- EXCLUSIONS (faux positifs) -------------------------------------
    (r"\b(preparateur|livreur|vendeur|conseiller de vente|caissier)\b", "Hors périmètre — vente/logistique", "EXCLU_DU_PERIMETRE", 1),
    (r"\b(gestionnaire carriere|remuneration|paie)\b", "Hors périmètre — RH/paie", "EXCLU_DU_PERIMETRE", 1),
    (r"\b(developpeur|integrateur crm|consultant odoo|lead developer|referent technique)\b", "Hors périmètre — développement/IT", "EXCLU_DU_PERIMETRE", 1),
    (r"\b(conseiller relation client|chargé de suivi client|charge de suivi client|conseiller clientele)\b", "Hors périmètre — relation client", "EXCLU_DU_PERIMETRE", 1),
    (r"\btalent acquisition|charge de recrutement\b", "Hors périmètre — recrutement", "EXCLU_DU_PERIMETRE", 1),
    (r"\bproduct builder|ingenieur ia|agent builder|developpeur d agents\b", "Hors périmètre — tech/produit IA", "EXCLU_DU_PERIMETRE", 4),
    (r"\b(chef de projet informatique|service delivery manager|consultant bi)\b", "Hors périmètre — IT/BI", "EXCLU_DU_PERIMETRE", 3),

    # --- MÉTIERS IA ÉMERGENTS -------------------------------------------
    (r"\b(geo|ai visibility)\b.*\b(manager|specialist|consultant)\b|seo sea geo", "SEO/SEA/GEO — AI Visibility Manager", "METIER_IA_EMERGENT", 3),
    (r"\bseo\b.*\bgeo\b|\bgeo\b.*\bseo\b", "Consultant SEO / GEO", "METIER_IA_EMERGENT", 3),
    (r"\bai content manager|ai marketing|marketing ia\b", "AI Marketing / AI Content Manager", "METIER_IA_EMERGENT", 3),
    (r"agents ia", "Community Manager — Agents IA & GEO/SEO", "METIER_IA_EMERGENT", 3),
    (r"growth manager ia", "Growth Manager IA", "METIER_IA_EMERGENT", 3),
    (r"revops.*(ai|ia)|ai automation analyst", "RevOps — AI, Data & Automation", "METIER_IA_EMERGENT", 4),

    # --- MARTECH / MARKETING OPS / REVOPS -------------------------------
    (r"\brevops|revenue operations\b", "Revenue Operations Manager (RevOps)", "MARTECH_MARKETING_OPS", 4),
    (r"\bsales operations|sales ops\b", "Sales Operations Manager", "MARTECH_MARKETING_OPS", 4),
    (r"marketing operations|marketing ops", "Marketing Operations Manager", "MARTECH_MARKETING_OPS", 4),
    (r"customer data platform|\bcdp\b", "Expert Customer Data Platform (CDP)", "MARTECH_MARKETING_OPS", 4),
    (r"marketing automation", "Marketing Automation Manager / Spécialiste", "MARTECH_MARKETING_OPS", 3),

    # --- CRM / LIFECYCLE ------------------------------------------------
    (r"lifecycle", "Lifecycle / CRM Lifecycle Manager", "CRM_LIFECYCLE", 3),
    (r"\bcrm\b.*\bautomation\b|\bautomation\b.*\bcrm\b", "CRM & Automation Manager", "CRM_LIFECYCLE", 3),
    (r"campaign manager.*crm|crm.*campaign manager|crm & campaign", "CRM Campaign Manager", "CRM_LIFECYCLE", 3),
    (r"\bcrm\b.*(manager|lead|responsable|expert|chef de projet|project manager|domain)", "CRM Manager / Responsable CRM", "CRM_LIFECYCLE", 3),
    (r"(charge|assistant|specialist).*\bcrm\b|\bcrm\b.*(assistant|specialist)", "Chargé / Assistant CRM", "CRM_LIFECYCLE", 2),
    (r"\bcrm\b", "CRM Manager / Responsable CRM", "CRM_LIFECYCLE", 3),
    (r"fidelisation|loyalty|retention", "Retention / Fidélisation Manager", "CRM_LIFECYCLE", 3),
    (r"campaign manager|campagnes? (marketing|digitales)", "Campaign Manager", "CRM_LIFECYCLE", 2),

    # --- SEO / SEA / SEARCH ---------------------------------------------
    (r"\bsea\b.*\bsma\b|\bsma\b.*\bsea\b|paid (search|media).*sma|paid media \(sea", "Consultant SEA / SMA / Paid Media", "SEO_SEA", 2),
    (r"paid search|\bsea\b|google ads|search consultant|search marketing", "Consultant / Manager SEA (Paid Search)", "SEO_SEA", 2),
    (r"\bseo\b|referenceur|referencement naturel", "Consultant / Manager SEO", "SEO_SEA", 2),

    # --- ACQUISITION / PERFORMANCE / GROWTH -----------------------------
    (r"growth (marketing )?(manager|marketer|associate|specialist|hacker|lead)|head of growth|growth & |growth and |\bgrowth\b", "Growth Marketing Manager / Growth Manager", "ACQUISITION_PERFORMANCE", 3),
    (r"traffic manager|trafic manager", "Traffic Manager", "ACQUISITION_PERFORMANCE", 3),
    (r"paid social|social ads", "Consultant / Manager Paid Social", "ACQUISITION_PERFORMANCE", 2),
    (r"media buyer|paid media|investissement media|trader media|programmatique", "Media Buyer / Paid Media", "ACQUISITION_PERFORMANCE", 2),
    (r"performance marketing", "Performance Marketing Manager", "ACQUISITION_PERFORMANCE", 3),
    (r"acquisition", "Responsable / Chargé Acquisition", "ACQUISITION_PERFORMANCE", 3),
    (r"demand generation|lead generation|leadgen|generation de leads", "Demand / Lead Generation Manager", "ACQUISITION_PERFORMANCE", 3),

    # --- DATA / ANALYTICS / CRO / TRACKING ------------------------------
    (r"\bcro\b|conversion rate optimi|optimisation de conversion", "CRO / Conversion Specialist", "DATA_ANALYTICS_CRO", 3),
    (r"web analyst|web analyste|digital analyst|analytics", "Web / Digital Analyst", "DATA_ANALYTICS_CRO", 3),
    (r"(marketing|growth) (data )?analyst|data analyst.*marketing|analyste marketing", "Marketing / Growth Data Analyst", "DATA_ANALYTICS_CRO", 3),
    (r"data analyst|data operations", "Data Analyst (finalité marketing)", "DATA_ANALYTICS_CRO", 3),
    (r"tracking|tagging", "Tracking / Tagging Specialist", "DATA_ANALYTICS_CRO", 4),

    # --- E-COMMERCE -----------------------------------------------------
    (r"e[- ]?merchandis", "E-merchandiser", "ECOMMERCE", 2),
    (r"marketplace", "Marketplace Manager / Specialist", "ECOMMERCE", 2),
    (r"e[- ]?commerce|ecommerce", "E-commerce Manager / Responsable e-commerce", "ECOMMERCE", 2),

    # --- PRODUCT MARKETING ----------------------------------------------
    (r"product marketing|go.?to.?market|\bgtm\b", "Product Marketing Manager", "PRODUCT_MARKETING", 3),
    (r"chef de produit|chef de produits|product manager", "Chef de produit / Product Manager", "METIER_ADJACENT", 2),
    (r"trade marketing", "Chef de projet Trade Marketing", "METIER_ADJACENT", 1),

    # --- CONTENT / BRAND / INFLUENCE ------------------------------------
    (r"influence|influencer|creator partnership", "Influence / Influencer Marketing Manager", "CONTENT_BRAND", 1),
    (r"brand content|brand strategist|content strategist|strategie editoriale", "Content Strategist / Brand Content Manager", "CONTENT_BRAND", 2),
    (r"content (marketing )?manager|content creator|copywriter|redacteur|contenus?\b|editorial", "Content Manager / Content Marketing Manager", "CONTENT_BRAND", 2),

    # --- SOCIAL MEDIA ---------------------------------------------------
    (r"community manager|community et web", "Community Manager", "SOCIAL_MEDIA", 1),
    (r"social media|reseaux sociaux|social m(e|é)dia", "Social Media Manager / Specialist", "SOCIAL_MEDIA", 1),

    # --- CŒUR GÉNÉRALISTE -----------------------------------------------
    (r"(responsable|directeur|director|head of|chef de service).*(marketing digital|digital marketing|marketing & digital|marketing et digital)", "Responsable / Directeur Marketing Digital", "COEUR_GENERALISTE", 2),
    (r"digital marketing manager", "Responsable / Directeur Marketing Digital", "COEUR_GENERALISTE", 2),
    (r"(chef de projet|chef de projets|chef\.?fe de projet|project manager).*(marketing digital|digital|web)", "Chef de projet Marketing Digital / Digital", "COEUR_GENERALISTE", 2),
    (r"(assistant|alternant|alternance|stagiaire|stage).*(marketing digital|digital marketing|webmarketing)", "Assistant / Alternant Marketing Digital", "COEUR_GENERALISTE", 1),
    (r"(charge|chargee|charge e).*(marketing digital|digital marketing|webmarketing|web marketing|marketing & communication digitale)", "Chargé de Marketing Digital", "COEUR_GENERALISTE", 1),
    (r"webmarket|web marketing|webmarketeur", "Webmarketeur / Chargé de webmarketing", "COEUR_GENERALISTE", 2),
    (r"marketing digital|digital marketing", "Chargé de Marketing Digital", "COEUR_GENERALISTE", 1),
    (r"(responsable|directeur|head of|manager) digital\b|digital manager|responsable digital|e[- ]?business", "Responsable Digital", "COEUR_GENERALISTE", 2),
    (r"communication digitale|communication & marketing|communication et marketing|charge de communication", "Chargé de Communication Digitale", "COEUR_GENERALISTE", 1),

    # --- MÉTIERS ADJACENTS ----------------------------------------------
    (r"\bsdr\b|sales development|business developer|business developper|commercial", "Business Developer / SDR", "METIER_ADJACENT", 1),
    (r"(responsable|directeur|head of|chef).*(marketing)|marketing manager|marketing director", "Responsable / Directeur Marketing (généraliste)", "METIER_ADJACENT", 2),
    (r"assistant.*marketing|alternant.*marketing|marketing", "Assistant / Chargé Marketing (généraliste)", "METIER_ADJACENT", 1),
]

def classer(intitule, competences=""):
    t = key(intitule)
    for rx, metier, famille, tech in REGLES:
        if re.search(rx, t):
            return metier, famille, tech
    return "Non classé", "EXCLU_DU_PERIMETRE", 1

# ---------------------------------------------------------------- CONTRATS
def norm_contrat(c, intitule=""):
    c = key(c); t = key(intitule)
    if "alternance" in c or "apprentissage" in c: return "ALTERNANCE"
    if "stage" in c or "stagiaire" in c: return "STAGE"
    if "freelance" in c: return "FREELANCE"
    if "interim" in c: return "INTERIM"
    if c.strip() == "cdd": return "CDD"
    if c.strip() == "cdi": return "CDI"
    # déduction depuis l'intitulé uniquement si le champ contrat est vide/NC
    if c in ("nc", ""):
        if "alternance" in t or "alternant" in t or "apprenti" in t: return "ALTERNANCE"
        if "stage" in t or "stagiaire" in t: return "STAGE"
        if "freelance" in t: return "FREELANCE"
        if re.search(r"\bcdd\b", t): return "CDD"
        if re.search(r"\bcdi\b", t): return "CDI"
    return "NC"

# ---------------------------------------------------------------- SÉNIORITÉ
def norm_seniorite(exp, contrat, intitule=""):
    e = key(exp); t = key(intitule)
    if contrat in ("ALTERNANCE", "STAGE"): return "DEBUTANT"
    if e in ("nc", ""):
        # secours : mentions explicites dans le titre uniquement
        if re.search(r"\b(senior|confirme|expert|lead)\b", t): return "SENIOR"
        if re.search(r"\b(junior|debutant)\b", t): return "JUNIOR"
        if re.search(r"\b(head of|directeur|director|responsable d equipe)\b", t): return "MANAGER_HEAD_DIRECTOR"
        return "NC"
    if "direction" in e or "head" in e or "management" in e: return "MANAGER_HEAD_DIRECTOR"
    if "debutant" in e or "graduate" in e: return "DEBUTANT"
    m = re.findall(r"(\d+)", e)
    if m:
        n = int(m[0])
        if n <= 1: return "DEBUTANT"
        if n <= 2: return "JUNIOR"
        if n <= 5: return "INTERMEDIAIRE"
        return "SENIOR"
    if "junior" in e: return "JUNIOR"
    if "premiere experience" in e or "premiere" in e: return "JUNIOR"
    if "senior" in e or "confirme" in e or "experimente" in e or "expert" in e or "significative" in e: return "SENIOR"
    return "NC"

SENIORITE_ORDRE = ["DEBUTANT", "JUNIOR", "INTERMEDIAIRE", "SENIOR", "MANAGER_HEAD_DIRECTOR", "NC"]

# ---------------------------------------------------------------- COMPÉTENCES
# famille -> {compétence normalisée: regex}
DICO = {
"PUBLICITE": {
    "Google Ads": r"google ads|adwords",
    "Meta Ads / Facebook Ads": r"meta ads|facebook ads|fb ads",
    "Instagram Ads": r"instagram ads",
    "LinkedIn Ads": r"linkedin ads",
    "TikTok Ads": r"tiktok ads",
    "Microsoft / Bing Ads": r"microsoft ads|bing ads",
    "Amazon Ads / retail media": r"amazon ads|cdiscount ads|manomano ads|retail media",
    "Programmatique / DV360": r"programmatiq|dv360|display",
    "Snapchat / Pinterest Ads": r"snapchat|snap ads|pinterest ads",
},
"SEO_SEA": {
    "SEO": r"\bseo\b|referencement naturel|referenceur",
    "SEO technique": r"seo technique|technical seo|audits? techniques?",
    "SEA / Paid Search": r"\bsea\b|paid search",
    "Netlinking / contenu SEO": r"netlinking|content seo|contenus? optimises?",
    "GEO / AEO / AI Search": r"\bgeo\b|generative engine|answer engine|ai visibility|ai search",
},
"ANALYTICS_TRACKING": {
    "Google Analytics 4 / GA4": r"\bga4\b|google analytics",
    "Google Tag Manager / GTM": r"\bgtm\b|google tag manager|tag manager",
    "Looker Studio / dashboards": r"looker|dashboard|data studio",
    "Tracking / data layer / plan de taggage": r"tracking|data layer|taggage|tagging|pixels?",
    "Attribution": r"attribution",
    "Amplitude / Mixpanel / Matomo / Piano": r"amplitude|mixpanel|matomo|piano analytics|adobe analytics",
    "A/B testing / expérimentation": r"a/?b test|experimentation|testing",
    "KPI / reporting / analyse de performance": r"\bkpi\b|reporting|analyse de (la )?performance|performance metrics",
},
"CRM_AUTOMATION": {
    "HubSpot": r"hubspot",
    "Salesforce / Marketing Cloud / Pardot": r"salesforce|marketing cloud|pardot",
    "Braze": r"braze",
    "Klaviyo": r"klaviyo",
    "Brevo / Sendinblue": r"brevo|sendinblue",
    "Adobe Campaign": r"adobe campaign",
    "ActiveCampaign / Mailchimp / Splio / Dotdigital / Actito": r"activecampaign|mailchimp|splio|dotdigital|actito|dartagnan",
    "CRM (générique)": r"\bcrm\b",
    "Marketing automation": r"marketing automation|automation|automatis",
    "Emailing / newsletters / push": r"emailing|email marketing|newsletter|push notification|campagnes email",
    "Segmentation / scoring / nurturing": r"segmentation|scoring|nurturing|lifecycle",
},
"CRO_UX": {
    "CRO / optimisation de conversion": r"\bcro\b|conversion rate|optimisation de conversion|tunnel de conversion|taux de conversion",
    "AB Tasty / Kameleoon / Optimizely / Contentsquare / Hotjar": r"ab tasty|kameleoon|optimizely|contentsquare|hotjar|clarity",
},
"DATA_BI": {
    "SQL": r"\bsql\b",
    "BigQuery / data warehouse": r"bigquery|databricks|data warehouse|entrepot de donnees",
    "Power BI / Tableau / Looker": r"power ?bi|tableau\b|looker\b|datorama",
    "Python": r"python",
    "Excel / Google Sheets": r"excel|google sheets|sheets",
    "CDP / Customer Data Platform": r"\bcdp\b|customer data platform|blueconic|treasure data|imagino|data cloud",
    "Gouvernance / qualité de la donnée": r"gouvernance de la donnee|qualite de la donnee|data quality|fiabilite de la donnee",
},
"NO_CODE_IA": {
    "IA générative (ChatGPT, Claude, Gemini…)": r"ia generative|generative ai|genai|chatgpt|claude|gemini|copilot|midjourney|firefly|\bllm\b",
    "Agents IA / prompt engineering": r"agents? ia|ai agents?|prompt|\bmcp\b",
    "No-code / automatisation (Zapier, Make, n8n)": r"zapier|\bmake\b|n8n|no.?code|airtable|webflow|bubble",
    "IA appliquée au marketing (packshot, création, workflow)": r"packshot ia|creation visuelle.*ia|workflow.*ia|ia.*workflow|automatisation.*ia|ia.*automatis",
    "API / webhook / intégrations": r"\bapi\b|webhook|integration",
},
"ECOMMERCE_SKILL": {
    "E-commerce / gestion de site": r"e.?commerce|boutique en ligne|site marchand",
    "Marketplaces": r"marketplace|amazon\b",
    "Shopify / PrestaShop / Magento / WordPress": r"shopify|prestashop|magento|wordpress|\bcms\b",
    "E-merchandising / catalogue produits": r"merchandising|catalogue|fiches? produits?|flux produits?",
},
"CONTENU_SOCIAL": {
    "Réseaux sociaux (organique)": r"reseaux sociaux|social media|instagram|tiktok|linkedin|facebook|youtube|community",
    "Création de contenu / rédaction": r"creation de contenu|redaction|copywriting|contenus?|editorial|articles? de blog",
    "Vidéo / motion / création visuelle": r"video|montage|reels|motion|creation visuelle|graphi",
    "Influence / partenariats créateurs": r"influence|influenceur|creator|partenariats",
},
"BUSINESS_TRANSVERSE": {
    "Gestion de projet": r"gestion de projet|chef de projet|coordination|project management",
    "Pilotage budgétaire / média": r"budget|investissement media|pilotage budgetaire",
    "Stratégie marketing": r"strategie marketing|strategie digitale|strategie d acquisition|go.?to.?market",
    "Business / ROI / revenue": r"\broi\b|\broas\b|revenue|business|chiffre d affaires|rentabilite",
    "Anglais": r"anglais|english|fluent",
    "B2B": r"\bb2b\b|btob|b to b",
    "B2C": r"\bb2c\b|btoc|b to c",
},
}

def detecter_competences(texte):
    t = key(texte)
    trouve = {}
    for fam, comps in DICO.items():
        for nom, rx in comps.items():
            if re.search(rx, t):
                trouve.setdefault(fam, []).append(nom)
    return trouve

# ---------------------------------------------------------------- TECHNICITÉ
def niveau_technicite(comps_plates, tech_base):
    """N1 exécution / N2 expertise canal / N3 performance-data-automation / N4 MarTech-systèmes."""
    n4 = {"CDP / Customer Data Platform", "BigQuery / data warehouse", "SQL",
          "Gouvernance / qualité de la donnée", "API / webhook / intégrations", "Python"}
    n3 = {"Google Analytics 4 / GA4", "Google Tag Manager / GTM", "Tracking / data layer / plan de taggage",
          "Attribution", "CRO / optimisation de conversion", "Marketing automation",
          "Segmentation / scoring / nurturing", "Looker Studio / dashboards", "A/B testing / expérimentation",
          "Power BI / Tableau / Looker", "No-code / automatisation (Zapier, Make, n8n)",
          "Agents IA / prompt engineering", "Amplitude / Mixpanel / Matomo / Piano"}
    n2 = {"SEO", "SEA / Paid Search", "Google Ads", "Meta Ads / Facebook Ads", "LinkedIn Ads",
          "TikTok Ads", "CRM (générique)", "HubSpot", "Salesforce / Marketing Cloud / Pardot",
          "Braze", "Klaviyo", "Programmatique / DV360", "SEO technique", "GEO / AEO / AI Search",
          "Emailing / newsletters / push", "Marketplaces"}
    s = set(comps_plates)
    if len(s & n4) >= 1: return 4
    if len(s & n3) >= 2: return 3
    if len(s & n3) >= 1 and tech_base >= 3: return 3
    if len(s & n2) >= 1: return max(2, tech_base if tech_base <= 2 else 2)
    return tech_base if tech_base <= 2 else 2

# ---------------------------------------------------------------- SALAIRES
def parse_salaire(v):
    v = (v or "NC").strip()
    if v in ("NC", ""): return None
    m = re.findall(r"\d+", v.replace(" ", "").replace(" ", ""))
    if not m: return None
    n = int(m[0])
    if n < 1000: return None          # ni un TJM ni un mensuel exploitable tel quel
    if n < 10000: return None          # valeurs ambiguës (mensuel) — non retenues
    if n > 300000: return None
    return n

# ---------------------------------------------------------------- RÉGIONS
VILLES_NEXA = {
    "Paris / Île-de-France": ["75", "77", "78", "91", "92", "93", "94", "95"],
    "Lyon métropole": ["69"],
    "Lille métropole": ["59", "62"],
    "Bordeaux métropole": ["33"],
    "Nantes métropole": ["44"],
    "Marseille - Aix": ["13"],
}
PERIMETRES = {
    "Paris / Île-de-France": "Région Île-de-France (75, 77, 78, 91, 92, 93, 94, 95)",
    "Lyon métropole": "Département du Rhône (69), métropole de Lyon et Villeurbanne",
    "Lille métropole": "Nord (59) et Pas-de-Calais (62), MEL et bassin lillois",
    "Bordeaux métropole": "Gironde (33), Bordeaux Métropole",
    "Nantes métropole": "Loire-Atlantique (44), Nantes Métropole et Saint-Nazaire",
    "Marseille - Aix": "Bouches-du-Rhône (13), Marseille, Aix-en-Provence, Aubagne",
}

def ville_nexa(dept):
    for v, depts in VILLES_NEXA.items():
        if dept in depts: return v
    return None
