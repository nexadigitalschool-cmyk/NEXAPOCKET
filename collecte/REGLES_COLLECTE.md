# RÈGLES DE COLLECTE (à respecter strictement)

Contexte : étude du marché de l'emploi du développement web en France pour NEXA Digital School. Date de collecte : 2026-09-06.
Contrainte technique : SEUL l'outil WebSearch fonctionne. WebFetch et curl sont bloqués par le proxy (ne pas réessayer, ne pas perdre de temps). Toute donnée vient donc des titres, URL et extraits renvoyés par WebSearch (pages publiques indexées).

## Interdictions absolues
- Ne JAMAIS inventer une offre, une entreprise, un salaire, une expérience, une date, un chiffre ou une URL.
- Ne JAMAIS compléter un champ par déduction du titre : si l'extrait ne le dit pas, mettre "NC".
- Ne pas collecter de noms de personnes (recruteurs). Nom d'entreprise et cabinet : oui.
- Une offre = une URL de page d'offre individuelle (pas une page de liste). Les pages de liste servent uniquement aux VOLUMES (voir plus bas).

## Fichier de sortie : JSON Lines (une offre par ligne), UTF-8
Champs (tous obligatoires, "NC" si inconnu) :
ID_OFFRE (préfixe agent + numéro, ex "P-001"), SOURCE (Indeed / France Travail / Apec / Welcome to the Jungle / HelloWork / LinkedIn / Free-Work / Jooble / Talent.com / Meteojob / Monster / JobTeaser / LesJeudis / ChooseYourBoss / Site carrière / Autre), URL, DATE_PUBLICATION (AAAA-MM-JJ ou "2026-MM" ou NC), DATE_COLLECTE ("2026-09-06"), ENTREPRISE, CABINET_OU_INTERMEDIAIRE (nom ou "Non" ou NC), INTITULE_BRUT (titre exact), REGION (région administrative), DEPARTEMENT (numéro ou NC), VILLE, TELETRAVAIL (Oui/Partiel/Non/NC + précision si donnée), TYPE_CONTRAT (CDI/CDD/ALTERNANCE/STAGE/FREELANCE/INTERIM/MISSION_COURTE/AUTRE/NC), DUREE, TEMPS_PLEIN_OU_PARTIEL, SALAIRE_MINIMUM (nombre annuel brut € ou TJM avec unité, ou NC), SALAIRE_MAXIMUM, EXPERIENCE (texte tel qu'indiqué, ex "3 ans" ou "débutant accepté"), DIPLOME, LANGAGES, FRAMEWORKS, BASES_DE_DONNEES, CLOUD, DEVOPS, TEST, CYBERSECURITE, ARCHITECTURE, METHODES_PROJET, COMPETENCES_IA (mentions explicites : Copilot, Cursor, Claude Code, ChatGPT, LLM, RAG, agents IA, MCP, prompt engineering, IA générative... sinon "Aucune mention dans l'extrait"), SOFT_SKILLS, ANGLAIS, SECTEUR_ENTREPRISE, DESCRIPTION_SYNTHETIQUE (1-2 phrases reprenant l'extrait), PREUVE (copie textuelle de l'extrait ou du titre renvoyé par WebSearch qui justifie les champs remplis), REQUETE (la requête WebSearch exacte qui a fait remonter l'offre).

Tous les champs techniques (LANGAGES...) : lister ce qui est cité dans le titre ou l'extrait, séparés par " ; ". Sinon "NC".

## Fichier VOLUMES : JSON Lines séparé
Quand un titre ou extrait donne un COMPTE d'offres (ex : "Développeur Full Stack, Lyon (69) : plus de 75 emplois (11 août 2026) | Indeed", "Plus de 450 Offres - 6 août 2026 | Hellowork", "1 234 offres"), enregistrer une ligne :
{SOURCE, URL, INTITULE_RECHERCHE, ZONE, TYPE_CONTRAT (si la page est filtrée), NOMBRE (tel qu'affiché, ex "plus de 75"), DATE_DU_COMPTE (date figurant dans le titre/extrait), PREUVE, REQUETE}
Ces comptes sont des STOCKS d'offres actives à une date ; ils sont précieux. En collecter le plus possible, y compris à des dates différentes de 2024, 2025 et 2026 pour la même page (les moteurs indexent plusieurs versions ; varier les requêtes avec "2024", "2025", "janvier 2026", etc.).

## Fichier PLATEFORMES_SANS_DONNEES : JSON Lines
Pour chaque plateforme testée sans résultat exploitable : {PLATEFORME, URL, DATE_DU_TEST, METIERS_TESTES, ZONES_TESTEES, DONNEES_RECHERCHEES, RESULTAT, DONNEES_MANQUANTES, AUTRES_CHEMINS_TESTES, SOURCE_DE_REMPLACEMENT, IMPACT_SUR_L_ANALYSE}

## Fichier JOURNAL : liste de toutes les requêtes WebSearch lancées (une par ligne) avec le nombre d'offres individuelles obtenues.

## Méthode
- Utiliser des requêtes "site:" : site:fr.indeed.com/viewjob, site:candidat.francetravail.fr/offres/recherche/detail, site:apec.fr detail-offre, site:welcometothejungle.com/fr/companies, site:hellowork.com/fr-fr/emplois, site:fr.linkedin.com/jobs/view, site:free-work.com, site:jobteaser.com, site:lesjeudis.com, site:chooseyourboss.com, site:meteojob.com, site:fr.talent.com, site:fr.jooble.org, site:monster.fr.
- Varier intitulés FR/EN, technologies (React, Angular, Vue, Node, PHP, Symfony, Laravel, Java, Spring, .NET, Python, Django, WordPress, Shopify, PrestaShop, Magento, TypeScript), contrat (CDI, CDD, alternance, stage, freelance), séniorité (junior, débutant, senior, lead), ville.
- Exclure les faux positifs : webmarketing, webdesigner sans développement, content manager, chef de projet digital sans code, SEO, data analyst.
- Objectif : le PLUS GRAND nombre d'offres individuelles réelles, sans jamais inventer. Faire au minimum 60 requêtes WebSearch. Continuer tant que de nouvelles offres apparaissent.
- Ne pas dupliquer une même URL dans le fichier.
