# -*- coding: utf-8 -*-
"""Normalisation des offres collectées : métiers, régions, contrats, séniorité, salaires, compétences."""
import re
import unicodedata

NC = "NC"


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def norm(s):
    if s is None:
        return ""
    return re.sub(r"\s+", " ", strip_accents(str(s)).lower()).strip()


def is_nc(v):
    if v is None:
        return True
    s = str(v).strip()
    return s == "" or s.upper().startswith("NC") or s.lower().startswith("aucune mention")


# ---------------------------------------------------------------------------
# TAXONOMIE DES MÉTIERS
# ---------------------------------------------------------------------------
COEUR = "COEUR_DE_MARCHE"
EVOL = "EVOLUTION_NATURELLE"
SPEC = "SPECIALISATION"
IA = "METIER_EMERGENT_IA"
ADJ = "METIER_ADJACENT"
EXCLU = "EXCLU_DU_PERIMETRE"

# (regex sur le titre normalisé, métier normalisé, famille) — ordre = priorité
RULES = [
    # Exclusions explicites (faux positifs)
    (r"\b(webmarketing|web marketing|content manager|community manager|traffic manager|referenceur|seo manager|consultant seo|redacteur)\b", "Exclu : marketing / contenu / SEO", EXCLU),
    (r"\b(webdesigner|web designer|ux designer|ui designer|graphiste|product designer|designer)\b", "Exclu : design sans développement", EXCLU),
    (r"\b(data analyst|analyste data|business analyst|data scientist)\b", "Exclu : data sans développement web", EXCLU),
    (r"\b(commercial|business developer|sales|account manager|recruteur|charge de recrutement|talent acquisition)\b", "Exclu : commercial / RH", EXCLU),
    (r"\b(formateur|formatrice|intervenant|enseignant|professeur|formation)\b", "Exclu : formation / enseignement", EXCLU),
    (r"\b(chef de projet|cheffe de projet|project manager|product owner|product manager|scrum master)\b(?!.*(dev|technique))", "Exclu : gestion de projet sans programmation", EXCLU),
    (r"\b(technicien support|support informatique|helpdesk|administrateur systeme|administrateur reseau|sysadmin)\b", "Exclu : support / administration systèmes", EXCLU),

    # Métiers émergents liés à l'IA (composante développement)
    (r"\b(prompt engineer)\b", "Prompt Engineer (avec composante développement)", IA),
    (r"\b(llm|large language|genai|gen ai|generative ai|ia generative|generative|generatif|generative)\b.*\b(engineer|ingenieur|developpeur|developer|dev)\b|\b(engineer|ingenieur|developpeur|developer)\b.*\b(llm|genai|gen ai|generative|ia generative|generatif)\b", "LLM / Generative AI Engineer", IA),
    (r"\brag\b", "Développeur RAG / applications LLM", IA),
    (r"\b(agent(s)? ia|agents? ai|agentic|ai agent|multi-agent)\b", "Développeur d'agents IA", IA),
    (r"\b(ai integration|integration ia|ai automation|automation developer|developpeur automatisation|automatisation)\b", "AI Integration / Automation Developer", IA),
    (r"\b(low[- ]?code|no[- ]?code|power platform|power apps|outsystems|mendix|bubble)\b", "Low-code / No-code Developer", IA),
    (r"\b(machine learning|ml engineer|mlops|data engineer|deep learning|computer vision|nlp)\b", "Machine Learning / Data Engineer", ADJ),
    (r"\b(ai|ia)\b.*\b(software|application|app|full ?stack|fullstack|web|backend|back-end|frontend|front-end)\b.*\b(engineer|ingenieur|developpeur|developer)\b|\b(developpeur|developer|ingenieur|engineer)\b.*\b(full ?stack|fullstack|web|software|application)\b.*\b(ai|ia)\b", "AI Software / Application Engineer", IA),
    (r"\b(ai engineer|ia engineer|ingenieur ia|ingenieur ai|ingenieur intelligence artificielle|ai developer|developpeur ia|developpeur ai|developpeur intelligence artificielle|developpeur en ia|applied ai|forward deployed)\b|\b(intelligence artificielle)\b.*\b(developpeur|ingenieur|engineer|developer)\b|\b(developpeur|ingenieur|engineer|developer)\b.*\b(intelligence artificielle|\bia\b|\bai\b)", "AI Engineer / Développeur IA", IA),

    # Spécialisations
    (r"\b(site reliability|sre)\b", "Site Reliability Engineer (SRE)", SPEC),
    (r"\b(platform engineer|ingenieur plateforme)\b", "Platform Engineer", SPEC),
    (r"\b(devsecops|appsec|securite applicative|application security|pentester|pentest|securite)\b", "Ingénieur sécurité applicative / DevSecOps", SPEC),
    (r"\b(devops|dev ops)\b", "DevOps Engineer", SPEC),
    (r"\b(cloud engineer|ingenieur cloud|cloud architect|architecte cloud|cloud native|aws engineer|azure engineer|gcp engineer|developpeur cloud)\b", "Cloud Engineer", SPEC),
    (r"\b(qa|test automation|automatisation des tests|testeur|test engineer|quality assurance|ingenieur test|automaticien)\b", "QA / Test Automation Engineer", SPEC),
    (r"\b(accessibilite|rgaa|wcag)\b", "Développeur spécialisé accessibilité", SPEC),
    (r"\b(green it|eco-?conception|ecoconception|numerique responsable)\b", "Développeur Green IT / éco-conception", SPEC),

    # Évolutions naturelles
    (r"\b(architecte|architect)\b", "Architecte logiciel / solutions", EVOL),
    (r"\b(tech ?lead|lead dev|lead developpeur|lead developer|lead technique|responsable technique|head of engineering|engineering manager|staff engineer|principal engineer|cto)\b", "Tech Lead / Lead Developer", EVOL),
    (r"\b(solutions? engineer|solution engineer|ingenieur solutions|ingenieur avant-vente|pre-?sales engineer)\b", "Solutions Engineer", EVOL),
    (r"\b(product engineer)\b", "Product Engineer", EVOL),
    (r"\b(mobile|android|ios|flutter|react native|kotlin|swift)\b", "Développeur mobile", EVOL),
    (r"\b(api)\b(?!.*full)", "Développeur API / intégration", EVOL),

    # Métiers adjacents (hors web)
    (r"\b(embarque|embedded|c\+\+|firmware|automaticien|plc|sap|abap|cobol|mainframe|as400|powerbuilder|windev|salesforce|servicenow|erp|dynamics|business central|sharepoint|talend|bi\b|power bi)\b", "Développeur logiciel hors web (embarqué, ERP, BI...)", ADJ),

    # Cœur de marché
    (r"\b(full ?stack|fullstack|full-stack)\b", "Développeur full stack", COEUR),
    (r"\b(integrateur|integratrice|integration web|html/css|html css)\b", "Intégrateur web", COEUR),
    (r"\b(front ?end|front-end|frontend|front)\b", "Développeur front-end", COEUR),
    (r"\b(back ?end|back-end|backend|back)\b", "Développeur back-end", COEUR),
    (r"\b(wordpress|drupal|shopify|prestashop|magento|adobe commerce|woocommerce|cms|e-?commerce|ecommerce|sylius|hubspot)\b", "Développeur CMS / e-commerce", COEUR),
    (r"\b(php|symfony|laravel)\b", "Développeur PHP / Symfony / Laravel", COEUR),
    (r"\b(java|spring|jee|j2ee)\b(?!script)", "Développeur Java / Spring", COEUR),
    (r"(\.net|dotnet|\bc#|csharp|asp\.net|\bnet core|\bnet\b)", "Développeur .NET / C#", COEUR),
    (r"\b(python|django|flask|fastapi)\b", "Développeur Python / Django", COEUR),
    (r"\b(react|reactjs|angular|angularjs|vue|vuejs|vue\.js|node|nodejs|node\.js|javascript|typescript|\bjs\b|nextjs|next\.js|nuxt|svelte|nest|nestjs)\b", "Développeur JavaScript / TypeScript", COEUR),
    (r"\b(ruby|rails)\b", "Développeur Ruby on Rails", COEUR),
    (r"\b(go|golang|rust|scala|elixir|kotlin)\b", "Développeur logiciel (autre langage web/back)", COEUR),
    (r"\b(concepteur developpeur|concepteur|developpeur d'applications|developpeur applications|developpeur applicatif|application developer|developpeur logiciel|software developer|developpeur informatique)\b", "Concepteur développeur d'applications / logiciel", COEUR),
    (r"\b(software engineer|ingenieur logiciel|ingenieur developpement|ingenieur d'etudes|ingenieur etudes|ingenieur en developpement|ingenieur r&d|ingenieur developpeur|ingenieur software|ingenieur informatique|ingenieur e en developpement|ingenieur e developpement|ingenieur en informatique)\b", "Software Engineer / Ingénieur logiciel", EVOL),
    (r"\b(web)\b", "Développeur web (intitulé générique)", COEUR),
    (r"\b(developpeur|developpeuse|developer|dev|programmeur|codeur)\b", "Développeur (intitulé générique)", COEUR),
]

# Sous-métiers "technologie" pour INTITULES_ASSOCIES même quand le métier est full stack / front / back
TECH_IN_TITLE = [
    ("React", r"\breact\b(?! native)"), ("Angular", r"\bangular\b"), ("Vue.js", r"\bvue\b|\bvuejs\b|vue\.js"),
    ("Node.js", r"\bnode\b|nodejs|node\.js"), ("JavaScript", r"\bjavascript\b|\bjs\b"), ("TypeScript", r"\btypescript\b|\bts\b"),
    ("PHP", r"\bphp\b"), ("Symfony", r"\bsymfony\b"), ("Laravel", r"\blaravel\b"), ("Java", r"\bjava\b(?!script)"),
    ("Spring", r"\bspring\b"), (".NET", r"\.net|dotnet|\bc#"), ("Python", r"\bpython\b"), ("Django", r"\bdjango\b"),
    ("WordPress", r"\bwordpress\b"), ("Drupal", r"\bdrupal\b"), ("Shopify", r"\bshopify\b"), ("PrestaShop", r"\bprestashop\b"),
    ("Magento", r"\bmagento\b|adobe commerce"), ("Ruby", r"\bruby\b|\brails\b"), ("Go", r"\bgolang\b|\bgo\b"),
]

FAMILLE_ORDER = [COEUR, EVOL, SPEC, IA, ADJ, EXCLU]


def classify_title(title):
    t = norm(title)
    t = t.replace("h/f", " ").replace("f/h", " ").replace("(h/f)", " ").replace("h/f/x", " ").replace("f/h/x", " ")
    t = re.sub(r"\b(ingenieur|developpeur|concepteur|architecte|consultant)[- ]e\b", r"\1", t)
    t = re.sub(r"[\(\)\[\]\-–—/,:;|]+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    # Cas particulier : "chef de projet technique / dev" => évolution
    for rx, metier, fam in RULES:
        if re.search(rx, t):
            return metier, fam
    return "Non classé", ADJ


def techs_in_title(title):
    t = norm(title)
    return [name for name, rx in TECH_IN_TITLE if re.search(rx, t)]


# ---------------------------------------------------------------------------
# RÉGIONS / VILLES NEXA
# ---------------------------------------------------------------------------
REGIONS = [
    "Île-de-France", "Auvergne-Rhône-Alpes", "Hauts-de-France", "Nouvelle-Aquitaine", "Pays de la Loire",
    "Provence-Alpes-Côte d'Azur", "Occitanie", "Grand Est", "Bretagne", "Normandie", "Centre-Val de Loire",
    "Bourgogne-Franche-Comté", "Corse", "La Réunion", "Martinique", "Guadeloupe", "Guyane", "Mayotte",
]

DEPT_REGION = {
    **{d: "Île-de-France" for d in ["75", "77", "78", "91", "92", "93", "94", "95"]},
    **{d: "Auvergne-Rhône-Alpes" for d in ["01", "03", "07", "15", "26", "38", "42", "43", "63", "69", "73", "74"]},
    **{d: "Hauts-de-France" for d in ["02", "59", "60", "62", "80"]},
    **{d: "Nouvelle-Aquitaine" for d in ["16", "17", "19", "23", "24", "33", "40", "47", "64", "79", "86", "87"]},
    **{d: "Pays de la Loire" for d in ["44", "49", "53", "72", "85"]},
    **{d: "Provence-Alpes-Côte d'Azur" for d in ["04", "05", "06", "13", "83", "84"]},
    **{d: "Occitanie" for d in ["09", "11", "12", "30", "31", "32", "34", "46", "48", "65", "66", "81", "82"]},
    **{d: "Grand Est" for d in ["08", "10", "51", "52", "54", "55", "57", "67", "68", "88"]},
    **{d: "Bretagne" for d in ["22", "29", "35", "56"]},
    **{d: "Normandie" for d in ["14", "27", "50", "61", "76"]},
    **{d: "Centre-Val de Loire" for d in ["18", "28", "36", "37", "41", "45"]},
    **{d: "Bourgogne-Franche-Comté" for d in ["21", "25", "39", "58", "70", "71", "89", "90"]},
    "2A": "Corse", "2B": "Corse", "20": "Corse", "971": "Guadeloupe", "972": "Martinique", "973": "Guyane", "974": "La Réunion", "976": "Mayotte",
}

CITY_DEPT = {
    "paris": "75", "boulogne-billancourt": "92", "boulogne": "92", "issy-les-moulineaux": "92", "nanterre": "92", "la defense": "92", "courbevoie": "92",
    "levallois-perret": "92", "levallois": "92", "neuilly-sur-seine": "92", "neuilly": "92", "puteaux": "92", "montrouge": "92", "clichy": "92", "rueil-malmaison": "92",
    "la garenne-colombes": "92", "colombes": "92", "gennevilliers": "92", "malakoff": "92", "vanves": "92", "meudon": "92", "suresnes": "92", "asnieres-sur-seine": "92", "chatillon": "92", "bagneux": "92", "sevres": "92",
    "montreuil": "93", "saint-denis": "93", "saint-ouen": "93", "pantin": "93", "bobigny": "93", "aubervilliers": "93", "noisy-le-grand": "93", "rosny-sous-bois": "93",
    "ivry-sur-seine": "94", "vincennes": "94", "creteil": "94", "vitry-sur-seine": "94", "charenton-le-pont": "94", "rungis": "94", "fontenay-sous-bois": "94", "maisons-alfort": "94", "arcueil": "94", "gentilly": "94", "villejuif": "94",
    "versailles": "78", "saint-quentin-en-yvelines": "78", "guyancourt": "78", "velizy-villacoublay": "78", "velizy": "78", "montigny-le-bretonneux": "78", "poissy": "78", "les mureaux": "78",
    "massy": "91", "evry": "91", "evry-courcouronnes": "91", "palaiseau": "91", "saclay": "91", "orsay": "91", "les ulis": "91", "courtaboeuf": "91",
    "cergy": "95", "roissy": "95", "argenteuil": "95", "marne-la-vallee": "77", "serris": "77", "chessy": "77", "melun": "77", "torcy": "77", "noisiel": "77", "lognes": "77",
    "lyon": "69", "villeurbanne": "69", "venissieux": "69", "bron": "69", "vaulx-en-velin": "69", "saint-priest": "69", "ecully": "69", "limonest": "69", "dardilly": "69", "tassin-la-demi-lune": "69", "caluire-et-cuire": "69", "meyzieu": "69", "oullins": "69", "decines-charpieu": "69", "saint-genis-laval": "69", "champagne-au-mont-d'or": "69",
    "marseille": "13", "aix-en-provence": "13", "aubagne": "13", "vitrolles": "13", "les milles": "13", "martigues": "13", "salon-de-provence": "13", "istres": "13", "gemenos": "13", "rousset": "13", "meyreuil": "13",
    "lille": "59", "villeneuve-d'ascq": "59", "villeneuve d'ascq": "59", "roubaix": "59", "tourcoing": "59", "marcq-en-baroeul": "59", "lesquin": "59", "wasquehal": "59", "la madeleine": "59", "lomme": "59", "loos": "59", "valenciennes": "59", "dunkerque": "59", "croix": "59", "seclin": "59", "euratechnologies": "59",
    "nantes": "44", "saint-herblain": "44", "carquefou": "44", "reze": "44", "orvault": "44", "saint-nazaire": "44", "bouguenais": "44", "vertou": "44", "la chapelle-sur-erdre": "44",
    "bordeaux": "33", "merignac": "33", "pessac": "33", "begles": "33", "talence": "33", "cenon": "33", "bruges": "33", "le haillan": "33", "gradignan": "33", "floirac": "33", "lormont": "33", "villenave-d'ornon": "33", "blanquefort": "33", "eysines": "33", "libourne": "33",
    "toulouse": "31", "labege": "31", "blagnac": "31", "colomiers": "31", "ramonville": "31", "balma": "31", "montpellier": "34", "castelnau-le-lez": "34", "perols": "34", "nimes": "30", "perpignan": "66", "albi": "81",
    "rennes": "35", "cesson-sevigne": "35", "saint-malo": "35", "brest": "29", "quimper": "29", "vannes": "56", "lorient": "56", "saint-brieuc": "22", "lannion": "22",
    "strasbourg": "67", "schiltigheim": "67", "illkirch": "67", "mulhouse": "68", "colmar": "68", "nancy": "54", "metz": "57", "reims": "51", "troyes": "10",
    "grenoble": "38", "meylan": "38", "clermont-ferrand": "63", "annecy": "74", "saint-etienne": "42", "valence": "26", "chambery": "73",
    "nice": "06", "sophia antipolis": "06", "sophia-antipolis": "06", "valbonne": "06", "biot": "06", "antibes": "06", "cannes": "06", "toulon": "83", "avignon": "84",
    "poitiers": "86", "limoges": "87", "pau": "64", "bayonne": "64", "biarritz": "64", "anglet": "64", "la rochelle": "17", "niort": "79", "angouleme": "16",
    "angers": "49", "le mans": "72", "laval": "53", "la roche-sur-yon": "85", "amiens": "80", "arras": "62", "rouen": "76", "le havre": "76", "caen": "14",
    "tours": "37", "orleans": "45", "blois": "41", "chartres": "28", "dijon": "21", "besancon": "25", "belfort": "90", "ajaccio": "2A", "bastia": "2B",
    "saint-denis (la reunion)": "974", "fort-de-france": "972", "pointe-a-pitre": "971", "cayenne": "973",
}

NEXA_ZONES = {
    "Paris et Île-de-France": {"region": "Île-de-France"},
    "Lyon et métropole": {"depts": ["69"]},
    "Lille et métropole": {"cities": ["lille", "villeneuve-d'ascq", "villeneuve d'ascq", "roubaix", "tourcoing", "marcq-en-baroeul", "lesquin", "wasquehal", "la madeleine", "lomme", "loos", "croix", "seclin", "euratechnologies"]},
    "Bordeaux et métropole": {"cities": ["bordeaux", "merignac", "pessac", "begles", "talence", "cenon", "bruges", "le haillan", "gradignan", "floirac", "lormont", "villenave-d'ornon", "blanquefort", "eysines"]},
    "Nantes et métropole": {"cities": ["nantes", "saint-herblain", "carquefou", "reze", "orvault", "bouguenais", "vertou", "la chapelle-sur-erdre"]},
    "Marseille et Aix-en-Provence": {"cities": ["marseille", "aix-en-provence", "aubagne", "vitrolles", "les milles", "gemenos", "rousset", "meyreuil", "martigues"]},
}


def clean_city(v):
    if is_nc(v):
        return NC
    s = str(v).strip()
    s = re.sub(r"\s*\(\d+\)\s*$", "", s)
    s = re.sub(r"\s+\d{5}$", "", s)
    s = re.sub(r"\s*\d+e(r)?\s*(arrondissement)?$", "", s, flags=re.I)  # Paris 13e
    s = re.sub(r"\s*-\s*\d{5}.*$", "", s)
    return s.strip(" -,")


def city_key(v):
    c = norm(clean_city(v))
    c = re.sub(r"\s*\(.*\)$", "", c).strip()
    if c.startswith("paris"):
        return "paris"
    if c.startswith("marseille"):
        return "marseille"
    if c.startswith("lyon"):
        return "lyon"
    return c


def normalize_region(region, dept, ville):
    r = str(region or "").strip()
    rn = norm(r)
    tele = "teletravail" in rn or "remote" in rn or "teletravail" in norm(ville) or "remote" in norm(ville) or "full remote" in norm(ville)
    # 1) département
    d = str(dept or "").strip()
    d = re.sub(r"[^0-9AB]", "", d.upper())
    if d in DEPT_REGION:
        return DEPT_REGION[d], d, tele
    # 2) ville
    ck = city_key(ville)
    if ck in CITY_DEPT:
        d2 = CITY_DEPT[ck]
        return DEPT_REGION[d2], d2, tele
    # 3) région déclarée
    for reg in REGIONS:
        if norm(reg) in rn or rn.startswith(norm(reg)[:8]):
            return reg, NC, tele
    if "paca" in rn or "provence" in rn:
        return "Provence-Alpes-Côte d'Azur", NC, tele
    if "ile de france" in rn or "idf" in rn:
        return "Île-de-France", NC, tele
    if "aura" in rn or "rhone" in rn:
        return "Auvergne-Rhône-Alpes", NC, tele
    if tele:
        return "Télétravail (France entière)", NC, True
    return NC, NC, tele


def nexa_zone(region, dept, ville, tele_full):
    ck = city_key(ville)
    for z, spec in NEXA_ZONES.items():
        if "region" in spec and region == spec["region"]:
            return z
        if "depts" in spec and dept in spec["depts"]:
            return z
        if "cities" in spec and ck in spec["cities"]:
            return z
    if region == "Télétravail (France entière)":
        return "Marché national à distance"
    return "Hors villes NEXA"


# ---------------------------------------------------------------------------
# CONTRATS
# ---------------------------------------------------------------------------
def normalize_contract(v, title=""):
    s = norm(v)
    t = norm(title)
    if s and not s.startswith("nc"):
        if "alternance" in s or "apprenti" in s or "professionnalisation" in s:
            return "ALTERNANCE"
        if "stage" in s or "intern" in s:
            return "STAGE"
        if "cdi" in s:
            return "CDI"
        if "cdd" in s:
            return "CDD"
        if "freelance" in s or "independant" in s or "portage" in s:
            return "FREELANCE"
        if "interim" in s:
            return "INTERIM"
        if "mission" in s:
            return "MISSION_COURTE"
        if "autre" in s or "poei" in s or "fonction publique" in s or "contractuel" in s:
            return "AUTRE"
    # sinon déduction limitée au titre pour alternance / stage / freelance (mentions explicites)
    if re.search(r"\b(alternance|alternant|alternante|apprenti|apprentissage)\b", t):
        return "ALTERNANCE"
    if re.search(r"\b(stage|stagiaire|internship|intern)\b", t):
        return "STAGE"
    if re.search(r"\b(freelance|independant)\b", t):
        return "FREELANCE"
    if re.search(r"\bcdi\b", t):
        return "CDI"
    if re.search(r"\bcdd\b", t):
        return "CDD"
    return NC


# ---------------------------------------------------------------------------
# SÉNIORITÉ
# ---------------------------------------------------------------------------
def parse_years(s):
    s = norm(s)
    nums = [float(x.replace(",", ".")) for x in re.findall(r"(\d+(?:[.,]\d+)?)\s*(?:\+|ans|an\b|years|year|y\b)", s)]
    if not nums:
        nums = [float(x) for x in re.findall(r"\b(\d{1,2})\b", s)]
        nums = [n for n in nums if n <= 20]
    return nums


def normalize_seniority(exp, title, contract):
    """Retourne (SENIORITE, ORIGINE). Priorité à l'expérience réellement demandée."""
    t = norm(title)
    e = norm(exp)
    if re.search(r"\b(tech ?lead|lead dev|lead developpeur|lead developer|lead technique|architecte|architect|head of|engineering manager|staff|principal|cto)\b", t):
        return "LEAD_OU_ARCHITECTE", "titre (responsabilité technique)"
    if e and not e.startswith("nc"):
        if re.search(r"debutant accepte|sans experience|aucune experience|0 an|premiere experience|jeune diplome|young graduate|entry level|entry-level|0 a 1|0-1", e):
            return "DEBUTANT", "expérience demandée"
        nums = parse_years(e)
        if nums:
            mn = min(nums)
            if mn < 1:
                return "DEBUTANT", "expérience demandée"
            if mn < 3:
                return "JUNIOR", "expérience demandée"
            if mn <= 5:
                return "INTERMEDIAIRE", "expérience demandée"
            return "SENIOR", "expérience demandée"
        if "junior" in e:
            return "JUNIOR", "expérience demandée (mention 'junior')"
        if "senior" in e or "confirme" in e or "experimente" in e:
            return "SENIOR", "expérience demandée (mention 'senior/confirmé')"
        if "intermediaire" in e or "mid" in e:
            return "INTERMEDIAIRE", "expérience demandée"
        if "debutant" in e:
            return "DEBUTANT", "expérience demandée"
    if contract in ("STAGE", "ALTERNANCE"):
        return "DEBUTANT", "contrat (stage/alternance = sans expérience requise)"
    return NC, "non renseigné dans l'extrait"


def seniority_hint_title(title):
    t = norm(title)
    if re.search(r"\b(junior|debutant)\b", t):
        return "junior (titre)"
    if re.search(r"\b(senior|confirme|experimente)\b", t):
        return "senior (titre)"
    return NC


# ---------------------------------------------------------------------------
# SALAIRES
# ---------------------------------------------------------------------------
def _salary_values(txt, unit):
    tn = norm(txt).replace("\xa0", " ")
    vals = []
    for m in re.finditer(r"(\d{1,3}(?:[ .]\d{3})+|\d+(?:[.,]\d+)?)\s*(k€|ke|k\b)?", tn):
        raw = m.group(1)
        if re.fullmatch(r"\d{1,3}(?:[ .]\d{3})+", raw):
            v = float(re.sub(r"[ .]", "", raw))
        else:
            try:
                v = float(raw.replace(",", "."))
            except ValueError:
                continue
        if m.group(2):
            v *= 1000
        elif unit == "ANNUEL" and v < 200:
            v *= 1000
        vals.append(v)
    return [v for v in vals if v > 0]


def parse_salary(vmin, vmax, contract):
    """Retourne (min_annuel, max_annuel, unite, brut_texte)."""
    parts = [str(x) for x in (vmin, vmax) if not is_nc(x)]
    if not parts:
        return None, None, NC, NC
    txt = " | ".join(parts)
    tn = norm(txt)
    unit = "ANNUEL"
    if re.search(r"tjm|/ ?jour|/j\b|par jour|€ ?/ ?day|/day|jour", tn):
        unit = "TJM"
    elif re.search(r"/ ?mois|par mois|mensuel|month", tn):
        unit = "MENSUEL"
    elif re.search(r"/ ?h\b|/heure|par heure|hour|heure", tn):
        unit = "HORAIRE"
    vals = []
    for p_ in parts:
        vals.extend(_salary_values(p_, unit))
    if unit == "ANNUEL":
        vals = [v for v in vals if 12000 <= v <= 250000]
    elif unit == "MENSUEL":
        vals = [v for v in vals if 300 <= v <= 20000]
    elif unit == "TJM":
        vals = [v for v in vals if 100 <= v <= 2500]
    elif unit == "HORAIRE":
        vals = [v for v in vals if 8 <= v <= 300]
    if not vals:
        return None, None, unit, txt
    return min(vals), max(vals), unit, txt


# ---------------------------------------------------------------------------
# COMPÉTENCES
# ---------------------------------------------------------------------------
SKILLS = {
    "LANGAGES": [("JavaScript", r"\bjavascript\b|\bjs\b(?!on)"), ("TypeScript", r"\btypescript\b|\bts\b"), ("PHP", r"\bphp\b"), ("Java", r"\bjava\b(?!script)"), ("C#", r"\bc#|csharp"), ("Python", r"\bpython\b"), ("Ruby", r"\bruby\b"), ("Go", r"\bgolang\b|\bgo\b(?! to)"), ("Rust", r"\brust\b"), ("Kotlin", r"\bkotlin\b"), ("Swift", r"\bswift\b"), ("Scala", r"\bscala\b"), ("HTML/CSS", r"\bhtml\b|\bcss\b|\bsass\b|\bscss\b|tailwind"), ("SQL", r"\bsql\b(?! server)"), ("C/C++", r"\bc\+\+|\bc\b/c\+\+")],
    "FRONT_END": [("React", r"\breact\b(?![ -]native)|reactjs|react\.js"), ("Angular", r"\bangular\b"), ("Vue.js", r"\bvue\b|vuejs|vue\.js"), ("Next.js", r"nextjs|next\.js"), ("Nuxt", r"\bnuxt\b"), ("Svelte", r"\bsvelte\b"), ("jQuery", r"\bjquery\b"), ("Redux", r"\bredux\b")],
    "BACK_END": [("Node.js", r"\bnode\b|nodejs|node\.js|\bnestjs\b|\bnest\b|express"), ("Symfony", r"\bsymfony\b"), ("Laravel", r"\blaravel\b"), ("Spring", r"\bspring\b"), ("Django", r"\bdjango\b"), ("Flask", r"\bflask\b"), ("FastAPI", r"\bfastapi\b"), (".NET", r"\.net|dotnet|asp\.net"), ("Ruby on Rails", r"\brails\b"), ("Java EE / Jakarta", r"\bjee\b|j2ee|jakarta"), ("Hibernate/JPA", r"hibernate|\bjpa\b")],
    "FULL_STACK": [("Full stack", r"full ?stack|fullstack")],
    "BASES_DE_DONNEES": [("PostgreSQL", r"postgres"), ("MySQL/MariaDB", r"\bmysql\b|mariadb"), ("MongoDB", r"\bmongo"), ("SQL Server", r"sql server|\bmssql\b"), ("Oracle", r"\boracle\b"), ("Redis", r"\bredis\b"), ("Elasticsearch", r"elastic"), ("NoSQL", r"\bnosql\b")],
    "API_ET_MICROSERVICES": [("API REST", r"\bapi\b|\brest\b|restful"), ("GraphQL", r"graphql"), ("Microservices", r"micro-?services?"), ("gRPC", r"\bgrpc\b"), ("Kafka/RabbitMQ", r"\bkafka\b|rabbitmq")],
    "CLOUD": [("AWS", r"\baws\b|amazon web"), ("Azure", r"\bazure\b"), ("GCP", r"\bgcp\b|google cloud"), ("OVH/Scaleway", r"\bovh|scaleway"), ("Cloud (générique)", r"\bcloud\b"), ("Serverless", r"serverless|lambda")],
    "DEVOPS_ET_CI_CD": [("CI/CD", r"ci/cd|ci-cd|\bci\b|integration continue|continuous integration"), ("GitLab", r"gitlab"), ("GitHub", r"\bgithub\b(?! copilot)"), ("Jenkins", r"jenkins"), ("Terraform", r"terraform"), ("Ansible", r"ansible"), ("Git", r"\bgit\b"), ("DevOps", r"devops"), ("Linux", r"\blinux\b")],
    "CONTENEURS": [("Docker", r"\bdocker\b"), ("Kubernetes", r"kubernetes|\bk8s\b")],
    "TEST_ET_QUALITE": [("Tests unitaires", r"tests? unitaires?|unit tests?|jest|phpunit|junit|pytest|mocha"), ("Tests automatisés / E2E", r"tests? automatis|cypress|playwright|selenium|e2e|end-to-end"), ("TDD/BDD", r"\btdd\b|\bbdd\b"), ("Qualité de code", r"clean code|qualite du code|code review|revue de code|sonar")],
    "CYBERSECURITE": [("Sécurité applicative", r"securite|security|owasp|appsec|devsecops"), ("Authentification", r"oauth|jwt|keycloak|sso")],
    "PERFORMANCE": [("Performance/optimisation", r"performance|optimisation|scalab")],
    "ACCESSIBILITE": [("Accessibilité", r"accessibilit|rgaa|wcag")],
    "UX_UI": [("UX/UI", r"\bux\b|\bui\b|figma|design system")],
    "DATA": [("Data", r"\bdata\b|big data|etl|datalake|data ?warehouse")],
    "ARCHITECTURE": [("Architecture", r"architecture|architect|ddd|hexagonal|clean architecture|design patterns|solid")],
    "IA_GENERATIVE": [("IA générative / LLM", r"ia generative|generative ai|genai|gen ai|\bllm\b|large language|gpt|mistral|openai|anthropic|claude(?! code)|gemini"), ("RAG", r"\brag\b"), ("Agents IA", r"agents? ia|ai agents?|agentic|multi-agent|langchain|langgraph|llamaindex"), ("MCP", r"\bmcp\b|model context protocol"), ("Prompt engineering", r"prompt"), ("IA (mention générale)", r"intelligence artificielle|\bia\b|\bai\b|machine learning")],
    "OUTILS_DE_CODAGE_IA": [("GitHub Copilot", r"copilot"), ("Cursor", r"\bcursor\b"), ("Claude Code", r"claude code"), ("ChatGPT", r"chatgpt"), ("Codex", r"\bcodex\b"), ("Développement assisté par IA", r"ai-assisted|assiste par (l')?ia|vibe coding|ai coding")],
    "LOW_CODE_NO_CODE": [("Low-code / No-code", r"low[- ]?code|no[- ]?code|power platform|power apps|n8n|make\.com|zapier|bubble")],
    "GESTION_DE_PROJET": [("Agile/Scrum", r"\bagile\b|\bscrum\b|kanban|safe\b"), ("Jira", r"\bjira\b")],
    "PRODUIT_ET_BUSINESS": [("Compréhension produit/métier", r"produit|product|metier|business|fonctionnel")],
    "SOFT_SKILLS": [("Autonomie", r"autonom"), ("Communication", r"communic"), ("Esprit d'équipe", r"equipe|team"), ("Rigueur", r"rigueur|rigoureux"), ("Curiosité", r"curieu|curiosit|veille")],
    "ANGLAIS": [("Anglais", r"\banglais\b|\benglish\b")],
    "MOBILE": [("Mobile (iOS/Android/Flutter/React Native)", r"\bmobile\b|\bandroid\b|\bios\b|flutter|react[ -]native")],
    "CMS_ECOMMERCE": [("WordPress", r"wordpress"), ("Drupal", r"drupal"), ("Shopify", r"shopify"), ("PrestaShop", r"prestashop"), ("Magento / Adobe Commerce", r"magento|adobe commerce"), ("E-commerce", r"e-?commerce")],
}

SKILL_FIELDS = ["INTITULE_BRUT", "LANGAGES", "FRAMEWORKS", "BASES_DE_DONNEES", "CLOUD", "DEVOPS", "TEST", "CYBERSECURITE", "ARCHITECTURE", "METHODES_PROJET", "COMPETENCES_IA", "SOFT_SKILLS", "ANGLAIS", "DESCRIPTION_SYNTHETIQUE", "PREUVE"]


def extract_skills(row):
    text = " ".join(str(row.get(f, "")) for f in SKILL_FIELDS if not is_nc(row.get(f)))
    t = norm(text)
    found = {}
    for fam, items in SKILLS.items():
        for name, rx in items:
            if re.search(rx, t):
                found.setdefault(fam, []).append(name)
    # nettoyage : "IA (mention générale)" uniquement si aucune mention précise ; éviter faux positifs 'ia' dans le champ COMPETENCES_IA "Aucune mention"
    ia_field = norm(row.get("COMPETENCES_IA", ""))
    ia_explicit = ia_field and not ia_field.startswith("nc") and not ia_field.startswith("aucune")
    if not ia_explicit:
        # ne garder que des mentions IA trouvées dans le titre/description (pas dans le champ vide)
        tt = norm(" ".join(str(row.get(f, "")) for f in ("INTITULE_BRUT", "DESCRIPTION_SYNTHETIQUE", "PREUVE") if not is_nc(row.get(f))))
        for fam in ("IA_GENERATIVE", "OUTILS_DE_CODAGE_IA"):
            if fam in found:
                keep = [n for n in found[fam] if any(re.search(rx, tt) for nn, rx in SKILLS[fam] if nn == n)]
                if keep:
                    found[fam] = keep
                else:
                    del found[fam]
    return found
