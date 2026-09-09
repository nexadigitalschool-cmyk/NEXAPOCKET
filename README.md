# Observatoire du marché de l'emploi du développement web en France — NEXA Digital School

Collecte arrêtée au 6 septembre 2026, analyse finalisée le 9 septembre 2026, pour aider NEXA à décider de l'avenir de sa filière Développement Web (Bachelor à Mastère).

Échantillon : 3 465 lignes d'offres collectées sur 17 plateformes en cinq vagues (A à E), 2 972 offres uniques après dédoublonnage (2 953 dans le périmètre), 1 259 séries de stocks d'offres datés (2024-2026), près de 500 sources documentaires citées avec leur URL (Apec, France Travail BMO et Data Emploi, Dares, Insee, Numeum, OPIIEC, Indeed Hiring Lab, HelloWork, cabinets, études internationales).

Conclusion : la filière doit être TRANSFORMÉE (full stack industrialisé, IA intégrée comme compétence transversale) et RENFORCÉE EN MASTÈRE (architecture, cloud/DevOps, IA applicative, sécurité applicative), avec l'alternance comme canal principal d'insertion.

## Livrables

| Fichier | Contenu |
|---|---|
| `NEXA_Marche_Emploi_Developpement_Web_France_2026.xlsx` | 5 onglets : SYNTHESE_METIERS (une ligne par métier, mini-vue nationale, séries de stocks, études, graphiques), REGIONS_METIERS (région × métier, matrice et carte thermique, population active et ratio pour 100 000 actifs, données externes, stocks régionaux), VILLES_NEXA (ville × métier, comparatif des six campus et du distanciel), COMPETENCES_ET_IA (compétences, bloc développeur augmenté, référentiel cible, études), OFFRES_DETAILLEES (une ligne par offre avec URL, source, statut de doublon, champs observés et normalisés) |
| `NEXA_Synthese_Marche_Emploi_Developpement_Web_2026.docx` | Synthèse pour la Direction Générale, Marketing et Pédagogique : conclusion, marché, évolution, métiers, régions, villes NEXA, contrats et séniorité, salaires, compétences, IA, développeur augmenté, implications pédagogiques, scénarios A/B/C, recommandation, hypothèses H1-H10, sources cliquables |
| `NEXA_Perimetre_Metiers_et_Plateformes_Sans_Donnees.md` | Journal séparé : taxonomie complète des métiers (variantes, technologies, famille, inclusion, requêtes) et plateformes sans données, journaux de requêtes par vague |

## Données et reproductibilité

- `collecte/` : données brutes (JSON Lines) — `offres/` et `etudes/` (session initiale), `A_*`, `B_*`, `C_*` (sessions parallèles initiales), `D1_*` à `D7_*` (agents de la session principale), `E1_*` à `E5_*` (sessions distantes indépendantes : France Travail/Apec, HelloWork, Indeed, WTTJ/LinkedIn/Free-Work, études), journaux de requêtes, plateformes sans données, `REGLES_COLLECTE.md` et `D_CONSIGNES.md` (règles et consignes de collecte), `urls_existantes.txt` (anti-doublons).
- `scripts/` : pipeline Python (`consolide.py` → `build_excel.py`, `build_docx.py`, `build_md.py`) ; `normalize.py` contient la taxonomie, les règles de normalisation (métier, région, contrat, séniorité, salaire) et le dictionnaire de compétences ; `analysis.py` les agrégats, les séries de stocks et le chargement des études.

```bash
pip install openpyxl python-docx
cd scripts && python3 consolide.py && python3 build_excel.py && python3 build_docx.py && python3 build_md.py
```

## Limites

Aucun accès HTTP direct aux sites (proxy) ni à l'API France Travail : toutes les données proviennent des pages publiques indexées par un moteur de recherche (titres, URL, extraits) et d'études publiées, avec un plafond de 200 requêtes par session (d'où les cinq vagues). Les champs absents des extraits sont notés NC (contrat renseigné pour 58 % des offres uniques, expérience ou contrat stage/alternance pour 44 %, salaire pour 12 %) ; les comptes d'offres sont des bornes basses arrondies ; les évolutions et le ratio pour 100 000 actifs sont marqués ESTIMATION. Voir le fichier Markdown pour le journal complet.
