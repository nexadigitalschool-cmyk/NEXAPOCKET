# -*- coding: utf-8 -*-
import json, os, sys
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import normalize as N, referentiel as R

D = json.load(open("/home/user/NEXAPOCKET/collecte_cyber/consolide.json", encoding="utf-8"))
OFFRES = D["offres"]; PER = [o for o in OFFRES if o["STATUT_DOUBLON"]=="OFFRE_UNIQUE" and o["DANS_PERIMETRE"]]
SANS = D["sans_donnees"]
OUT = "/home/user/NEXAPOCKET/NEXA_Perimetre_Metiers_Cybersecurite_et_Plateformes_Sans_Donnees.md"

META = {
"Analyste SOC": dict(fr="Analyste SOC ; Analyste Sécurité SOC ; Analyste cyberdéfense ; Analyste SOC N1/N2/N3 ; Ingénieur CyberSOC ; Analyste SOC/CSIRT ; Analyste SOC/VOC ; Analyste sécurité N3/L3",
 en="SOC Analyst ; Security Operations Analyst ; Cyber Defense Analyst ; Blue Team Analyst ; Security Monitoring Analyst ; Managed Security Analyst ; EDR/XDR Analyst",
 comp="Analyse d'incidents ; qualification d'alertes ; corrélation ; MITRE ATT&CK ; analyse de logs ; systèmes Windows/Linux ; réseaux ; threat hunting (N2/N3) ; forensic de premier niveau",
 out="SIEM (Splunk, Microsoft Sentinel, IBM QRadar, Elastic/ELK) ; EDR/XDR (CrowdStrike, SentinelOne, Microsoft Defender, Cortex XDR) ; IDS/IPS ; SOAR ; TheHive ; Qualys ; sandbox",
 cert="CompTIA Security+ ; CompTIA CySA+ ; Microsoft SC-200 ; certifications Splunk ; GIAC (GCIA/GCIH)",
 prox="Cœur du métier cybersécurité défensif", incl="INCLUS",
 just="Métier central du périmètre, présent dans toutes les sources et chez tous les types d'employeurs (MSSP, ESN, banques, secteur public, industrie). Sous-niveaux SOC_LEVEL_1/2/3 distingués lorsque l'intitulé le précise ; en pratique nos offres CDI sont quasi exclusivement N2/N3."),
"Detection Engineer / SOC Engineering": dict(fr="Ingénieur détection ; Ingénieur cas d'usage SIEM ; Intégrateur SOC ; Ingénieur de parsing/normalisation de logs",
 en="Detection Engineer ; SIEM Engineer ; SOAR Engineer ; Security Automation Engineer (finalité cyber) ; Log Integrator ; Parsing Engineer",
 comp="Detection engineering ; écriture et optimisation de règles de corrélation ; Sigma ; YARA ; MITRE ATT&CK ; playbooks SOAR ; parsing/normalisation/enrichissement ; scripting Python",
 out="Microsoft Sentinel ; Splunk ; QRadar ; Elastic ; Cortex XSOAR ; Splunk SOAR ; Tines ; API/webhooks",
 cert="Microsoft SC-200 ; certifications Splunk ; GIAC (GCDA)",
 prox="Cœur du métier — segment à plus forte valeur du SOC", incl="INCLUS",
 just="Distingué de l'analyste SOC car les compétences (conception de détection, automatisation, scripting) et l'exposition à l'automatisation diffèrent radicalement. C'est le segment du SOC dont la valeur augmente avec l'IA."),
"SecOps / Security Operations Engineer": dict(fr="Ingénieur sécurité opérationnelle ; Ingénieur MCS (maintien en condition de sécurité) ; Expert SecOps",
 en="SecOps Engineer ; Security Operations Engineer ; Security Platform Engineer ; Security Tools Engineer",
 comp="Exploitation et industrialisation des solutions de sécurité ; durcissement (hardening) ; automatisation ; scripting ; intégration d'outils",
 out="EDR/XDR ; firewalls ; SIEM ; SOAR ; PAM ; NAC ; SASE/SSE ; Python/PowerShell",
 cert="Certifications éditeurs (Microsoft, Palo Alto, Fortinet, CrowdStrike)",
 prox="Cœur du métier", incl="INCLUS",
 just="Famille distincte du SOC analytique : il s'agit de faire fonctionner et d'industrialiser la plateforme de sécurité, pas d'analyser les alertes."),
"Analyste DFIR / Incident Response": dict(fr="Analyste réponse à incident ; Analyste CERT ; Analyste CSIRT ; Analyste forensic ; Investigateur numérique ; Analyste de malware ; Rétro-ingénieur sécurité",
 en="Incident Response Analyst ; Incident Responder ; DFIR Analyst ; Digital Forensics Analyst ; Forensic Investigator ; Malware Analyst ; Reverse Engineer",
 comp="Investigation avancée ; forensic disque et mémoire ; analyse de malware ; gestion de crise ; chaîne de preuve ; APT/exfiltration",
 out="Volatility ; Wireshark ; sandbox ; outils forensic ; PCAP ; EDR", cert="GIAC (GCFA/GCFE/GREM) ; certifications éditeurs",
 prox="Cœur du métier", incl="INCLUS",
 just="Volume faible mais expertise stratégique. Aucune offre junior observée : à ne pas présenter comme un débouché de sortie d'école."),
"Analyste Threat Intelligence / Threat Hunter": dict(fr="Analyste renseignement sur la menace ; Analyste CTI ; Analyste de la menace ; Analyste cybercriminalité et darkweb ; Chasseur de menaces",
 en="Cyber Threat Intelligence Analyst ; CTI Analyst ; Threat Hunter ; Threat Hunting Analyst ; Threat Researcher",
 comp="OSINT ; analyse de campagnes ; TTP ; IOC ; attribution ; veille ; threat hunting ; rédaction de notes de renseignement",
 out="MISP ; OpenCTI ; STIX/TAXII ; plateformes CTI ; SIEM ; darkweb monitoring", cert="GIAC (GCTI) ; certifications éditeurs",
 prox="Cœur du métier", incl="INCLUS",
 just="Famille séparée du SOC (les extraits distinguent nettement CTI et détection). Portes juniors rares : apprentissage ANSSI, stage Sopra Steria."),
"Pentester / Consultant sécurité offensive": dict(fr="Testeur d'intrusion ; Consultant pentest ; Consultant sécurité offensive ; Hacker éthique ; Ingénieur sécurité pentester ; Auditeur technique",
 en="Pentester ; Penetration Tester ; Ethical Hacker ; Offensive Security Consultant ; Red Team Operator ; Security Researcher ; Vulnerability Researcher ; Web/Mobile/Infrastructure/AD Pentester",
 comp="Pentest web, API, infrastructure, Active Directory, mobile ; élévation de privilèges ; mouvement latéral ; exploitation ; recherche de vulnérabilités ; rédaction de rapports",
 out="Kali Linux ; Burp Suite ; Metasploit ; Nmap ; Nessus ; BloodHound ; Impacket ; Mimikatz ; Wireshark ; OWASP Top 10",
 cert="OSCP ; OSWE ; CompTIA PenTest+ ; CEH ; GIAC (GPEN/GXPN)",
 prox="Cœur du métier", incl="INCLUS (sous-catégories PENTEST_WEB / PENTEST_INFRA / PENTEST_AD / RED_TEAM / SECURITY_RESEARCH distinguées lorsque l'intitulé le permet)",
 just="Inclus mais mesuré avec une attention particulière : c'est le métier dont l'écart entre attractivité étudiante et volume réel de recrutement est le plus grand (≈ 33 offres nationales « pentester » au 28/08/2026 contre ≥ 800 DevSecOps)."),
"Analyste / Manager Vulnérabilités (VOC)": dict(fr="Analyste vulnérabilités ; Analyste VOC (Vulnerability Operation Center) ; Responsable VOC ; Analyste gestion des vulnérabilités",
 en="Vulnerability Analyst ; Vulnerability Management Analyst/Engineer ; Vulnerability Manager ; Exposure Management Specialist ; Attack Surface Management Analyst",
 comp="Scan et priorisation ; CVE/CVSS ; remédiation ; relation avec les équipes IT ; reporting ; conformité",
 out="Tenable/Nessus ; Qualys ; Rapid7 InsightVM ; outils de scan de conteneurs", cert="CompTIA Security+ ; certifications éditeurs (Tenable, Qualys)",
 prox="Cœur du métier", incl="INCLUS",
 just="Famille distincte, en structuration en France (émergence des « VOC » à côté des SOC chez Crédit Mutuel, Sopra Steria, Urssaf). Bonne porte d'entrée junior (stages et alternances observés)."),
"Cloud Security Engineer / Architect": dict(fr="Ingénieur sécurité cloud ; Architecte sécurité cloud ; Consultant sécurité cloud ; Expert sécurité cloud",
 en="Cloud Security Engineer/Analyst/Architect/Consultant ; AWS/Azure/GCP Security Engineer ; CNAPP Engineer ; CSPM Specialist ; Cloud Security Operations Engineer",
 comp="Sécurité AWS/Azure/GCP ; IAM cloud ; Zero Trust ; posture management ; sécurité des conteneurs et de Kubernetes ; IaC ; chiffrement ; architecture cloud sécurisée",
 out="Microsoft Defender for Cloud ; AWS Security Hub ; GuardDuty ; Prisma Cloud ; Wiz ; Orca ; Terraform ; Azure Policy ; Entra ID",
 cert="AZ-500 ; SC-100 ; AWS Certified Security Specialty ; Google Cloud Security Engineer ; CCSP",
 prox="Cœur du métier", incl="INCLUS",
 just="L'un des trois plus gros stocks observés. Compétence à la fois autonome (postes dédiés) et transverse (présente dans les offres d'architecture, DevSecOps, IAM et généralistes)."),
"DevSecOps Engineer": dict(fr="Ingénieur DevSecOps ; Consultant DevSecOps ; Consultant cyber DevSecOps ; Architecte DevSecOps",
 en="DevSecOps Engineer/Consultant ; Platform Security Engineer ; CI/CD Security Engineer ; Container Security Engineer ; Kubernetes Security Engineer",
 comp="Intégration de la sécurité au cycle de développement ; pipelines sécurisés ; SBOM ; suivi CVE ; sécurité des conteneurs et de Kubernetes ; IaC ; scripting ; culture développement",
 out="GitLab CI ; GitHub Actions ; Jenkins ; Docker ; Kubernetes ; Terraform ; Ansible ; Snyk ; SonarQube ; Trivy ; Semgrep ; secrets management",
 cert="AWS Certified Security ; AZ-500 ; certifications Kubernetes (CKS)",
 prox="Cœur du métier, à la frontière avec le développement et l'infrastructure", incl="INCLUS",
 just="Distingué d'AppSec : le DevSecOps outille et sécurise la chaîne de livraison, l'AppSec sécurise le produit et le code. Stock le plus élevé de toutes les spécialités cyber observées (≥ 817 au 04/09/2026)."),
"AppSec / Product Security Engineer": dict(fr="Ingénieur sécurité applicative ; Consultant sécurité des applications ; Responsable sécurité produit ; Manager sécurité applicative",
 en="Application Security Engineer ; AppSec Engineer ; Product Security Engineer/Analyst ; Secure Software Engineer ; Software Security Engineer ; API Security Engineer ; Security Champion Lead",
 comp="Secure coding ; OWASP Top 10 ; threat modeling ; revue de code ; SSDLC ; sécurité des API ; accompagnement des équipes produit",
 out="SAST/DAST/SCA (Snyk, SonarQube, Checkmarx, Veracode, Semgrep) ; secret scanning ; GitHub Advanced Security ; Burp Suite",
 cert="CSSLP ; OSWE ; certifications éditeurs", prox="Cœur du métier, à la frontière avec le développement", incl="INCLUS",
 just="Distingué de DevSecOps et de Product Security lorsque l'intitulé le permet. Exige une compréhension réelle du code : point de convergence avec la filière Développement Web."),
"Consultant / Ingénieur IAM - PAM": dict(fr="Consultant IAM ; Ingénieur IAM ; Architecte système IAM ; Consultant PAM ; Consultant IGA ; Chef de projet cybersécurité IAM ; Responsable d'offre IAM",
 en="IAM Analyst/Consultant/Engineer/Architect ; Identity Security Engineer ; Identity Governance Specialist ; PAM Consultant/Engineer ; Access Management Specialist ; CyberArk/SailPoint/Okta Consultant ; Entra ID Security Specialist",
 comp="Gestion des identités et des accès ; gouvernance des identités (IGA) ; revues d'habilitations ; SSO ; MFA ; RBAC/ABAC ; Zero Trust Identity ; PKI et cycle de vie des certificats",
 out="Entra ID / Azure AD ; Active Directory ; CyberArk ; SailPoint ; Okta ; Ping Identity ; ForgeRock ; One Identity ; Evidian ; Wallix ; Delinea ; RACF",
 cert="Microsoft SC-300 ; certifications éditeurs (SailPoint, CyberArk, Okta)", prox="Cœur du métier", incl="INCLUS",
 just="Famille à part entière, sous-estimée par les étudiants et fortement demandée (≥ 732 offres « IAM » au 31/03/2026). Seuils d'entrée parmi les plus bas des spécialités techniques (Deloitte : 2 ans ; Aix : 1 an ; une alternance IAM observée)."),
"Consultant GRC / Risque / Conformité": dict(fr="Consultant GRC ; Consultant cybersécurité et gouvernance ; Analyste risques cyber ; Risk Manager cyber ; Chargé de conformité cyber ; Consultant NIS2 ; Consultant DORA ; Consultant EBIOS RM ; Consultant SMSI ; Analyste GRC",
 en="GRC Analyst/Consultant ; Cyber Risk Analyst/Consultant ; IT Risk Analyst/Consultant ; Security Compliance Analyst ; Cyber Compliance Officer ; Third Party Risk Analyst/Manager ; Cyber Governance Consultant",
 comp="Gouvernance et PSSI ; analyse de risques (EBIOS RM, ISO 27005) ; conformité (ISO 27001, NIS2, DORA, RGPD, HDS, SOC 2, LPM) ; audit ; risque fournisseurs ; continuité (PCA/PRA) ; gestion de crise ; sensibilisation",
 out="Outils GRC ; référentiels ISO ; méthode EBIOS RM ; tableaux de bord de conformité",
 cert="ISO 27001 Lead Implementer / Lead Auditor ; EBIOS Risk Manager ; CISM ; CISA ; CISSP (senior)",
 prox="Cœur du métier — dimension organisationnelle", incl="INCLUS (GRC, audit et conformité distingués : voir la ligne AUDIT_COMPLIANCE)",
 just="Famille la plus ouverte aux profils en formation dans notre corpus (11 alternances GRC sur 62). Attention : GRC n'est pas assimilable à de la cybersécurité opérationnelle — la distinction est maintenue dans la taxonomie."),
"Auditeur cybersécurité / SSI": dict(fr="Auditeur cybersécurité ; Auditeur SSI ; Auditeur IT ; Auditeur sécurité des SI",
 en="Cybersecurity Auditor ; IT Security Auditor ; Information Security Consultant",
 comp="Conduite d'audit ; référentiels ; collecte et qualification de preuves ; restitution ; plans de remédiation",
 out="Référentiels ISO 27001/27002 ; grilles d'audit ; outils de scan", cert="ISO 27001 Lead Auditor ; CISA",
 prox="Cœur du métier — proche du GRC mais posture et livrables distincts", incl="INCLUS",
 just="Non fusionné avec le GRC : l'audit est une posture de contrôle indépendante, avec des exigences propres (indépendance, méthode, preuve)."),
"Architecte sécurité / cybersécurité": dict(fr="Architecte sécurité ; Architecte cybersécurité ; Architecte sécurité des SI ; Architecte sécurité cloud ; Architecte système IAM ; Architecte Zero Trust",
 en="Security Architect ; Cybersecurity Architect ; Cloud Security Architect ; Zero Trust Architect ; Security Solutions Architect ; Security Infrastructure Engineer",
 comp="Architecture de sécurité ; security by design ; cyber-résilience ; analyse de risques ; sécurisation des flux critiques ; SSDLC ; revues d'architecture",
 out="Référentiels d'architecture ; Azure/AWS/GCP ; PAM/IAM ; segmentation ; PKI",
 cert="SC-100 ; CISSP ; SABSA ; TOGAF (adjacent)", prox="Cœur du métier — niveau expert", incl="INCLUS",
 just="Premier métier en volume selon l'Observatoire ANSSI (21 % des offres), confirmé par nos relevés (≈ 400 offres France sur deux sources). Mais métier de destination à 7-10 ans, jamais un débouché de sortie d'école : c'est le principal piège d'interprétation du marché cyber français."),
"Ingénieur sécurité réseau / infrastructure": dict(fr="Ingénieur sécurité réseau ; Ingénieur réseaux et sécurité ; Ingénieur sécurité des infrastructures ; Ingénieur systèmes, réseaux et sécurité ; Ingénieur sécurité SI",
 en="Network Security Engineer ; Infrastructure Security Engineer ; Firewall Engineer ; Endpoint Security Engineer ; Security Systems Engineer ; Secure Network Engineer",
 comp="TCP/IP ; DNS ; DHCP ; VPN ; segmentation ; durcissement ; SASE/SSE ; Zero Trust réseau ; NAC ; supervision",
 out="Palo Alto ; Fortinet/FortiGate ; Cisco ; Check Point ; Zscaler ; Netskope ; F5 ; WAF ; proxy ; IDS/IPS ; NDR",
 cert="CCNA ; CCNP Security ; certifications Fortinet et Palo Alto", prox="Cœur du métier — socle technique", incl="INCLUS (uniquement lorsque la composante sécurité est explicite)",
 just="Famille conservée car elle constitue, avec le généraliste, la porte d'entrée la plus large observée (14 alternances sur 62). Les postes d'administration réseau sans mission de sécurité sont exclus."),
"Ingénieur / Consultant sécurité OT-ICS": dict(fr="Ingénieur cybersécurité industrielle ; Consultant cybersécurité OT ; Analyste cybersécurité OT ; Ingénieur cybersécurité nucléaire ; Ingénieur sécurité des systèmes industriels",
 en="OT Security Engineer ; ICS Security Engineer ; Industrial Cybersecurity Engineer ; OT Security Consultant ; IoT Security Engineer ; Embedded Security Engineer (finalité cyber explicite)",
 comp="Protocoles industriels ; SCADA/DCS/PLC ; segmentation IT/OT ; IEC 62443 ; analyse de risques industriels ; LPM/NIS2 ; contrôle-commande",
 out="Outils de supervision OT ; sondes industrielles ; SIEM OT ; PCAP", cert="IEC 62443 ; GICSP",
 prox="Cœur du métier — spécialité sectorielle", incl="INCLUS",
 just="Marché national étroit (≈ 54 offres « OT Security » au 19/05/2026) mais très ancré dans les bassins industriels (Lyon, Grenoble, Toulouse, Belfort, Grand Est), donc pertinent à l'échelle d'un campus et non à l'échelle nationale."),
"RSSI / CISO / Responsable cybersécurité": dict(fr="RSSI ; RSSI adjoint ; Référent sécurité des SI ; Responsable cybersécurité ; Officier de sécurité ; Responsable Campus Cyber ; Manager cybersécurité",
 en="CISO ; Deputy CISO ; Head of Cybersecurity ; Security Manager ; SOC Manager ; Cybersecurity Program Manager ; Security Program Manager",
 comp="Gouvernance ; stratégie ; pilotage d'équipe ; budget ; conformité ; gestion de crise ; relation direction générale",
 out="Tableaux de bord ; référentiels ; outils GRC", cert="CISSP ; CISM ; ISO 27001 Lead Implementer",
 prox="Cœur du métier — management", incl="INCLUS pour l'analyse des trajectoires, EXCLU des débouchés juniors",
 just="Métier le plus représenté parmi les professionnels cyber (30 %, Observatoire ANSSI) mais exigeant 8 ans et plus. À utiliser dans la communication NEXA comme HORIZON de carrière, jamais comme débouché de sortie."),
"Chef de projet cybersécurité": dict(fr="Chef de projet cybersécurité ; Cheffe de projet cybersécurité ; Consultant AMOA cybersécurité ; Chef de projet sécurité et conformité",
 en="Cybersecurity Project Manager ; Security Program Manager", comp="Pilotage de projet ; coordination ; conformité ; budget ; relation métier",
 out="Outils de gestion de projet", cert="Certifications de gestion de projet (adjacentes)",
 prox="Cœur du métier — pilotage", incl="INCLUS", just="Conservé car récurrent dans les offres, mais suppose une légitimité technique préalable : pas un débouché de sortie d'école."),
"Ingénieur cybersécurité (généraliste)": dict(fr="Ingénieur cybersécurité ; Ingénieur cyber sécurité ; Ingénieur sécurité ; Ingénieur SSI ; Ingénieur d'études cybersécurité ; Ingénieur d'affaires cybersécurité",
 en="Cybersecurity Engineer ; Security Engineer ; Information Security Engineer ; IT Security Specialist",
 comp="Socle transverse : systèmes, réseaux, cloud, SOC, vulnérabilités, conformité — selon l'employeur",
 out="Variable selon le poste (SIEM, EDR, firewall, cloud, IAM)", cert="Variable ; CompTIA Security+ pour l'entrée",
 prox="Cœur du métier", incl="INCLUS",
 just="Intitulé « parapluie » : le plus gros stock brut (≥ 1 000 offres) mais recouvrant en réalité du SOC, du réseau, du cloud, de l'IAM, de l'OT et de la conformité. À utiliser comme mesure de la popularité de l'intitulé, jamais comme preuve de l'existence d'un métier généraliste homogène."),
"Consultant cybersécurité (généraliste)": dict(fr="Consultant cybersécurité ; Consultant SSI ; Expert cybersécurité ; Conseiller cybersécurité ; Consultant junior cybersécurité",
 en="Cybersecurity Consultant ; Cyber Security Consultant ; Security Specialist ; Information Security Consultant",
 comp="Conseil ; audit ; analyse de risques ; accompagnement client ; restitution ; polyvalence",
 out="Variable selon la mission", cert="ISO 27001 ; EBIOS RM ; certifications éditeurs selon la mission",
 prox="Cœur du métier", incl="INCLUS",
 just="Deuxième métier de l'Observatoire ANSSI (15 %). Voie d'entrée la plus fréquente pour un diplômé, via les ESN, MSSP et cabinets qui recrutent en volume et forment en interne."),
"Analyste cybersécurité (généraliste)": dict(fr="Analyste cybersécurité ; Analyste sécurité ; Analyste cyber ; Chargé de cybersécurité",
 en="Cybersecurity Analyst ; Security Analyst ; Cyber Analyst", comp="Analyse d'alertes ; suivi de vulnérabilités ; reporting ; sensibilisation ; support sécurité",
 out="SIEM ; EDR ; outils de scan ; Microsoft Defender", cert="CompTIA Security+ ; SC-200",
 prox="Cœur du métier", incl="INCLUS",
 just="Intitulé fréquent en alternance. C'est aussi le poste dont le contenu est le plus directement exposé à l'automatisation : classé EXPOSITION ÉLEVÉE."),
"Administrateur / technicien sécurité": dict(fr="Administrateur sécurité ; Administrateur cybersécurité ; Technicien sécurité informatique ; Technicien systèmes et réseaux orienté sécurité ; Assistant ingénieur cybersécurité",
 en="Security Administrator ; Security Technician ; IT Security Support",
 comp="Exploitation des solutions de sécurité ; administration ; support ; suivi des vulnérabilités ; Microsoft 365 ; Windows/Linux",
 out="Antivirus/EDR ; firewall ; Active Directory ; Microsoft 365 ; outils de sauvegarde", cert="CompTIA Security+ ; certifications éditeurs",
 prox="Périphérie opérationnelle du cœur de métier", incl="INCLUS lorsque la mission de sécurité est explicite",
 just="Niveau de technicité 1-2, accessible à Bac+2/+3. Porte d'entrée réelle mais fortement exposée à l'automatisation : à ne pas positionner comme cible d'un Bachelor Bac+3."),
"AI Security / LLM Security Engineer": dict(fr="Pentester IA ; Ingénieur développement cybersécurité IA ; Architecte sécurité cloud, DevSecOps & IA ; Ingénieur sécurité système (IA appliquée à l'analyse cyber)",
 en="AI Security Engineer/Specialist/Researcher ; AI Red Team Engineer ; AI Red Teamer ; LLM Security Engineer ; GenAI Security Engineer ; ML Security Engineer ; Adversarial ML Engineer ; AI Governance Specialist ; AI Risk Analyst ; AI Security Architect ; Agentic AI Security Engineer ; Prompt Injection Security Specialist",
 comp="Sécurisation des applications à base de LLM ; prompt injection ; jailbreak ; adversarial ML ; sécurité des agents IA et des pipelines RAG ; gouvernance de l'IA ; OWASP Top 10 for LLM Applications ; MITRE ATLAS",
 out="Garak ; PyRIT ; plateformes LLM ; vector databases ; MCP ; Security Copilot",
 cert="Aucune certification établie et reconnue par les recruteurs français à la date de la collecte",
 prox="Émergent — extension des métiers cyber existants", incl="INCLUS AVEC RÉSERVE MAJEURE",
 just="Aucun stock d'offres mesurable en France : nos 6 offres relevant de ce champ sont des postes cyber ou IA existants auxquels s'ajoute une dimension IA, et une seule alternance a été identifiée. Conclusion : compétence transverse à enseigner, PAS une spécialisation autonome finançable par le marché en 2026."),
"Métier adjacent (DevOps / Cloud / Data / IA sans mission sécurité explicite)": dict(
 fr="Administrateur systèmes ; Administrateur réseaux ; Ingénieur réseaux ; Ingénieur cloud ; Ingénieur DevOps ; SRE ; Développeur ; Architecte cloud ; Data engineer ; Data analyst ; DPO ; Responsable IT ; Auditeur IT généraliste ; Risk Manager non cyber ; Consultant RGPD ; Consultant IT ; Product Manager ; Chef de projet IT ; Technicien support ; Administrateur Microsoft 365",
 en="Systems/Network Administrator ; Cloud Engineer ; DevOps Engineer ; SRE ; Software Engineer ; Cloud Architect ; Data Engineer/Analyst ; IT Auditor ; IT Consultant ; Product/Project Manager ; Helpdesk Technician",
 comp="Compétences IT génériques sans responsabilité de sécurité explicite", out="Variable", cert="Variable",
 prox="Adjacent — vivier et voisinage", incl="IDENTIFIÉ MAIS NON INTÉGRÉ AUX VOLUMES CYBER",
 just="Conservés séparément pour mesurer la porosité entre cyber, DevOps, cloud et data, et pour documenter la trajectoire réelle de nombreux profils (première expérience IT puis bascule cyber). Jamais additionnés aux volumes cyber."),
"Hors périmètre (faux positif)": dict(
 fr="Talent acquisition cybersécurité ; commercial/marketing cybersécurité ; auditeur financier ; auditeur interne non IT ; agent de sécurité physique ; ingénieur sécurité incendie ; professeur de cybersécurité ; chargé de recrutement ; analyste de politiques publiques",
 en="Talent Acquisition Specialist ; Sales/Marketing (cybersecurity vendor) ; Financial Auditor ; Physical Security Officer ; Fire Safety Engineer",
 comp="Sans objet", out="Sans objet", cert="Sans objet", prox="Aucune — homonymie ou secteur d'activité", incl="EXCLU",
 just="Filtre explicite appliqué à la classification (liste EXCLUSIONS dans scripts_cyber/normalize.py). 3 offres du corpus ont été écartées à ce titre, notamment un stage « Talent Acquisition Specialist Cybersécurité » (poste RH dans une société cyber) et un poste commercial/marketing."),
}

REQ = defaultdict(set)
for o in OFFRES:
    for q in (o.get("REQUETE") or "").split(" | "):
        if q: REQ[o["METIER_NORMALISE"]].add(q)

lines = []
A = lines.append
A("# NEXA Digital School — Périmètre des métiers de la cybersécurité et journal des plateformes sans données")
A("")
A("**Étude :** Observatoire du marché de l'emploi de la cybersécurité en France — décision sur l'avenir de la filière Cybersécurité de NEXA (Bachelor → Mastère).  ")
A("**Date de collecte :** 8 septembre 2026.  ")
A(f"**Échantillon :** {len(OFFRES)} lignes d'offres collectées, {len([o for o in OFFRES if o['STATUT_DOUBLON']=='OFFRE_UNIQUE'])} offres uniques après dédoublonnage, dont {len(PER)} dans le périmètre cybersécurité ; "
  f"{len(D['volumes'])} relevés de stocks d'offres datés (2025-2026) ; {len(D['etudes'])} sources documentaires ; {len(SANS)} plateformes ou voies d'accès sans données exploitables.  ")
A("**Fichier compagnon :** `NEXA_Marche_Emploi_Cybersecurite_France_2026.xlsx` (onglet OFFRES_DETAILLEES pour le détail ligne à ligne).")
A("")
A("> Ce fichier constitue le **journal séparé de la collecte**. Il n'est pas destiné à être lu par la Direction Générale : "
  "la synthèse décisionnelle se trouve dans `NEXA_Synthese_Marche_Emploi_Cybersecurite_2026.docx`.")
A("")
A("---")
A("")
A("## Sommaire")
A("")
A("- [Partie A — Taxonomie des métiers](#partie-a--taxonomie-des-métiers)")
A("- [Partie B — Plateformes sans données exploitables](#partie-b--plateformes-sans-données-exploitables)")
A("")
A("---")
A("")
A("## Partie A — Taxonomie des métiers")
A("")
A("La taxonomie a été construite **avant** la collecte à partir du périmètre demandé (cœur généraliste, SOC/Blue Team/SecOps, "
  "Incident Response/Forensics, Threat Intelligence, Offensive Security, Vulnerability Management, Cloud Security, "
  "AppSec/Product Security, DevSecOps, IAM/PAM, GRC/Risques, Audit/Conformité, Architecture/Engineering, "
  "Sécurité réseau/infrastructure, OT/IoT, Management, AI Security émergent, métiers adjacents), puis **complétée pendant la collecte** "
  "avec les intitulés réellement rencontrés (notamment : Analyste VOC / Vulnerability Operation Center, SOC Log Integrator & Parsing Engineer, "
  "Officier de sécurité en cybersécurité, Responsable Campus Cyber régional, Pentester IA / Offensive Cybersecurity Engineer, "
  "Analyste cybersécurité nucléaire, Consultant AMOA cybersécurité, Expert conformité DORA).")
A("")
A("Les règles de classification sont implémentées dans `scripts_cyber/normalize.py` (fonction `classifier`) : "
  "elles s'appliquent d'abord à l'intitulé, puis au contexte (description, compétences, outils, normes) si l'intitulé est ambigu, "
  "avec un filtre de faux positifs appliqué en premier.")
A("")
A("### Familles retenues")
A("")
A("| Code famille | Libellé | Offres uniques (périmètre) |")
A("|---|---|---|")
famc = Counter(o["FAMILLE_METIER"] for o in PER)
for code, lib in N.FAMILLE_LIB.items():
    n = famc.get(code, 0)
    if code == "EXCLU_DU_PERIMETRE":
        n = len([o for o in OFFRES if o["FAMILLE_METIER"] == code])
        A(f"| `{code}` | {lib} | {n} (écartées) |")
    else:
        A(f"| `{code}` | {lib} | {n} |")
A("")
A("### Fiches métiers")
A("")
ordre = [m for m, _ in Counter(o["METIER_NORMALISE"] for o in PER).most_common()]
for m in META:
    if m not in ordre: ordre.append(m)
for m in ordre:
    meta = META.get(m)
    if not meta: continue
    ref = R.ref(m)
    lst = [o for o in PER if o["METIER_NORMALISE"] == m]
    fam = lst[0]["FAMILLE_METIER"] if lst else ("EXCLU_DU_PERIMETRE" if m.startswith("Hors") else "METIER_ADJACENT")
    niv = Counter(o["NIVEAU_TECHNICITE"] for o in lst).most_common(1)[0][0] if lst else 0
    A(f"#### {m}")
    A("")
    A(f"- **INTITULE_NORMALISE :** {m}")
    A(f"- **VARIANTES_FRANCAISES :** {meta['fr']}")
    A(f"- **VARIANTES_ANGLAISES :** {meta['en']}")
    A(f"- **COMPETENCES_ASSOCIEES :** {meta['comp']}")
    A(f"- **OUTILS_ASSOCIES :** {meta['out']}")
    A(f"- **CERTIFICATIONS_ASSOCIEES :** {meta['cert']}")
    A(f"- **FAMILLE :** `{fam}` — {N.FAMILLE_LIB.get(fam, fam)}")
    A(f"- **NIVEAU_TECHNICITE :** {N.TECH_LIB.get(niv, 'NC')}")
    A(f"- **ACCESSIBILITE_JUNIOR_PRESUMEE :** {ref['ACCESSIBILITE']} — {ref['ACCESSIBILITE_JUST']}")
    A(f"- **PROXIMITE_AVEC_CYBERSECURITE :** {meta['prox']}")
    A(f"- **INCLUS_OU_EXCLU :** {meta['incl']}")
    A(f"- **JUSTIFICATION :** {meta['just']}")
    A(f"- **OFFRES_UNIQUES_COLLECTEES :** {len(lst)}")
    A(f"- **STOCK_OBSERVE :** national — {ref['STOCK_NATIONAL']} ; Paris/IdF — {ref['STOCK_PARIS']}")
    qs = sorted(REQ.get(m, []))
    A(f"- **REQUETES_UTILISEES ({len(qs)}) :**")
    for q in qs[:14]:
        A(f"  - `{q}`")
    if len(qs) > 14: A(f"  - … et {len(qs)-14} autre(s) requête(s), tracées dans la colonne `REQUETE` de l'onglet OFFRES_DETAILLEES.")
    if not qs: A("  - *(métier issu de la taxonomie initiale, non rencontré dans la collecte)*")
    A("")
A("### Métiers émergents liés à l'IA — état de la mesure")
A("")
A("Les intitulés suivants ont été recherchés explicitement : AI Security Engineer, AI Security Specialist, AI Security Researcher, "
  "AI Red Team Engineer, AI Red Teamer, LLM Security Engineer, GenAI Security Engineer, ML Security Engineer, "
  "Machine Learning Security Engineer, AI Governance Specialist, AI Risk Analyst, AI Security Architect, AI Threat Researcher, "
  "Adversarial ML Engineer, AI Application Security Engineer, AI Safety & Security Engineer, Prompt Injection Security Specialist, "
  "Agentic AI Security Engineer.")
A("")
A("**Résultat :** aucun de ces intitulés ne produit de stock d'offres mesurable sur les plateformes françaises. "
  "Les seules offres françaises rattachables à ce champ sont :")
A("")
for o in PER:
    if o["FAMILLE_METIER"] == "AI_SECURITY_EMERGENT":
        A(f"- **{o['INTITULE_BRUT']}** — {o.get('ENTREPRISE','NC')}, {o.get('VILLE','NC')} ({o['SOURCE']}) : {o.get('DESCRIPTION_SYNTHETIQUE','NC')}")
A("")
A("À quoi s'ajoutent les offres de cybersécurité classique dans lesquelles une compétence de sécurisation ou d'usage de l'IA "
  "apparaît **sans modifier l'intitulé du poste** :")
A("")
for o in PER:
    ia = set((o.get("COMPETENCES_DETECTEES") or "").split(" ; ")) & {"IA générative / LLM","AI Security / sécurisation des systèmes IA","Agents IA / RAG"}
    if ia and o["FAMILLE_METIER"] != "AI_SECURITY_EMERGENT":
        A(f"- **{o['INTITULE_BRUT']}** ({o.get('VILLE','NC')}, {o['SOURCE']}) — mentions : {' ; '.join(sorted(ia))}")
A("")
A(f"**Conclusion de mesure :** {sum(1 for o in PER if set((o.get('COMPETENCES_DETECTEES') or '').split(' ; ')) & {'IA générative / LLM','AI Security / sécurisation des systèmes IA','Agents IA / RAG'})} offres sur {len(PER)} "
  f"({100*sum(1 for o in PER if set((o.get('COMPETENCES_DETECTEES') or '').split(' ; ')) & {'IA générative / LLM','AI Security / sécurisation des systèmes IA','Agents IA / RAG'})/len(PER):.1f} %) portent une mention IA. "
  "L'AI Security se présente en France en 2026 comme une **extension de métiers existants**, pas comme un métier autonome.")
A("")
A("### Métiers adjacents identifiés mais non intégrés aux volumes")
A("")
adj = [o for o in OFFRES if o["FAMILLE_METIER"] == "METIER_ADJACENT"]
A(f"{len(adj)} offres ont été classées « métier adjacent » : elles portent sur du DevOps, du cloud, de l'infrastructure ou de l'IA "
  "sans responsabilité de sécurité explicitement énoncée dans l'extrait. Elles sont conservées dans le fichier détaillé "
  "(colonne `DANS_PERIMETRE` = False) et **jamais additionnées aux volumes cyber**.")
A("")
for o in adj:
    A(f"- {o['INTITULE_BRUT']} — {o.get('VILLE','NC')} ({o['SOURCE']})")
A("")
A("### Faux positifs écartés")
A("")
exc = [o for o in OFFRES if o["FAMILLE_METIER"] == "EXCLU_DU_PERIMETRE"]
A(f"{len(exc)} offres ont été écartées par le filtre de faux positifs :")
A("")
for o in exc:
    A(f"- {o['INTITULE_BRUT']} — {o.get('VILLE','NC')} ({o['SOURCE']}) — motif : intitulé RH, commercial ou sans composante technique cyber.")
A("")
A("Les catégories de faux positifs exclues par construction sont : administrateur systèmes ou réseaux sans mission de sécurité, "
  "développeur sans responsabilité sécurité, DevOps sans DevSecOps, support IT et helpdesk, data analyst sans sécurité, "
  "DPO purement juridique, consultant RGPD sans dimension sécurité, auditeur financier, risk manager sans risque IT ou cyber, "
  "ingénieur sécurité incendie, agent de sécurité physique et sûreté, product manager sans responsabilité sécurité, "
  "consultant IT généraliste, ainsi que les fonctions RH, marketing et commerciales exercées au sein d'entreprises de cybersécurité.")
A("")
A("---")
A("")
A("## Partie B — Plateformes sans données exploitables")
A("")
A("Cette partie recense **toutes les plateformes et voies d'accès testées pour lesquelles aucune donnée exploitable n'a pu être obtenue**, "
  "ainsi que la source de remplacement utilisée. Elle explique pourquoi l'objectif indicatif de 500 à 1 000 offres uniques n'a pas été atteint.")
A("")
for s in SANS:
    A(f"### {s['PLATEFORME']}")
    A("")
    A(f"- **URL :** {s['URL']}")
    A(f"- **DATE_DU_TEST :** {s['DATE_DU_TEST']}")
    A(f"- **METIERS_TESTES :** {s['METIERS_TESTES']}")
    A(f"- **ZONES_TESTEES :** {s['ZONES_TESTEES']}")
    A(f"- **DONNEES_RECHERCHEES :** {s['DONNEES_RECHERCHEES']}")
    A(f"- **RESULTAT :** {s['RESULTAT']}")
    A(f"- **DONNEES_MANQUANTES :** {s['DONNEES_MANQUANTES']}")
    A(f"- **AUTRES_CHEMINS_TESTES :** {s['AUTRES_CHEMINS_TESTES']}")
    A(f"- **SOURCE_DE_REMPLACEMENT :** {s['SOURCE_DE_REMPLACEMENT']}")
    A(f"- **IMPACT_SUR_L_ANALYSE :** {s['IMPACT_SUR_L_ANALYSE']}")
    A("")
A("### Plateformes ayant effectivement fourni des données")
A("")
A("| Plateforme | Offres individuelles retenues | Relevés de stocks datés |")
A("|---|---|---:|")
volc = Counter(v.get("SOURCE","NC") for v in D["volumes"])
srcc = Counter(o["SOURCE"] for o in OFFRES)
for s in sorted(set(list(srcc) + list(volc))):
    A(f"| {s} | {srcc.get(s,0)} | {volc.get(s,0)} |")
A("")
A("### Conséquence méthodologique")
A("")
A("L'accès direct aux pages (WebFetch et requêtes HTTP) étant bloqué par le proxy de la session, **toutes les données proviennent "
  "des titres, URL et extraits renvoyés par un moteur de recherche sur des pages publiques indexées**. Il en découle trois limites "
  "que le document de synthèse rappelle explicitement :")
A("")
A("1. **Champs incomplets.** Le salaire n'est renseigné que dans 3 offres sur 342, l'expérience dans une minorité d'offres, "
   "les certifications dans 4 offres. Ces taux sont des **bornes basses** liées à la troncature des extraits, et non des mesures du marché.")
A("2. **Volumes = stocks indexés à des dates hétérogènes.** Les compteurs relevés (« plus de N emplois (date) ») sont des comptes de "
   "pertinence par mots-clés, sur des requêtes larges qui se recouvrent. Ils ne doivent jamais être additionnés ni lus comme un nombre "
   "d'emplois disponibles ; ils ne valent qu'en **comparaison relative** entre métiers et entre zones.")
A("3. **Pas de séries temporelles complètes.** Sauf exception (un point Sophia Antipolis de novembre 2025), nous ne disposons pas de "
   "relevés 2024 et 2025 comparables pour la même requête. **Aucune évolution annuelle n'est donc calculée à partir de nos propres relevés** : "
   "les colonnes EVOLUTION_2025 et EVOLUTION_2024 sont à « NC (séries insuffisantes) ». Les tendances pluriannuelles utilisées dans la "
   "synthèse proviennent exclusivement de sources publiées (Observatoire ANSSI : +49 % d'offres entre 2019 et 2024 ; Apec ; Numeum ; BMO).")
A("")
A(f"*Fichier généré le 8 septembre 2026 par `scripts_cyber/build_md.py`.*")

open(OUT, "w", encoding="utf-8").write("\n".join(lines))
print("Markdown écrit :", OUT, os.path.getsize(OUT), "octets,", len(lines), "lignes")
