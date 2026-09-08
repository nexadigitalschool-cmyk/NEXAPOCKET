# NEXA Digital School — Périmètre des métiers de la cybersécurité et journal des plateformes sans données

**Étude :** Observatoire du marché de l'emploi de la cybersécurité en France — décision sur l'avenir de la filière Cybersécurité de NEXA (Bachelor → Mastère).  
**Date de collecte :** 8 septembre 2026.  
**Échantillon :** 348 lignes d'offres collectées, 345 offres uniques après dédoublonnage, dont 342 dans le périmètre cybersécurité ; 223 relevés de stocks d'offres datés (2025-2026) ; 35 sources documentaires ; 12 plateformes ou voies d'accès sans données exploitables.  
**Fichier compagnon :** `NEXA_Marche_Emploi_Cybersecurite_France_2026.xlsx` (onglet OFFRES_DETAILLEES pour le détail ligne à ligne).

> Ce fichier constitue le **journal séparé de la collecte**. Il n'est pas destiné à être lu par la Direction Générale : la synthèse décisionnelle se trouve dans `NEXA_Synthese_Marche_Emploi_Cybersecurite_2026.docx`.

---

## Sommaire

- [Partie A — Taxonomie des métiers](#partie-a--taxonomie-des-métiers)
- [Partie B — Plateformes sans données exploitables](#partie-b--plateformes-sans-données-exploitables)

---

## Partie A — Taxonomie des métiers

La taxonomie a été construite **avant** la collecte à partir du périmètre demandé (cœur généraliste, SOC/Blue Team/SecOps, Incident Response/Forensics, Threat Intelligence, Offensive Security, Vulnerability Management, Cloud Security, AppSec/Product Security, DevSecOps, IAM/PAM, GRC/Risques, Audit/Conformité, Architecture/Engineering, Sécurité réseau/infrastructure, OT/IoT, Management, AI Security émergent, métiers adjacents), puis **complétée pendant la collecte** avec les intitulés réellement rencontrés (notamment : Analyste VOC / Vulnerability Operation Center, SOC Log Integrator & Parsing Engineer, Officier de sécurité en cybersécurité, Responsable Campus Cyber régional, Pentester IA / Offensive Cybersecurity Engineer, Analyste cybersécurité nucléaire, Consultant AMOA cybersécurité, Expert conformité DORA).

Les règles de classification sont implémentées dans `scripts_cyber/normalize.py` (fonction `classifier`) : elles s'appliquent d'abord à l'intitulé, puis au contexte (description, compétences, outils, normes) si l'intitulé est ambigu, avec un filtre de faux positifs appliqué en premier.

### Familles retenues

| Code famille | Libellé | Offres uniques (périmètre) |
|---|---|---|
| `COEUR_GENERALISTE` | Cœur généraliste | 87 |
| `SOC_BLUE_TEAM_SECOPS` | SOC / Blue Team / SecOps | 38 |
| `INCIDENT_RESPONSE_FORENSICS` | Incident Response / Forensics | 3 |
| `THREAT_INTELLIGENCE` | Threat Intelligence | 8 |
| `OFFENSIVE_SECURITY` | Offensive Security / Pentest | 12 |
| `VULNERABILITY_MANAGEMENT` | Vulnerability Management | 8 |
| `CLOUD_SECURITY` | Cloud Security | 10 |
| `APPSEC_PRODUCT_SECURITY` | AppSec / Product Security | 6 |
| `DEVSECOPS` | DevSecOps | 16 |
| `IAM_PAM` | IAM / PAM | 12 |
| `GRC_RISK` | GRC / Risques | 37 |
| `AUDIT_COMPLIANCE` | Audit / Conformité | 3 |
| `ARCHITECTURE_ENGINEERING` | Architecture / Security Engineering | 13 |
| `NETWORK_INFRA_SECURITY` | Sécurité réseau / infrastructure | 33 |
| `OT_IOT_SECURITY` | Sécurité OT / IoT | 14 |
| `MANAGEMENT_CYBER` | Management cyber | 25 |
| `AI_SECURITY_EMERGENT` | AI Security (émergent) | 6 |
| `METIER_ADJACENT` | Métier adjacent | 11 |
| `EXCLU_DU_PERIMETRE` | Exclu du périmètre | 3 (écartées) |

### Fiches métiers

#### Ingénieur cybersécurité (généraliste)

- **INTITULE_NORMALISE :** Ingénieur cybersécurité (généraliste)
- **VARIANTES_FRANCAISES :** Ingénieur cybersécurité ; Ingénieur cyber sécurité ; Ingénieur sécurité ; Ingénieur SSI ; Ingénieur d'études cybersécurité ; Ingénieur d'affaires cybersécurité
- **VARIANTES_ANGLAISES :** Cybersecurity Engineer ; Security Engineer ; Information Security Engineer ; IT Security Specialist
- **COMPETENCES_ASSOCIEES :** Socle transverse : systèmes, réseaux, cloud, SOC, vulnérabilités, conformité — selon l'employeur
- **OUTILS_ASSOCIES :** Variable selon le poste (SIEM, EDR, firewall, cloud, IAM)
- **CERTIFICATIONS_ASSOCIEES :** Variable ; CompTIA Security+ pour l'entrée
- **FAMILLE :** `COEUR_GENERALISTE` — Cœur généraliste
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — ≥ 300 « Cybersécurité Junior » (02/09/2026) et ≥ 100 « Débutant Cybersécurité » (01/09/2026) mais seulement ≥ 25 « Débutant Cybersécurité » en IdF (extrait : 26) au 04/09/2026 — soit environ 1 % du stock cyber francilien (≈ 2 444 offres). L'écart entre le stock global et le stock réellement ouvert aux débutants est le résultat le plus important de cette étude.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Intitulé « parapluie » : le plus gros stock brut (≥ 1 000 offres) mais recouvrant en réalité du SOC, du réseau, du cloud, de l'IAM, de l'OT et de la conformité. À utiliser comme mesure de la popularité de l'intitulé, jamais comme preuve de l'existence d'un métier généraliste homogène.
- **OFFRES_UNIQUES_COLLECTEES :** 53
- **STOCK_OBSERVE :** national — ≥ 1 000 « Ingénieur Cybersécurité » (07/09/2026) ; ≥ 1 000 « Ingénieur Cyber Sécurité » (20/08/2026) ; Paris/IdF — ≥ 600 (07/09/2026)
- **REQUETES_UTILISEES (28) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance cybersécurité SOC réseaux`
  - `site:candidat.francetravail.fr/offres/recherche/detail analyste SOC OR pentest OR IAM OR RSSI`
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité`
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité Lyon OR Lille OR Nantes OR Bordeaux OR Marseille`
  - `site:fr.indeed.com/viewjob "OT" OR "industrielle" OR "IoT" cybersécurité ingénieur consultant`
  - `site:fr.indeed.com/viewjob "ingénieur sécurité" OR "security engineer" CDI France`
  - `site:fr.indeed.com/viewjob DevSecOps ingénieur`
  - `site:fr.indeed.com/viewjob EDR OR XDR OR CrowdStrike OR "Defender" sécurité`
  - `site:fr.indeed.com/viewjob GRC OR "ISO 27001" OR "EBIOS" consultant sécurité`
  - `site:fr.indeed.com/viewjob alternance cybersécurité alternant`
  - `site:fr.indeed.com/viewjob cybersécurité Lille OR Villeneuve-d'Ascq OR Roubaix`
  - `site:fr.indeed.com/viewjob cybersécurité Lyon OR Villeurbanne ingénieur consultant`
  - `site:fr.indeed.com/viewjob cybersécurité Marseille OR Aix-en-Provence OR Toulon`
  - `site:fr.indeed.com/viewjob cybersécurité Nantes OR Saint-Herblain OR Rennes`
  - … et 14 autre(s) requête(s), tracées dans la colonne `REQUETE` de l'onglet OFFRES_DETAILLEES.

#### Consultant GRC / Risque / Conformité

- **INTITULE_NORMALISE :** Consultant GRC / Risque / Conformité
- **VARIANTES_FRANCAISES :** Consultant GRC ; Consultant cybersécurité et gouvernance ; Analyste risques cyber ; Risk Manager cyber ; Chargé de conformité cyber ; Consultant NIS2 ; Consultant DORA ; Consultant EBIOS RM ; Consultant SMSI ; Analyste GRC
- **VARIANTES_ANGLAISES :** GRC Analyst/Consultant ; Cyber Risk Analyst/Consultant ; IT Risk Analyst/Consultant ; Security Compliance Analyst ; Cyber Compliance Officer ; Third Party Risk Analyst/Manager ; Cyber Governance Consultant
- **COMPETENCES_ASSOCIEES :** Gouvernance et PSSI ; analyse de risques (EBIOS RM, ISO 27005) ; conformité (ISO 27001, NIS2, DORA, RGPD, HDS, SOC 2, LPM) ; audit ; risque fournisseurs ; continuité (PCA/PRA) ; gestion de crise ; sensibilisation
- **OUTILS_ASSOCIES :** Outils GRC ; référentiels ISO ; méthode EBIOS RM ; tableaux de bord de conformité
- **CERTIFICATIONS_ASSOCIEES :** ISO 27001 Lead Implementer / Lead Auditor ; EBIOS Risk Manager ; CISM ; CISA ; CISSP (senior)
- **FAMILLE :** `GRC_RISK` — GRC / Risques
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE — C'est la famille la plus ouverte aux profils en formation dans notre corpus : 12 alternances GRC identifiées (MGEN, Safran, Thales Bordeaux, Framatome/EDF Grenoble, Onet Marseille, PSTB, Icademie, Lyon...) et des seuils d'entrée CDI plus bas (Upcoop 3-5 ans, Toulouse 3-5 ans, CyberTee 4 ans). Attention : les postes « confirmés » restent majoritaires.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — dimension organisationnelle
- **INCLUS_OU_EXCLU :** INCLUS (GRC, audit et conformité distingués : voir la ligne AUDIT_COMPLIANCE)
- **JUSTIFICATION :** Famille la plus ouverte aux profils en formation dans notre corpus (11 alternances GRC sur 62). Attention : GRC n'est pas assimilable à de la cybersécurité opérationnelle — la distinction est maintenue dans la taxonomie.
- **OFFRES_UNIQUES_COLLECTEES :** 37
- **STOCK_OBSERVE :** national — ≥ 200 « Cybersécurité GRC » (extrait : 242) au 03/09/2026 ; ≥ 300 « ISO 27001 » à Paris (21/10/2025). Local : ≈ 14 à Lyon (03/01/2026) ; Paris/IdF — ≥ 100 (extrait : 112) au 03/09/2026 ; ≥ 75 IdF (extrait : 92) au 11/08/2026
- **REQUETES_UTILISEES (17) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance cybersécurité SOC réseaux`
  - `site:candidat.francetravail.fr/offres/recherche/detail consultant GRC OR audit OR conformité sécurité 2026`
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité Lyon OR Lille OR Nantes OR Bordeaux OR Marseille`
  - `site:fr.indeed.com/viewjob "consultant SSI" OR "expert SSI" OR "gouvernance sécurité" offre`
  - `site:fr.indeed.com/viewjob GRC OR "ISO 27001" OR "EBIOS" consultant sécurité`
  - `site:fr.indeed.com/viewjob alternance cybersécurité alternant`
  - `site:fr.indeed.com/viewjob cybersécurité Lille OR Villeneuve-d'Ascq OR Roubaix`
  - `site:fr.indeed.com/viewjob cybersécurité Rouen OR Caen OR Brest OR Angers OR Tours OR Orléans`
  - `site:fr.indeed.com/viewjob cybersécurité Toulouse OR Montpellier OR Nice OR Sophia Antipolis`
  - `site:fr.indeed.com/viewjob stage cybersécurité 2026 étudiant`
  - `site:www.free-work.com consultant cybersécurité offre emploi`
  - `site:www.free-work.com offre emploi cybersécurité GRC OR conformité OR NIS2 OR DORA consultant`
  - `site:www.hellowork.com/fr-fr/emplois alternance OR stage cybersécurité GRC cloud`
  - `site:www.hellowork.com/fr-fr/emplois cybersécurité`
  - … et 3 autre(s) requête(s), tracées dans la colonne `REQUETE` de l'onglet OFFRES_DETAILLEES.

#### Analyste SOC

- **INTITULE_NORMALISE :** Analyste SOC
- **VARIANTES_FRANCAISES :** Analyste SOC ; Analyste Sécurité SOC ; Analyste cyberdéfense ; Analyste SOC N1/N2/N3 ; Ingénieur CyberSOC ; Analyste SOC/CSIRT ; Analyste SOC/VOC ; Analyste sécurité N3/L3
- **VARIANTES_ANGLAISES :** SOC Analyst ; Security Operations Analyst ; Cyber Defense Analyst ; Blue Team Analyst ; Security Monitoring Analyst ; Managed Security Analyst ; EDR/XDR Analyst
- **COMPETENCES_ASSOCIEES :** Analyse d'incidents ; qualification d'alertes ; corrélation ; MITRE ATT&CK ; analyse de logs ; systèmes Windows/Linux ; réseaux ; threat hunting (N2/N3) ; forensic de premier niveau
- **OUTILS_ASSOCIES :** SIEM (Splunk, Microsoft Sentinel, IBM QRadar, Elastic/ELK) ; EDR/XDR (CrowdStrike, SentinelOne, Microsoft Defender, Cortex XDR) ; IDS/IPS ; SOAR ; TheHive ; Qualys ; sandbox
- **CERTIFICATIONS_ASSOCIEES :** CompTIA Security+ ; CompTIA CySA+ ; Microsoft SC-200 ; certifications Splunk ; GIAC (GCIA/GCIH)
- **FAMILLE :** `SOC_BLUE_TEAM_SECOPS` — SOC / Blue Team / SecOps
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — Dans notre corpus, la quasi-totalité des postes d'analyste SOC en CDI exigent N2/N3 ou 4-6 ans (Atos : Bac+5 + 4 ans ; Michael Page : Bac+3 + 5 ans ; Ivry : Bac+5 + 4 ans + certification SIEM/SOAR/EDR). Les entrées juniors passent par l'alternance et le stage (Advens Lille, IMS Networks Castres, CHANEL, apprenti analyste SOC junior Paris) ou par des postes N1 peu nombreux.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier cybersécurité défensif
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Métier central du périmètre, présent dans toutes les sources et chez tous les types d'employeurs (MSSP, ESN, banques, secteur public, industrie). Sous-niveaux SOC_LEVEL_1/2/3 distingués lorsque l'intitulé le précise ; en pratique nos offres CDI sont quasi exclusivement N2/N3.
- **OFFRES_UNIQUES_COLLECTEES :** 28
- **STOCK_OBSERVE :** national — ≥ 300 (28/05/2026, « Analyste Soc ») ; ≥ 400 « Cyber Security SOC Analyste » (14/08/2026) ; ≈ 329 « Analyste Cybersécurité » (20/03/2026) ; ≈ 231 « Analyste Cyber Security » (23/05/2026) ; Paris/IdF — ≥ 50 (Indeed, 29/06/2026, Paris 75) ; ≥ 50 SOC Analyst IdF (11/08/2026)
- **REQUETES_UTILISEES (10) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail analyste SOC OR pentest OR IAM OR RSSI`
  - `site:fr.indeed.com/viewjob "Microsoft Sentinel" OR Splunk OR QRadar analyste sécurité`
  - `site:fr.indeed.com/viewjob "threat intelligence" OR CERT OR CSIRT OR forensic analyste`
  - `site:fr.indeed.com/viewjob analyste SOC alternance OR junior N1 2026`
  - `site:fr.indeed.com/viewjob analyste SOC cybersécurité`
  - `site:fr.indeed.com/viewjob stage cybersécurité 2026 étudiant`
  - `site:www.hellowork.com/fr-fr/emplois "analyste SOC" OR "detection engineer" OR "threat intelligence" 2026`
  - `site:www.hellowork.com/fr-fr/emplois SOC analyste OR pentest OR IAM sécurité`
  - `site:www.hellowork.com/fr-fr/emplois analyste cybersécurité OR "consultant cybersécurité" Toulouse OR Rennes OR Grenoble OR Strasbourg`
  - `site:www.welcometothejungle.com/fr/companies SOC analyst OR pentester OR "threat intelligence" France CDI`

#### Ingénieur sécurité réseau / infrastructure

- **INTITULE_NORMALISE :** Ingénieur sécurité réseau / infrastructure
- **VARIANTES_FRANCAISES :** Ingénieur sécurité réseau ; Ingénieur réseaux et sécurité ; Ingénieur sécurité des infrastructures ; Ingénieur systèmes, réseaux et sécurité ; Ingénieur sécurité SI
- **VARIANTES_ANGLAISES :** Network Security Engineer ; Infrastructure Security Engineer ; Firewall Engineer ; Endpoint Security Engineer ; Security Systems Engineer ; Secure Network Engineer
- **COMPETENCES_ASSOCIEES :** TCP/IP ; DNS ; DHCP ; VPN ; segmentation ; durcissement ; SASE/SSE ; Zero Trust réseau ; NAC ; supervision
- **OUTILS_ASSOCIES :** Palo Alto ; Fortinet/FortiGate ; Cisco ; Check Point ; Zscaler ; Netskope ; F5 ; WAF ; proxy ; IDS/IPS ; NDR
- **CERTIFICATIONS_ASSOCIEES :** CCNA ; CCNP Security ; certifications Fortinet et Palo Alto
- **FAMILLE :** `NETWORK_INFRA_SECURITY` — Sécurité réseau / infrastructure
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE — C'est la porte d'entrée la plus large observée : alternances systèmes-réseaux-sécurité nombreuses (Sopra Steria Villeneuve-d'Ascq, Metz, Aubière Bac+3/4, Bordeaux, Sarcelles), postes de technicien/administrateur sécurité accessibles à Bac+2/+3.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — socle technique
- **INCLUS_OU_EXCLU :** INCLUS (uniquement lorsque la composante sécurité est explicite)
- **JUSTIFICATION :** Famille conservée car elle constitue, avec le généraliste, la porte d'entrée la plus large observée (14 alternances sur 62). Les postes d'administration réseau sans mission de sécurité sont exclus.
- **OFFRES_UNIQUES_COLLECTEES :** 28
- **STOCK_OBSERVE :** national — ≥ 1 000 « Ingénieur Réseau Sécurité » (extrait : 1 736) au 04/08/2026 — requête large ; ≥ 600 « Ingénieur Réseaux Cyber Sécurité » (25/07/2026) ; Paris/IdF — ≥ 600 IdF (extrait : 684) au 28/05/2026
- **REQUETES_UTILISEES (20) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance cybersécurité SOC réseaux`
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité`
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité Lyon OR Lille OR Nantes OR Bordeaux OR Marseille`
  - `site:candidat.francetravail.fr/offres/recherche/detail sécurité informatique ingénieur cloud DevSecOps`
  - `site:candidat.francetravail.fr/offres/recherche/detail technicien OR administrateur systèmes réseaux sécurité alternance 2026`
  - `site:fr.indeed.com/viewjob "ingénieur sécurité" OR "security engineer" CDI France`
  - `site:fr.indeed.com/viewjob "sécurité réseau" Fortinet OR "Palo Alto" OR firewall ingénieur`
  - `site:fr.indeed.com/viewjob GRC OR "ISO 27001" OR "EBIOS" consultant sécurité`
  - `site:fr.indeed.com/viewjob alternance cybersécurité alternant`
  - `site:fr.indeed.com/viewjob cybersécurité Bordeaux OR Mérignac OR Pessac`
  - `site:fr.indeed.com/viewjob cybersécurité Lille OR Villeneuve-d'Ascq OR Roubaix`
  - `site:fr.indeed.com/viewjob cybersécurité Marseille OR Aix-en-Provence OR Toulon`
  - `site:fr.indeed.com/viewjob cybersécurité Rouen OR Caen OR Brest OR Angers OR Tours OR Orléans`
  - `site:fr.indeed.com/viewjob cybersécurité freelance mission CDD intérim 2026`
  - … et 6 autre(s) requête(s), tracées dans la colonne `REQUETE` de l'onglet OFFRES_DETAILLEES.

#### Consultant cybersécurité (généraliste)

- **INTITULE_NORMALISE :** Consultant cybersécurité (généraliste)
- **VARIANTES_FRANCAISES :** Consultant cybersécurité ; Consultant SSI ; Expert cybersécurité ; Conseiller cybersécurité ; Consultant junior cybersécurité
- **VARIANTES_ANGLAISES :** Cybersecurity Consultant ; Cyber Security Consultant ; Security Specialist ; Information Security Consultant
- **COMPETENCES_ASSOCIEES :** Conseil ; audit ; analyse de risques ; accompagnement client ; restitution ; polyvalence
- **OUTILS_ASSOCIES :** Variable selon la mission
- **CERTIFICATIONS_ASSOCIEES :** ISO 27001 ; EBIOS RM ; certifications éditeurs selon la mission
- **FAMILLE :** `COEUR_GENERALISTE` — Cœur généraliste
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — ≥ 50 « Consultant Cybersécurité Junior » (extrait : 66) au 19/03/2026 : le junior existe, principalement en cabinet et en ESN, avec un parcours d'intégration (AlgoSecure : 2-3 semaines d'intégration puis mission client). C'est la voie d'entrée la plus fréquente pour un diplômé.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Deuxième métier de l'Observatoire ANSSI (15 %). Voie d'entrée la plus fréquente pour un diplômé, via les ESN, MSSP et cabinets qui recrutent en volume et forment en interne.
- **OFFRES_UNIQUES_COLLECTEES :** 20
- **STOCK_OBSERVE :** national — ≥ 800 « Consultant Cybersécurité » (extrait : 802) au 02/09/2026 ; ≥ 600 « Consultant Junior Cyber Sécurité » (02/09/2026) ; Paris/IdF — ≥ 200 (extrait : 286) au 18/05/2026
- **REQUETES_UTILISEES (15) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail architecte sécurité OR cloud OR IAM OR vulnérabilités`
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité`
  - `site:fr.indeed.com/viewjob "sécurité réseau" Fortinet OR "Palo Alto" OR firewall ingénieur`
  - `site:fr.indeed.com/viewjob cybersécurité Lille OR Villeneuve-d'Ascq OR Roubaix`
  - `site:fr.indeed.com/viewjob cybersécurité Lyon OR Villeurbanne ingénieur consultant`
  - `site:fr.indeed.com/viewjob cybersécurité Marseille OR Aix-en-Provence OR Toulon`
  - `site:fr.indeed.com/viewjob cybersécurité Strasbourg OR Nancy OR Metz OR Dijon OR Reims`
  - `site:fr.indeed.com/viewjob cybersécurité freelance mission CDD intérim 2026`
  - `site:fr.indeed.com/viewjob stage cybersécurité 2026 étudiant`
  - `site:www.free-work.com consultant cybersécurité offre emploi`
  - `site:www.free-work.com offre emploi cybersécurité GRC OR conformité OR NIS2 OR DORA consultant`
  - `site:www.hellowork.com/fr-fr/emplois "analyste SOC" OR "detection engineer" OR "threat intelligence" 2026`
  - `site:www.hellowork.com/fr-fr/emplois analyste cybersécurité OR "consultant cybersécurité" Toulouse OR Rennes OR Grenoble OR Strasbourg`
  - `site:www.welcometothejungle.com/fr/companies ingénieur cybersécurité alternance 2026 CDI France`
  - … et 1 autre(s) requête(s), tracées dans la colonne `REQUETE` de l'onglet OFFRES_DETAILLEES.

#### RSSI / CISO / Responsable cybersécurité

- **INTITULE_NORMALISE :** RSSI / CISO / Responsable cybersécurité
- **VARIANTES_FRANCAISES :** RSSI ; RSSI adjoint ; Référent sécurité des SI ; Responsable cybersécurité ; Officier de sécurité ; Responsable Campus Cyber ; Manager cybersécurité
- **VARIANTES_ANGLAISES :** CISO ; Deputy CISO ; Head of Cybersecurity ; Security Manager ; SOC Manager ; Cybersecurity Program Manager ; Security Program Manager
- **COMPETENCES_ASSOCIEES :** Gouvernance ; stratégie ; pilotage d'équipe ; budget ; conformité ; gestion de crise ; relation direction générale
- **OUTILS_ASSOCIES :** Tableaux de bord ; référentiels ; outils GRC
- **CERTIFICATIONS_ASSOCIEES :** CISSP ; CISM ; ISO 27001 Lead Implementer
- **FAMILLE :** `MANAGEMENT_CYBER` — Management cyber
- **NIVEAU_TECHNICITE :** NIVEAU_4 — Architecture / expertise avancée / recherche
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** TRES_DIFFICILE — 8 ans (Unibail), expérience confirmée de RSSI exigée (Nanterre) : trajectoire de carrière, jamais un débouché de sortie d'école.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — management
- **INCLUS_OU_EXCLU :** INCLUS pour l'analyse des trajectoires, EXCLU des débouchés juniors
- **JUSTIFICATION :** Métier le plus représenté parmi les professionnels cyber (30 %, Observatoire ANSSI) mais exigeant 8 ans et plus. À utiliser dans la communication NEXA comme HORIZON de carrière, jamais comme débouché de sortie.
- **OFFRES_UNIQUES_COLLECTEES :** 19
- **STOCK_OBSERVE :** national — ≥ 400 « RSSI, CISO » (03/09/2026) ; 52 « information systems security officer » (Glassdoor, juin 2026) ; Paris/IdF — NC
- **REQUETES_UTILISEES (11) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail analyste SOC OR pentest OR IAM OR RSSI`
  - `site:fr.indeed.com/viewjob "auditeur" OR "risk manager" cyber sécurité SI conformité`
  - `site:fr.indeed.com/viewjob "consultant SSI" OR "expert SSI" OR "gouvernance sécurité" offre`
  - `site:fr.indeed.com/viewjob GRC OR "ISO 27001" OR "EBIOS" consultant sécurité`
  - `site:fr.indeed.com/viewjob cybersécurité Lille OR Villeneuve-d'Ascq OR Roubaix`
  - `site:fr.indeed.com/viewjob cybersécurité Strasbourg OR Nancy OR Metz OR Dijon OR Reims`
  - `site:fr.indeed.com/viewjob cybersécurité Toulouse OR Montpellier OR Nice OR Sophia Antipolis`
  - `site:www.free-work.com "analyste SOC" OR "architecte sécurité" OR RSSI mission`
  - `site:www.hellowork.com/fr-fr/emplois RSSI OR "responsable sécurité" OR "chef de projet cybersécurité" 2026`
  - `site:www.hellowork.com/fr-fr/emplois cybersécurité`
  - `site:www.welcometothejungle.com/fr/companies "security engineer" OR "ingénieur sécurité" scale-up startup Paris CDI`

#### DevSecOps Engineer

- **INTITULE_NORMALISE :** DevSecOps Engineer
- **VARIANTES_FRANCAISES :** Ingénieur DevSecOps ; Consultant DevSecOps ; Consultant cyber DevSecOps ; Architecte DevSecOps
- **VARIANTES_ANGLAISES :** DevSecOps Engineer/Consultant ; Platform Security Engineer ; CI/CD Security Engineer ; Container Security Engineer ; Kubernetes Security Engineer
- **COMPETENCES_ASSOCIEES :** Intégration de la sécurité au cycle de développement ; pipelines sécurisés ; SBOM ; suivi CVE ; sécurité des conteneurs et de Kubernetes ; IaC ; scripting ; culture développement
- **OUTILS_ASSOCIES :** GitLab CI ; GitHub Actions ; Jenkins ; Docker ; Kubernetes ; Terraform ; Ansible ; Snyk ; SonarQube ; Trivy ; Semgrep ; secrets management
- **CERTIFICATIONS_ASSOCIEES :** AWS Certified Security ; AZ-500 ; certifications Kubernetes (CKS)
- **FAMILLE :** `DEVSECOPS` — DevSecOps
- **NIVEAU_TECHNICITE :** NIVEAU_3 — Engineering / automation / cloud / AppSec
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — Portes juniors réelles et documentées : « Ingénieur DevSecOps Junior » (France Travail, Toulouse, avec description de poste junior explicite : pipelines SAST/SCA/DAST, SBOM, templates CI/CD), alternance DevSecOps (Padoa), ≥ 25 stages DevSecOps (Indeed, 01/06/2026), 21 alternances DevSecOps en IdF (24/05/2026). MAIS le prérequis est un socle développement + CI/CD + conteneurs que les cursus cyber généralistes ne donnent pas.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier, à la frontière avec le développement et l'infrastructure
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Distingué d'AppSec : le DevSecOps outille et sécurise la chaîne de livraison, l'AppSec sécurise le produit et le code. Stock le plus élevé de toutes les spécialités cyber observées (≥ 817 au 04/09/2026).
- **OFFRES_UNIQUES_COLLECTEES :** 16
- **STOCK_OBSERVE :** national — ≥ 800 « DevSecOps » (extrait : 817) au 04/09/2026 ; ≥ 700 au 15/04/2026. Local : ≈ 52 à Lyon (06/09/2026), ≈ 43 à Toulouse (03/03/2026) ; Paris/IdF — ≥ 300 (extrait : 330) au 15/04/2026 ; ≥ 200 « DevSecOps Engineer » (extrait : 248) au 28/08/2026
- **REQUETES_UTILISEES (5) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail sécurité informatique ingénieur cloud DevSecOps`
  - `site:fr.indeed.com/viewjob DevSecOps ingénieur`
  - `site:www.free-work.com IAM OR cloud security OR devsecops OR pentest offre emploi France`
  - `site:www.hellowork.com/fr-fr/emplois architecte sécurité OR cloud security OR devsecops CDI`
  - `site:www.welcometothejungle.com/fr/companies cloud security OR devsecops OR appsec engineer France`

#### Ingénieur / Consultant sécurité OT-ICS

- **INTITULE_NORMALISE :** Ingénieur / Consultant sécurité OT-ICS
- **VARIANTES_FRANCAISES :** Ingénieur cybersécurité industrielle ; Consultant cybersécurité OT ; Analyste cybersécurité OT ; Ingénieur cybersécurité nucléaire ; Ingénieur sécurité des systèmes industriels
- **VARIANTES_ANGLAISES :** OT Security Engineer ; ICS Security Engineer ; Industrial Cybersecurity Engineer ; OT Security Consultant ; IoT Security Engineer ; Embedded Security Engineer (finalité cyber explicite)
- **COMPETENCES_ASSOCIEES :** Protocoles industriels ; SCADA/DCS/PLC ; segmentation IT/OT ; IEC 62443 ; analyse de risques industriels ; LPM/NIS2 ; contrôle-commande
- **OUTILS_ASSOCIES :** Outils de supervision OT ; sondes industrielles ; SIEM OT ; PCAP
- **CERTIFICATIONS_ASSOCIEES :** IEC 62443 ; GICSP
- **FAMILLE :** `OT_IOT_SECURITY` — Sécurité OT / IoT
- **NIVEAU_TECHNICITE :** NIVEAU_4 — Architecture / expertise avancée / recherche
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DIFFICILE — Les offres exigent 5 à 8 ans et une culture industrielle (SCADA, DCS, PLC). Portes juniors observées : alternance sécurité des systèmes industriels (ZF, Bouzonville), stage détection comportementale industrielle (Framatome, Lyon), alternance Framatome Montreuil-Juigné.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — spécialité sectorielle
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Marché national étroit (≈ 54 offres « OT Security » au 19/05/2026) mais très ancré dans les bassins industriels (Lyon, Grenoble, Toulouse, Belfort, Grand Est), donc pertinent à l'échelle d'un campus et non à l'échelle nationale.
- **OFFRES_UNIQUES_COLLECTEES :** 14
- **STOCK_OBSERVE :** national — ≥ 50 « OT Security » (extrait : 54) au 19/05/2026 ; Paris/IdF — NC
- **REQUETES_UTILISEES (11) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité`
  - `site:fr.indeed.com/viewjob "AI security" OR "sécurité IA" OR "LLM" ingénieur sécurité France`
  - `site:fr.indeed.com/viewjob "OT" OR "industrielle" OR "IoT" cybersécurité ingénieur consultant`
  - `site:fr.indeed.com/viewjob "analyste cybersécurité" OR "chargé de sécurité" OR "coordinateur sécurité" 2026 offre`
  - `site:fr.indeed.com/viewjob cybersécurité Bordeaux OR Mérignac OR Pessac`
  - `site:fr.indeed.com/viewjob cybersécurité Lyon OR Villeurbanne ingénieur consultant`
  - `site:fr.indeed.com/viewjob stage cybersécurité 2026 étudiant`
  - `site:www.free-work.com consultant cybersécurité offre emploi`
  - `site:www.hellowork.com/fr-fr/emplois analyste cybersécurité OR "consultant cybersécurité" Toulouse OR Rennes OR Grenoble OR Strasbourg`
  - `site:www.hellowork.com/fr-fr/emplois cybersécurité`
  - `site:www.welcometothejungle.com/fr/companies ingénieur cybersécurité alternance 2026 CDI France`

#### Analyste cybersécurité (généraliste)

- **INTITULE_NORMALISE :** Analyste cybersécurité (généraliste)
- **VARIANTES_FRANCAISES :** Analyste cybersécurité ; Analyste sécurité ; Analyste cyber ; Chargé de cybersécurité
- **VARIANTES_ANGLAISES :** Cybersecurity Analyst ; Security Analyst ; Cyber Analyst
- **COMPETENCES_ASSOCIEES :** Analyse d'alertes ; suivi de vulnérabilités ; reporting ; sensibilisation ; support sécurité
- **OUTILS_ASSOCIES :** SIEM ; EDR ; outils de scan ; Microsoft Defender
- **CERTIFICATIONS_ASSOCIEES :** CompTIA Security+ ; SC-200
- **FAMILLE :** `COEUR_GENERALISTE` — Cœur généraliste
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — Plusieurs offres Bac+3 + première expérience (Crédit Mutuel Arkéa) et de nombreuses alternances « analyste cybersécurité ».
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Intitulé fréquent en alternance. C'est aussi le poste dont le contenu est le plus directement exposé à l'automatisation : classé EXPOSITION ÉLEVÉE.
- **OFFRES_UNIQUES_COLLECTEES :** 14
- **STOCK_OBSERVE :** national — ≥ 300 « Analyste Cyber Security » (31/08/2026) ; Paris/IdF — NC
- **REQUETES_UTILISEES (10) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance cybersécurité SOC réseaux`
  - `site:fr.indeed.com/viewjob "threat intelligence" OR CERT OR CSIRT OR forensic analyste`
  - `site:fr.indeed.com/viewjob analyste SOC alternance OR junior N1 2026`
  - `site:fr.indeed.com/viewjob cybersécurité Marseille OR Aix-en-Provence OR Toulon`
  - `site:fr.indeed.com/viewjob stage cybersécurité 2026 étudiant`
  - `site:fr.jooble.org OR site:fr.talent.com cybersécurité offre emploi analyste`
  - `site:www.hellowork.com/fr-fr/emplois SOC analyste OR pentest OR IAM sécurité`
  - `site:www.hellowork.com/fr-fr/emplois analyste cybersécurité OR "consultant cybersécurité" Toulouse OR Rennes OR Grenoble OR Strasbourg`
  - `site:www.welcometothejungle.com/fr/companies IAM OR "identity" OR GRC OR risque cyber CDI France`
  - `site:www.welcometothejungle.com/fr/companies jobs cybersécurité analyste sécurité`

#### Architecte sécurité / cybersécurité

- **INTITULE_NORMALISE :** Architecte sécurité / cybersécurité
- **VARIANTES_FRANCAISES :** Architecte sécurité ; Architecte cybersécurité ; Architecte sécurité des SI ; Architecte sécurité cloud ; Architecte système IAM ; Architecte Zero Trust
- **VARIANTES_ANGLAISES :** Security Architect ; Cybersecurity Architect ; Cloud Security Architect ; Zero Trust Architect ; Security Solutions Architect ; Security Infrastructure Engineer
- **COMPETENCES_ASSOCIEES :** Architecture de sécurité ; security by design ; cyber-résilience ; analyse de risques ; sécurisation des flux critiques ; SSDLC ; revues d'architecture
- **OUTILS_ASSOCIES :** Référentiels d'architecture ; Azure/AWS/GCP ; PAM/IAM ; segmentation ; PKI
- **CERTIFICATIONS_ASSOCIEES :** SC-100 ; CISSP ; SABSA ; TOGAF (adjacent)
- **FAMILLE :** `ARCHITECTURE_ENGINEERING` — Architecture / Security Engineering
- **NIVEAU_TECHNICITE :** NIVEAU_4 — Architecture / expertise avancée / recherche
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** TRES_DIFFICILE — Safran exige Bac+5 + 5 ans, l'architecte Sécurité & Réseau Cloud (France Travail) 7-8 ans. C'est un métier de destination à 8-10 ans, pas un débouché de sortie d'école — alors qu'il constitue le premier volume du marché.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — niveau expert
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Premier métier en volume selon l'Observatoire ANSSI (21 % des offres), confirmé par nos relevés (≈ 400 offres France sur deux sources). Mais métier de destination à 7-10 ans, jamais un débouché de sortie d'école : c'est le principal piège d'interprétation du marché cyber français.
- **OFFRES_UNIQUES_COLLECTEES :** 13
- **STOCK_OBSERVE :** national — ≥ 400 « Security Architect » (11/06/2026) ; ≈ 455 « Cybersecurity Architect » (22/06/2026) ; 404 (Glassdoor, 07/2026). Ordre de grandeur indépendant : ≈ 400 recrutements d'architectes cyber en France en 2025 contre ≈ 350 en 2024 (Mercato de l'Emploi) ; Paris/IdF — ≥ 200 (extrait : 277) au 18/08/2026 ; 270 (Glassdoor, août 2026)
- **REQUETES_UTILISEES (5) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail architecte sécurité OR cloud OR IAM OR vulnérabilités`
  - `site:fr.indeed.com/viewjob "AI security" OR "sécurité IA" OR "LLM" ingénieur sécurité France`
  - `site:fr.indeed.com/viewjob EDR OR XDR OR CrowdStrike OR "Defender" sécurité`
  - `site:www.hellowork.com/fr-fr/emplois architecte sécurité OR cloud security OR devsecops CDI`
  - `site:www.welcometothejungle.com/fr/companies "cloud security" OR "sécurité cloud" OR "security architect" France offre`

#### Pentester / Consultant sécurité offensive

- **INTITULE_NORMALISE :** Pentester / Consultant sécurité offensive
- **VARIANTES_FRANCAISES :** Testeur d'intrusion ; Consultant pentest ; Consultant sécurité offensive ; Hacker éthique ; Ingénieur sécurité pentester ; Auditeur technique
- **VARIANTES_ANGLAISES :** Pentester ; Penetration Tester ; Ethical Hacker ; Offensive Security Consultant ; Red Team Operator ; Security Researcher ; Vulnerability Researcher ; Web/Mobile/Infrastructure/AD Pentester
- **COMPETENCES_ASSOCIEES :** Pentest web, API, infrastructure, Active Directory, mobile ; élévation de privilèges ; mouvement latéral ; exploitation ; recherche de vulnérabilités ; rédaction de rapports
- **OUTILS_ASSOCIES :** Kali Linux ; Burp Suite ; Metasploit ; Nmap ; Nessus ; BloodHound ; Impacket ; Mimikatz ; Wireshark ; OWASP Top 10
- **CERTIFICATIONS_ASSOCIEES :** OSCP ; OSWE ; CompTIA PenTest+ ; CEH ; GIAC (GPEN/GXPN)
- **FAMILLE :** `OFFENSIVE_SECURITY` — Offensive Security / Pentest
- **NIVEAU_TECHNICITE :** NIVEAU_4 — Architecture / expertise avancée / recherche
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** TRES_DIFFICILE — Synacktiv exige 3 ans minimum d'expérience offensive et la maîtrise complète de la chaîne (AD, cloud, CI/CD) ; Deloitte exige une expérience de pentest démontrée. Aucune alternance pentest « pure » dans notre corpus : les seules portes juniors observées sont des stages de recherche (Thales THALIUM, Framatome) et des alternances mixtes (Schneider Electric : DevSecOps + tests d'intrusion).
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS (sous-catégories PENTEST_WEB / PENTEST_INFRA / PENTEST_AD / RED_TEAM / SECURITY_RESEARCH distinguées lorsque l'intitulé le permet)
- **JUSTIFICATION :** Inclus mais mesuré avec une attention particulière : c'est le métier dont l'écart entre attractivité étudiante et volume réel de recrutement est le plus grand (≈ 33 offres nationales « pentester » au 28/08/2026 contre ≥ 800 DevSecOps).
- **OFFRES_UNIQUES_COLLECTEES :** 12
- **STOCK_OBSERVE :** national — ≥ 25 « Pentester » (extrait : 33) au 28/08/2026 ; 31 « penetration testing » (Glassdoor, 05/2026). Local : 4 à 6 à Lyon (20 et 22/07/2026). Ordre de grandeur indépendant : ≈ 150 recrutements de pentesters en France en 2025 contre ≈ 120 en 2024 (Mercato de l'Emploi) ; Paris/IdF — page datée sans compte (11/08/2026)
- **REQUETES_UTILISEES (9) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance cybersécurité SOC réseaux`
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité Lyon OR Lille OR Nantes OR Bordeaux OR Marseille`
  - `site:fr.indeed.com/viewjob "application security" OR AppSec OR "sécurité applicative"`
  - `site:fr.indeed.com/viewjob cybersécurité Nantes OR Saint-Herblain OR Rennes`
  - `site:fr.indeed.com/viewjob pentest OR pentester OR "test d'intrusion"`
  - `site:www.hellowork.com/fr-fr/emplois SOC analyste OR pentest OR IAM sécurité`
  - `site:www.hellowork.com/fr-fr/emplois analyste cybersécurité OR "consultant cybersécurité" Toulouse OR Rennes OR Grenoble OR Strasbourg`
  - `site:www.hellowork.com/fr-fr/emplois ingénieur cybersécurité Lyon OR Nantes OR Bordeaux OR Lille`
  - `site:www.welcometothejungle.com/fr/companies SOC analyst OR pentester OR "threat intelligence" France CDI`

#### Consultant / Ingénieur IAM - PAM

- **INTITULE_NORMALISE :** Consultant / Ingénieur IAM - PAM
- **VARIANTES_FRANCAISES :** Consultant IAM ; Ingénieur IAM ; Architecte système IAM ; Consultant PAM ; Consultant IGA ; Chef de projet cybersécurité IAM ; Responsable d'offre IAM
- **VARIANTES_ANGLAISES :** IAM Analyst/Consultant/Engineer/Architect ; Identity Security Engineer ; Identity Governance Specialist ; PAM Consultant/Engineer ; Access Management Specialist ; CyberArk/SailPoint/Okta Consultant ; Entra ID Security Specialist
- **COMPETENCES_ASSOCIEES :** Gestion des identités et des accès ; gouvernance des identités (IGA) ; revues d'habilitations ; SSO ; MFA ; RBAC/ABAC ; Zero Trust Identity ; PKI et cycle de vie des certificats
- **OUTILS_ASSOCIES :** Entra ID / Azure AD ; Active Directory ; CyberArk ; SailPoint ; Okta ; Ping Identity ; ForgeRock ; One Identity ; Evidian ; Wallix ; Delinea ; RACF
- **CERTIFICATIONS_ASSOCIEES :** Microsoft SC-300 ; certifications éditeurs (SailPoint, CyberArk, Okta)
- **FAMILLE :** `IAM_PAM` — IAM / PAM
- **NIVEAU_TECHNICITE :** NIVEAU_3 — Engineering / automation / cloud / AppSec
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — Seuils d'entrée relativement bas pour une spécialité technique : Deloitte 2 ans, Aix-en-Provence Bac+4/5 + 1 an, et une alternance IAM explicite observée (Montrouge, septembre 2026). C'est, avec le GRC, la spécialisation technique la plus atteignable après un premier poste.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Famille à part entière, sous-estimée par les étudiants et fortement demandée (≥ 732 offres « IAM » au 31/03/2026). Seuils d'entrée parmi les plus bas des spécialités techniques (Deloitte : 2 ans ; Aix : 1 an ; une alternance IAM observée).
- **OFFRES_UNIQUES_COLLECTEES :** 12
- **STOCK_OBSERVE :** national — ≥ 700 « IAM » (extrait : 732) au 31/03/2026 ; ≈ 405 « Identity Access Management » (18/07/2025) et 399 sur Glassdoor (09/2025). Local : ≈ 35 à Nantes (04/05/2026) ; Paris/IdF — ≥ 300 « Identity Access Management » (extrait : 360) au 26/05/2026
- **REQUETES_UTILISEES (5) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail analyste SOC OR pentest OR IAM OR RSSI`
  - `site:fr.indeed.com/viewjob "gestion des identités" OR "IAM" OR "PAM" ingénieur France offre emploi`
  - `site:fr.indeed.com/viewjob IAM OR "identity access management" OR CyberArk OR SailPoint`
  - `site:fr.indeed.com/viewjob cybersécurité Nantes OR Saint-Herblain OR Rennes`
  - `site:www.welcometothejungle.com/fr/companies IAM OR "identity" OR GRC OR risque cyber CDI France`

#### Métier adjacent (DevOps / Cloud / Data / IA sans mission sécurité explicite)

- **INTITULE_NORMALISE :** Métier adjacent (DevOps / Cloud / Data / IA sans mission sécurité explicite)
- **VARIANTES_FRANCAISES :** Administrateur systèmes ; Administrateur réseaux ; Ingénieur réseaux ; Ingénieur cloud ; Ingénieur DevOps ; SRE ; Développeur ; Architecte cloud ; Data engineer ; Data analyst ; DPO ; Responsable IT ; Auditeur IT généraliste ; Risk Manager non cyber ; Consultant RGPD ; Consultant IT ; Product Manager ; Chef de projet IT ; Technicien support ; Administrateur Microsoft 365
- **VARIANTES_ANGLAISES :** Systems/Network Administrator ; Cloud Engineer ; DevOps Engineer ; SRE ; Software Engineer ; Cloud Architect ; Data Engineer/Analyst ; IT Auditor ; IT Consultant ; Product/Project Manager ; Helpdesk Technician
- **COMPETENCES_ASSOCIEES :** Compétences IT génériques sans responsabilité de sécurité explicite
- **OUTILS_ASSOCIES :** Variable
- **CERTIFICATIONS_ASSOCIEES :** Variable
- **FAMILLE :** `METIER_ADJACENT` — Métier adjacent
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DONNEES_INSUFFISANTES — Hors périmètre.
- **PROXIMITE_AVEC_CYBERSECURITE :** Adjacent — vivier et voisinage
- **INCLUS_OU_EXCLU :** IDENTIFIÉ MAIS NON INTÉGRÉ AUX VOLUMES CYBER
- **JUSTIFICATION :** Conservés séparément pour mesurer la porosité entre cyber, DevOps, cloud et data, et pour documenter la trajectoire réelle de nombreux profils (première expérience IT puis bascule cyber). Jamais additionnés aux volumes cyber.
- **OFFRES_UNIQUES_COLLECTEES :** 11
- **STOCK_OBSERVE :** national — ≥ 2 000 « Cloud Engineer » (07/09/2026) — hors périmètre cyber strict ; Paris/IdF — NC
- **REQUETES_UTILISEES (7) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité Lyon OR Lille OR Nantes OR Bordeaux OR Marseille`
  - `site:candidat.francetravail.fr/offres/recherche/detail sécurité informatique ingénieur cloud DevSecOps`
  - `site:fr.indeed.com/viewjob "AI security" OR "sécurité IA" OR "LLM" ingénieur sécurité France`
  - `site:fr.indeed.com/viewjob "cloud security engineer" OR "ingénieur sécurité cloud" AWS Azure France`
  - `site:fr.indeed.com/viewjob DevSecOps ingénieur`
  - `site:fr.indeed.com/viewjob cybersécurité Rouen OR Caen OR Brest OR Angers OR Tours OR Orléans`
  - `site:www.welcometothejungle.com/fr/companies ingénieur cybersécurité alternance 2026 CDI France`

#### Cloud Security Engineer / Architect

- **INTITULE_NORMALISE :** Cloud Security Engineer / Architect
- **VARIANTES_FRANCAISES :** Ingénieur sécurité cloud ; Architecte sécurité cloud ; Consultant sécurité cloud ; Expert sécurité cloud
- **VARIANTES_ANGLAISES :** Cloud Security Engineer/Analyst/Architect/Consultant ; AWS/Azure/GCP Security Engineer ; CNAPP Engineer ; CSPM Specialist ; Cloud Security Operations Engineer
- **COMPETENCES_ASSOCIEES :** Sécurité AWS/Azure/GCP ; IAM cloud ; Zero Trust ; posture management ; sécurité des conteneurs et de Kubernetes ; IaC ; chiffrement ; architecture cloud sécurisée
- **OUTILS_ASSOCIES :** Microsoft Defender for Cloud ; AWS Security Hub ; GuardDuty ; Prisma Cloud ; Wiz ; Orca ; Terraform ; Azure Policy ; Entra ID
- **CERTIFICATIONS_ASSOCIEES :** AZ-500 ; SC-100 ; AWS Certified Security Specialty ; Google Cloud Security Engineer ; CCSP
- **FAMILLE :** `CLOUD_SECURITY` — Cloud Security
- **NIVEAU_TECHNICITE :** NIVEAU_3 — Engineering / automation / cloud / AppSec
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — Peu de postes cloud security « juniors » en propre, mais la compétence cloud est demandée dès l'alternance (MONEXT : Sentinel, Intune, Azure AD, Defender ; France Travail Bordeaux : SI, réseaux et cloud) et un stage/alternance dédié « Cloud et sécurité » a été observé. Prérequis : systèmes, réseaux et IaC.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** L'un des trois plus gros stocks observés. Compétence à la fois autonome (postes dédiés) et transverse (présente dans les offres d'architecture, DevSecOps, IAM et généralistes).
- **OFFRES_UNIQUES_COLLECTEES :** 10
- **STOCK_OBSERVE :** national — ≥ 400 « Cloud Security Engineer » (extrait : 438) au 25/05/2026 ; ≥ 1 000 « Cloud Security » (extrait : 1 324) au 08/09/2026. Local : ≈ 69 « Cyber Sécurité Cloud » à Lyon (18/06/2026), ≥ 25 à Nantes (06/09/2024) ; Paris/IdF — ≥ 200 « Cloud Security Engineer » (extrait : 273) au 26/05/2026 ; ≥ 700 « Cloud Security » Paris (extrait : 769) au 01/09/2026
- **REQUETES_UTILISEES (9) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance cybersécurité SOC réseaux`
  - `site:fr.indeed.com/viewjob "cloud security engineer" OR "ingénieur sécurité cloud" AWS Azure France`
  - `site:fr.indeed.com/viewjob "cloud security" OR "sécurité cloud" Azure AWS`
  - `site:www.free-work.com IAM OR cloud security OR devsecops OR pentest offre emploi France`
  - `site:www.hellowork.com/fr-fr/emplois alternance OR stage cybersécurité GRC cloud`
  - `site:www.hellowork.com/fr-fr/emplois architecte sécurité OR cloud security OR devsecops CDI`
  - `site:www.welcometothejungle.com/fr/companies "cloud security" OR "sécurité cloud" OR "security architect" France offre`
  - `site:www.welcometothejungle.com/fr/companies IAM OR "identity" OR GRC OR risque cyber CDI France`
  - `site:www.welcometothejungle.com/fr/companies cloud security OR devsecops OR appsec engineer France`

#### Analyste Threat Intelligence / Threat Hunter

- **INTITULE_NORMALISE :** Analyste Threat Intelligence / Threat Hunter
- **VARIANTES_FRANCAISES :** Analyste renseignement sur la menace ; Analyste CTI ; Analyste de la menace ; Analyste cybercriminalité et darkweb ; Chasseur de menaces
- **VARIANTES_ANGLAISES :** Cyber Threat Intelligence Analyst ; CTI Analyst ; Threat Hunter ; Threat Hunting Analyst ; Threat Researcher
- **COMPETENCES_ASSOCIEES :** OSINT ; analyse de campagnes ; TTP ; IOC ; attribution ; veille ; threat hunting ; rédaction de notes de renseignement
- **OUTILS_ASSOCIES :** MISP ; OpenCTI ; STIX/TAXII ; plateformes CTI ; SIEM ; darkweb monitoring
- **CERTIFICATIONS_ASSOCIEES :** GIAC (GCTI) ; certifications éditeurs
- **FAMILLE :** `THREAT_INTELLIGENCE` — Threat Intelligence
- **NIVEAU_TECHNICITE :** NIVEAU_3 — Engineering / automation / cloud / AppSec
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DIFFICILE — Les offres CTI observées demandent 3 à 7 ans (Sopra Steria) ou une première expérience réussie en SOC/CSIRT (Thales). Deux portes juniors observées : apprenti analyste de la menace (ANSSI) et stage CTI (Sopra Steria).
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Famille séparée du SOC (les extraits distinguent nettement CTI et détection). Portes juniors rares : apprentissage ANSSI, stage Sopra Steria.
- **OFFRES_UNIQUES_COLLECTEES :** 8
- **STOCK_OBSERVE :** national — ≥ 100 « Threat Intelligence » (16/07/2026) ; ≥ 50 « Threat Hunting » (21/07/2026) ; Paris/IdF — ≥ 25 « Cyber Threat Intelligence » (20/05/2026)
- **REQUETES_UTILISEES (6) :**
  - `site:fr.indeed.com/viewjob "threat intelligence" OR CERT OR CSIRT OR forensic analyste`
  - `site:fr.jooble.org OR site:fr.talent.com cybersécurité offre emploi analyste`
  - `site:www.hellowork.com/fr-fr/emplois "analyste SOC" OR "detection engineer" OR "threat intelligence" 2026`
  - `site:www.welcometothejungle.com/fr/companies SOC analyst OR pentester OR "threat intelligence" France CDI`
  - `site:www.welcometothejungle.com/fr/companies jobs cybersécurité analyste sécurité`
  - `site:www.welcometothejungle.com/fr/companies stage cybersécurité 2026 France`

#### Analyste / Manager Vulnérabilités (VOC)

- **INTITULE_NORMALISE :** Analyste / Manager Vulnérabilités (VOC)
- **VARIANTES_FRANCAISES :** Analyste vulnérabilités ; Analyste VOC (Vulnerability Operation Center) ; Responsable VOC ; Analyste gestion des vulnérabilités
- **VARIANTES_ANGLAISES :** Vulnerability Analyst ; Vulnerability Management Analyst/Engineer ; Vulnerability Manager ; Exposure Management Specialist ; Attack Surface Management Analyst
- **COMPETENCES_ASSOCIEES :** Scan et priorisation ; CVE/CVSS ; remédiation ; relation avec les équipes IT ; reporting ; conformité
- **OUTILS_ASSOCIES :** Tenable/Nessus ; Qualys ; Rapid7 InsightVM ; outils de scan de conteneurs
- **CERTIFICATIONS_ASSOCIEES :** CompTIA Security+ ; certifications éditeurs (Tenable, Qualys)
- **FAMILLE :** `VULNERABILITY_MANAGEMENT` — Vulnerability Management
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — Postes CDI demandant typiquement 5 ans, mais portes juniors réelles observées : stage analyste VOC (Sopra Steria ×2), alternance évaluation vulnérabilités (Schneider Electric), analyste VOC Bac+3 + première expérience (Crédit Mutuel Arkéa).
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Famille distincte, en structuration en France (émergence des « VOC » à côté des SOC chez Crédit Mutuel, Sopra Steria, Urssaf). Bonne porte d'entrée junior (stages et alternances observés).
- **OFFRES_UNIQUES_COLLECTEES :** 8
- **STOCK_OBSERVE :** national — ≥ 100 « Vulnerability Management » (extrait : 153) au 15/06/2026 ; ≥ 50 « VM Lead » (21/07/2026) ; Paris/IdF — NC
- **REQUETES_UTILISEES (6) :**
  - `site:fr.indeed.com/viewjob "analyste cybersécurité" OR "chargé de sécurité" OR "coordinateur sécurité" 2026 offre`
  - `site:fr.indeed.com/viewjob "ingénieur sécurité" OR "security engineer" CDI France`
  - `site:fr.indeed.com/viewjob "threat intelligence" OR CERT OR CSIRT OR forensic analyste`
  - `site:www.hellowork.com/fr-fr/emplois analyste cybersécurité OR "consultant cybersécurité" Toulouse OR Rennes OR Grenoble OR Strasbourg`
  - `site:www.welcometothejungle.com/fr/companies jobs cybersécurité analyste sécurité`
  - `site:www.welcometothejungle.com/fr/companies stage cybersécurité 2026 France`

#### Chef de projet cybersécurité

- **INTITULE_NORMALISE :** Chef de projet cybersécurité
- **VARIANTES_FRANCAISES :** Chef de projet cybersécurité ; Cheffe de projet cybersécurité ; Consultant AMOA cybersécurité ; Chef de projet sécurité et conformité
- **VARIANTES_ANGLAISES :** Cybersecurity Project Manager ; Security Program Manager
- **COMPETENCES_ASSOCIEES :** Pilotage de projet ; coordination ; conformité ; budget ; relation métier
- **OUTILS_ASSOCIES :** Outils de gestion de projet
- **CERTIFICATIONS_ASSOCIEES :** Certifications de gestion de projet (adjacentes)
- **FAMILLE :** `MANAGEMENT_CYBER` — Management cyber
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DIFFICILE — Suppose une légitimité technique préalable ; quelques alternances (Onet Technologies, Savencia).
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — pilotage
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Conservé car récurrent dans les offres, mais suppose une légitimité technique préalable : pas un débouché de sortie d'école.
- **OFFRES_UNIQUES_COLLECTEES :** 6
- **STOCK_OBSERVE :** national — NC en propre ; Paris/IdF — NC
- **REQUETES_UTILISEES (6) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité`
  - `site:fr.indeed.com/viewjob "cloud security engineer" OR "ingénieur sécurité cloud" AWS Azure France`
  - `site:fr.indeed.com/viewjob cybersécurité Nantes OR Saint-Herblain OR Rennes`
  - `site:www.free-work.com consultant cybersécurité offre emploi`
  - `site:www.hellowork.com/fr-fr/emplois cybersécurité`
  - `site:www.welcometothejungle.com/fr/companies stage cybersécurité 2026 France`

#### AI Security / LLM Security Engineer

- **INTITULE_NORMALISE :** AI Security / LLM Security Engineer
- **VARIANTES_FRANCAISES :** Pentester IA ; Ingénieur développement cybersécurité IA ; Architecte sécurité cloud, DevSecOps & IA ; Ingénieur sécurité système (IA appliquée à l'analyse cyber)
- **VARIANTES_ANGLAISES :** AI Security Engineer/Specialist/Researcher ; AI Red Team Engineer ; AI Red Teamer ; LLM Security Engineer ; GenAI Security Engineer ; ML Security Engineer ; Adversarial ML Engineer ; AI Governance Specialist ; AI Risk Analyst ; AI Security Architect ; Agentic AI Security Engineer ; Prompt Injection Security Specialist
- **COMPETENCES_ASSOCIEES :** Sécurisation des applications à base de LLM ; prompt injection ; jailbreak ; adversarial ML ; sécurité des agents IA et des pipelines RAG ; gouvernance de l'IA ; OWASP Top 10 for LLM Applications ; MITRE ATLAS
- **OUTILS_ASSOCIES :** Garak ; PyRIT ; plateformes LLM ; vector databases ; MCP ; Security Copilot
- **CERTIFICATIONS_ASSOCIEES :** Aucune certification établie et reconnue par les recruteurs français à la date de la collecte
- **FAMILLE :** `AI_SECURITY_EMERGENT` — AI Security (émergent)
- **NIVEAU_TECHNICITE :** NIVEAU_4 — Architecture / expertise avancée / recherche
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DONNEES_INSUFFISANTES — Une seule alternance identifiée (« Ingénieur Développement cybersécurité IA », Vélizy). Aucun marché junior observable.
- **PROXIMITE_AVEC_CYBERSECURITE :** Émergent — extension des métiers cyber existants
- **INCLUS_OU_EXCLU :** INCLUS AVEC RÉSERVE MAJEURE
- **JUSTIFICATION :** Aucun stock d'offres mesurable en France : nos 6 offres relevant de ce champ sont des postes cyber ou IA existants auxquels s'ajoute une dimension IA, et une seule alternance a été identifiée. Conclusion : compétence transverse à enseigner, PAS une spécialisation autonome finançable par le marché en 2026.
- **OFFRES_UNIQUES_COLLECTEES :** 6
- **STOCK_OBSERVE :** national — Aucun compteur dédié observé sur les jobboards français. Un cabinet de recrutement avance 119 offres « Red Team » sur LinkedIn France en mai 2026 (non vérifiable, non spécifique AI Security). ; Paris/IdF — NC
- **REQUETES_UTILISEES (4) :**
  - `site:fr.indeed.com/viewjob "OT" OR "industrielle" OR "IoT" cybersécurité ingénieur consultant`
  - `site:fr.indeed.com/viewjob "gestion des identités" OR "IAM" OR "PAM" ingénieur France offre emploi`
  - `site:fr.indeed.com/viewjob IAM OR "identity access management" OR CyberArk OR SailPoint`
  - `site:www.welcometothejungle.com/fr/companies IAM OR "identity" OR GRC OR risque cyber CDI France`

#### AppSec / Product Security Engineer

- **INTITULE_NORMALISE :** AppSec / Product Security Engineer
- **VARIANTES_FRANCAISES :** Ingénieur sécurité applicative ; Consultant sécurité des applications ; Responsable sécurité produit ; Manager sécurité applicative
- **VARIANTES_ANGLAISES :** Application Security Engineer ; AppSec Engineer ; Product Security Engineer/Analyst ; Secure Software Engineer ; Software Security Engineer ; API Security Engineer ; Security Champion Lead
- **COMPETENCES_ASSOCIEES :** Secure coding ; OWASP Top 10 ; threat modeling ; revue de code ; SSDLC ; sécurité des API ; accompagnement des équipes produit
- **OUTILS_ASSOCIES :** SAST/DAST/SCA (Snyk, SonarQube, Checkmarx, Veracode, Semgrep) ; secret scanning ; GitHub Advanced Security ; Burp Suite
- **CERTIFICATIONS_ASSOCIEES :** CSSLP ; OSWE ; certifications éditeurs
- **FAMILLE :** `APPSEC_PRODUCT_SECURITY` — AppSec / Product Security
- **NIVEAU_TECHNICITE :** NIVEAU_3 — Engineering / automation / cloud / AppSec
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DIFFICILE — Les offres AppSec exigent une compréhension réelle du code : Akeneo demande 2-5 ans de sécurité en environnement web, Tiime 4-6 ans, Safran un accompagnement des équipes produit. Le poste « Application Security Manager » (Bordeaux) exige la maîtrise de SAST/DAST/SCA/API/conteneurs et du threat modeling. Aucune alternance AppSec pure dans notre corpus.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier, à la frontière avec le développement
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Distingué de DevSecOps et de Product Security lorsque l'intitulé le permet. Exige une compréhension réelle du code : point de convergence avec la filière Développement Web.
- **OFFRES_UNIQUES_COLLECTEES :** 6
- **STOCK_OBSERVE :** national — ≥ 600 « Application Security Engineer » (10/08/2026) ; ≈ 1 142 « Sécurité applicative » (04/02/2026) ; ≥ 400 « Ingénieur Sécurité Applicative » (23/05/2026) ; Paris/IdF — ≥ 300 « Application Security Engineer » (extrait : 354) au 17/08/2026
- **REQUETES_UTILISEES (3) :**
  - `site:fr.indeed.com/viewjob "application security" OR AppSec OR "sécurité applicative"`
  - `site:www.welcometothejungle.com/fr/companies "security engineer" OR "ingénieur sécurité" scale-up startup Paris CDI`
  - `site:www.welcometothejungle.com/fr/companies cloud security OR devsecops OR appsec engineer France`

#### SecOps / Security Operations Engineer

- **INTITULE_NORMALISE :** SecOps / Security Operations Engineer
- **VARIANTES_FRANCAISES :** Ingénieur sécurité opérationnelle ; Ingénieur MCS (maintien en condition de sécurité) ; Expert SecOps
- **VARIANTES_ANGLAISES :** SecOps Engineer ; Security Operations Engineer ; Security Platform Engineer ; Security Tools Engineer
- **COMPETENCES_ASSOCIEES :** Exploitation et industrialisation des solutions de sécurité ; durcissement (hardening) ; automatisation ; scripting ; intégration d'outils
- **OUTILS_ASSOCIES :** EDR/XDR ; firewalls ; SIEM ; SOAR ; PAM ; NAC ; SASE/SSE ; Python/PowerShell
- **CERTIFICATIONS_ASSOCIEES :** Certifications éditeurs (Microsoft, Palo Alto, Fortinet, CrowdStrike)
- **FAMILLE :** `SOC_BLUE_TEAM_SECOPS` — SOC / Blue Team / SecOps
- **NIVEAU_TECHNICITE :** NIVEAU_3 — Engineering / automation / cloud / AppSec
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DIFFICILE — Les offres SecOps observées demandent une expérience opérationnelle confirmée (souvent 5 ans et plus) ; aucune offre junior identifiée hors alternance.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Famille distincte du SOC analytique : il s'agit de faire fonctionner et d'industrialiser la plateforme de sécurité, pas d'analyser les alertes.
- **OFFRES_UNIQUES_COLLECTEES :** 5
- **STOCK_OBSERVE :** national — NC en propre ; Paris/IdF — NC
- **REQUETES_UTILISEES (5) :**
  - `site:fr.indeed.com/viewjob "ingénieur sécurité" OR "security engineer" CDI France`
  - `site:fr.indeed.com/viewjob cybersécurité Bordeaux OR Mérignac OR Pessac`
  - `site:www.free-work.com consultant cybersécurité offre emploi`
  - `site:www.free-work.com mission cybersécurité SOC OR SIEM OR Splunk OR Sentinel 2026`
  - `site:www.hellowork.com/fr-fr/emplois cybersécurité`

#### Administrateur / technicien sécurité

- **INTITULE_NORMALISE :** Administrateur / technicien sécurité
- **VARIANTES_FRANCAISES :** Administrateur sécurité ; Administrateur cybersécurité ; Technicien sécurité informatique ; Technicien systèmes et réseaux orienté sécurité ; Assistant ingénieur cybersécurité
- **VARIANTES_ANGLAISES :** Security Administrator ; Security Technician ; IT Security Support
- **COMPETENCES_ASSOCIEES :** Exploitation des solutions de sécurité ; administration ; support ; suivi des vulnérabilités ; Microsoft 365 ; Windows/Linux
- **OUTILS_ASSOCIES :** Antivirus/EDR ; firewall ; Active Directory ; Microsoft 365 ; outils de sauvegarde
- **CERTIFICATIONS_ASSOCIEES :** CompTIA Security+ ; certifications éditeurs
- **FAMILLE :** `NETWORK_INFRA_SECURITY` — Sécurité réseau / infrastructure
- **NIVEAU_TECHNICITE :** NIVEAU_1 — Fondamentaux / support / gouvernance simple
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE — Niveau Bac+2/+3 fréquemment suffisant ; nombreuses alternances support IT / systèmes-réseaux avec volet cybersécurité.
- **PROXIMITE_AVEC_CYBERSECURITE :** Périphérie opérationnelle du cœur de métier
- **INCLUS_OU_EXCLU :** INCLUS lorsque la mission de sécurité est explicite
- **JUSTIFICATION :** Niveau de technicité 1-2, accessible à Bac+2/+3. Porte d'entrée réelle mais fortement exposée à l'automatisation : à ne pas positionner comme cible d'un Bachelor Bac+3.
- **OFFRES_UNIQUES_COLLECTEES :** 5
- **STOCK_OBSERVE :** national — ≥ 700 « Administrateur Sécurité Informatique » (extrait : 744) au 25/08/2026 — requête large ; ≥ 50 « Administrateur Cyber Sécurité » (05/02/2026) ; Paris/IdF — NC
- **REQUETES_UTILISEES (4) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail technicien OR administrateur systèmes réseaux sécurité alternance 2026`
  - `site:fr.indeed.com/viewjob "sécurité réseau" Fortinet OR "Palo Alto" OR firewall ingénieur`
  - `site:fr.indeed.com/viewjob alternance cybersécurité alternant`
  - `site:www.welcometothejungle.com/fr/companies stage cybersécurité 2026 France`

#### Detection Engineer / SOC Engineering

- **INTITULE_NORMALISE :** Detection Engineer / SOC Engineering
- **VARIANTES_FRANCAISES :** Ingénieur détection ; Ingénieur cas d'usage SIEM ; Intégrateur SOC ; Ingénieur de parsing/normalisation de logs
- **VARIANTES_ANGLAISES :** Detection Engineer ; SIEM Engineer ; SOAR Engineer ; Security Automation Engineer (finalité cyber) ; Log Integrator ; Parsing Engineer
- **COMPETENCES_ASSOCIEES :** Detection engineering ; écriture et optimisation de règles de corrélation ; Sigma ; YARA ; MITRE ATT&CK ; playbooks SOAR ; parsing/normalisation/enrichissement ; scripting Python
- **OUTILS_ASSOCIES :** Microsoft Sentinel ; Splunk ; QRadar ; Elastic ; Cortex XSOAR ; Splunk SOAR ; Tines ; API/webhooks
- **CERTIFICATIONS_ASSOCIEES :** Microsoft SC-200 ; certifications Splunk ; GIAC (GCDA)
- **FAMILLE :** `SOC_BLUE_TEAM_SECOPS` — SOC / Blue Team / SecOps
- **NIVEAU_TECHNICITE :** NIVEAU_3 — Engineering / automation / cloud / AppSec
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — Une alternance explicitement « SOC Detection Engineer » observée (Advens, Lille, 2026) et une alternance Analyste SOC/risk (CHANEL) : la porte d'entrée existe mais reste étroite et adossée à un encadrement expert.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — segment à plus forte valeur du SOC
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Distingué de l'analyste SOC car les compétences (conception de détection, automatisation, scripting) et l'exposition à l'automatisation diffèrent radicalement. C'est le segment du SOC dont la valeur augmente avec l'IA.
- **OFFRES_UNIQUES_COLLECTEES :** 5
- **STOCK_OBSERVE :** national — NC en propre (intitulé peu utilisé dans les pages de liste indexées) ; Paris/IdF — NC
- **REQUETES_UTILISEES (4) :**
  - `site:fr.indeed.com/viewjob cybersécurité Lille OR Villeneuve-d'Ascq OR Roubaix`
  - `site:www.free-work.com mission cybersécurité SOC OR SIEM OR Splunk OR Sentinel 2026`
  - `site:www.hellowork.com/fr-fr/emplois SOC analyste OR pentest OR IAM sécurité`
  - `site:www.welcometothejungle.com/fr/companies SOC analyst OR pentester OR "threat intelligence" France CDI`

#### Auditeur cybersécurité / SSI

- **INTITULE_NORMALISE :** Auditeur cybersécurité / SSI
- **VARIANTES_FRANCAISES :** Auditeur cybersécurité ; Auditeur SSI ; Auditeur IT ; Auditeur sécurité des SI
- **VARIANTES_ANGLAISES :** Cybersecurity Auditor ; IT Security Auditor ; Information Security Consultant
- **COMPETENCES_ASSOCIEES :** Conduite d'audit ; référentiels ; collecte et qualification de preuves ; restitution ; plans de remédiation
- **OUTILS_ASSOCIES :** Référentiels ISO 27001/27002 ; grilles d'audit ; outils de scan
- **CERTIFICATIONS_ASSOCIEES :** ISO 27001 Lead Auditor ; CISA
- **FAMILLE :** `AUDIT_COMPLIANCE` — Audit / Conformité
- **NIVEAU_TECHNICITE :** NIVEAU_2 — Expertise cyber opérationnelle
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** ACCESSIBLE_AVEC_PRE_REQUIS — L'offre d'auditeur cyber de l'Urssaf demande Bac+5 ou 5 ans d'expérience, avec exposition pentest et gestion des vulnérabilités.
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier — proche du GRC mais posture et livrables distincts
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Non fusionné avec le GRC : l'audit est une posture de contrôle indépendante, avec des exigences propres (indépendance, méthode, preuve).
- **OFFRES_UNIQUES_COLLECTEES :** 3
- **STOCK_OBSERVE :** national — NC en propre ; Paris/IdF — NC
- **REQUETES_UTILISEES (3) :**
  - `site:fr.indeed.com/viewjob "auditeur" OR "risk manager" cyber sécurité SI conformité`
  - `site:fr.indeed.com/viewjob "cloud security engineer" OR "ingénieur sécurité cloud" AWS Azure France`
  - `site:fr.indeed.com/viewjob cybersécurité Nantes OR Saint-Herblain OR Rennes`

#### Analyste DFIR / Incident Response

- **INTITULE_NORMALISE :** Analyste DFIR / Incident Response
- **VARIANTES_FRANCAISES :** Analyste réponse à incident ; Analyste CERT ; Analyste CSIRT ; Analyste forensic ; Investigateur numérique ; Analyste de malware ; Rétro-ingénieur sécurité
- **VARIANTES_ANGLAISES :** Incident Response Analyst ; Incident Responder ; DFIR Analyst ; Digital Forensics Analyst ; Forensic Investigator ; Malware Analyst ; Reverse Engineer
- **COMPETENCES_ASSOCIEES :** Investigation avancée ; forensic disque et mémoire ; analyse de malware ; gestion de crise ; chaîne de preuve ; APT/exfiltration
- **OUTILS_ASSOCIES :** Volatility ; Wireshark ; sandbox ; outils forensic ; PCAP ; EDR
- **CERTIFICATIONS_ASSOCIEES :** GIAC (GCFA/GCFE/GREM) ; certifications éditeurs
- **FAMILLE :** `INCIDENT_RESPONSE_FORENSICS` — Incident Response / Forensics
- **NIVEAU_TECHNICITE :** NIVEAU_4 — Architecture / expertise avancée / recherche
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** TRES_DIFFICILE — Aucune offre junior DFIR observée ; les postes exigent une expertise forensic/malware confirmée (analyste DFIR/CTI senior, DFIR incident response).
- **PROXIMITE_AVEC_CYBERSECURITE :** Cœur du métier
- **INCLUS_OU_EXCLU :** INCLUS
- **JUSTIFICATION :** Volume faible mais expertise stratégique. Aucune offre junior observée : à ne pas présenter comme un débouché de sortie d'école.
- **OFFRES_UNIQUES_COLLECTEES :** 3
- **STOCK_OBSERVE :** national — NC en propre ; « Threat Hunting » ≥ 50 (21/07/2026) ; Paris/IdF — NC
- **REQUETES_UTILISEES (2) :**
  - `site:www.free-work.com "analyste SOC" OR "architecte sécurité" OR RSSI mission`
  - `site:www.hellowork.com/fr-fr/emplois "analyste SOC" OR "detection engineer" OR "threat intelligence" 2026`

#### Hors périmètre (faux positif)

- **INTITULE_NORMALISE :** Hors périmètre (faux positif)
- **VARIANTES_FRANCAISES :** Talent acquisition cybersécurité ; commercial/marketing cybersécurité ; auditeur financier ; auditeur interne non IT ; agent de sécurité physique ; ingénieur sécurité incendie ; professeur de cybersécurité ; chargé de recrutement ; analyste de politiques publiques
- **VARIANTES_ANGLAISES :** Talent Acquisition Specialist ; Sales/Marketing (cybersecurity vendor) ; Financial Auditor ; Physical Security Officer ; Fire Safety Engineer
- **COMPETENCES_ASSOCIEES :** Sans objet
- **OUTILS_ASSOCIES :** Sans objet
- **CERTIFICATIONS_ASSOCIEES :** Sans objet
- **FAMILLE :** `EXCLU_DU_PERIMETRE` — Exclu du périmètre
- **NIVEAU_TECHNICITE :** HORS PERIMETRE
- **ACCESSIBILITE_JUNIOR_PRESUMEE :** DONNEES_INSUFFISANTES — Volume observé insuffisant.
- **PROXIMITE_AVEC_CYBERSECURITE :** Aucune — homonymie ou secteur d'activité
- **INCLUS_OU_EXCLU :** EXCLU
- **JUSTIFICATION :** Filtre explicite appliqué à la classification (liste EXCLUSIONS dans scripts_cyber/normalize.py). 3 offres du corpus ont été écartées à ce titre, notamment un stage « Talent Acquisition Specialist Cybersécurité » (poste RH dans une société cyber) et un poste commercial/marketing.
- **OFFRES_UNIQUES_COLLECTEES :** 0
- **STOCK_OBSERVE :** national — NC ; Paris/IdF — NC
- **REQUETES_UTILISEES (2) :**
  - `site:candidat.francetravail.fr/offres/recherche/detail cybersécurité`
  - `site:fr.indeed.com/viewjob stage cybersécurité 2026 étudiant`

### Métiers émergents liés à l'IA — état de la mesure

Les intitulés suivants ont été recherchés explicitement : AI Security Engineer, AI Security Specialist, AI Security Researcher, AI Red Team Engineer, AI Red Teamer, LLM Security Engineer, GenAI Security Engineer, ML Security Engineer, Machine Learning Security Engineer, AI Governance Specialist, AI Risk Analyst, AI Security Architect, AI Threat Researcher, Adversarial ML Engineer, AI Application Security Engineer, AI Safety & Security Engineer, Prompt Injection Security Specialist, Agentic AI Security Engineer.

**Résultat :** aucun de ces intitulés ne produit de stock d'offres mesurable sur les plateformes françaises. Les seules offres françaises rattachables à ce champ sont :

- **Cheffe / Chef de projet Cybersécurité IAM** — NC, Issy-les-Moulineaux (Indeed) : Bonne connaissance des enjeux IAM (IAG, gouvernance des identités), idéalement CyberArk PAM
- **Ingénieur sécurité IAM (F/H)** — Eviden, Bezons (Welcome to the Jungle) : NC
- **Consultante / Consultant Cybersécurité IAM - PAM** — Capgemini, Paris (Welcome to the Jungle) : Poste localisé au Campus Cyber
- **APPRENTISSAGE - Ingénieur Développement cybersécurité IA (F/H)** — NC, Vélizy-Villacoublay (Indeed) : NC
- **Consultant Sécurité IAM H/F** — NC, Paris (Indeed) : Accompagnement des clients sur la stratégie technique ou la mise en œuvre de solutions IAM/PAM
- **Consultant sécurité IAM H/F** — NC, Aix-en-Provence (Indeed) : NC

À quoi s'ajoutent les offres de cybersécurité classique dans lesquelles une compétence de sécurisation ou d'usage de l'IA apparaît **sans modifier l'intitulé du poste** :

- **Pentester IA / Offensive Cybersecurity Engineer** (Île-de-France, HelloWork) — mentions : Agents IA / RAG ; IA générative / LLM
- **Architecte Sécurité Cloud, DevSecOps & IA (H/F)** (Île-de-France, Free-Work) — mentions : IA générative / LLM
- **Chargé de Gouvernance Cybersécurité & Risques Fournisseurs (All Gender)** (Colomiers (Toulouse), Indeed) — mentions : AI Security / sécurisation des systèmes IA
- **Ingénieur Sécurité Système** (Paris 15e, Indeed) — mentions : IA générative / LLM
- **RSSI / Head Of Cybersecurity (leader européen Data & IA BtoB)** (Paris 1er, HelloWork) — mentions : IA générative / LLM
- **POEI Ingénieur IA INDUSTRIEL** (Paris 16e, Indeed) — mentions : AI Security / sécurisation des systèmes IA ; Agents IA / RAG ; IA générative / LLM
- **Software Engineer - AI Agent (Expert)** (Paris, Indeed) — mentions : Agents IA / RAG ; IA générative / LLM
- **Alternant(e) Ingénieur IA & Automatisation** (Moissy-Cramayel, Indeed) — mentions : Agents IA / RAG ; IA générative / LLM
- **Développeur IA / LLM (H/F)** (Paris 4e, Indeed) — mentions : IA générative / LLM
- **ALTERNANT IA / DATA & AUTOMATISATION F/H** (Toulouse, Indeed) — mentions : IA générative / LLM
- **Architecte GCP - Data & IA Hybride (H/F)** (Hauts-de-Seine, France Travail) — mentions : IA générative / LLM

**Conclusion de mesure :** 13 offres sur 342 (3.8 %) portent une mention IA. L'AI Security se présente en France en 2026 comme une **extension de métiers existants**, pas comme un métier autonome.

### Métiers adjacents identifiés mais non intégrés aux volumes

11 offres ont été classées « métier adjacent » : elles portent sur du DevOps, du cloud, de l'infrastructure ou de l'IA sans responsabilité de sécurité explicitement énoncée dans l'extrait. Elles sont conservées dans le fichier détaillé (colonne `DANS_PERIMETRE` = False) et **jamais additionnées aux volumes cyber**.

- Ingénieur Cloud / Infra / DevOps F/H — Tours (Indeed)
- DevOps Junior (H/F) — Rouen (Indeed)
- Ingénieur DevOps Azure Confirmé H/F (H/F) — Suresnes (France Travail)
- Alternance Septembre 2026 - Informatique/Cybersécurité/Data H/F — Roissy-en-France (Welcome to the Jungle)
- Ingénieur Cloud & DevOps expérimenté H/F — Paris (Indeed)
- Ingénierie Cloud / Data — Nantes (Indeed)
- Cloud DevOps AWS (H/F/X) — Bagneux (Indeed)
- Software Engineer - AI Agent (Expert) — Paris (Indeed)
- Développeur IA / LLM (H/F) — Paris 4e (Indeed)
- ALTERNANT IA / DATA & AUTOMATISATION F/H — Toulouse (Indeed)
- Ingénieur DevOps (H/F) — Paris 11e (France Travail)

### Faux positifs écartés

3 offres ont été écartées par le filtre de faux positifs :

- Professeur/e cybersécurité informatique, réseau électronique 2026 (H/F) — Île-de-France (France Travail) — motif : intitulé RH, commercial ou sans composante technique cyber.
- STAGE – Talent Acquisition Specialist Cybersécurité h/f — Paris 16e (Indeed) — motif : intitulé RH, commercial ou sans composante technique cyber.
- Stage ou Alternance Commercial & Marketing Digital – Cybersécurité / IT / IA — Valence (Indeed) — motif : intitulé RH, commercial ou sans composante technique cyber.

Les catégories de faux positifs exclues par construction sont : administrateur systèmes ou réseaux sans mission de sécurité, développeur sans responsabilité sécurité, DevOps sans DevSecOps, support IT et helpdesk, data analyst sans sécurité, DPO purement juridique, consultant RGPD sans dimension sécurité, auditeur financier, risk manager sans risque IT ou cyber, ingénieur sécurité incendie, agent de sécurité physique et sûreté, product manager sans responsabilité sécurité, consultant IT généraliste, ainsi que les fonctions RH, marketing et commerciales exercées au sein d'entreprises de cybersécurité.

---

## Partie B — Plateformes sans données exploitables

Cette partie recense **toutes les plateformes et voies d'accès testées pour lesquelles aucune donnée exploitable n'a pu être obtenue**, ainsi que la source de remplacement utilisée. Elle explique pourquoi l'objectif indicatif de 500 à 1 000 offres uniques n'a pas été atteint.

### Accès HTTP direct à toutes les plateformes (WebFetch et curl)

- **URL :** https://fr.indeed.com/ ; https://candidat.francetravail.fr/ ; https://www.apec.fr/ ; https://www.welcometothejungle.com/ ; https://www.hellowork.com/ ; https://fr.linkedin.com/jobs/ ; https://www.free-work.com/ ; https://cyber.gouv.fr/ ; etc.
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Tous les métiers du périmètre cybersécurité
- **ZONES_TESTEES :** France, régions, villes NEXA
- **DONNEES_RECHERCHEES :** Contenu intégral des offres (description, salaire, expérience, compétences, certifications), compteurs en direct des moteurs de recherche, PDF des études (ANSSI, OPIIEC, Apec)
- **RESULTAT :** Bloqué : le proxy de la session refuse toutes les connexions sortantes hors moteur de recherche (curl : « CONNECT tunnel failed, response 403 » ; WebFetch : « EGRESS_BLOCKED »). Testé sur cyber.gouv.fr, hellowork.com, francetravail.fr, welcometothejungle API, ssi.gouv.fr
- **DONNEES_MANQUANTES :** Descriptions complètes des offres, dates de publication exactes, salaires affichés, listes de compétences exhaustives, compteurs en direct, pages des rapports PDF
- **AUTRES_CHEMINS_TESTES :** curl direct, WebFetch, statut du proxy agent (/__agentproxy/status), API publique WTTJ
- **SOURCE_DE_REMPLACEMENT :** Recherche web (titres, URL et extraits des pages publiques indexées), y compris compteurs datés figurant dans les titres de pages de liste Indeed/Glassdoor
- **IMPACT_SUR_L_ANALYSE :** Majeur : beaucoup de champs d'offres à « NC » ; les volumes sont des stocks indexés à des dates hétérogènes et non des relevés simultanés ; l'objectif indicatif de 500-1 000 offres uniques n'a pas pu être atteint (348 offres uniques collectées)

### Apec (pages détail-offre)

- **URL :** https://www.apec.fr/candidat/recherche-emploi.html/emploi/detail-offre/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Ingénieur cybersécurité, consultant cybersécurité
- **ZONES_TESTEES :** France, Toulouse, Grenoble, Île-de-France
- **DONNEES_RECHERCHEES :** Offres individuelles avec expérience, salaire, diplôme
- **RESULTAT :** Très peu de pages détail-offre indexées ; la majorité des résultats sont des pages de recherche paramétrées sans contenu exploitable, et les extraits renvoient des messages d'erreur ou du contenu générique
- **DONNEES_MANQUANTES :** Volumes d'offres cadres cyber par métier et par région, contenu des offres
- **AUTRES_CHEMINS_TESTES :** site:www.apec.fr detail-offre, site:jd.apec.fr, requêtes par intitulé et par région
- **SOURCE_DE_REMPLACEMENT :** Études Apec publiées (Prévisions de recrutements de cadres 2026, étude cybersécurité 2022) ; Indeed, France Travail, HelloWork, WTTJ, Free-Work pour les offres
- **IMPACT_SUR_L_ANALYSE :** L'Apec, source de référence sur l'emploi cadre, n'est représentée que par 2 offres individuelles ; ses études compensent partiellement pour le cadrage macro

### LinkedIn Jobs

- **URL :** https://fr.linkedin.com/jobs/view/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Cybersecurity engineer, security engineer, analyste SOC
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Offres individuelles récentes et compteurs
- **RESULTAT :** Pages d'offres indexées mais majoritairement anciennes (identifiants d'offres correspondant à des publications antérieures) ; aucun compteur exploitable ; pas de date de publication dans les extraits
- **DONNEES_MANQUANTES :** Dates de publication, statut actif/inactif des offres, volumes
- **AUTRES_CHEMINS_TESTES :** site:fr.linkedin.com/jobs/view avec variantes d'intitulés
- **SOURCE_DE_REMPLACEMENT :** Indeed, France Travail, HelloWork, WTTJ, Free-Work
- **IMPACT_SUR_L_ANALYSE :** 8 offres LinkedIn retenues, marquées comme non datées ; exclues du raisonnement sur les flux récents

### Monster France

- **URL :** https://www.monster.fr/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Ingénieur cybersécurité
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Offres individuelles et volumes
- **RESULTAT :** Aucun résultat du domaine renvoyé par la recherche web (requête combinée Meteojob/Monster : seuls des résultats Meteojob sont remontés)
- **DONNEES_MANQUANTES :** Toutes
- **AUTRES_CHEMINS_TESTES :** site:www.monster.fr cybersécurité emploi ingénieur
- **SOURCE_DE_REMPLACEMENT :** Meteojob, Indeed, HelloWork
- **IMPACT_SUR_L_ANALYSE :** Plateforme non couverte ; impact faible (généraliste, forte redondance avec les autres jobboards)

### JobTeaser

- **URL :** https://www.jobteaser.com/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Alternance et stage cybersécurité
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Offres alternance/stage individuelles et volumes
- **RESULTAT :** Seule une page « entreprise » (Orange Cyberdefense) est remontée, sans offre individuelle ni compteur
- **DONNEES_MANQUANTES :** Volumes et offres alternance/stage
- **AUTRES_CHEMINS_TESTES :** Requête ESN/MSSP recrutement, requêtes alternance
- **SOURCE_DE_REMPLACEMENT :** Indeed (pages alternance datées), HelloWork, Welcome to the Jungle, France Travail
- **IMPACT_SUR_L_ANALYSE :** Faible : l'alternance est bien couverte par Indeed, HelloWork, WTTJ et France Travail (plus de 45 offres d'alternance et 15 stages collectés)

### Meteojob

- **URL :** https://www.meteojob.com/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Ingénieur cybersécurité, ingénieur sécurité informatique
- **ZONES_TESTEES :** France, Paris, Saint-Maur-des-Fossés, Saint-Ouen-sur-Seine
- **DONNEES_RECHERCHEES :** Offres individuelles
- **RESULTAT :** Uniquement des pages de liste (aucune page d'offre individuelle indexée) ; un ordre de grandeur exploitable dans l'extrait (77 offres « ingénieur cybersécurité »), mais non daté dans le titre
- **DONNEES_MANQUANTES :** Offres individuelles, dates des compteurs
- **AUTRES_CHEMINS_TESTES :** site:www.meteojob.com avec plusieurs intitulés
- **SOURCE_DE_REMPLACEMENT :** Indeed, HelloWork
- **IMPACT_SUR_L_ANALYSE :** Faible : 1 ligne conservée, marquée comme page de liste et non comme offre

### Talent.com et Jooble

- **URL :** https://fr.talent.com/ ; https://fr.jooble.org/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Analyste cybersécurité, CTI, cybersécurité junior, alternance
- **ZONES_TESTEES :** France, Paris, Toulouse
- **DONNEES_RECHERCHEES :** Offres individuelles et volumes datés
- **RESULTAT :** Uniquement des pages de recherche agrégées ; aucune offre individuelle ni compteur daté. Une donnée salariale (47 124 €/an pour « analyste cybersécurité » sur Jooble) mais sans méthode publiée
- **DONNEES_MANQUANTES :** Offres individuelles, volumes datés, méthode de calcul salarial
- **AUTRES_CHEMINS_TESTES :** site:fr.talent.com, site:fr.jooble.org avec plusieurs intitulés
- **SOURCE_DE_REMPLACEMENT :** Indeed, France Travail, HelloWork, WTTJ, Free-Work
- **IMPACT_SUR_L_ANALYSE :** Faible : agrégateurs fortement redondants avec les sources primaires déjà couvertes ; 2 lignes conservées comme pages de liste

### Sites carrières d'ESN/MSSP (Orange Cyberdefense, I-TRACING, Almond, Advens)

- **URL :** https://jobs.orangecyberdefense.com/jobs ; sites carrières respectifs
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Analyste, consultant, pentester, architecte
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Offres individuelles et volumes par employeur
- **RESULTAT :** Pages d'accueil carrières et pages institutionnelles indexées, sans offre individuelle ni compteur exploitable dans les extraits
- **DONNEES_MANQUANTES :** Nombre d'offres ouvertes par employeur, répartition par métier
- **AUTRES_CHEMINS_TESTES :** Requêtes ciblées par nom d'entreprise + recrutement 2026
- **SOURCE_DE_REMPLACEMENT :** Offres de ces mêmes employeurs captées via Indeed, HelloWork, WTTJ et France Travail (Sopra Steria, Atos, Capgemini, Thales, Deloitte, Devoteam, Advens, AlgoSecure, Itrust, Synacktiv, XMCO...)
- **IMPACT_SUR_L_ANALYSE :** Modéré : la structure employeur est reconstituée à partir des jobboards, sans compte direct par ESN

### Cybersecurityjobsite.com

- **URL :** https://www.cybersecurityjobsite.com/jobs/france/application-security/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Application security
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Offres individuelles et volumes AppSec
- **RESULTAT :** Pages de liste remontées sans compteur ni offre individuelle exploitable dans les extraits
- **DONNEES_MANQUANTES :** Volumes AppSec, offres individuelles
- **AUTRES_CHEMINS_TESTES :** Requête AppSec France
- **SOURCE_DE_REMPLACEMENT :** Indeed (compteurs datés Application Security Engineer), WTTJ (offres AppSec nommées)
- **IMPACT_SUR_L_ANALYSE :** Faible

### ChooseYourBoss, LesJeudis, Stage.fr, Jobijoba, Freelance-Informatique, Cyberfreelance

- **URL :** https://www.chooseyourboss.com/ ; https://lesjeudis.com/ ; https://www.stage.fr/ ; https://www.jobijoba.com/ ; https://www.freelance-informatique.fr/ ; https://www.cyberfreelance.fr/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Cybersécurité (générique), alternance, freelance
- **ZONES_TESTEES :** France, Bouches-du-Rhône, Île-de-France
- **DONNEES_RECHERCHEES :** Offres individuelles et compteurs datés
- **RESULTAT :** Uniquement des pages de liste ou des pages métiers ; aucun compteur daté ni offre individuelle exploitable
- **DONNEES_MANQUANTES :** Volumes datés, offres individuelles
- **AUTRES_CHEMINS_TESTES :** Requêtes site: et requêtes par métier + zone
- **SOURCE_DE_REMPLACEMENT :** Indeed, France Travail, HelloWork, WTTJ, Free-Work
- **IMPACT_SUR_L_ANALYSE :** Faible : plateformes secondaires largement redondantes

### Données ANSSI / cyber.gouv.fr (rapports en PDF)

- **URL :** https://cyber.gouv.fr/
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Ensemble du périmètre
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Chiffres détaillés de l'Observatoire des métiers 2025 (répartition par métier, par région, par séniorité)
- **RESULTAT :** Domaine bloqué par le proxy (EGRESS_BLOCKED) ; seules les données reprises dans les pages indexées et la presse ont pu être exploitées
- **DONNEES_MANQUANTES :** Tableaux détaillés de l'Observatoire (ventilation fine par métier, région, contrat, expérience)
- **AUTRES_CHEMINS_TESTES :** WebFetch sur cyber.gouv.fr, recherches ciblées sur les chiffres de l'observatoire
- **SOURCE_DE_REMPLACEMENT :** Reprises documentées des chiffres clés (23 000 offres, +49 %, 21 % architectes, 15 % consultants, 15 % ingénieurs, 47 % Bac+5) par plusieurs sources secondaires convergentes
- **IMPACT_SUR_L_ANALYSE :** Modéré : la structure fine du corpus ANSSI n'a pas pu être reprise ; seuls les grands agrégats sont utilisés

### Navigation par navigateur réel (Chromium / Playwright) — Indeed, HelloWork, France Travail

- **URL :** https://fr.indeed.com/q-analyste-soc-emplois.html ; https://www.hellowork.com/fr-fr/emploi/recherche.html?k=cybersecurite&l=France ; https://candidat.francetravail.fr/offres/recherche?motsCles=cybersecurite
- **DATE_DU_TEST :** 2026-09-08
- **METIERS_TESTES :** Analyste SOC et cybersécurité (requêtes de test) ; objectif = compteurs par métier via les filtres des sites
- **ZONES_TESTEES :** France, Île-de-France
- **DONNEES_RECHERCHEES :** Nombre d'offres affiché par les moteurs de recherche internes des sites, en appliquant les filtres métier, contrat, expérience et localisation
- **RESULTAT :** Échec sur les trois cibles, avec et sans le proxy de session : net::ERR_TUNNEL_CONNECTION_FAILED. Chromium (build 1194 préinstallé) démarre correctement, la page ne se charge jamais. En parallèle, une requête HTTP directe hors proxy sur fr.indeed.com renvoie « HTTP/2 403, x-deny-reason: host_not_allowed » : c'est la passerelle réseau qui refuse, pas le site. Le statut du proxy enregistre pour chaque hôte « gateway answered 403 to CONNECT (policy denial) ». Les moteurs de recherche généralistes (google.com, duckduckgo.com) sont eux aussi refusés ; seul github.com est joignable.
- **DONNEES_MANQUANTES :** Compteurs en direct par filtre (contrat, expérience, date de publication, rayon géographique), qui auraient permis des relevés simultanés et donc de vraies séries comparables
- **AUTRES_CHEMINS_TESTES :** Chromium via HTTPS_PROXY ; Chromium en connexion directe ; curl via proxy ; curl --noproxy avec User-Agent navigateur ; vérification DNS (la résolution fonctionne, l'interception est au niveau de la passerelle) ; consultation du statut du proxy agent
- **SOURCE_DE_REMPLACEMENT :** Relevé systématique des compteurs figurant dans les TITRES des pages de résultats filtrées, telles qu'indexées par un moteur de recherche (« X emplois (date) »). 223 relevés obtenus sur 138 requêtes distinctes et 15 zones, dont des points de 2024 et 2025.
- **IMPACT_SUR_L_ANALYSE :** La couverture ville × métier est bonne (voir §5.1 bis du document de synthèse). En revanche, faute de relevés simultanés maîtrisés, aucune série d'évolution n'est calculable : la vérification montre que deux formes d'URL d'une même requête donnent des comptes différant d'un facteur 4 à 16, et qu'aucune des 223 mesures ne constitue une série sur une URL strictement identique à deux dates. Les compteurs ne servent donc qu'à comparer des domaines entre eux à une date donnée.

### Plateformes ayant effectivement fourni des données

| Plateforme | Offres individuelles retenues | Relevés de stocks datés |
|---|---|---:|
| Apec | 2 | 0 |
| France Travail | 48 | 0 |
| Free-Work | 19 | 0 |
| Glassdoor | 0 | 8 |
| HelloWork | 56 | 0 |
| Indeed | 152 | 215 |
| Jooble | 1 | 0 |
| LinkedIn | 8 | 0 |
| Meteojob | 1 | 0 |
| Talent.com | 1 | 0 |
| Welcome to the Jungle | 60 | 0 |

### Conséquence méthodologique

L'accès direct aux pages (WebFetch et requêtes HTTP) étant bloqué par le proxy de la session, **toutes les données proviennent des titres, URL et extraits renvoyés par un moteur de recherche sur des pages publiques indexées**. Il en découle trois limites que le document de synthèse rappelle explicitement :

1. **Champs incomplets.** Le salaire n'est renseigné que dans 3 offres sur 342, l'expérience dans une minorité d'offres, les certifications dans 4 offres. Ces taux sont des **bornes basses** liées à la troncature des extraits, et non des mesures du marché.
2. **Volumes = stocks indexés à des dates hétérogènes.** Les compteurs relevés (« plus de N emplois (date) ») sont des comptes de pertinence par mots-clés, sur des requêtes larges qui se recouvrent. Ils ne doivent jamais être additionnés ni lus comme un nombre d'emplois disponibles ; ils ne valent qu'en **comparaison relative** entre métiers et entre zones.
3. **Pas de séries temporelles complètes.** Sauf exception (un point Sophia Antipolis de novembre 2025), nous ne disposons pas de relevés 2024 et 2025 comparables pour la même requête. **Aucune évolution annuelle n'est donc calculée à partir de nos propres relevés** : les colonnes EVOLUTION_2025 et EVOLUTION_2024 sont à « NC (séries insuffisantes) ». Les tendances pluriannuelles utilisées dans la synthèse proviennent exclusivement de sources publiées (Observatoire ANSSI : +49 % d'offres entre 2019 et 2024 ; Apec ; Numeum ; BMO).

*Fichier généré le 8 septembre 2026 par `scripts_cyber/build_md.py`.*