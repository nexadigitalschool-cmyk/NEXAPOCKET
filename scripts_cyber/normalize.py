# -*- coding: utf-8 -*-
"""Taxonomie métiers cybersécurité, normalisation et dictionnaire de compétences.
Étude NEXA Digital School — marché de l'emploi cybersécurité France 2026."""
import re, unicodedata

DATE_COLLECTE = "2026-09-08"

def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

def norm(s):
    return strip_accents((s or "").lower())

# ---------------------------------------------------------------- RÉGIONS
DEPT_REGION = {}
for reg, depts in {
 "Île-de-France": ["75","77","78","91","92","93","94","95"],
 "Auvergne-Rhône-Alpes": ["01","03","07","15","26","38","42","43","63","69","73","74"],
 "Hauts-de-France": ["02","59","60","62","80"],
 "Nouvelle-Aquitaine": ["16","17","19","23","24","33","40","47","64","79","86","87"],
 "Occitanie": ["09","11","12","30","31","32","34","46","48","65","66","81","82"],
 "Provence-Alpes-Côte d'Azur": ["04","05","06","13","83","84"],
 "Pays de la Loire": ["44","49","53","72","85"],
 "Bretagne": ["22","29","35","56"],
 "Grand Est": ["08","10","51","52","54","55","57","67","68","88"],
 "Normandie": ["14","27","50","61","76"],
 "Bourgogne-Franche-Comté": ["21","25","39","58","70","71","89","90"],
 "Centre-Val de Loire": ["18","28","36","37","41","45"],
 "Corse": ["2A","2B","20"],
 "Outre-mer / COM": ["971","972","973","974","976","98"],
}.items():
    for d in depts:
        DEPT_REGION[d] = reg

VILLE_REGION = {
 "paris":"Île-de-France","ile-de-france":"Île-de-France","lyon":"Auvergne-Rhône-Alpes",
 "villeurbanne":"Auvergne-Rhône-Alpes","grenoble":"Auvergne-Rhône-Alpes","lille":"Hauts-de-France",
 "nantes":"Pays de la Loire","bordeaux":"Nouvelle-Aquitaine","marseille":"Provence-Alpes-Côte d'Azur",
 "aix-en-provence":"Provence-Alpes-Côte d'Azur","toulouse":"Occitanie","rennes":"Bretagne",
 "strasbourg":"Grand Est","hauts-de-france":"Hauts-de-France","suisse":"Hors France",
 "noumea":"Outre-mer / COM","teletravail":"National / distanciel","france":"National / distanciel",
}

def region_from(dep, ville):
    dep = (dep or "NC").strip()
    if dep and dep != "NC":
        d = dep.zfill(2) if len(dep) == 1 else dep
        if d in DEPT_REGION: return DEPT_REGION[d]
        if d[:3] in DEPT_REGION: return DEPT_REGION[d[:3]]
    v = norm(ville)
    for k, r in VILLE_REGION.items():
        if k in v: return r
    if "teletravail" in v or "remote" in v or "distanciel" in v: return "National / distanciel"
    return "NC"

# --------------------------------------------------- VILLES NEXA (périmètres)
VILLES_NEXA = {
 "Paris / Île-de-France": {"depts": ["75","77","78","91","92","93","94","95"],
   "perimetre": "Région Île-de-France (8 départements : 75, 77, 78, 91, 92, 93, 94, 95), incluant La Défense, Courbevoie, Puteaux, Nanterre, Boulogne-Billancourt, Saint-Denis, Issy-les-Moulineaux, Montrouge, Bezons, Massy, Élancourt, Vélizy, Roissy."},
 "Lyon métropole": {"depts": ["69"], "villes": ["lyon","villeurbanne","craponne","ecully","genas"],
   "perimetre": "Métropole de Lyon et Rhône (69) : Lyon, Villeurbanne, Écully, Craponne, Genas. Grenoble (38) et Clermont-Ferrand (63) sont comptés dans la région mais hors périmètre ville."},
 "Lille métropole": {"depts": ["59","62"], "villes": ["lille","villeneuve-d'ascq","roubaix","ronchin","tourcoing"],
   "perimetre": "Métropole Européenne de Lille (59) et Pas-de-Calais limitrophe (62) : Lille, Villeneuve-d'Ascq, Roubaix, Ronchin."},
 "Bordeaux métropole": {"depts": ["33"], "villes": ["bordeaux","merignac","pessac","talence"],
   "perimetre": "Bordeaux Métropole (33) : Bordeaux, Mérignac, Pessac, Talence."},
 "Nantes métropole": {"depts": ["44"], "villes": ["nantes","saint-herblain","reze"],
   "perimetre": "Nantes Métropole (44) : Nantes, Saint-Herblain, Rezé. Rennes (35) et Cholet (49) sont hors périmètre ville."},
 "Marseille - Aix-en-Provence": {"depts": ["13"], "villes": ["marseille","aix-en-provence","aubagne"],
   "perimetre": "Métropole Aix-Marseille-Provence (13) : Marseille, Aix-en-Provence, Aubagne."},
 "National / distanciel": {"depts": [], "villes": ["teletravail","remote","france","national","distanciel"],
   "perimetre": "Offres explicitement en télétravail total ou à périmètre national, sans ancrage géographique déclaré."},
}

def ville_nexa(dep, ville, teletravail):
    v = norm(ville); d = (dep or "NC").strip()
    if "teletravail total" in norm(teletravail) or "full remote" in norm(teletravail) or v in ("nc","") and "teletravail" in norm(teletravail):
        return "National / distanciel"
    if "teletravail" in v or "remote" in v or v in ("france","france (national)","national"):
        return "National / distanciel"
    for nom, cfg in VILLES_NEXA.items():
        if nom == "National / distanciel": continue
        if d in cfg["depts"]:
            if "villes" in cfg:
                if any(x in v for x in cfg["villes"]) or v in ("nc",""): return nom
                return nom  # même département = bassin
            return nom
        if "villes" in cfg and any(x in v for x in cfg["villes"]): return nom
    return "Hors villes NEXA"

# ------------------------------------------------------------ TAXONOMIE
# (metier_normalise, famille, niveau_technicite, motifs regex)
TAXONOMIE = [
 ("AI Security / LLM Security Engineer","AI_SECURITY_EMERGENT",4,
  r"(ai security|securite (de l')?ia|llm security|ai red team|genai security|ml security|adversarial|prompt injection|cybersecurite ia|securite des llm|agentic ai security)"),
 ("Pentester / Consultant sécurité offensive","OFFENSIVE_SECURITY",4,
  r"(pentest|penetration test|test d'intrusion|tests d'intrusion|ethical hack|offensive|red team|securite offensive|vulnerability research|recherche de vulnerabilites)"),
 ("Cloud Security Engineer / Architect","CLOUD_SECURITY",3,
  r"(cloud security|securite cloud|cloud securite|cspm|cnapp|aws security|azure security|gcp security)"),
 ("DevSecOps Engineer","DEVSECOPS",3, r"(devsecops|dev ?sec ?ops)"),
 ("AppSec / Product Security Engineer","APPSEC_PRODUCT_SECURITY",3,
  r"(appsec|application security|securite applicative|product security|secure software|api security|security & compliance engineer|information security engineer)"),
 ("Consultant / Ingénieur IAM - PAM","IAM_PAM",3,
  r"(\biam\b|identity (and |& )?access|gestion des identites|\bpam\b|privileged access|cyberark|sailpoint|okta|forgerock|iga\b|identity security|entra id|identity provider|identity & digital)"),
 ("Detection Engineer / SOC Engineering","SOC_BLUE_TEAM_SECOPS",3,
  r"(detection engineer|soc detection|detection engineering|siem engineer|soar engineer|log integrator|parsing engineer)"),
 ("Analyste SOC","SOC_BLUE_TEAM_SECOPS",2,
  r"(analyste soc|soc analyst|analyst soc|analyste securite soc|analyste cyber ?securite soc|cyberdefense|cyber defense analyst|analyste n3 soc|soc/csirt|cybersoc|soc/voc|analyste soc/voc)"),
 ("SecOps / Security Operations Engineer","SOC_BLUE_TEAM_SECOPS",3,
  r"((?<!dev)secops|security operations engineer|security operations|maintien en condition de securite)"),
 ("Analyste DFIR / Incident Response","INCIDENT_RESPONSE_FORENSICS",4,
  r"(dfir|incident response|incident responder|forensic|\bcert\b|csirt|reponse aux incidents|malware analyst|reverse engineer)"),
 ("Analyste Threat Intelligence / Threat Hunter","THREAT_INTELLIGENCE",3,
  r"(threat intelligence|\bcti\b|threat hunt|renseignement sur la menace|cybercriminalite|darkweb|analyste de la menace|osint|analyste menaces)"),
 ("Analyste / Manager Vulnérabilités (VOC)","VULNERABILITY_MANAGEMENT",2,
  r"(vulnerabilit|\bvoc\b|vulnerability|exposure management|attack surface)"),
 ("Architecte sécurité / cybersécurité","ARCHITECTURE_ENGINEERING",4, r"(architecte|architect)"),
 ("RSSI / CISO / Responsable cybersécurité","MANAGEMENT_CYBER",4,
  r"(rssi|ciso|responsable (de la )?securite|responsable securite|head of cyber|security manager|soc manager|responsable cyber|officier de securite|cybersecurity officer|senior manager|engineering manager|responsable campus|adjoint au responsable|referent securite|adjoint responsable)"),
 ("Auditeur cybersécurité / SSI","AUDIT_COMPLIANCE",2, r"(auditeur|auditrice|audit )"),
 ("Consultant GRC / Risque / Conformité","GRC_RISK",2,
  r"(\bgrc\b|gouvernance|risques?|\brisk\b|conformite|compliance|nis ?2|\bdora\b|iso ?27001|ebios|smsi|homologation|sensibilisation|resilience|gestion de crise|third party|tprm)"),
 ("Ingénieur / Consultant sécurité OT-ICS","OT_IOT_SECURITY",4,
  r"(\bot\b|\bics\b|scada|industriel|nucleaire|\biot\b|embarque|cyber-physical)"),
 ("Ingénieur sécurité réseau / infrastructure","NETWORK_INFRA_SECURITY",2,
  r"(reseau|network|firewall|pare-feu|infrastructure|systeme et reseau|systemes et reseaux|endpoint|sase|proxy|casb)"),
 ("Chef de projet cybersécurité","MANAGEMENT_CYBER",2,
  r"(chef de projet|cheffe|chef ?fe de projet|project manager|program manager|amoa|assistant.?e chef de projet)"),
 ("Ingénieur cybersécurité (généraliste)","COEUR_GENERALISTE",2,
  r"(ingenieur.?e? (de )?(la )?cyber|ingenieur.?e? cyber|ingenieur.?e? securite|cyber ?security engineer|security engineer|ingenieur.?e? ssi|ingenieur.?e? d'etudes cyber|ingenieux cyber|ingenieur.?e? d'affaires cyber)"),
 ("Consultant cybersécurité (généraliste)","COEUR_GENERALISTE",2,
  r"(consultant|consultante|consulting|expert.?e? cyber|expert.?e? securite|expert cybersecurite|expert ssi|specialist|expert en cyber|expert reseau et cyber|expert risques)"),
 ("Analyste cybersécurité (généraliste)","COEUR_GENERALISTE",2, r"(analyste|analyst|cyber analyst)"),
 ("Administrateur / technicien sécurité","NETWORK_INFRA_SECURITY",1,
  r"(administrateur|administratrice|technicien|support it|assistant)"),
 ("Métier adjacent (DevOps / Cloud / Data / IA sans mission sécurité explicite)","METIER_ADJACENT",2,
  r"(devops|cloud engineer|\bsre\b|developpeur|software engineer|data|ingenierie cloud|intelligence artificielle)"),
]

# Intitulés hors périmètre (faux positifs)
EXCLUSIONS = r"(talent acquisition|recrutement|marketing|commercial|comptable|affreteur|agent de securite|securite incendie|sûrete|assistant/e activites|animateur reseau automobile|professeur|auditeur iscc|auditeur interne|inspecteur auditeur|auditeurs / recetteurs|verification asic|analyste parcours|analyste\(s\) des politiques|chargé de recrutement|analyste innovation)"

def classifier(intitule, contexte=""):
    t = norm(intitule); ctx = norm(contexte)
    if re.search(EXCLUSIONS, t):
        return ("Hors périmètre (faux positif)", "EXCLU_DU_PERIMETRE", 0)
    blob = t + " || " + ctx
    for metier, famille, niv, pattern in TAXONOMIE:
        if re.search(pattern, t):
            return (metier, famille, niv)
    for metier, famille, niv, pattern in TAXONOMIE:
        if famille in ("METIER_ADJACENT",): continue
        if re.search(pattern, blob):
            return (metier, famille, niv)
    if re.search(r"(cyber|securite|security|ssi)", blob):
        return ("Ingénieur cybersécurité (généraliste)", "COEUR_GENERALISTE", 2)
    return ("Métier adjacent (DevOps / Cloud / Data / IA sans mission sécurité explicite)", "METIER_ADJACENT", 2)

FAMILLE_LIB = {
 "COEUR_GENERALISTE":"Cœur généraliste","SOC_BLUE_TEAM_SECOPS":"SOC / Blue Team / SecOps",
 "INCIDENT_RESPONSE_FORENSICS":"Incident Response / Forensics","THREAT_INTELLIGENCE":"Threat Intelligence",
 "OFFENSIVE_SECURITY":"Offensive Security / Pentest","VULNERABILITY_MANAGEMENT":"Vulnerability Management",
 "CLOUD_SECURITY":"Cloud Security","APPSEC_PRODUCT_SECURITY":"AppSec / Product Security","DEVSECOPS":"DevSecOps",
 "IAM_PAM":"IAM / PAM","GRC_RISK":"GRC / Risques","AUDIT_COMPLIANCE":"Audit / Conformité",
 "ARCHITECTURE_ENGINEERING":"Architecture / Security Engineering","NETWORK_INFRA_SECURITY":"Sécurité réseau / infrastructure",
 "OT_IOT_SECURITY":"Sécurité OT / IoT","MANAGEMENT_CYBER":"Management cyber","AI_SECURITY_EMERGENT":"AI Security (émergent)",
 "METIER_ADJACENT":"Métier adjacent","EXCLU_DU_PERIMETRE":"Exclu du périmètre",
}

# ------------------------------------------------------------ CONTRATS
def contrat_norm(c):
    n = norm(c)
    if "alternance" in n or "apprentis" in n or "alternant" in n: return "ALTERNANCE"
    if "stage" in n or "stagiaire" in n: return "STAGE"
    if "freelance" in n or "mission" in n: return "FREELANCE"
    if "interim" in n: return "INTERIM"
    if "cdd" in n and "cdi" in n: return "CDD"
    if "cdd" in n: return "CDD"
    if "cdi" in n: return "CDI"
    return "NC"

# ------------------------------------------------------------ SÉNIORITÉ
def seniorite(exp_txt, intitule, contrat):
    c = contrat_norm(contrat)
    if c in ("ALTERNANCE","STAGE"): return "DEBUTANT"
    e = norm(exp_txt); t = norm(intitule)
    if re.search(r"(head of|rssi|ciso|directeur|manager|responsable|soc manager|program manager)", t):
        return "MANAGER_HEAD_DIRECTOR"
    m = re.findall(r"(\d+)\s*(?:a|-|à)?\s*(\d+)?\s*ans", e)
    if m:
        lo = int(m[0][0]); hi = int(m[0][1]) if m[0][1] else lo
        v = (lo + hi) / 2
        if v <= 1: return "DEBUTANT"
        if v <= 2: return "JUNIOR"
        if v <= 5: return "INTERMEDIAIRE"
        return "SENIOR"
    if re.search(r"(debutant|sans experience|entry.?level|premiere experience|junior)", e): return "JUNIOR"
    if re.search(r"(senior|confirme|expert|10 ans)", e): return "SENIOR"
    if re.search(r"\b(junior|apprenti|debutant)\b", t): return "JUNIOR"
    if re.search(r"(senior|expert|confirme|principal|\bn3\b|niveau 3)", t): return "SENIOR"
    return "NC"

SENIO_ORDRE = ["DEBUTANT","JUNIOR","INTERMEDIAIRE","SENIOR","MANAGER_HEAD_DIRECTOR","NC"]

# ------------------------------------------------------------ DIPLÔME
def niveau_etude(dip, desc):
    b = norm(dip + " " + desc)
    if re.search(r"bac\s*\+?\s*5|master|mastere|ingenieur|m1|m2", b): return "Bac+5"
    if re.search(r"bac\s*\+?\s*4", b): return "Bac+4"
    if re.search(r"bac\s*\+?\s*3|bachelor|licence", b): return "Bac+3"
    if re.search(r"bac\s*\+?\s*2|bts|dut", b): return "Bac+2"
    return "NC"

# ------------------------------------------------------------ COMPÉTENCES
DICO = [
 ("SYSTEMES","Linux",r"\blinux\b"),("SYSTEMES","Windows",r"\bwindows\b"),
 ("SYSTEMES","Active Directory",r"(active directory|\bad\b(?! ?hoc)|bloodhound)"),
 ("SYSTEMES","Entra ID / Azure AD",r"(entra id|azure ad|azure active directory)"),
 ("RESEAUX","Réseaux / TCP-IP",r"(reseau|network|tcp/ip|vlan|routage|dns|dhcp|protocoles reseaux)"),
 ("RESEAUX","Firewall / Palo Alto / Fortinet",r"(firewall|pare-feu|palo alto|fortinet|fortigate|check point)"),
 ("RESEAUX","VPN / Proxy / SASE / Zero Trust",r"(vpn|proxy|sase|sse|zero trust|casb|netskope|zscaler|segmentation)"),
 ("RESEAUX","IDS / IPS / NDR",r"(ids|ips|\bndr\b)"),
 ("SOC","SOC / supervision",r"(\bsoc\b|supervision|monitoring|surveillance)"),
 ("SOC","SIEM",r"(\bsiem\b)"),("SOC","Splunk",r"splunk"),("SOC","Microsoft Sentinel",r"sentinel"),
 ("SOC","QRadar",r"qradar"),("SOC","Elastic / ELK",r"(elastic|\belk\b)"),
 ("SOC","EDR / XDR",r"(\bedr\b|\bxdr\b|crowdstrike|sentinelone|defender for endpoint|cortex xdr)"),
 ("SOC","SOAR / playbooks",r"(soar|playbook|xsoar)"),
 ("SOC","Detection engineering / règles",r"(detection engineering|regles de detection|detection rules|use cases de detection|cas d'usage de detection|correlation|sigma|yara)"),
 ("SOC","MITRE ATT&CK",r"(mitre|att&ck|attack framework)"),
 ("SOC","Threat hunting",r"(threat hunt|chasse aux menaces)"),
 ("IR_FORENSICS","Incident Response",r"(incident response|reponse (a|aux) incident|gestion d'incident|gestion des incidents|traitement d'incident)"),
 ("IR_FORENSICS","Forensic / DFIR",r"(forensic|dfir|investigation)"),
 ("IR_FORENSICS","Malware analysis / reverse",r"(malware|reverse engineer|sandbox)"),
 ("CTI","Threat Intelligence / OSINT",r"(threat intelligence|\bcti\b|osint|misp|opencti|darkweb|ioc\b|stix|taxii)"),
 ("OFFENSIVE","Pentest",r"(pentest|test d'intrusion|tests d'intrusion|penetration test)"),
 ("OFFENSIVE","Red Team",r"(red team)"),
 ("OFFENSIVE","Outils offensifs (Burp, Metasploit, Nmap...)",r"(burp|metasploit|nmap|nessus|impacket|mimikatz|kali|wireshark)"),
 ("VULN","Vulnerability management / CVE-CVSS",r"(vulnerabilit|cve\b|cvss|remediation|tenable|qualys|rapid7|exposure management)"),
 ("CLOUD","Cloud (générique)",r"(\bcloud\b)"),("CLOUD","AWS",r"\baws\b"),("CLOUD","Azure",r"\bazure\b"),
 ("CLOUD","GCP",r"(\bgcp\b|google cloud)"),
 ("CLOUD","CSPM / CNAPP / Prisma / Wiz",r"(cspm|cnapp|cwpp|prisma cloud|\bwiz\b|orca security|guardduty|security hub|defender for cloud)"),
 ("APPSEC","Sécurité applicative / OWASP",r"(appsec|application security|securite applicative|owasp|secure coding|ssdlc|threat modeling|revue de code|code review)"),
 ("APPSEC","SAST / DAST / SCA",r"(\bsast\b|\bdast\b|\bsca\b|snyk|sonarqube|checkmarx|veracode|semgrep|secret scanning|sbom)"),
 ("APPSEC","API Security",r"(api security|securite des api)"),
 ("DEVSECOPS","DevSecOps",r"(devsecops|dev ?sec ?ops)"),
 ("DEVSECOPS","CI/CD",r"(ci/cd|\bci ?cd\b|integration continue|gitlab ci|github actions|jenkins|pipeline)"),
 ("DEVSECOPS","Conteneurs / Docker",r"(docker|conteneur|container)"),
 ("DEVSECOPS","Kubernetes",r"(kubernetes|k8s|\bgke\b|\becs\b|nomad)"),
 ("DEVSECOPS","Infrastructure as Code / Terraform",r"(terraform|infrastructure as code|\biac\b|ansible)"),
 ("IAM","IAM / gestion des identités",r"(\biam\b|identity (and |& )?access|gestion des identites|\biga\b|identity governance|sso|\bmfa\b|rbac)"),
 ("IAM","PAM / accès à privilèges",r"(\bpam\b|privileged access|cyberark|wallix|delinea)"),
 ("IAM","Outils IAM (SailPoint, Okta, Ping...)",r"(sailpoint|okta|ping identity|forgerock|one identity|evidian|memority|racf)"),
 ("IAM","PKI / cryptographie",r"(\bpki\b|certificat|cryptograph|chiffrement|\btls\b)"),
 ("GRC","Gouvernance / PSSI",r"(gouvernance|pssi|politique de securite|security policy)"),
 ("GRC","Gestion des risques",r"(gestion des risques|analyse de risques|risk (management|analysis|assessment)|cyber risk|risques? cyber)"),
 ("GRC","ISO 27001 / SMSI",r"(iso ?270|smsi|isms|\bhds\b|soc ?2)"),
 ("GRC","EBIOS RM",r"ebios"),("GRC","NIS2",r"(nis ?2|nis2)"),("GRC","DORA",r"\bdora\b"),
 ("GRC","RGPD / conformité",r"(rgpd|gdpr|conformite|compliance|\blpm\b|\bcra\b|homologation)"),
 ("GRC","Audit",r"(audit)"),
 ("GRC","Third-party / fournisseurs",r"(third party|tiers|fournisseur|supply chain|tprm|vendor)"),
 ("GRC","Continuité / gestion de crise / résilience",r"(continuite|pca|pra|\bbcp\b|disaster recovery|gestion de crise|resilience)"),
 ("GRC","Sensibilisation",r"(sensibilisation|awareness|formation des utilisateurs)"),
 ("OT","OT / ICS / SCADA",r"(\bot\b|\bics\b|scada|\bdcs\b|\bplc\b|industriel|iec ?62443|nucleaire)"),
 ("OT","IoT / embarqué",r"(\biot\b|embarque)"),
 ("SCRIPTING","Python",r"\bpython\b"),("SCRIPTING","PowerShell",r"powershell"),("SCRIPTING","Bash",r"\bbash\b"),
 ("SCRIPTING","Automatisation",r"(automatisation|automation|automatis)"),
 ("SCRIPTING","Git",r"(\bgit\b|github|gitlab)"),
 ("IA","IA générative / LLM",r"(\bllm\b|ia generative|generative ai|genai|chatgpt|claude|gemini|copilot|intelligence artificielle|\bia\b)"),
 ("IA","AI Security / sécurisation des systèmes IA",r"(ai security|securite de l'ia|securite des llm|prompt injection|adversarial|ai red team|agentic ai|rag security|securisation.*(ia|llm))"),
 ("IA","Agents IA / RAG",r"(agents? ia|ai agents?|agentic|\brag\b)"),
 ("TRANSVERSE","Gestion de projet",r"(gestion de projet|chef de projet|project manage|amoa)"),
 ("TRANSVERSE","Communication / pédagogie",r"(communication|pedagogi|redaction|reporting|documentation|restitution)"),
 ("TRANSVERSE","Anglais",r"(anglais|english)"),
 ("TRANSVERSE","Architecture",r"(architecture|architecte)"),
]

CERTIFS = [
 ("CISSP",r"\bcissp\b"),("CISM",r"\bcism\b"),("CISA",r"\bcisa\b"),
 ("OSCP",r"\boscp\b"),("CEH",r"\bceh\b"),("CompTIA Security+",r"(security\+|comptia security)"),
 ("CompTIA CySA+",r"(cysa\+)"),("CompTIA PenTest+",r"(pentest\+)"),
 ("Microsoft SC-200",r"\bsc-?200\b"),("Microsoft SC-300",r"\bsc-?300\b"),("Microsoft SC-100",r"\bsc-?100\b"),
 ("Microsoft AZ-500",r"\baz-?500\b"),("Azure Administrator Associate",r"azure administrator"),
 ("AWS Certified Security",r"(aws certified security|aws security specialty)"),
 ("AWS Solutions Architect",r"aws (certified )?solutions? architect"),
 ("ISO 27001 Lead Auditor / Implementer",r"(lead auditor|lead implementer)"),
 ("EBIOS RM (certification)",r"ebios risk manager"),
 ("CCSP",r"\bccsp\b"),("CCNA / CCNP Security",r"(ccna|ccnp)"),("GIAC",r"\bgiac\b"),
 ("Certification SIEM/SOAR/EDR/XDR (non nommée)",r"certification technique (siem|soar|edr|xdr)"),
]

def extraire(champs, dico):
    blob = norm(" | ".join([c for c in champs if c and c != "NC"]))
    out = []
    for item in dico:
        if len(item) == 3 and isinstance(item[2], str) and item[0] in ("SYSTEMES","RESEAUX","SOC","IR_FORENSICS","CTI","OFFENSIVE","VULN","CLOUD","APPSEC","DEVSECOPS","IAM","GRC","OT","SCRIPTING","IA","TRANSVERSE"):
            fam, nom, pat = item
            if re.search(pat, blob): out.append((fam, nom))
        else:
            nom, pat = item
            if re.search(pat, blob): out.append(("CERTIFICATION", nom))
    return out

# ---------------------------------------------------- NIVEAU DE TECHNICITÉ
def technicite(niv_metier, comps):
    noms = {n for _, n in comps}
    score = niv_metier
    n3 = {"Detection engineering / règles","SOAR / playbooks","DevSecOps","CI/CD","Kubernetes",
          "Infrastructure as Code / Terraform","SAST / DAST / SCA","Threat hunting","Automatisation",
          "CSPM / CNAPP / Prisma / Wiz","Python","PowerShell"}
    n4 = {"Malware analysis / reverse","Red Team","AI Security / sécurisation des systèmes IA","Architecture",
          "PKI / cryptographie","OT / ICS / SCADA"}
    if noms & n4: score = max(score, 4)
    elif len(noms & n3) >= 2: score = max(score, 3)
    return max(1, min(4, score))

TECH_LIB = {0:"HORS PERIMETRE",1:"NIVEAU_1 — Fondamentaux / support / gouvernance simple",
 2:"NIVEAU_2 — Expertise cyber opérationnelle",3:"NIVEAU_3 — Engineering / automation / cloud / AppSec",
 4:"NIVEAU_4 — Architecture / expertise avancée / recherche"}
