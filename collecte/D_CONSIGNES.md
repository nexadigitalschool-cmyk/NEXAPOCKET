# CONSIGNES COMMUNES — VAGUES DE COLLECTE D et E (2026-09-06)

Tu participes à une étude du marché de l'emploi du développement web en France pour NEXA Digital School.
Lis d'abord collecte/REGLES_COLLECTE.md (à la racine du dépôt NEXAPOCKET) (schéma des fichiers et règles) : il s'applique intégralement.

## Contrainte technique (vérifiée aujourd'hui, ne pas re-tester)
- SEUL l'outil WebSearch fonctionne. WebFetch, curl, requests, wget : tous bloqués par le proxy (EGRESS_BLOCKED / 403). Ne perds aucune requête à les essayer.
- Toute donnée provient donc des titres, URL et extraits renvoyés par WebSearch. Si un champ n'est pas dans l'extrait : "NC". Ne JAMAIS déduire ni inventer.
- Budget : le quota est de 200 requêtes WebSearch PAR SESSION (partagé entre tous les agents de la session : ne lance donc PAS de sous-agents). Fais au moins 150 requêtes, jusqu'à 190. Écris tes fichiers au fur et à mesure (toutes les 20 requêtes environ, en mode ajout), pour ne rien perdre.

## Anti-doublons
- Le fichier collecte/urls_existantes.txt contient les URL d'offres déjà collectées (vagues A à D). Avant d'ajouter une offre, vérifie (grep -F de l'URL) qu'elle n'y figure pas. Si elle y est, ne la ré-enregistre PAS (sauf si ton extrait apporte un champ nouveau : expérience, salaire, contrat, télétravail — dans ce cas enregistre-la avec le champ "ENRICHISSEMENT": "Oui" et l'URL identique ; elle sera fusionnée).
- Une même URL ne doit apparaître qu'une fois dans ton fichier.

## Fichiers de sortie (dans collecte/ à la racine du dépôt), préfixe = ton code agent (E1, E2, ...)
- <PREFIXE>_offres.jsonl : une offre par ligne, schéma de REGLES_COLLECTE.md (+ champ "ENRICHISSEMENT" optionnel). ID_OFFRE = "<PREFIXE>-001", etc.
- <PREFIXE>_volumes.jsonl : comptes d'offres datés (schéma REGLES_COLLECTE.md). Très précieux quand la même page (même intitulé × même zone × même source) est vue à des dates différentes (2024, 2025, 2026) : cherche activement ces versions datées.
- <PREFIXE>_plateformes_sans_donnees.jsonl : schéma REGLES_COLLECTE.md.
- <PREFIXE>_journal.txt : une ligne par requête WebSearch : `<requête>\t=> <n offres> (+<n volumes>)`.
- Pour les agents "études" : <PREFIXE>_etudes.jsonl (schéma indiqué dans ton brief).

## Rappels de qualité
- INTITULE_BRUT = titre exact de l'offre tel qu'affiché (sans le suffixe " - Ville - Indeed.com").
- PREUVE = copie textuelle du titre/extrait qui justifie les champs (obligatoire).
- EXPERIENCE : texte exact ("Débutant accepté", "3 ans", "Minimum 5 ans", "Expérience exigée de 2 An(s)"...).
- SALAIRE : tel qu'affiché ("35 000 - 45 000 € par an", "De 40 000 à 50 000 EUR par an", "2 200 € par mois", "TJM 500 €").
- Faux positifs à exclure : webmarketing, webdesigner sans code, content manager, chef de projet sans code, SEO, data analyst.
- Ne collecte pas de noms de personnes (recruteurs).
- À la fin, rends un rapport court : nombre de requêtes, d'offres, de volumes, ce qui a été trouvé/pas trouvé, et 5 observations qualitatives (séniorité, contrats, salaires, IA, régions).

## Git (sessions de collecte E)
- Travaille sur la branche indiquée dans ton brief (`git checkout -b <branche>` depuis la branche de départ). N'y modifie QUE tes fichiers collecte/<PREFIXE>_*.
- Toutes les 40 requêtes environ, puis à la fin : `git add collecte/<PREFIXE>_* && git commit -m "Collecte <PREFIXE> : ..." && git push -u origin <branche>` (retente le push en cas d'erreur réseau : 2 s, 4 s, 8 s, 16 s).
- Ne touche pas aux livrables (.xlsx, .docx, .md) ni aux scripts.
