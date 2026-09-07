# Observatoires du marché de l'emploi — NEXA Digital School

Ce dépôt regroupe les études de marché de l'emploi réalisées pour aider NEXA Digital School à arbitrer l'avenir de ses filières (Bachelor à Mastère).

---

## 1. Filière Développement Web — étude du 6 septembre 2026

Échantillon : 1 687 lignes d'offres collectées sur 16 plateformes, 1 431 offres uniques après dédoublonnage (1 421 dans le périmètre), 683 séries de stocks d'offres datés (2024-2026), plus de 300 sources documentaires.

**Conclusion : la filière doit être TRANSFORMÉE** (full stack industrialisé, IA intégrée comme compétence transversale) **et RENFORCÉE EN MASTÈRE** (architecture, cloud/DevOps, IA applicative, sécurité applicative).

| Fichier | Contenu |
|---|---|
| `NEXA_Marche_Emploi_Developpement_Web_France_2026.xlsx` | 5 onglets : SYNTHESE_METIERS, REGIONS_METIERS, VILLES_NEXA, COMPETENCES_ET_IA, OFFRES_DETAILLEES |
| `NEXA_Synthese_Marche_Emploi_Developpement_Web_2026.docx` | Synthèse Direction Générale / Marketing / Pédagogique |
| `NEXA_Perimetre_Metiers_et_Plateformes_Sans_Donnees.md` | Taxonomie des métiers et plateformes sans données |

Données : `collecte/` · Scripts : `scripts/`

---

## 2. Filière Marketing Digital — étude du 7 septembre 2026

Échantillon : **507 offres collectées** sur 4 plateformes (Indeed, Welcome to the Jungle, HelloWork, France Travail), **504 offres uniques** après dédoublonnage, dont **495 dans le périmètre marketing digital** (446 hors métiers adjacents), **90 stocks d'offres datés** relevés sur les jobboards, **38 sources documentaires** (Apec, France Travail/BMO, Dares, Fevad, SRI-UDECAM-Oliver Wyman, Alliance Digitale/EY, observatoires salariaux).

**Conclusion : ADOPTER UN MODÈLE HYBRIDE SPÉCIALISÉ.** Conserver en Bachelor un socle généraliste mais réellement technicisé — c'est lui qui capte l'alternance et l'accès junior — et transformer le Mastère en deux spécialisations techniques (Marketing Performance & Growth ; CRM, Data & Marketing Automation), en supprimant le parcours Social Media / Community Management autonome et en traitant l'IA comme une couche de compétences obligatoire et transversale, jamais comme un parcours dédié.

### Résultats structurants

- **Le marché croît mais se polarise.** Filière à 14,4 Md€ et ~310 000 emplois, croissance 5× supérieure au PIB (Alliance Digitale/EY) ; publicité digitale +11 % en 2025 et +12 % au S1 2026 ; e-commerce +7 % de CA et +9 % d'emplois.
- **Le marché est majoritairement spécialisé** : 51,9 % des offres du périmètre relèvent des familles spécialisées contre 22,4 % pour le cœur généraliste.
- **Mais les débouchés d'entrée sont dans le généraliste** : 40,5 % d'alternance et 47,7 % de débutants/juniors, contre 0 % d'alternance en MarTech, Product Marketing et métiers IA émergents, et 3,2 % en data marketing. C'est la tension centrale que NEXA doit arbitrer.
- **La technicité commande tout** : de 1,03 (social media) à 2,82 (MarTech), corrélée aux salaires (facteur 3 entre exécution généraliste et expertise senior) et inversement corrélée à l'accès junior.
- **Le « marketeur augmenté par l'IA » n'est pas encore un marché** : 2,4 % des offres mentionnent explicitement l'IA — un chiffre qui converge avec la mesure indépendante de l'Apec (2 % des offres commercial-marketing). Les postes d'orchestration d'agents IA sont aujourd'hui captés par des profils tech, pas par des marketeurs.
- **Matrice d'arbitrage pondérée** : HYBRIDE SPÉCIALISÉE 87 % · TECHNIQUE 68 % · GÉNÉRALISTE 57 % · RÉDUCTION/FUSION/FERMETURE 5 %.

| Fichier | Contenu |
|---|---|
| `NEXA_Marche_Emploi_Marketing_Digital_France_2026.xlsx` | 5 onglets : SYNTHESE_METIERS (+ stocks datés et sources), REGIONS_METIERS, VILLES_NEXA, COMPETENCES_TECH_IA, OFFRES_DETAILLEES — tableaux filtrables, 5 graphiques, matrice régions × familles |
| `NEXA_Synthese_Marche_Emploi_Marketing_Digital_2026.docx` | Synthèse Direction Générale / Marketing / Pédagogique : marché, évolution, métiers, généralistes vs spécialistes, régions, campus, contrats, alternance, salaires, compétences, technicité, IA, hypothèses H1-H18, implications Bachelor/Mastère, 4 scénarios, matrice d'arbitrage, recommandation, sources cliquables, encadré de décision |
| `NEXA_Perimetre_Metiers_Marketing_et_Plateformes_Sans_Donnees.md` | Journal séparé : taxonomie complète (familles, fiches métiers, variantes, outils, requêtes), métiers non observés, faux positifs exclus, plateformes sans données, comptes de volumes écartés |

Données : `collecte_mkt/` · Scripts : `scripts_mkt/`

```bash
pip install openpyxl python-docx
cd scripts_mkt && python3 consolide_mkt.py && python3 build_excel_mkt.py && python3 build_docx_mkt.py && python3 build_md_mkt.py
```

- `normalize_mkt.py` : taxonomie (64 règles ordonnées), normalisation métier/famille/contrat/séniorité/salaire/région, dictionnaire de compétences (10 familles), échelle de technicité 1-4.
- `analyse_mkt.py` : indicateurs de tension et de qualité du débouché, tests des hypothèses H1-H18, quatre scénarios, matrice d'arbitrage pondérée.

---

## Limites communes aux deux études

Aucun accès HTTP direct aux sites (bloqué par le proxy) ni aux API France Travail ou Apec : **toutes les données proviennent des titres, URL et extraits de pages publiques indexées par un moteur de recherche**, et d'études publiées. Trois conséquences, signalées partout où elles s'appliquent :

1. Les champs absents des extraits sont notés `NC` et n'ont **jamais** été déduits (30,1 % de contrats et 52,9 % de séniorités non renseignés sur l'étude Marketing Digital).
2. Les comptes de compétences sont des **bornes basses**.
3. Les **séries historiques annuelles comparables n'ont pas pu être reconstituées** par métier : toutes les affirmations d'évolution s'appuient sur des études publiées, jamais sur les échantillons d'offres.

Les comptes de jobboards sont des **stocks d'offres actives à une date donnée**, non dédoublonnés entre plateformes : ils donnent un ordre de grandeur, jamais un nombre d'emplois. Les estimations sont marquées `ESTIMATION` et leur mode de calcul est documenté. Aucune offre, aucun volume, aucune évolution et aucune URL n'a été inventé.
