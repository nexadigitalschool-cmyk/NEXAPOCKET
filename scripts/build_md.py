# -*- coding: utf-8 -*-
"""Livrable 3 : NEXA_Perimetre_Metiers_et_Plateformes_Sans_Donnees.md"""
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis import load, uniques, SCRATCH, OFFRES_DIR, ETUDES_DIR, COLLECTE_DIR
from normalize import NC, is_nc, norm, COEUR, EVOL, SPEC, IA, ADJ, EXCLU

OUTDIR = os.environ.get("NEXA_OUT", "/home/user/NEXAPOCKET")
DATE = "2026-09-06"

# Taxonomie initiale (brief) + métiers découverts. (intitulé, variantes FR, variantes EN, technos, famille, proximité, inclus, justification)
TAXO = [
    # Cœur de marché
    ("Développeur web", "Développeur web ; Développeuse web ; Développeur internet ; Développeur d'applications web", "Web Developer ; Web Engineer", "HTML/CSS, JavaScript, PHP, frameworks web", COEUR, "Métier de référence", "INCLUS", "Intitulé générique du cœur de marché ; regroupé sous 'Développeur web (intitulé générique)' quand aucune techno ni couche n'est précisée."),
    ("Développeur front-end", "Développeur front ; Développeur frontend ; Développeur interface", "Front-End Developer ; Frontend Engineer ; UI Developer (avec code)", "JavaScript, TypeScript, React, Angular, Vue.js, Next.js", COEUR, "Très forte", "INCLUS", "Couche présentation des applications web."),
    ("Développeur back-end", "Développeur back ; Développeur backend ; Développeur serveur", "Back-End Developer ; Backend Engineer ; Server-side Developer", "Node.js, PHP/Symfony/Laravel, Java/Spring, .NET, Python/Django, SQL", COEUR, "Très forte", "INCLUS", "Couche serveur, API et données des applications web."),
    ("Développeur full stack", "Développeur fullstack ; Développeur full-stack ; Développeur web full stack", "Full Stack Developer ; Full-Stack Engineer", "JS/TS + framework back (Node, Symfony, Spring, .NET, Django)", COEUR, "Très forte", "INCLUS", "Intitulé dominant du marché : couvre front et back."),
    ("Intégrateur web", "Intégrateur HTML/CSS ; Intégratrice web ; Développeur intégrateur", "Web Integrator ; HTML/CSS Developer", "HTML, CSS, JavaScript, CMS", COEUR, "Forte", "INCLUS", "Métier d'entrée historique du web ; très peu d'offres observées en 2026."),
    ("Concepteur développeur d'applications", "Concepteur développeur ; Développeur d'applications ; Développeur applicatif ; Développeur informatique", "Application Developer ; Software Developer", "Java, .NET, PHP, JavaScript", COEUR, "Forte", "INCLUS", "Intitulé des titres RNCP et de nombreuses ESN ; inclut le développement d'applications web."),
    ("Développeur JavaScript / TypeScript", "Développeur JS ; Développeur TypeScript ; Développeur Node.js ; Développeur React ; Développeur Angular ; Développeur Vue.js", "JavaScript Developer ; TypeScript Developer ; React Developer ; Angular Developer ; Vue Developer ; Node.js Developer", "JavaScript, TypeScript, React, Angular, Vue.js, Node.js, Next.js, NestJS", COEUR, "Très forte", "INCLUS", "Regroupe les intitulés par technologie JavaScript (front et back)."),
    ("Développeur PHP / Symfony / Laravel", "Développeur PHP ; Développeur Symfony ; Développeur Laravel", "PHP Developer ; Symfony Developer ; Laravel Developer", "PHP, Symfony, Laravel, MySQL", COEUR, "Très forte", "INCLUS", "Écosystème web historique français (ESN, agences, éditeurs)."),
    ("Développeur Java / Spring (web)", "Développeur Java ; Développeur Java web ; Développeur Spring ; Développeur Java/JEE", "Java Developer ; Spring Developer ; Java Backend Engineer", "Java, Spring Boot, JEE, Hibernate, Angular/React associés", COEUR, "Forte", "INCLUS", "Java web (Spring) est un des premiers volumes d'offres ; les offres Java embarqué/mainframe sont exclues."),
    ("Développeur .NET / C#", "Développeur .NET ; Développeur C# ; Développeur ASP.NET", ".NET Developer ; C# Developer", "C#, .NET, ASP.NET Core, SQL Server, Angular/React associés", COEUR, "Forte", "INCLUS", "Stack web Microsoft, fréquente en ESN et éditeurs."),
    ("Développeur Python / Django", "Développeur Python ; Développeur Django ; Développeur Flask", "Python Developer ; Django Developer", "Python, Django, Flask, FastAPI", COEUR, "Forte", "INCLUS", "Python web ; attention, beaucoup d'offres 'développeur Python' relèvent de la data (exclues si sans composante web)."),
    ("Développeur CMS / e-commerce", "Développeur WordPress ; Développeur Drupal ; Développeur Shopify ; Développeur PrestaShop ; Développeur Magento ; Développeur e-commerce", "WordPress Developer ; Drupal Developer ; Shopify Developer ; Magento Developer ; E-commerce Developer", "WordPress, Drupal, Shopify, PrestaShop, Magento/Adobe Commerce, Sylius", COEUR, "Forte", "INCLUS", "Développement sur CMS et plateformes e-commerce ; volumes faibles dans l'échantillon."),
    ("Développeur Ruby on Rails", "Développeur Ruby ; Développeur Rails", "Ruby on Rails Developer", "Ruby, Rails", COEUR, "Forte", "INCLUS", "Découvert pendant la collecte (Paris) ; ajouté au cœur de marché."),
    ("Développeur logiciel (autre langage web/back)", "Développeur Go ; Développeur Rust ; Développeur Scala", "Go Developer ; Rust Developer", "Go, Rust, Scala, Elixir", COEUR, "Moyenne", "INCLUS", "Langages back modernes utilisés pour des services web ; ajouté à la marge."),
    ("Développeur (intitulé générique)", "Développeur ; Développeuse ; Développeur en alternance", "Developer ; Programmer", "Non précisé", COEUR, "Forte", "INCLUS", "Intitulés sans précision de couche ni de techno ; rattachés au cœur de marché mais à lire avec prudence."),
    # Évolutions naturelles
    ("Software Engineer / Ingénieur logiciel", "Ingénieur logiciel ; Ingénieur développement logiciel ; Ingénieur d'études et développement ; Ingénieur informatique", "Software Engineer ; Software Development Engineer", "Tous langages", EVOL, "Forte", "INCLUS", "Prolongement du développeur web vers l'ingénierie logicielle ; intitulé en progression."),
    ("Application Developer", "Développeur d'applications", "Application Developer", "Tous langages", EVOL, "Forte", "INCLUS", "Regroupé avec 'Concepteur développeur d'applications' dans la normalisation."),
    ("Product Engineer", "Ingénieur produit", "Product Engineer", "JS/TS, produit", EVOL, "Moyenne", "INCLUS", "Développeur orienté produit (start-up) ; aucune offre observée dans l'échantillon."),
    ("Développeur API / intégration", "Développeur API ; Développeur intégration", "API Developer ; Integration Engineer", "REST, GraphQL, microservices", EVOL, "Forte", "INCLUS", "Spécialisation back sur les API."),
    ("Développeur mobile", "Développeur mobile ; Développeur iOS ; Développeur Android ; Développeur Flutter ; Développeur React Native", "Mobile Developer ; iOS/Android Engineer", "Swift, Kotlin, Flutter, React Native", EVOL, "Moyenne", "INCLUS", "Débouché adjacent naturel des développeurs JS (React Native) ; comptabilisé dans les évolutions, pas dans le cœur."),
    ("Tech Lead / Lead Developer", "Tech lead ; Lead développeur ; Responsable technique", "Tech Lead ; Lead Developer ; Engineering Manager", "Tous", EVOL, "Forte", "INCLUS", "Évolution à 5+ ans ; cible de la communication Mastère."),
    ("Architecte logiciel / solutions", "Architecte logiciel ; Architecte applicatif ; Architecte solutions", "Software Architect ; Solutions Architect", "Architecture, cloud, microservices", EVOL, "Forte", "INCLUS", "Évolution senior ; cible Mastère."),
    ("Solutions Engineer", "Ingénieur solutions ; Ingénieur avant-vente technique", "Solutions Engineer ; Sales Engineer", "Intégration, API", EVOL, "Moyenne", "INCLUS", "Aucune offre observée ; conservé pour veille."),
    # Spécialisations
    ("DevOps Engineer", "Ingénieur DevOps ; Développeur DevOps", "DevOps Engineer", "Docker, Kubernetes, CI/CD, Terraform, Ansible, AWS/Azure/GCP", SPEC, "Forte", "INCLUS (spécialisation)", "Industrialisation du déploiement ; famille en tension selon Apec/BMO."),
    ("Cloud Engineer", "Ingénieur cloud ; Développeur cloud native", "Cloud Engineer ; Cloud Developer", "AWS, Azure, GCP, Kubernetes", SPEC, "Forte", "INCLUS (spécialisation)", "Compétence cloud demandée aux développeurs ; métier propre pour les seniors."),
    ("Platform Engineer", "Ingénieur plateforme", "Platform Engineer", "Kubernetes, IaC", SPEC, "Moyenne", "INCLUS (spécialisation)", "Évolution du DevOps ; rare dans l'échantillon."),
    ("Site Reliability Engineer (SRE)", "Ingénieur fiabilité", "SRE ; Site Reliability Engineer", "Observabilité, Kubernetes, cloud", SPEC, "Moyenne", "INCLUS (spécialisation)", "Métier d'exploitation logicielle ; profils seniors."),
    ("QA / Test Automation Engineer", "Testeur automaticien ; Ingénieur test ; Ingénieur QA", "QA Automation Engineer ; Test Automation Engineer ; SDET", "Cypress, Playwright, Selenium, Jest", SPEC, "Forte", "INCLUS (spécialisation)", "Contrôle qualité, renforcé par l'IA (validation des sorties)."),
    ("Ingénieur sécurité applicative / DevSecOps", "Ingénieur sécurité applicative ; DevSecOps ; Pentester applicatif", "Application Security Engineer ; AppSec ; DevSecOps", "OWASP, SAST/DAST, IAM", SPEC, "Forte", "INCLUS (spécialisation)", "Passerelle vers la filière Cybersécurité NEXA."),
    ("Développeur spécialisé accessibilité", "Développeur accessibilité ; Expert RGAA", "Accessibility Developer", "RGAA, WCAG, ARIA", SPEC, "Forte", "INCLUS (spécialisation)", "Aucune offre dédiée observée ; compétence citée dans quelques offres front."),
    ("Développeur Green IT / éco-conception", "Développeur éco-conception ; Green IT", "Green Software Engineer", "Éco-conception, RGESN", SPEC, "Moyenne", "INCLUS (spécialisation)", "Aucune offre dédiée observée."),
    # IA
    ("AI Engineer / Développeur IA", "Ingénieur IA ; Développeur IA ; Développeur intelligence artificielle ; Ingénieur en intelligence artificielle", "AI Engineer ; AI Developer ; Applied AI Engineer ; Forward Deployed Engineer", "Python, LLM, API OpenAI/Mistral/Anthropic, LangChain, RAG, cloud", IA, "Moyenne à forte", "INCLUS (émergent)", "Développement d'applications intégrant des modèles ; intitulé le plus fréquent de la famille IA dans l'échantillon."),
    ("AI Software / Application Engineer", "Développeur full stack IA ; Développeur d'applications IA", "AI Software Engineer ; AI Application Developer ; Full Stack AI Engineer", "TS/Python, LLM, API de modèles", IA, "Forte", "INCLUS (émergent)", "Le plus proche du 'développeur augmenté' : développeur web intégrant l'IA."),
    ("LLM / Generative AI Engineer", "Ingénieur IA générative ; Ingénieur LLM", "LLM Engineer ; Generative AI Engineer ; GenAI Engineer", "LLM, fine-tuning, RAG, évaluation", IA, "Moyenne", "INCLUS (émergent)", "Spécialisation IA générative ; ESN et grands comptes."),
    ("Développeur RAG / applications LLM", "Développeur RAG", "RAG Developer", "RAG, bases vectorielles, LangChain/LlamaIndex", IA, "Moyenne", "INCLUS (émergent)", "Rarement un intitulé autonome ; plutôt une compétence citée."),
    ("Développeur d'agents IA", "Développeur agents IA ; Ingénieur agentique", "AI Agent Developer ; Agentic AI Engineer", "Agents, MCP, orchestration", IA, "Moyenne", "INCLUS (émergent)", "Émergent ; très peu d'offres."),
    ("AI Integration / Automation Developer", "Développeur automatisation ; Intégrateur IA", "AI Integration Engineer ; Automation Developer", "n8n, Make, API, LLM", IA, "Moyenne", "INCLUS (émergent)", "Automatisation de processus avec briques IA."),
    ("Low-code / No-code Developer", "Développeur low-code ; Développeur no-code ; Développeur Power Platform", "Low-code Developer ; No-code Developer", "Power Platform, OutSystems, Mendix, Bubble", IA, "Faible à moyenne", "INCLUS (émergent, à la marge)", "Aucune offre observée dans l'échantillon ; conservé pour veille."),
    ("Prompt Engineer (avec composante développement)", "Ingénieur prompt", "Prompt Engineer", "LLM, évaluation", IA, "Faible", "INCLUS (émergent, à la marge)", "Aucune offre observée ; non confirmé comme métier autonome."),
    # Adjacents / exclus
    ("Machine Learning / Data Engineer", "Ingénieur machine learning ; Data engineer ; MLOps", "ML Engineer ; Data Engineer ; MLOps Engineer", "Python, Spark, MLflow", ADJ, "Faible à moyenne", "EXCLU DES VOLUMES (adjacent)", "Relève de la filière IA & Data ; compté à part."),
    ("Développeur logiciel hors web (embarqué, ERP, BI, mainframe)", "Développeur embarqué ; Développeur SAP ; Développeur Salesforce ; Développeur Windev ; Développeur Cobol", "Embedded Developer ; SAP Developer ; Salesforce Developer", "C/C++, ABAP, Apex, Windev, Cobol", ADJ, "Faible", "EXCLU DES VOLUMES (adjacent)", "Découvert pendant la collecte ; hors périmètre web."),
    ("Webmarketing / SEO / content", "Chargé de webmarketing ; Référenceur SEO ; Content manager ; Community manager", "Digital Marketer ; SEO Specialist", "-", EXCLU, "Nulle", "EXCLU", "Faux positif du mot-clé 'web'."),
    ("Webdesigner / UX-UI designer sans code", "Webdesigner ; UX designer ; UI designer", "Web Designer ; Product Designer", "Figma", EXCLU, "Faible", "EXCLU", "Pas de programmation."),
    ("Chef de projet digital sans programmation", "Chef de projet digital ; Chef de projet web ; Product owner", "Digital Project Manager ; Product Owner", "-", EXCLU, "Faible", "EXCLU", "Pas de développement (sauf 'chef de projet technique / dev', inclus au cas par cas)."),
    ("Data analyst sans développement web", "Data analyst ; Analyste données", "Data Analyst", "SQL, Power BI", EXCLU, "Faible", "EXCLU", "Filière IA & Data."),
    ("Formateur / enseignant en développement web", "Formateur développement web ; Intervenant", "Trainer", "-", EXCLU, "Moyenne", "EXCLU", "Découvert pendant la collecte (organismes de formation) ; hors emploi de développeur."),
]


def load_journal_queries():
    qs = []
    for f in glob.glob(os.path.join(OFFRES_DIR, "*journal.txt")) + glob.glob(os.path.join(COLLECTE_DIR, "*journal.txt")):
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if line and not line.upper().startswith(("ARRET", "NOTE", "#", "---")):
                qs.append(line)
    return qs


def queries_for(taxo_row, queries):
    kw = [norm(x) for x in re.split(r"[;/]", taxo_row[0] + ";" + taxo_row[1] + ";" + taxo_row[2]) if len(x.strip()) > 3]
    kw = [k.replace("developpeur ", "") for k in kw]
    hits = []
    for q in queries:
        qn = norm(q)
        if any(k in qn for k in kw):
            hits.append(q.split(" => ")[0].split(" | ")[0].strip())
    hits = list(dict.fromkeys(hits))
    return hits[:6]


def load_platform_logs():
    rows = []
    for f in sorted(glob.glob(os.path.join(OFFRES_DIR, "*plateformes_sans_donnees.jsonl")) + glob.glob(os.path.join(COLLECTE_DIR, "*plateformes_sans_donnees.jsonl"))):
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    d = json.loads(line)
                    d["_agent"] = os.path.basename(f).split("_")[0]
                    rows.append(d)
                except json.JSONDecodeError:
                    pass
    return rows


def load_study_gaps():
    rows = []
    for f in sorted(glob.glob(os.path.join(ETUDES_DIR, "*sans_donnees.jsonl")) + glob.glob(os.path.join(COLLECTE_DIR, "C_sans_donnees.jsonl")) + glob.glob(os.path.join(COLLECTE_DIR, "D*_sans_donnees.jsonl"))):
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if line:
                try:
                    d = json.loads(line)
                    if d.get("SOURCE") or d.get("THEME") or d.get("PLATEFORME"):
                        rows.append(d)
                except json.JSONDecodeError:
                    pass
    return rows


PLATFORM_HOME = {
    "france travail": "https://candidat.francetravail.fr/offres/recherche", "apec": "https://www.apec.fr/candidat/recherche-emploi.html/emploi", "indeed": "https://fr.indeed.com/",
    "linkedin": "https://www.linkedin.com/jobs/", "welcome to the jungle": "https://www.welcometothejungle.com/fr/jobs", "hellowork": "https://www.hellowork.com/fr-fr/emploi/recherche.html",
    "meteojob": "https://www.meteojob.com/", "monster": "https://www.monster.fr/", "talent.com": "https://fr.talent.com/", "jobteaser": "https://www.jobteaser.com/", "jooble": "https://fr.jooble.org/",
    "lesjeudis": "https://www.lesjeudis.com/", "chooseyourboss": "https://www.chooseyourboss.com/", "free-work": "https://www.free-work.com/fr/tech-it/jobs", "glassdoor": "https://www.glassdoor.fr/",
    "api france travail": "https://francetravail.io/data/api/offres-emploi", "data.gouv.fr": "https://www.data.gouv.fr/datasets/offres-demploi-diffusees-a-france-travail",
}


def main():
    rows, vols = load()
    U = uniques(rows)
    cnt = Counter(r["METIER_NORMALISE"] for r in U)
    cnt_all = Counter(r["METIER_NORMALISE"] for r in rows)
    queries = load_journal_queries()
    plat = load_platform_logs()
    gaps = load_study_gaps()
    src_counts = Counter(r["SOURCE"] for r in U)

    L = []
    L.append("# NEXA — Périmètre des métiers et plateformes sans données\n")
    L.append(f"Étude du marché de l'emploi du développement web en France — journal séparé de la collecte. Date de collecte : {DATE}. Voir aussi le fichier Excel (onglet OFFRES_DETAILLEES) et le document Word de synthèse.\n")
    L.append("## Contexte technique de la collecte\n")
    L.append("- L'environnement d'exécution ne permettait aucun accès HTTP direct aux sites externes (proxy réseau : toutes les connexions vers les jobboards, France Travail, Apec, data.gouv.fr, INSEE, Dares, Numeum, etc. ont été refusées avec un code 403 au niveau du proxy ; l'API France Travail nécessite en outre une clé OAuth non disponible).")
    L.append("- Seule voie disponible : un moteur de recherche web renvoyant, pour chaque requête, les titres, URL et extraits des pages publiques indexées. Toutes les offres et tous les comptes d'offres proviennent donc de ces pages indexées (pages d'offres individuelles et pages de liste datées des jobboards).")
    L.append("- Le budget de requêtes était plafonné (200 requêtes par session) ; la collecte a été répartie sur plusieurs sessions parallèles. Les journaux de requêtes sont conservés (fichiers *_journal.txt du dossier `collecte/`).")
    L.append("- Conséquences : de nombreux champs (expérience, salaire, télétravail) ne figurent pas dans les extraits et sont notés NC ; les comptes d'offres des pages de liste sont des bornes basses arrondies (« plus de N »).\n")
    L.append("## PARTIE A — TAXONOMIE DES MÉTIERS\n")
    L.append(f"Taxonomie initiale du brief complétée par les métiers découverts pendant la collecte. Nombre d'offres = offres uniques observées dans l'échantillon ({len(U)} offres uniques dans le périmètre, {len(rows)} lignes brutes).\n")
    fam_names = {COEUR: "COEUR_DE_MARCHE", EVOL: "EVOLUTION_NATURELLE", SPEC: "SPECIALISATION", IA: "METIER_EMERGENT_IA (adjacent, compté à part)", ADJ: "METIER_ADJACENT", EXCLU: "EXCLU_DU_PERIMETRE"}
    # correspondance vers les métiers normalisés observés
    alias = {"Développeur web": "Développeur web (intitulé générique)", "Concepteur développeur d'applications": "Concepteur développeur d'applications / logiciel", "Application Developer": "Concepteur développeur d'applications / logiciel", "Développeur Java / Spring (web)": "Développeur Java / Spring"}
    for row in TAXO:
        name, fr, en, tech, fam, prox, incl, just = row
        key = alias.get(name, name)
        n = cnt.get(key, 0)
        nb = cnt_all.get(key, 0)
        L.append(f"### {name}\n")
        L.append(f"- INTITULE_NORMALISE : {key}")
        L.append(f"- VARIANTES_FRANCAISES : {fr}")
        L.append(f"- VARIANTES_ANGLAISES : {en}")
        L.append(f"- TECHNOLOGIES_ASSOCIEES : {tech}")
        L.append(f"- FAMILLE : {fam_names[fam]}")
        L.append(f"- PROXIMITE_AVEC_LE_DEV_WEB : {prox}")
        L.append(f"- INCLUS_OU_EXCLU : {incl}")
        L.append(f"- JUSTIFICATION : {just}")
        L.append(f"- OFFRES_OBSERVEES : {n} unique(s) / {nb} brute(s)" + (" (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)" if n == 0 else ""))
        qs = queries_for(row, queries)
        L.append("- REQUETES_UTILISEES : " + (" ; ".join(f"`{q}`" for q in qs) if qs else "requêtes génériques par ville et par technologie (voir journaux)"))
        L.append("")
    # métiers découverts non prévus
    known = set(alias.get(r[0], r[0]) for r in TAXO)
    discovered = [m for m in cnt if m not in known and not m.startswith("Exclu")]
    if discovered:
        L.append("### Autres intitulés normalisés apparus dans la collecte\n")
        for m in discovered:
            L.append(f"- {m} : {cnt[m]} offre(s) unique(s)")
        L.append("")
    L.append("### Règles de classement appliquées\n")
    L.append("- Le classement se fait sur l'intitulé de l'offre (règles regex ordonnées : exclusions, puis IA, spécialisations, évolutions, cœur de marché). Un intitulé « full stack » prime sur la technologie citée ; une technologie citée prime sur « développeur web » générique.")
    L.append("- La séniorité est déduite de l'expérience réellement demandée quand elle figure dans l'extrait ; les stages et alternances sont classés DEBUTANT ; les intitulés « lead / architecte » sont classés LEAD_OU_ARCHITECTE (responsabilité technique). Une mention « junior » ou « senior » dans le seul titre est conservée à part (colonne SENIORITE_INDICATIVE_TITRE) et n'est pas comptée.")
    L.append("- Les métiers adjacents (ML/data, embarqué, ERP) et les métiers émergents IA ne sont pas additionnés aux volumes du développement web ; ils sont présentés séparément.\n")

    L.append("## PARTIE B — PLATEFORMES SANS DONNÉES OU AVEC DONNÉES PARTIELLES\n")
    L.append("Toutes les plateformes ont d'abord été testées en accès direct (HTTP) : refus systématique du proxy (403). Le tableau ci-dessous consolide ensuite les tentatives via le moteur de recherche (pages publiques indexées), agent par agent.\n")
    L.append("### B.1 — Accès direct et API (test du " + DATE + ")\n")
    direct = ["France Travail (candidat.francetravail.fr)", "API France Travail Offres d'emploi (api.francetravail.io)", "data.gouv.fr (jeu de données offres France Travail, BMO)", "Apec", "Indeed", "LinkedIn Jobs", "Welcome to the Jungle", "HelloWork", "Meteojob", "Monster", "Talent.com", "JobTeaser", "Jooble", "LesJeudis", "ChooseYourBoss", "Free-Work", "Glassdoor", "statistiques.francetravail.org (BMO)", "INSEE", "Dares", "Numeum", "corporate.apec.fr (études)", "francetravail.org (études)", "FRED (indice Indeed)", "Wikipedia / archives web"]
    L.append("| PLATEFORME | URL | DATE_DU_TEST | METIERS_TESTES | ZONES_TESTEES | DONNEES_RECHERCHEES | RESULTAT | DONNEES_MANQUANTES | AUTRES_CHEMINS_TESTES | SOURCE_DE_REMPLACEMENT | IMPACT_SUR_L_ANALYSE |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for d in direct:
        L.append(f"| {d} | (page d'accueil / API) | {DATE} | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |")
    L.append("")
    L.append("### B.2 — Résultats par plateforme via le moteur de recherche (offres individuelles obtenues dans l'échantillon)\n")
    L.append("| PLATEFORME | OFFRES_UNIQUES_OBTENUES | STATUT |")
    L.append("|---|---|---|")
    all_pl = ["France Travail", "Apec", "Indeed", "LinkedIn", "Welcome to the Jungle", "HelloWork", "Meteojob", "Monster", "Talent.com", "JobTeaser", "Jooble", "LesJeudis", "ChooseYourBoss", "Free-Work", "Glassdoor", "Site carrière", "Autre"]
    for p in all_pl:
        n = src_counts.get(p, 0)
        st = "Données obtenues" if n >= 10 else ("Données partielles" if n > 0 else "AUCUNE DONNÉE EXPLOITABLE")
        L.append(f"| {p} | {n} | {st} |")
    L.append("")
    L.append("### B.3 — Journal détaillé des plateformes sans données (par agent de collecte)\n")
    L.append("| PLATEFORME | URL | DATE_DU_TEST | METIERS_TESTES | ZONES_TESTEES | DONNEES_RECHERCHEES | RESULTAT | DONNEES_MANQUANTES | AUTRES_CHEMINS_TESTES | SOURCE_DE_REMPLACEMENT | IMPACT_SUR_L_ANALYSE |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for d in plat:
        cells = [d.get("PLATEFORME"), d.get("URL") or PLATFORM_HOME.get(norm(d.get("PLATEFORME", "")).split(",")[0].strip(), ""), d.get("DATE_DU_TEST") or DATE, d.get("METIERS_TESTES"), d.get("ZONES_TESTEES"), d.get("DONNEES_RECHERCHEES"), d.get("RESULTAT"), d.get("DONNEES_MANQUANTES"), d.get("AUTRES_CHEMINS_TESTES"), d.get("SOURCE_DE_REMPLACEMENT"), d.get("IMPACT_SUR_L_ANALYSE")]
        cells = [str(c if c not in (None, "") else NC).replace("|", "/").replace("\n", " ") for c in cells]
        cells[0] += f" (agent {d['_agent']})"
        L.append("| " + " | ".join(cells) + " |")
    L.append("")
    L.append("### B.4 — Études et sources documentaires recherchées sans résultat exploitable\n")
    L.append("| SOURCE | REQUETES | RESULTAT |")
    L.append("|---|---|---|")
    for g in gaps:
        src = g.get("SOURCE") or g.get("THEME") or g.get("PLATEFORME")
        rq = g.get("REQUETES") or g.get("REQUETES_LANCEES") or g.get("REQUETE") or ""
        if isinstance(rq, list):
            rq = " ; ".join(rq)
        res = g.get("RESULTAT") or g.get("DONNEES_MANQUANTES") or ""
        L.append(f"| {str(src).replace('|', '/')} | {str(rq).replace('|', '/')[:300]} | {str(res).replace('|', '/')[:400]} |")
    L.append("")
    L.append("### B.5 — Journaux de requêtes\n")
    L.append(f"{len(queries)} requêtes journalisées (fichiers `collecte/*_journal.txt`). Extrait :\n")
    for q in queries[:40]:
        L.append(f"- `{q}`")
    L.append("")
    out = os.path.join(OUTDIR, "NEXA_Perimetre_Metiers_et_Plateformes_Sans_Donnees.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print("Markdown écrit :", out)


if __name__ == "__main__":
    main()
