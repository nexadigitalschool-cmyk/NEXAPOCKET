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
