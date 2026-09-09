# Observatoire du marché de l'emploi du développement web en France — NEXA Digital School

Étude réalisée le 6 septembre 2026 pour aider NEXA à décider de l'avenir de sa filière Développement Web (Bachelor à Mastère).

Échantillon : 1 687 lignes d'offres collectées sur 16 plateformes, 1 431 offres uniques après dédoublonnage (1 421 dans le périmètre), 683 séries de stocks d'offres datés (2024-2026), plus de 300 sources documentaires (Apec, France Travail BMO, Dares, Insee, Numeum, Indeed Hiring Lab, jobboards, cabinets).

Conclusion : la filière doit être TRANSFORMÉE (full stack industrialisé, IA intégrée comme compétence transversale) et RENFORCÉE EN MASTÈRE (architecture, cloud/DevOps, IA applicative, sécurité applicative).

## Livrables

| Fichier | Contenu |
|---|---|
| `NEXA_Marche_Emploi_Developpement_Web_France_2026.xlsx` | 5 onglets : SYNTHESE_METIERS, REGIONS_METIERS, VILLES_NEXA, COMPETENCES_ET_IA, OFFRES_DETAILLEES (tableaux filtrables, graphiques, séries de stocks datées, données externes avec URL) |
| `NEXA_Synthese_Marche_Emploi_Developpement_Web_2026.docx` | Synthèse pour la Direction Générale, Marketing et Pédagogique : conclusion, marché, régions, villes NEXA, contrats, salaires, compétences, IA, hypothèses H1-H10, scénarios A/B/C, recommandation, sources cliquables |
| `NEXA_Perimetre_Metiers_et_Plateformes_Sans_Donnees.md` | Journal séparé : taxonomie complète des métiers (variantes, technologies, famille, inclusion, requêtes) et plateformes sans données |

## Données et reproductibilité

- `collecte/` : données brutes collectées (JSON Lines) — `offres/` et `etudes/` (agents de la session principale), `A_*`, `B_*`, `C_*` (trois sessions de collecte complémentaires : offres, volumes, compétences, IA, régions), journaux de requêtes, plateformes sans données, règles de collecte.
- `scripts/` : pipeline Python (`consolide.py` → `build_excel.py`, `build_docx.py`, `build_md.py`) ; `normalize.py` contient la taxonomie, les règles de normalisation (métier, région, contrat, séniorité, salaire) et le dictionnaire de compétences ; `analysis.py` les agrégats.

```bash
pip install openpyxl python-docx
cd scripts && python3 consolide.py && python3 build_excel.py && python3 build_docx.py && python3 build_md.py
```

## Limites

Aucun accès HTTP direct aux sites (proxy) ni à l'API France Travail : toutes les données proviennent des pages publiques indexées par un moteur de recherche (titres, URL, extraits) et d'études publiées. Les champs absents des extraits sont notés NC ; les comptes d'offres sont des bornes basses arrondies ; les évolutions qui en découlent sont marquées ESTIMATION. Voir le fichier Markdown pour le journal complet.

---

# Observatoire du marché de l'emploi de la cybersécurité en France — NEXA Digital School

Étude réalisée le 8 septembre 2026 pour aider NEXA à décider de l'avenir de sa filière Cybersécurité (Bachelor à Mastère).

Échantillon : 348 lignes d'offres collectées sur 10 plateformes, 345 offres uniques après dédoublonnage (342 dans le périmètre cyber), 223 relevés de stocks d'offres datés (mai 2024 – septembre 2026, 138 requêtes distinctes, 15 zones), 35 sources documentaires (ANSSI, OPIIEC, Apec, France Travail BMO, Dares, Numeum, Wavestone, ISC2, ENISA, Banque de France, baromètres).

Conclusion : **ADOPTER_MODELE_HYBRIDE_SPECIALISE** — filière conservée mais restructurée : Bachelor Cybersecurity Engineering fortement technicisé visant l'alternance, puis Mastère limité à trois spécialisations (Cloud Security & DevSecOps ; SecOps, Detection & Automation ; Cyber GRC, Risques & IAM), avec dépriorisation du pentest, du DFIR et de l'AI Security comme parcours autonomes.

## Livrables

| Fichier | Contenu |
|---|---|
| `NEXA_Marche_Emploi_Cybersecurite_France_2026.xlsx` | 5 onglets : SYNTHESE_METIERS (+ stocks datés, sources, 8 graphiques), REGIONS_METIERS (+ matrice régions × familles), VILLES_NEXA (+ synthèse comparative des campus), COMPETENCES_TECH_CERTIFS_IA, OFFRES_DETAILLEES (+ journal des plateformes sans données) |
| `NEXA_Synthese_Marche_Emploi_Cybersecurite_2026.docx` | 18 sections : conclusion en une phrase, marché national, tension vs accessibilité junior, métiers, régions, villes NEXA, contrats et alternance, compétences et certifications, analyse des 10 domaines, IA, Bachelor/Mastère, campus, hypothèses H1-H30, 4 scénarios, matrice d'arbitrage, recommandation, réponses aux 50 questions, sources cliquables, encadré de décision |
| `NEXA_Perimetre_Metiers_Cybersecurite_et_Plateformes_Sans_Donnees.md` | Journal séparé : taxonomie complète (18 familles, 25 fiches métiers avec variantes FR/EN, compétences, outils, certifications, requêtes) et 12 plateformes ou voies d'accès sans données exploitables, dont la navigation par navigateur réel |

## Données et reproductibilité

- `collecte_cyber/` : données brutes (JSON Lines) — `offres.jsonl`, `volumes.jsonl` (stocks datés), `etudes.jsonl`, `sans_donnees.jsonl`, `consolide.json`.
- `scripts_cyber/` : pipeline Python — `normalize.py` (taxonomie, classification, dictionnaire de compétences, régions, séniorité, technicité), `referentiel.py` (tension, accessibilité junior, exposition à l'automatisation et qualité du débouché, justifiées métier par métier), `consolide.py`, puis `build_excel.py`, `build_docx.py`, `build_md.py`.

```bash
pip install openpyxl python-docx
cd scripts_cyber && python3 consolide.py && python3 build_excel.py && python3 build_docx.py && python3 build_md.py
```

## Limites

Aucun accès HTTP direct aux sites ni aux PDF des rapports (proxy) : toutes les données proviennent des titres, URL et extraits de pages publiques indexées par un moteur de recherche. L'objectif indicatif de 500 à 1 000 offres uniques n'a donc pas été atteint (342 retenues dans le périmètre). Les volumes sont des stocks indexés à des dates hétérogènes, non additionnables ; aucune évolution annuelle n'est calculée à partir de nos propres relevés (séries insuffisantes). Aucune donnée interne NEXA n'était disponible : la recommandation porte sur le marché de l'emploi, pas sur l'économie de la filière. Voir le fichier Markdown pour le journal complet.
