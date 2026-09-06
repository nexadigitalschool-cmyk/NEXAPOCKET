# NEXA — Périmètre des métiers et plateformes sans données

Étude du marché de l'emploi du développement web en France — journal séparé de la collecte. Date de collecte : 2026-09-06. Voir aussi le fichier Excel (onglet OFFRES_DETAILLEES) et le document Word de synthèse.

## Contexte technique de la collecte

- L'environnement d'exécution ne permettait aucun accès HTTP direct aux sites externes (proxy réseau : toutes les connexions vers les jobboards, France Travail, Apec, data.gouv.fr, INSEE, Dares, Numeum, etc. ont été refusées avec un code 403 au niveau du proxy ; l'API France Travail nécessite en outre une clé OAuth non disponible).
- Seule voie disponible : un moteur de recherche web renvoyant, pour chaque requête, les titres, URL et extraits des pages publiques indexées. Toutes les offres et tous les comptes d'offres proviennent donc de ces pages indexées (pages d'offres individuelles et pages de liste datées des jobboards).
- Le budget de requêtes était plafonné (200 requêtes par session) ; la collecte a été répartie sur plusieurs sessions parallèles. Les journaux de requêtes sont conservés (fichiers *_journal.txt du dossier `collecte/`).
- Conséquences : de nombreux champs (expérience, salaire, télétravail) ne figurent pas dans les extraits et sont notés NC ; les comptes d'offres des pages de liste sont des bornes basses arrondies (« plus de N »).

## PARTIE A — TAXONOMIE DES MÉTIERS

Taxonomie initiale du brief complétée par les métiers découverts pendant la collecte. Nombre d'offres = offres uniques observées dans l'échantillon (1895 offres uniques dans le périmètre, 2223 lignes brutes).

### Développeur web

- INTITULE_NORMALISE : Développeur web (intitulé générique)
- VARIANTES_FRANCAISES : Développeur web ; Développeuse web ; Développeur internet ; Développeur d'applications web
- VARIANTES_ANGLAISES : Web Developer ; Web Engineer
- TECHNOLOGIES_ASSOCIEES : HTML/CSS, JavaScript, PHP, frameworks web
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Métier de référence
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulé générique du cœur de marché ; regroupé sous 'Développeur web (intitulé générique)' quand aucune techno ni couche n'est précisée.
- OFFRES_OBSERVEES : 134 unique(s) / 178 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com "Développeur web" Toulouse emplois` ; `site:fr.indeed.com "Développeur web" Occitanie "emplois"` ; `site:fr.indeed.com "Développeur web" Montpellier emplois` ; `site:fr.indeed.com "Développeur web" Rennes emplois` ; `site:fr.indeed.com "Développeur web" Strasbourg emplois` ; `site:fr.indeed.com "Développeur web" Bretagne emplois`

### Développeur front-end

- INTITULE_NORMALISE : Développeur front-end
- VARIANTES_FRANCAISES : Développeur front ; Développeur frontend ; Développeur interface
- VARIANTES_ANGLAISES : Front-End Developer ; Frontend Engineer ; UI Developer (avec code)
- TECHNOLOGIES_ASSOCIEES : JavaScript, TypeScript, React, Angular, Vue.js, Next.js
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Couche présentation des applications web.
- OFFRES_OBSERVEES : 122 unique(s) / 148 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur front-end React Angular Vue Paris` ; `site:welcometothejungle.com/fr/companies développeur front-end Paris` ; `site:candidat.francetravail.fr/offres/recherche/detail développeur front-end Paris` ; `site:apec.fr detail-offre développeur front-end OR back-end Paris` ; `site:welcometothejungle.com/fr/companies développeur front-end React Paris` ; `Indeed "Développeur Full Stack" OR "Développeur Front End" OR "Développeur Back End" France emplois "plus de"`

### Développeur back-end

- INTITULE_NORMALISE : Développeur back-end
- VARIANTES_FRANCAISES : Développeur back ; Développeur backend ; Développeur serveur
- VARIANTES_ANGLAISES : Back-End Developer ; Backend Engineer ; Server-side Developer
- TECHNOLOGIES_ASSOCIEES : Node.js, PHP/Symfony/Laravel, Java/Spring, .NET, Python/Django, SQL
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Couche serveur, API et données des applications web.
- OFFRES_OBSERVEES : 67 unique(s) / 75 brute(s)
- REQUETES_UTILISEES : `site:apec.fr detail-offre développeur front-end OR back-end Paris` ; `Indeed "Développeur Full Stack" OR "Développeur Front End" OR "Développeur Back End" France emplois "plus de"` ; `site:chooseyourboss.com développeur full stack OR front-end OR back-end` ; `site:welcometothejungle.com/fr/companies "Télétravail total" développeur backend OR frontend` ; `Hellowork "Emploi Développeur front end" OR "Emploi Développeur back end" OR "Emploi Développeur PHP" OR "Emploi Développeur React" "Plus de" Offres` ; `site:fr.indeed.com/viewjob développeur back-end Node.js OR Python OR ".NET" Paris CDI`

### Développeur full stack

- INTITULE_NORMALISE : Développeur full stack
- VARIANTES_FRANCAISES : Développeur fullstack ; Développeur full-stack ; Développeur web full stack
- VARIANTES_ANGLAISES : Full Stack Developer ; Full-Stack Engineer
- TECHNOLOGIES_ASSOCIEES : JS/TS + framework back (Node, Symfony, Spring, .NET, Django)
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulé dominant du marché : couvre front et back.
- OFFRES_OBSERVEES : 488 unique(s) / 589 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur full stack Montpellier` ; `site:apec.fr detail-offre développeur full stack Paris` ; `site:welcometothejungle.com/fr/companies développeur full stack Paris CDI` ; `site:fr.indeed.com/viewjob développeur full stack Paris CDI` ; `site:fr.linkedin.com/jobs/view développeur full stack Paris` ; `site:candidat.francetravail.fr/offres/recherche/detail développeur full stack Île-de-France`

### Intégrateur web

- INTITULE_NORMALISE : Intégrateur web
- VARIANTES_FRANCAISES : Intégrateur HTML/CSS ; Intégratrice web ; Développeur intégrateur
- VARIANTES_ANGLAISES : Web Integrator ; HTML/CSS Developer
- TECHNOLOGIES_ASSOCIEES : HTML, CSS, JavaScript, CMS
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Métier d'entrée historique du web ; très peu d'offres observées en 2026.
- OFFRES_OBSERVEES : 17 unique(s) / 18 brute(s)
- REQUETES_UTILISEES : `site:hellowork.com/fr-fr/emplois accessibilité RGAA développeur OR intégrateur` ; `site:welcometothejungle.com/fr/companies "intégrateur web" OR "développeur front-end" Paris CDI` ; `site:fr.indeed.com/viewjob "intégrateur web" OR "intégrateur front" Paris` ; `site:fr.linkedin.com/jobs/view "accessibilité" RGAA développeur OR intégrateur` ; `site:hellowork.com/fr-fr/emplois "Emploi Intégrateur web" "Offres"	=> 4 offres (+0 volumes)` ; `Q036`

### Concepteur développeur d'applications

- INTITULE_NORMALISE : Concepteur développeur d'applications / logiciel
- VARIANTES_FRANCAISES : Concepteur développeur ; Développeur d'applications ; Développeur applicatif ; Développeur informatique
- VARIANTES_ANGLAISES : Application Developer ; Software Developer
- TECHNOLOGIES_ASSOCIEES : Java, .NET, PHP, JavaScript
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulé des titres RNCP et de nombreuses ESN ; inclut le développement d'applications web.
- OFFRES_OBSERVEES : 50 unique(s) / 65 brute(s)
- REQUETES_UTILISEES : `site:hellowork.com/fr-fr/emplois "Emploi Développeur informatique" "Plus de" "Offres" 2024	=> 1 offres (+8 volumes)` ; `Q062` ; `Q067` ; `Q073` ; `Q074` ; `Q076`

### Développeur JavaScript / TypeScript

- INTITULE_NORMALISE : Développeur JavaScript / TypeScript
- VARIANTES_FRANCAISES : Développeur JS ; Développeur TypeScript ; Développeur Node.js ; Développeur React ; Développeur Angular ; Développeur Vue.js
- VARIANTES_ANGLAISES : JavaScript Developer ; TypeScript Developer ; React Developer ; Angular Developer ; Vue Developer ; Node.js Developer
- TECHNOLOGIES_ASSOCIEES : JavaScript, TypeScript, React, Angular, Vue.js, Node.js, Next.js, NestJS
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Regroupe les intitulés par technologie JavaScript (front et back).
- OFFRES_OBSERVEES : 54 unique(s) / 58 brute(s)
- REQUETES_UTILISEES : `site:free-work.com développeur React Paris` ; `site:fr.indeed.com/viewjob développeur front-end React Angular Vue Paris` ; `"Développeur React" OR "Developpeur React" emplois Indeed 2025 "plus de"	=> 0 offres (+7 volumes)` ; `"Développeur Angular" OR "Développeur Vue" emplois Indeed 2024 "offres d'emploi"	=> 0 offres (+2 volumes ; résultats CH/CA/BE ignorés)` ; `"Développeur Node" OR "Developpeur Node Js" emplois Indeed 2025 "plus de"	=> 0 offres (+7 volumes)` ; `site:welcometothejungle.com/fr/companies développeur front-end React Paris`

### Développeur PHP / Symfony / Laravel

- INTITULE_NORMALISE : Développeur PHP / Symfony / Laravel
- VARIANTES_FRANCAISES : Développeur PHP ; Développeur Symfony ; Développeur Laravel
- VARIANTES_ANGLAISES : PHP Developer ; Symfony Developer ; Laravel Developer
- TECHNOLOGIES_ASSOCIEES : PHP, Symfony, Laravel, MySQL
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Écosystème web historique français (ESN, agences, éditeurs).
- OFFRES_OBSERVEES : 59 unique(s) / 75 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur PHP Symfony Paris` ; `"Développeur Symfony" France emplois Indeed "2025"	=> 0 offres (+7 volumes)` ; `"Développeur PHP" "offres d'emploi" Indeed.com 2024 France "plus de"	=> 0 offres (+5 volumes)` ; `site:fr.indeed.com/viewjob développeur Symfony Paris` ; `Hellowork "Emploi Développeur front end" OR "Emploi Développeur back end" OR "Emploi Développeur PHP" OR "Emploi Développeur React" "Plus de" Offres` ; `site:welcometothejungle.com/fr/companies "Télétravail total" développeur Symfony OR Laravel OR PHP OR fullstack`

### Développeur Java / Spring (web)

- INTITULE_NORMALISE : Développeur Java / Spring
- VARIANTES_FRANCAISES : Développeur Java ; Développeur Java web ; Développeur Spring ; Développeur Java/JEE
- VARIANTES_ANGLAISES : Java Developer ; Spring Developer ; Java Backend Engineer
- TECHNOLOGIES_ASSOCIEES : Java, Spring Boot, JEE, Hibernate, Angular/React associés
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Java web (Spring) est un des premiers volumes d'offres ; les offres Java embarqué/mainframe sont exclues.
- OFFRES_OBSERVEES : 85 unique(s) / 92 brute(s)
- REQUETES_UTILISEES : `site:apec.fr detail-offre développeur Java Spring Paris` ; `site:fr.indeed.com/viewjob développeur Java Spring Boot Paris` ; `"Développeur Java" France emplois Indeed 2025 "plus de"	=> 0 offres (+8 volumes)` ; `site:fr.indeed.com/viewjob développeur Java Spring Paris CDI` ; `site:hellowork.com/fr-fr/emplois "Emploi Développeur Java" "Plus de" "Offres"	=> 2 offres (+5 volumes)` ; `site:hellowork.com/fr-fr/emplois "Emploi Développeur javascript" OR "Emploi Développeur React" "Offres"	=> 3 offres (+0 volumes)`

### Développeur .NET / C#

- INTITULE_NORMALISE : Développeur .NET / C#
- VARIANTES_FRANCAISES : Développeur .NET ; Développeur C# ; Développeur ASP.NET
- VARIANTES_ANGLAISES : .NET Developer ; C# Developer
- TECHNOLOGIES_ASSOCIEES : C#, .NET, ASP.NET Core, SQL Server, Angular/React associés
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Stack web Microsoft, fréquente en ESN et éditeurs.
- OFFRES_OBSERVEES : 80 unique(s) / 86 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur .NET C# Paris` ; `"Développeur .NET" OR "Developpeur Net" emplois Indeed 2025 "plus de"	=> 0 offres (+3 volumes ; BE/CA ignorés)` ; `site:welcometothejungle.com/fr/companies développeur ".NET" OR Angular Paris CDI` ; `site:fr.indeed.com/viewjob développeur back-end Node.js OR Python OR ".NET" Paris CDI` ; `site:fr.indeed.com/viewjob développeur ".NET" C# Paris CDI` ; `site:hellowork.com/fr-fr/emplois "Emploi Développeur .Net" OR "Emploi Développeur dotNet" "Plus de" "Offres"	=> 2 offres (+6 volumes)`

### Développeur Python / Django

- INTITULE_NORMALISE : Développeur Python / Django
- VARIANTES_FRANCAISES : Développeur Python ; Développeur Django ; Développeur Flask
- VARIANTES_ANGLAISES : Python Developer ; Django Developer
- TECHNOLOGIES_ASSOCIEES : Python, Django, Flask, FastAPI
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Python web ; attention, beaucoup d'offres 'développeur Python' relèvent de la data (exclues si sans composante web).
- OFFRES_OBSERVEES : 28 unique(s) / 29 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur Python Django Paris` ; `"Développeur Python" "offres d'emploi" Indeed.com 2024 "plus de"	=> 0 offres (+6 volumes)` ; `site:welcometothejungle.com/fr/companies développeur Python Django OR Ruby Paris CDI` ; `site:fr.indeed.com/viewjob développeur back-end Node.js OR Python OR ".NET" Paris CDI` ; `site:fr.indeed.com/viewjob développeur Python Django OR FastAPI OR Flask Paris` ; `site:hellowork.com/fr-fr/emplois "Emploi Développeur Python" "Plus de" "Offres"	=> 2 offres (+5 volumes)`

### Développeur CMS / e-commerce

- INTITULE_NORMALISE : Développeur CMS / e-commerce
- VARIANTES_FRANCAISES : Développeur WordPress ; Développeur Drupal ; Développeur Shopify ; Développeur PrestaShop ; Développeur Magento ; Développeur e-commerce
- VARIANTES_ANGLAISES : WordPress Developer ; Drupal Developer ; Shopify Developer ; Magento Developer ; E-commerce Developer
- TECHNOLOGIES_ASSOCIEES : WordPress, Drupal, Shopify, PrestaShop, Magento/Adobe Commerce, Sylius
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Développement sur CMS et plateformes e-commerce ; volumes faibles dans l'échantillon.
- OFFRES_OBSERVEES : 20 unique(s) / 23 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur WordPress OR Shopify OR PrestaShop OR Magento Paris` ; `"Développeur WordPress" OR "Développeur Shopify" OR "Développeur Prestashop" emplois Indeed 2024 2025	=> 0 offres (+6 volumes)` ; `site:fr.indeed.com/viewjob développeur WordPress OR Shopify OR PrestaShop Paris` ; `site:fr.indeed.com/viewjob développeur Shopify OR WordPress OR PrestaShop Toulouse OR Rennes OR Montpellier OR Strasbourg OR Nantes` ; `Q012` ; `Q016`

### Développeur Ruby on Rails

- INTITULE_NORMALISE : Développeur Ruby on Rails
- VARIANTES_FRANCAISES : Développeur Ruby ; Développeur Rails
- VARIANTES_ANGLAISES : Ruby on Rails Developer
- TECHNOLOGIES_ASSOCIEES : Ruby, Rails
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Découvert pendant la collecte (Paris) ; ajouté au cœur de marché.
- OFFRES_OBSERVEES : 1 unique(s) / 1 brute(s)
- REQUETES_UTILISEES : `site:welcometothejungle.com/fr/companies développeur Python Django OR Ruby Paris CDI`

### Développeur logiciel (autre langage web/back)

- INTITULE_NORMALISE : Développeur logiciel (autre langage web/back)
- VARIANTES_FRANCAISES : Développeur Go ; Développeur Rust ; Développeur Scala
- VARIANTES_ANGLAISES : Go Developer ; Rust Developer
- TECHNOLOGIES_ASSOCIEES : Go, Rust, Scala, Elixir
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Langages back modernes utilisés pour des services web ; ajouté à la marge.
- OFFRES_OBSERVEES : 2 unique(s) / 2 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur Python Django Paris` ; `Développeur Web "Provence-Alpes-Côte d'Azur" OR "Bourgogne-Franche-Comté" OR "Centre-Val de Loire" emplois [allowed: fr.indeed.com]	=> 0 offres (+9 volumes)` ; `Hellowork "Emploi Développeur web" Offres "Auvergne-Rhône-Alpes" OR "Provence-Alpes-Côte d'Azur" OR "Bourgogne-Franche-Comté" OR "Île-de-France"` ; `Indeed "Développeur Web" emplois "plus de" "Nouvelle-Aquitaine" OR "Pays de la Loire" OR "Centre-Val de Loire" OR "Bourgogne-Franche-Comté" OR Normandie` ; `site:welcometothejungle.com/fr/companies développeur Python Django OR Ruby Paris CDI` ; `Indeed "Développeur Web" emplois 2025 "plus de" "Pays de la Loire" OR "Nouvelle-Aquitaine" OR "Grand Est" OR Normandie OR "Bourgogne-Franche-Comté"`

### Développeur (intitulé générique)

- INTITULE_NORMALISE : Développeur (intitulé générique)
- VARIANTES_FRANCAISES : Développeur ; Développeuse ; Développeur en alternance
- VARIANTES_ANGLAISES : Developer ; Programmer
- TECHNOLOGIES_ASSOCIEES : Non précisé
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulés sans précision de couche ni de techno ; rattachés au cœur de marché mais à lire avec prudence.
- OFFRES_OBSERVEES : 77 unique(s) / 92 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com "Développeur web" Toulouse emplois` ; `site:fr.indeed.com "Développeur web" Occitanie "emplois"` ; `site:fr.indeed.com "Développeur web" Montpellier emplois` ; `site:fr.indeed.com "Développeur web" Rennes emplois` ; `site:fr.indeed.com "Développeur web" Strasbourg emplois` ; `site:fr.indeed.com "Développeur web" Bretagne emplois`

### Software Engineer / Ingénieur logiciel

- INTITULE_NORMALISE : Software Engineer / Ingénieur logiciel
- VARIANTES_FRANCAISES : Ingénieur logiciel ; Ingénieur développement logiciel ; Ingénieur d'études et développement ; Ingénieur informatique
- VARIANTES_ANGLAISES : Software Engineer ; Software Development Engineer
- TECHNOLOGIES_ASSOCIEES : Tous langages
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Prolongement du développeur web vers l'ingénierie logicielle ; intitulé en progression.
- OFFRES_OBSERVEES : 18 unique(s) / 19 brute(s)
- REQUETES_UTILISEES : `"Développeur Logiciel" OR "Ingénieur Logiciel" OR "Software Engineer" "offres d'emploi" Indeed.com 2024 "plus de"	=> 0 offres (+8 volumes)` ; `site:fr.indeed.com/viewjob "software engineer" OR "architecte logiciel" Paris CDI` ; `Q017` ; `Q042` ; `site:apec.fr detail-offre "Software Engineer" F/H Paris	=> 8 offres (+0 volumes)` ; `site:fr.indeed.com/viewjob "software engineer" OR "tech lead" OR "lead developer" Bordeaux OR Mérignac	=> 6 offre(s) individuelle(s)`

### Application Developer

- INTITULE_NORMALISE : Concepteur développeur d'applications / logiciel
- VARIANTES_FRANCAISES : Développeur d'applications
- VARIANTES_ANGLAISES : Application Developer
- TECHNOLOGIES_ASSOCIEES : Tous langages
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Regroupé avec 'Concepteur développeur d'applications' dans la normalisation.
- OFFRES_OBSERVEES : 50 unique(s) / 65 brute(s)
- REQUETES_UTILISEES : `PRÉVUES ET NON LANCÉES (quota) : salaires 2026 Silkhom / Hays / Robert Half / Michael Page / Urban Linker / Externatic / WeLoveDevs / Glassdoor / Talent.com par métier × séniorité × ville ; IA & développement (Apec cadres et IA 2026 détails, Syntec, France Stratégie, Institut Montaigne, DGE, Bpifrance, Malt ; Stack Overflow Developer Survey 2026, GitHub Octoverse 2025, Stanford/ADP jeunes développeurs) ; référentiels ROME M1805, Onisep développeur web, RNCP développeur web / concepteur développeur d'applications ; Apec baromètre T2 2026 chiffres ; Apec fiches PDF régionales ARA/Bretagne/NA/PDL/HDF/GE/Normandie/BFC (URL corporate.apec.fr/files/.../Nos regions/pdf/) ; Dares tensions 2025 (publication 2026) ; INSEE valeurs population active par région.`

### Product Engineer

- INTITULE_NORMALISE : Product Engineer
- VARIANTES_FRANCAISES : Ingénieur produit
- VARIANTES_ANGLAISES : Product Engineer
- TECHNOLOGIES_ASSOCIEES : JS/TS, produit
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Développeur orienté produit (start-up) ; aucune offre observée dans l'échantillon.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Développeur API / intégration

- INTITULE_NORMALISE : Développeur API / intégration
- VARIANTES_FRANCAISES : Développeur API ; Développeur intégration
- VARIANTES_ANGLAISES : API Developer ; Integration Engineer
- TECHNOLOGIES_ASSOCIEES : REST, GraphQL, microservices
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Spécialisation back sur les API.
- OFFRES_OBSERVEES : 6 unique(s) / 8 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur Python Django OR FastAPI OR Flask Paris` ; `site:welcometothejungle.com/fr/companies "AI Engineer" OR "LLM Engineer" OR "AI Integration Engineer" CDI Paris OR Lyon	=> 1 offres (+0 volumes)` ; `site:fr.indeed.com/viewjob "software engineer" OR "ingénieur logiciel" OR "ingénieur développement" Lyon OR Villeurbanne	=> 4 (+1 enrichie ; systèmes/réseaux et intégration exclus) offre(s) individuelle(s)`

### Développeur mobile

- INTITULE_NORMALISE : Développeur mobile
- VARIANTES_FRANCAISES : Développeur mobile ; Développeur iOS ; Développeur Android ; Développeur Flutter ; Développeur React Native
- VARIANTES_ANGLAISES : Mobile Developer ; iOS/Android Engineer
- TECHNOLOGIES_ASSOCIEES : Swift, Kotlin, Flutter, React Native
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Débouché adjacent naturel des développeurs JS (React Native) ; comptabilisé dans les évolutions, pas dans le cœur.
- OFFRES_OBSERVEES : 65 unique(s) / 74 brute(s)
- REQUETES_UTILISEES : `"Développeur Mobile" OR "Developpeur Mobile" emplois Indeed 2024 2025 "plus de"	=> 0 offres (+6 volumes)` ; `site:fr.indeed.com/viewjob développeur mobile "React Native" OR Flutter Paris` ; `site:fr.indeed.com/viewjob "développeur mobile" OR "React Native" OR Flutter Toulouse OR Rennes OR Grenoble OR Strasbourg OR Nice OR Montpellier` ; `Q019` ; `Q033` ; `Q172`

### Tech Lead / Lead Developer

- INTITULE_NORMALISE : Tech Lead / Lead Developer
- VARIANTES_FRANCAISES : Tech lead ; Lead développeur ; Responsable technique
- VARIANTES_ANGLAISES : Tech Lead ; Lead Developer ; Engineering Manager
- TECHNOLOGIES_ASSOCIEES : Tous
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Évolution à 5+ ans ; cible de la communication Mastère.
- OFFRES_OBSERVEES : 84 unique(s) / 87 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "Tech Lead" développeur web Paris OR Lyon` ; `"Tech Lead" OR "Architecte Logiciel" emplois Indeed 2025 "plus de" France	=> 0 offres (+8 volumes)` ; `site:fr.indeed.com/viewjob "tech lead" OR "lead développeur" Paris CDI` ; `site:welcometothejungle.com/fr/companies "tech lead" OR "lead développeur" OR "lead developer" Paris CDI` ; `Q022` ; `Q042`

### Architecte logiciel / solutions

- INTITULE_NORMALISE : Architecte logiciel / solutions
- VARIANTES_FRANCAISES : Architecte logiciel ; Architecte applicatif ; Architecte solutions
- VARIANTES_ANGLAISES : Software Architect ; Solutions Architect
- TECHNOLOGIES_ASSOCIEES : Architecture, cloud, microservices
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Évolution senior ; cible Mastère.
- OFFRES_OBSERVEES : 7 unique(s) / 7 brute(s)
- REQUETES_UTILISEES : `"Tech Lead" OR "Architecte Logiciel" emplois Indeed 2025 "plus de" France	=> 0 offres (+8 volumes)` ; `site:fr.indeed.com/viewjob "software engineer" OR "architecte logiciel" Paris CDI` ; `Q022` ; `site:fr.indeed.com/viewjob "architecte logiciel" OR "tech lead" OR "lead developer" Lyon OR Nantes	=> 5 (+1 enrichie ; Orly, Châtillon exclus) offre(s) individuelle(s)`

### Solutions Engineer

- INTITULE_NORMALISE : Solutions Engineer
- VARIANTES_FRANCAISES : Ingénieur solutions ; Ingénieur avant-vente technique
- VARIANTES_ANGLAISES : Solutions Engineer ; Sales Engineer
- TECHNOLOGIES_ASSOCIEES : Intégration, API
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Aucune offre observée ; conservé pour veille.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### DevOps Engineer

- INTITULE_NORMALISE : DevOps Engineer
- VARIANTES_FRANCAISES : Ingénieur DevOps ; Développeur DevOps
- VARIANTES_ANGLAISES : DevOps Engineer
- TECHNOLOGIES_ASSOCIEES : Docker, Kubernetes, CI/CD, Terraform, Ansible, AWS/Azure/GCP
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Industrialisation du déploiement ; famille en tension selon Apec/BMO.
- OFFRES_OBSERVEES : 84 unique(s) / 89 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "DevOps Engineer" Lyon` ; `"Devops" OR "Ingénieur Devops" France "offres d'emploi" Indeed.com 2024 "plus de"	=> 0 offres (+7 volumes)` ; `site:hellowork.com/fr-fr/emplois DevOps engineer CDI France` ; `Indeed "DevOps" OR "Cloud Engineer" OR "Site Reliability" France emplois "plus de"` ; `site:welcometothejungle.com/fr/companies "DevOps" CDI Toulouse OR Nantes OR Lille OR Rennes OR Bordeaux` ; `Hellowork "Emploi DevOps" OR "Emploi Ingénieur DevOps" "Plus de" Offres région`

### Cloud Engineer

- INTITULE_NORMALISE : Cloud Engineer
- VARIANTES_FRANCAISES : Ingénieur cloud ; Développeur cloud native
- VARIANTES_ANGLAISES : Cloud Engineer ; Cloud Developer
- TECHNOLOGIES_ASSOCIEES : AWS, Azure, GCP, Kubernetes
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Compétence cloud demandée aux développeurs ; métier propre pour les seniors.
- OFFRES_OBSERVEES : 10 unique(s) / 10 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "Cloud Engineer" Nantes OR Bordeaux OR Toulouse OR Lille` ; `"Cloud Engineer" OR "Site Reliability Engineer" OR "SRE" emplois Indeed 2025 "plus de"	=> 0 offres (+0 volumes ; résultats indeed.com US uniquement, ignorés)` ; `Site Reliability Engineer OR Cloud Engineer emplois "plus de" 2025 [allowed: fr.indeed.com]	=> 0 offres (+7 volumes)` ; `site:hellowork.com/fr-fr/emplois "Cloud Engineer" OR "Platform Engineer" CDI` ; `Indeed "DevOps" OR "Cloud Engineer" OR "Site Reliability" France emplois "plus de"` ; `site:fr.indeed.com/viewjob ingénieur cloud AWS OR Azure OR GCP CDI`

### Platform Engineer

- INTITULE_NORMALISE : Platform Engineer
- VARIANTES_FRANCAISES : Ingénieur plateforme
- VARIANTES_ANGLAISES : Platform Engineer
- TECHNOLOGIES_ASSOCIEES : Kubernetes, IaC
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Évolution du DevOps ; rare dans l'échantillon.
- OFFRES_OBSERVEES : 3 unique(s) / 4 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "Platform Engineer" France` ; `site:hellowork.com/fr-fr/emplois "Cloud Engineer" OR "Platform Engineer" CDI` ; `site:fr.indeed.com/viewjob "Platform Engineer" OR "Site Reliability Engineer" OR "SRE" CDI` ; `site:fr.linkedin.com/jobs/view "Platform Engineer" OR "Cloud Engineer" AWS OR GCP OR Azure France`

### Site Reliability Engineer (SRE)

- INTITULE_NORMALISE : Site Reliability Engineer (SRE)
- VARIANTES_FRANCAISES : Ingénieur fiabilité
- VARIANTES_ANGLAISES : SRE ; Site Reliability Engineer
- TECHNOLOGIES_ASSOCIEES : Observabilité, Kubernetes, cloud
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Métier d'exploitation logicielle ; profils seniors.
- OFFRES_OBSERVEES : 25 unique(s) / 34 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "SRE" OR "Site Reliability Engineer" Nantes OR Bordeaux OR Toulouse` ; `"Cloud Engineer" OR "Site Reliability Engineer" OR "SRE" emplois Indeed 2025 "plus de"	=> 0 offres (+0 volumes ; résultats indeed.com US uniquement, ignorés)` ; `Site Reliability Engineer OR Cloud Engineer emplois "plus de" 2025 [allowed: fr.indeed.com]	=> 0 offres (+7 volumes)` ; `site:welcometothejungle.com/fr/companies "Site Reliability Engineer" OR "SRE" CDI` ; `site:fr.linkedin.com/jobs/view "Ingénieur DevOps" OR "Cloud Engineer" OR "Site Reliability Engineer" France` ; `site:fr.indeed.com/viewjob "Platform Engineer" OR "Site Reliability Engineer" OR "SRE" CDI`

### QA / Test Automation Engineer

- INTITULE_NORMALISE : QA / Test Automation Engineer
- VARIANTES_FRANCAISES : Testeur automaticien ; Ingénieur test ; Ingénieur QA
- VARIANTES_ANGLAISES : QA Automation Engineer ; Test Automation Engineer ; SDET
- TECHNOLOGIES_ASSOCIEES : Cypress, Playwright, Selenium, Jest
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Contrôle qualité, renforcé par l'IA (validation des sorties).
- OFFRES_OBSERVEES : 47 unique(s) / 49 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "QA Automation" OR "Test Automation Engineer" France` ; `site:hellowork.com/fr-fr/emplois "QA automation" OR "testeur automaticien" CDI` ; `site:fr.linkedin.com/jobs/view "QA" OR "testeur automaticien" OR "test automation" engineer France` ; `site:fr.indeed.com/viewjob "QA" OR "testeur" OR "test automation" OR "ingénieur test" Marseille OR Lille OR Bordeaux	=> 5 (+1 enrichie ; Paris, Arcueil, télétravail exclus) offre(s) individuelle(s)`

### Ingénieur sécurité applicative / DevSecOps

- INTITULE_NORMALISE : Ingénieur sécurité applicative / DevSecOps
- VARIANTES_FRANCAISES : Ingénieur sécurité applicative ; DevSecOps ; Pentester applicatif
- VARIANTES_ANGLAISES : Application Security Engineer ; AppSec ; DevSecOps
- TECHNOLOGIES_ASSOCIEES : OWASP, SAST/DAST, IAM
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Passerelle vers la filière Cybersécurité NEXA.
- OFFRES_OBSERVEES : 38 unique(s) / 39 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "DevSecOps" OR "AppSec" OR "sécurité applicative" ingénieur` ; `site:hellowork.com/fr-fr/emplois "DevSecOps" OR "AppSec" ingénieur CDI` ; `Indeed "Testeur" OR "QA" OR "DevSecOps" OR "Cybersécurité" emplois "plus de" France` ; `site:welcometothejungle.com/fr/companies "AppSec" OR "sécurité applicative" OR "DevSecOps" CDI` ; `Hellowork "Emploi Cybersécurité" OR "Emploi DevSecOps" OR "Emploi Ingénieur cloud" OR "Emploi Cloud" "Plus de" Offres` ; `Indeed "DevOps" OR "Cloud Engineer" OR "DevSecOps" OR "Testeur QA" emplois "plus de" 2025 OR 2024`

### Développeur spécialisé accessibilité

- INTITULE_NORMALISE : Développeur spécialisé accessibilité
- VARIANTES_FRANCAISES : Développeur accessibilité ; Expert RGAA
- VARIANTES_ANGLAISES : Accessibility Developer
- TECHNOLOGIES_ASSOCIEES : RGAA, WCAG, ARIA
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Aucune offre dédiée observée ; compétence citée dans quelques offres front.
- OFFRES_OBSERVEES : 5 unique(s) / 5 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur "accessibilité" RGAA` ; `site:hellowork.com/fr-fr/emplois accessibilité RGAA développeur OR intégrateur` ; `site:welcometothejungle.com/fr/companies "Green IT" OR "éco-conception" OR "accessibilité numérique" développeur CDI` ; `site:fr.linkedin.com/jobs/view "accessibilité" RGAA développeur OR intégrateur` ; `site:candidat.francetravail.fr/offres/recherche/detail "testeur" OR "QA" OR "DevSecOps" OR "accessibilité numérique"`

### Développeur Green IT / éco-conception

- INTITULE_NORMALISE : Développeur Green IT / éco-conception
- VARIANTES_FRANCAISES : Développeur éco-conception ; Green IT
- VARIANTES_ANGLAISES : Green Software Engineer
- TECHNOLOGIES_ASSOCIEES : Éco-conception, RGESN
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Aucune offre dédiée observée.
- OFFRES_OBSERVEES : 5 unique(s) / 5 brute(s)
- REQUETES_UTILISEES : `site:hellowork.com/fr-fr/emplois "Green IT" OR "numérique responsable" développeur OR ingénieur` ; `site:welcometothejungle.com/fr/companies "Green IT" OR "éco-conception" OR "accessibilité numérique" développeur CDI` ; `site:fr.indeed.com/viewjob "Green IT" OR "éco-conception" OR "numérique responsable" développeur OR ingénieur`

### AI Engineer / Développeur IA

- INTITULE_NORMALISE : AI Engineer / Développeur IA
- VARIANTES_FRANCAISES : Ingénieur IA ; Développeur IA ; Développeur intelligence artificielle ; Ingénieur en intelligence artificielle
- VARIANTES_ANGLAISES : AI Engineer ; AI Developer ; Applied AI Engineer ; Forward Deployed Engineer
- TECHNOLOGIES_ASSOCIEES : Python, LLM, API OpenAI/Mistral/Anthropic, LangChain, RAG, cloud
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne à forte
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Développement d'applications intégrant des modèles ; intitulé le plus fréquent de la famille IA dans l'échantillon.
- OFFRES_OBSERVEES : 95 unique(s) / 112 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur web Nice OR Sophia-Antipolis` ; `site:fr.indeed.com/viewjob "AI Engineer" Paris` ; `site:fr.indeed.com/viewjob "développeur IA" LLM RAG` ; `site:welcometothejungle.com/fr/companies "AI Engineer" LLM Paris` ; `site:hellowork.com/fr-fr/emplois "ingénieur IA générative"` ; `site:apec.fr detail-offre "développeur full stack" "IA générative"`

### AI Software / Application Engineer

- INTITULE_NORMALISE : AI Software / Application Engineer
- VARIANTES_FRANCAISES : Développeur full stack IA ; Développeur d'applications IA
- VARIANTES_ANGLAISES : AI Software Engineer ; AI Application Developer ; Full Stack AI Engineer
- TECHNOLOGIES_ASSOCIEES : TS/Python, LLM, API de modèles
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Le plus proche du 'développeur augmenté' : développeur web intégrant l'IA.
- OFFRES_OBSERVEES : 19 unique(s) / 25 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### LLM / Generative AI Engineer

- INTITULE_NORMALISE : LLM / Generative AI Engineer
- VARIANTES_FRANCAISES : Ingénieur IA générative ; Ingénieur LLM
- VARIANTES_ANGLAISES : LLM Engineer ; Generative AI Engineer ; GenAI Engineer
- TECHNOLOGIES_ASSOCIEES : LLM, fine-tuning, RAG, évaluation
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Spécialisation IA générative ; ESN et grands comptes.
- OFFRES_OBSERVEES : 40 unique(s) / 44 brute(s)
- REQUETES_UTILISEES : `site:hellowork.com/fr-fr/emplois "ingénieur IA générative"` ; `site:welcometothejungle.com/fr/companies "LLM Engineer" OR "Generative AI Engineer" France` ; `site:fr.linkedin.com/jobs/view "AI Engineer" OR "LLM Engineer" France` ; `site:welcometothejungle.com/fr/companies "AI Engineer" OR "LLM Engineer" OR "AI Integration Engineer" CDI Paris OR Lyon	=> 1 offres (+0 volumes)` ; `Q021` ; `Q100`

### Développeur RAG / applications LLM

- INTITULE_NORMALISE : Développeur RAG / applications LLM
- VARIANTES_FRANCAISES : Développeur RAG
- VARIANTES_ANGLAISES : RAG Developer
- TECHNOLOGIES_ASSOCIEES : RAG, bases vectorielles, LangChain/LlamaIndex
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Rarement un intitulé autonome ; plutôt une compétence citée.
- OFFRES_OBSERVEES : 1 unique(s) / 1 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "développeur IA" LLM RAG` ; `site:fr.indeed.com/viewjob développeur "RAG" OR "LangChain" OR "agents IA"` ; `site:fr.linkedin.com/jobs/view "RAG" OR "LangChain" OR "agents IA" développeur France` ; `site:free-work.com "AI Engineer" OR "LLM" OR "IA générative" OR "RAG" mission` ; `site:fr.linkedin.com/jobs/view "développeur full stack" "LLM" OR "RAG" OR "agents IA"	=> 7 offres (+0 volumes)` ; `site:welcometothejungle.com/fr/companies "développeur full stack" "IA générative" OR "LLM" OR "RAG" CDI	=> 5 offres (+0 volumes)`

### Développeur d'agents IA

- INTITULE_NORMALISE : Développeur d'agents IA
- VARIANTES_FRANCAISES : Développeur agents IA ; Ingénieur agentique
- VARIANTES_ANGLAISES : AI Agent Developer ; Agentic AI Engineer
- TECHNOLOGIES_ASSOCIEES : Agents, MCP, orchestration
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Émergent ; très peu d'offres.
- OFFRES_OBSERVEES : 3 unique(s) / 3 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur "RAG" OR "LangChain" OR "agents IA"` ; `site:welcometothejungle.com/fr/companies "LLM" OR "agents IA" OR "agentic" développeur OR engineer CDI` ; `site:fr.linkedin.com/jobs/view "RAG" OR "LangChain" OR "agents IA" développeur France` ; `site:fr.linkedin.com/jobs/view "développeur full stack" "LLM" OR "RAG" OR "agents IA"	=> 7 offres (+0 volumes)` ; `site:free-work.com développeur "LLM" OR "IA générative" OR "agents IA" mission OR CDI	=> 0 offres (+0 volumes)`

### AI Integration / Automation Developer

- INTITULE_NORMALISE : AI Integration / Automation Developer
- VARIANTES_FRANCAISES : Développeur automatisation ; Intégrateur IA
- VARIANTES_ANGLAISES : AI Integration Engineer ; Automation Developer
- TECHNOLOGIES_ASSOCIEES : n8n, Make, API, LLM
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Automatisation de processus avec briques IA.
- OFFRES_OBSERVEES : 15 unique(s) / 18 brute(s)
- REQUETES_UTILISEES : `site:welcometothejungle.com/fr/companies "prompt engineer" OR "automation developer" OR "développeur no-code" OR "développeur low-code"` ; `site:fr.indeed.com/viewjob QA automatisation Cypress OR Playwright OR Selenium` ; `site:hellowork.com/fr-fr/emplois "n8n" OR "no-code" OR "low-code" développeur automatisation` ; `site:welcometothejungle.com/fr/companies "AI Engineer" OR "LLM Engineer" OR "AI Integration Engineer" CDI Paris OR Lyon	=> 1 offres (+0 volumes)`

### Low-code / No-code Developer

- INTITULE_NORMALISE : Low-code / No-code Developer
- VARIANTES_FRANCAISES : Développeur low-code ; Développeur no-code ; Développeur Power Platform
- VARIANTES_ANGLAISES : Low-code Developer ; No-code Developer
- TECHNOLOGIES_ASSOCIEES : Power Platform, OutSystems, Mendix, Bubble
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Faible à moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent, à la marge)
- JUSTIFICATION : Aucune offre observée dans l'échantillon ; conservé pour veille.
- OFFRES_OBSERVEES : 6 unique(s) / 6 brute(s)
- REQUETES_UTILISEES : `site:welcometothejungle.com/fr/companies "prompt engineer" OR "automation developer" OR "développeur no-code" OR "développeur low-code"` ; `site:hellowork.com/fr-fr/emplois "n8n" OR "no-code" OR "low-code" développeur automatisation` ; `site:apec.fr detail-offre "Développeur" F/H Bordeaux - 33	=> 0 offres nouvelles (+0 volumes) [178961270W, 177121507W déjà collectées ; exclus C++, AS400, Power Platform]`

### Prompt Engineer (avec composante développement)

- INTITULE_NORMALISE : Prompt Engineer (avec composante développement)
- VARIANTES_FRANCAISES : Ingénieur prompt
- VARIANTES_ANGLAISES : Prompt Engineer
- TECHNOLOGIES_ASSOCIEES : LLM, évaluation
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Faible
- INCLUS_OU_EXCLU : INCLUS (émergent, à la marge)
- JUSTIFICATION : Aucune offre observée ; non confirmé comme métier autonome.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `LLM OR "Prompt Engineer" OR "IA Générative" emplois "plus de" 2025 [allowed: fr.indeed.com]	=> 0 offres (+9 volumes)` ; `site:welcometothejungle.com/fr/companies "prompt engineer" OR "automation developer" OR "développeur no-code" OR "développeur low-code"` ; `site:fr.indeed.com/viewjob "prompt engineer" OR "prompt engineering" développeur`

### Machine Learning / Data Engineer

- INTITULE_NORMALISE : Machine Learning / Data Engineer
- VARIANTES_FRANCAISES : Ingénieur machine learning ; Data engineer ; MLOps
- VARIANTES_ANGLAISES : ML Engineer ; Data Engineer ; MLOps Engineer
- TECHNOLOGIES_ASSOCIEES : Python, Spark, MLflow
- FAMILLE : METIER_ADJACENT
- PROXIMITE_AVEC_LE_DEV_WEB : Faible à moyenne
- INCLUS_OU_EXCLU : EXCLU DES VOLUMES (adjacent)
- JUSTIFICATION : Relève de la filière IA & Data ; compté à part.
- OFFRES_OBSERVEES : 7 unique(s) / 7 brute(s)
- REQUETES_UTILISEES : `Hellowork "Emploi Ingénieur IA" OR "Emploi Intelligence artificielle" OR "Emploi Machine learning" "Plus de" Offres` ; `Indeed "AI Engineer" OR "Ingénieur IA" OR "Machine Learning Engineer" emplois "plus de" 2025 OR 2024` ; `Hellowork "Emploi Développeur IA" OR "Emploi Data scientist" OR "Emploi Ingénieur machine learning" "Plus de" Offres` ; `site:welcometothejungle.com/fr/companies "Télétravail total" "AI Engineer" OR "développeur IA" OR "Machine Learning Engineer"` ; `Q021` ; `Q172`

### Développeur logiciel hors web (embarqué, ERP, BI, mainframe)

- INTITULE_NORMALISE : Développeur logiciel hors web (embarqué, ERP, BI, mainframe)
- VARIANTES_FRANCAISES : Développeur embarqué ; Développeur SAP ; Développeur Salesforce ; Développeur Windev ; Développeur Cobol
- VARIANTES_ANGLAISES : Embedded Developer ; SAP Developer ; Salesforce Developer
- TECHNOLOGIES_ASSOCIEES : C/C++, ABAP, Apex, Windev, Cobol
- FAMILLE : METIER_ADJACENT
- PROXIMITE_AVEC_LE_DEV_WEB : Faible
- INCLUS_OU_EXCLU : EXCLU DES VOLUMES (adjacent)
- JUSTIFICATION : Découvert pendant la collecte ; hors périmètre web.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `012` ; `site:apec.fr detail-offre "Développeur" F/H Toulouse - 31	=> 7 offres nouvelles (+0 volumes) [exclus embarqué C, Sage X3]` ; `site:welcometothejungle.com/fr/companies développeur Bordeaux OR Mérignac OR Pessac	=> 9 (embarqué C exclu) offre(s) individuelle(s)` ; `site:free-work.com développeur Nantes OR Saint-Herblain	=> 2 (embarqué et Paris exclus ; extraits lead/TypeScript sans URL) offre(s) individuelle(s)` ; `site:fr.indeed.com/viewjob alternance OR stage développeur Marseille OR Aix-en-Provence web	=> 1 (+3 enrichies ; UX/UI intégrateur et embarqué exclus) offre(s) individuelle(s)` ; `site:fr.indeed.com/viewjob développeur "69001 Lyon" OR "69002 Lyon" OR "69003 Lyon" OR "69007 Lyon" OR "69008 Lyon"	=> 3 (+3 enrichies ; Cobol et business developer exclus) offre(s) individuelle(s)`

### Webmarketing / SEO / content

- INTITULE_NORMALISE : Webmarketing / SEO / content
- VARIANTES_FRANCAISES : Chargé de webmarketing ; Référenceur SEO ; Content manager ; Community manager
- VARIANTES_ANGLAISES : Digital Marketer ; SEO Specialist
- TECHNOLOGIES_ASSOCIEES : -
- FAMILLE : EXCLU_DU_PERIMETRE
- PROXIMITE_AVEC_LE_DEV_WEB : Nulle
- INCLUS_OU_EXCLU : EXCLU
- JUSTIFICATION : Faux positif du mot-clé 'web'.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Webdesigner / UX-UI designer sans code

- INTITULE_NORMALISE : Webdesigner / UX-UI designer sans code
- VARIANTES_FRANCAISES : Webdesigner ; UX designer ; UI designer
- VARIANTES_ANGLAISES : Web Designer ; Product Designer
- TECHNOLOGIES_ASSOCIEES : Figma
- FAMILLE : EXCLU_DU_PERIMETRE
- PROXIMITE_AVEC_LE_DEV_WEB : Faible
- INCLUS_OU_EXCLU : EXCLU
- JUSTIFICATION : Pas de programmation.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur "44000 Nantes" OR "44100 Nantes" OR "44200 Nantes" OR "44300 Nantes"	=> 3 (+1 enrichie ; data, commercial, webdesigner exclus) offre(s) individuelle(s)`

### Chef de projet digital sans programmation

- INTITULE_NORMALISE : Chef de projet digital sans programmation
- VARIANTES_FRANCAISES : Chef de projet digital ; Chef de projet web ; Product owner
- VARIANTES_ANGLAISES : Digital Project Manager ; Product Owner
- TECHNOLOGIES_ASSOCIEES : -
- FAMILLE : EXCLU_DU_PERIMETRE
- PROXIMITE_AVEC_LE_DEV_WEB : Faible
- INCLUS_OU_EXCLU : EXCLU
- JUSTIFICATION : Pas de développement (sauf 'chef de projet technique / dev', inclus au cas par cas).
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `site:apec.fr detail-offre "Développeur" F/H Rennes - 35	=> 7 offres (+0 volumes) [exclus: data, C++, Product owner]`

### Data analyst sans développement web

- INTITULE_NORMALISE : Data analyst sans développement web
- VARIANTES_FRANCAISES : Data analyst ; Analyste données
- VARIANTES_ANGLAISES : Data Analyst
- TECHNOLOGIES_ASSOCIEES : SQL, Power BI
- FAMILLE : EXCLU_DU_PERIMETRE
- PROXIMITE_AVEC_LE_DEV_WEB : Faible
- INCLUS_OU_EXCLU : EXCLU
- JUSTIFICATION : Filière IA & Data.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Formateur / enseignant en développement web

- INTITULE_NORMALISE : Formateur / enseignant en développement web
- VARIANTES_FRANCAISES : Formateur développement web ; Intervenant
- VARIANTES_ANGLAISES : Trainer
- TECHNOLOGIES_ASSOCIEES : -
- FAMILLE : EXCLU_DU_PERIMETRE
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : EXCLU
- JUSTIFICATION : Découvert pendant la collecte (organismes de formation) ; hors emploi de développeur.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `site:candidat.francetravail.fr/offres/recherche/detail développeur Marseille alternance OR junior OR "React" OR "Node"	=> 3 (Les Milles, Lyon, Bron ; formateur et hors zone exclus) offre(s) individuelle(s)`

### Autres intitulés normalisés apparus dans la collecte

- Développeur logiciel hors web (embarqué, ERP, BI...) : 25 offre(s) unique(s)
- Cybersécurité (hors développement, filière Cybersécurité) : 3 offre(s) unique(s)

### Règles de classement appliquées

- Le classement se fait sur l'intitulé de l'offre (règles regex ordonnées : exclusions, puis IA, spécialisations, évolutions, cœur de marché). Un intitulé « full stack » prime sur la technologie citée ; une technologie citée prime sur « développeur web » générique.
- La séniorité est déduite de l'expérience réellement demandée quand elle figure dans l'extrait ; les stages et alternances sont classés DEBUTANT ; les intitulés « lead / architecte » sont classés LEAD_OU_ARCHITECTE (responsabilité technique). Une mention « junior » ou « senior » dans le seul titre est conservée à part (colonne SENIORITE_INDICATIVE_TITRE) et n'est pas comptée.
- Les métiers adjacents (ML/data, embarqué, ERP) et les métiers émergents IA ne sont pas additionnés aux volumes du développement web ; ils sont présentés séparément.

## PARTIE B — PLATEFORMES SANS DONNÉES OU AVEC DONNÉES PARTIELLES

Toutes les plateformes ont d'abord été testées en accès direct (HTTP) : refus systématique du proxy (403). Le tableau ci-dessous consolide ensuite les tentatives via le moteur de recherche (pages publiques indexées), agent par agent.

### B.1 — Accès direct et API (test du 2026-09-06)

| PLATEFORME | URL | DATE_DU_TEST | METIERS_TESTES | ZONES_TESTEES | DONNEES_RECHERCHEES | RESULTAT | DONNEES_MANQUANTES | AUTRES_CHEMINS_TESTES | SOURCE_DE_REMPLACEMENT | IMPACT_SUR_L_ANALYSE |
|---|---|---|---|---|---|---|---|---|---|---|
| France Travail (candidat.francetravail.fr) | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| API France Travail Offres d'emploi (api.francetravail.io) | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| data.gouv.fr (jeu de données offres France Travail, BMO) | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Apec | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Indeed | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| LinkedIn Jobs | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Welcome to the Jungle | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| HelloWork | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Meteojob | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Monster | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Talent.com | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| JobTeaser | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Jooble | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| LesJeudis | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| ChooseYourBoss | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Free-Work | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Glassdoor | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| statistiques.francetravail.org (BMO) | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| INSEE | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Dares | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Numeum | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| corporate.apec.fr (études) | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| francetravail.org (études) | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| FRED (indice Indeed) | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |
| Wikipedia / archives web | (page d'accueil / API) | 2026-09-06 | tous | France | offres, volumes, études | Accès direct refusé (proxy 403 / EGRESS_BLOCKED) | contenu intégral des pages | moteur de recherche (pages indexées) | pages indexées de la même plateforme quand disponibles | champs non visibles dans les extraits = NC |

### B.2 — Résultats par plateforme via le moteur de recherche (offres individuelles obtenues dans l'échantillon)

| PLATEFORME | OFFRES_UNIQUES_OBTENUES | STATUT |
|---|---|---|
| France Travail | 231 | Données obtenues |
| Apec | 197 | Données obtenues |
| Indeed | 494 | Données obtenues |
| LinkedIn | 203 | Données obtenues |
| Welcome to the Jungle | 329 | Données obtenues |
| HelloWork | 364 | Données obtenues |
| Meteojob | 1 | Données partielles |
| Monster | 6 | Données partielles |
| Talent.com | 15 | Données obtenues |
| JobTeaser | 8 | Données partielles |
| Jooble | 0 | AUCUNE DONNÉE EXPLOITABLE |
| LesJeudis | 3 | Données partielles |
| ChooseYourBoss | 0 | AUCUNE DONNÉE EXPLOITABLE |
| Free-Work | 35 | Données obtenues |
| Glassdoor | 1 | Données partielles |
| Site carrière | 5 | Données partielles |
| Autre | 2 | Données partielles |

### B.3 — Journal détaillé des plateformes sans données (par agent de collecte)

| PLATEFORME | URL | DATE_DU_TEST | METIERS_TESTES | ZONES_TESTEES | DONNEES_RECHERCHEES | RESULTAT | DONNEES_MANQUANTES | AUTRES_CHEMINS_TESTES | SOURCE_DE_REMPLACEMENT | IMPACT_SUR_L_ANALYSE |
|---|---|---|---|---|---|---|---|---|---|---|
| Toutes plateformes (accès direct aux pages) (agent A) | https://fr.indeed.com/ ; https://candidat.francetravail.fr/ ; https://www.apec.fr/ ; https://www.welcometothejungle.com/ ; https://www.hellowork.com/ ; https://fr.linkedin.com/jobs/ ; https://www.free-work.com/ ; etc. | 2026-09-06 | Tous les métiers du périmètre | Lyon, Marseille/Aix, Lille, Nantes, Bordeaux et métropoles | Contenu intégral des offres (description, salaire, expérience, stack) et compteurs affichés dans les pages de liste | WebFetch et curl bloqués par le proxy de la session ; seule la recherche web (titres, URL, extraits) est disponible | Descriptions complètes, dates de publication exactes, salaires et exigences non présents dans les extraits ; compteurs en direct des moteurs de recherche des sites | Requêtes WebSearch avec opérateur site: ciblant les pages d'offres individuelles et les pages de liste indexées, variations d'intitulés FR/EN, contrats, séniorités, villes et codes postaux (200 requêtes) | Titres et extraits indexés par le moteur de recherche (WebSearch) ; pages de liste Indeed/HelloWork dont le titre contient un compte daté | Beaucoup de champs à 'NC' ; les volumes sont des compteurs indexés (souvent 'plus de N') à des dates hétérogènes, pas des relevés simultanés |
| ChooseYourBoss (agent A) | https://www.chooseyourboss.com/ | 2026-09-06 | développeur | Lyon, Nantes, Bordeaux | Offres individuelles et volumes | Aucun résultat du domaine renvoyé par WebSearch (site:chooseyourboss.com) | Toutes | Requête site:chooseyourboss.com développeur Lyon OR Nantes OR Bordeaux | Indeed, HelloWork, WTTJ, LinkedIn, France Travail, APEC | Plateforme non couverte |
| LesJeudis (agent A) | https://lesjeudis.com/jobs | 2026-09-06 | développeur, développeur full stack, nodejs, ai developer, .net, mobile, senior | Lille, Lyon, Marseille (aucun filtre zone dans les pages indexées) | Offres individuelles par ville et volumes par ville | Uniquement des pages de liste nationales avec un compte non daté (ex. '672 offres d'emploi disponibles pour développeur') ; aucune page d'offre individuelle indexée pour les zones | Offres individuelles, volumes par ville, dates | site:lesjeudis.com développeur Lille OR Lyon OR Marseille | Indeed, HelloWork | 4 volumes nationaux non datés enregistrés à titre indicatif ; pas de contribution aux zones |
| Meteojob (agent A) | https://www.meteojob.com/ | 2026-09-06 | développeur web, fullstack, informatique, .Net, front end, logiciel | Marseille, Aix-en-Provence, Lille, Lyon, Nantes, Bordeaux | Offres individuelles et volumes datés | Pages de liste sans compte ni date dans le titre ; un seul chiffre dans un extrait (18 offres Développeur informatique Bordeaux, non daté) ; extraits salariaux non attribuables à une offre précise | Offres individuelles, volumes datés | site:meteojob.com développeur Marseille OR Aix-en-Provence OR Lille ; site:meteojob.com "Développeur" Lyon OR Nantes OR Bordeaux "offres d'emploi" | Indeed, HelloWork | Plateforme quasi non exploitable via l'index |
| Jooble (agent A) | https://fr.jooble.org/ | 2026-09-06 | développeur, développeur web, junior, alternance, php, ios, android | Bordeaux, Mérignac, Lille, Lyon, Marseille, Nantes | Volumes datés par ville et offres individuelles | Pages de liste 'Besoin d'urgence' datées par année (2021-2026) sans compte fiable ; agrégats absurdes dans les extraits ('512 000 offres Lyon') ; extraits d'offres non attribuables | Comptes fiables, offres individuelles | site:fr.jooble.org développeur web Bordeaux OR Mérignac OR Lille ; site:fr.jooble.org "développeur" Lyon OR Marseille OR Nantes "offres d'emploi" nombre | Indeed, HelloWork, Jobijoba | Plateforme exclue des volumes |
| Monster (agent A) | https://www.monster.fr/ | 2026-09-06 | développeur, développeur web, python | Lyon, Marseille, Lille | Offres individuelles et volumes | Pages de liste sans compte ; pages d'offres renvoyées hors périmètre (marketing digital, architecte d'intérieur) ; extraits salariaux Marseille (45 k€, 55-65 k€) non rattachés à une URL d'offre développeur | Offres individuelles développeur, volumes | site:monster.fr développeur Lyon OR Marseille OR Lille | Indeed, HelloWork, LinkedIn | Plateforme non couverte |
| APEC (agent A) | https://www.apec.fr/candidat/recherche-emploi.html | 2026-09-06 | développeur full stack, Java, Angular, web, front, PHP/Symfony, Vue.js | Lyon, Marseille, Lille, Nantes, Bordeaux, Mérignac, Villeneuve-d'Ascq, Saint-Herblain | Volumes datés | Offres individuelles trouvées (28 enregistrées) mais les pages de liste APEC n'affichent aucun compte ni date dans le titre indexé ; extraits limités au titre et parfois à la date de publication | Volumes par ville, contenu des offres (salaire, expérience) | site:apec.fr detail-offre + ville + technologies (7 requêtes) | Indeed, HelloWork pour les volumes | APEC contribue aux offres (cadres) mais pas aux volumes |
| JobTeaser (agent A) | https://www.jobteaser.com/fr/job-search/ | 2026-09-06 | développement informatique, développeur, alternance | Lille, Lyon, Nantes, Bordeaux, Marseille | Offres individuelles et volumes | Peu de pages indexées : 1 offre individuelle (Astek mobile Nantes), quelques pages de liste avec un petit compte dans l'extrait (1 et 5 offres dev info Lille, 3 Lyon) et un compte tous secteurs (35 alternances Nantes) | Couverture Marseille/Bordeaux, dates précises | site:jobteaser.com développeur + villes (2 requêtes) | WTTJ, LinkedIn, HelloWork pour l'alternance | Contribution marginale |
| Glassdoor (agent A) | https://www.glassdoor.fr/Emploi/ | 2026-09-06 | développeur, développeur web, front end, freelance php | Lyon, Lille, Marseille, Nantes, Bordeaux | Volumes datés et offres individuelles | Comptes par ville présents dans les titres (ex. 'développeur - Lille : 249 emplois') mais sans date ; certains comptes incohérents ('12 382 emplois pour Développeur, Nantes' ; 'developpeur - Lille : 642') ; 1 seule offre individuelle indexée (Younup Nantes) | Dates des comptes, offres individuelles | site:glassdoor.fr + villes (3 requêtes) | Indeed, HelloWork | Volumes Glassdoor enregistrés avec DATE_DU_COMPTE = NC ; à traiter comme indicatifs |
| France Travail (pages de liste) (agent A) | https://candidat.francetravail.fr/offres/emploi/developpeur-web/... | 2026-09-06 | développeur web | Lyon, Marseille, Lille, Nantes, Bordeaux, Mérignac, Pessac, Tourcoing, Gironde, Nord, Bouches-du-Rhône, Rhône | Volumes datés par ville | Les pages de liste France Travail indexées ne contiennent ni compte ni date dans le titre ; extraits non attribuables | Volumes | site:candidat.francetravail.fr/offres/emploi "Développeur web" + villes ; les offres individuelles (detail) ont été collectées séparément (71 offres) | Indeed, HelloWork pour les volumes | France Travail contribue aux offres mais pas aux volumes |
| Talent.com (agent A) | https://fr.talent.com/ | 2026-09-06 | développeur, full stack, front | Marseille, Aix, Lille, Bordeaux, Nantes, Lyon, Villeurbanne | Volumes datés | Offres individuelles trouvées (14 enregistrées) mais aucune page de liste avec compte ; les extraits renvoient des pages de salaires moyens (ex. 33 000 €/an full stack France) non exploitables comme volumes | Volumes | site:fr.talent.com + villes (4 requêtes) | Indeed, HelloWork | Pas de volumes Talent.com |
| Free-Work (agent A) | https://www.free-work.com/fr/tech-it/jobs/ | 2026-09-06 | développeur, fullstack, react, java, angular, php, C/C++ | Bordeaux, Lyon, Lille, Nantes, Marseille | Volumes datés par ville | Pages de liste par technologie et ville sans compte dans le titre ; 2 comptes trouvés dans des extraits seulement (54 C/C++ Bordeaux ; 2 fullstack Marseille), non datés | Volumes datés | site:free-work.com + villes + technologies (7 requêtes) | Indeed, HelloWork | Free-Work contribue aux offres freelance (14 enregistrées) mais pas aux volumes |
| Indeed / HelloWork (comptes datés 2024 et 2025) (agent A) | https://fr.indeed.com/ ; https://www.hellowork.com/ | 2026-09-06 | développeur, développeur web, full stack, front end, back end, PHP, Java, software engineer, DevOps, alternance, stage, junior | Les 5 zones et communes périphériques | Comptes datés 2024 et 2025 pour les mêmes pages qu'en 2026 | L'index ne conserve qu'un seul instantané par URL : les comptes 2024/2025 n'existent que pour des URL alternatives (ex. /Lyon-(69)-Emplois-Developpeur-Web vs /q-developpeur-web-l-lyon-(69)-emplois.html) ; 2025 bien couvert (environ 60 lignes), 2024 partiel (environ 20 lignes) ; HelloWork n'a presque aucun compte daté 2024/2025 indexé | Séries mensuelles homogènes par ville ; comptes HelloWork 2024/2025 | Requêtes avec '2024', '2025', mois, 'offres d'emploi' (environ 20 requêtes) | Aucune ; comparer prudemment des URL différentes d'une même requête | Les tendances 2024→2026 ne peuvent être qu'indicatives (bornes 'plus de N', dates hétérogènes, attribution parfois incertaine signalée dans NOMBRE) |
| APEC (agent B) | https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=D%C3%A9veloppeur+web | 2026-09-06 | Développeur web ; Développeur Web Full-Stack ; Développeur Web Front-End Junior ; Développeur web en alternance | Paris ; France | Offres individuelles détaillées (salaire, expérience, stack) et nombre d'offres par région | Partiel : une seule page detail-offre indexée renvoyée (179135976W) ; les pages de liste APEC apparaissent avec le message « Une erreur inattendue est survenue » dans les extraits (rendu JavaScript), aucun compte d'offres lisible | Nombre d'offres par région ; contenu des offres (salaire, expérience, compétences) | Requête site:apec.fr detail-offre ; WebFetch/curl impossibles (proxy) | Hellowork, Indeed, France Travail, Welcome to the Jungle | Le segment cadres/APEC est sous-représenté dans l'échantillon B ; les volumes régionaux reposent sur Hellowork/Indeed |
| France Travail (DOM : Martinique, Guadeloupe) (agent B) | https://candidat.francetravail.fr/offres/recherche/detail/ | 2026-09-06 | Développeur web | La Réunion ; Martinique ; Guadeloupe | Offres individuelles de développeur web dans les DOM | Partiel : 1 offre à La Réunion (EDF Réunion, 207NRZM) ; pour la Guadeloupe seuls un poste de responsable technique et développement (183XJXN, périmètre non confirmé) et des offres hors périmètre (comptable, développement commercial) ; aucune offre Martinique dans les résultats indexés | Offres développeur web Martinique et Guadeloupe ; volumes DOM | Requête site:candidat.francetravail.fr avec OR sur les trois territoires | Aucune (à compléter par une requête Indeed/Hellowork DOM) | Les DOM restent très peu couverts dans l'échantillon B |
| Indeed (Corse) (agent B) | https://fr.indeed.com/viewjob | 2026-09-06 | Développeur web | Corse ; Ajaccio ; Bastia | Offres individuelles de développeur web en Corse | Aucune offre de développeur web indexée ; seuls des postes hors périmètre (téléconseiller, agent animalier, responsable IT à Bastia) et des pages Wikipédia | Offres et volumes développeur web en Corse | Requête site:fr.indeed.com/viewjob avec OR Corse/Ajaccio/Bastia | Aucune trouvée dans le budget | La Corse n'est pas représentée dans l'échantillon B |
| Indeed (mentions d'outils IA de codage) (agent B) | https://fr.indeed.com/viewjob | 2026-09-06 | Développeur citant GitHub Copilot, Cursor, Claude Code, vibe coding | France | Offres de développeur mentionnant explicitement des outils IA de codage | Aucune page d'offre Indeed renvoyée ; uniquement des pages Wikipédia, Coursera et G2 | Fréquence des mentions Copilot/Cursor/Claude Code dans les offres Indeed | Requête site:fr.indeed.com/viewjob avec OR sur les outils | Welcome to the Jungle (Koala Interactive cite Cursor et Claude Code) ; Indeed stage agents IA (Claude Code, n8n, LangGraph) | La mesure des mentions d'outils IA de codage reste anecdotique dans l'échantillon B |
| Indeed (Antilles) (agent B) | https://fr.indeed.com/viewjob | 2026-09-06 | Développeur web | Martinique ; Guadeloupe ; Fort-de-France ; Pointe-à-Pitre | Offres individuelles de développeur web aux Antilles | Aucune offre de développeur web ; une seule alternance support informatique (EFS) et des pages Wikipédia | Offres et volumes développeur web Martinique/Guadeloupe | France Travail (1 offre Réunion), Hellowork (1 offre Guadeloupe EXELCIA, 1 alternance Réunion) | Hellowork / France Travail | Antilles quasi absentes de l'échantillon B (1 offre Guadeloupe) |
| France Travail (volumes) (agent B) | https://candidat.francetravail.fr/offres/emploi/developpeur-web/s28m7 | 2026-09-06 | Développeur web (Informatique et télécoms ; Internet - Ecommerce) | France ; Paris ; Haute-Garonne ; Bas-Rhin ; Montpellier ; Strasbourg ; Var ; Tours | Nombre d'offres développeur web par région/département | Pages de résultats régionales indexées mais les extraits n'affichent que le texte d'aide à la recherche, aucun compte d'offres (compteurs dynamiques) | Volumes France Travail par région | Requête francetravail.fr développeur web résultats région ; pages detail utilisées pour les offres individuelles | Indeed et Hellowork (comptes datés par région) | Les volumes régionaux ne reposent pas sur France Travail, seule source publique exhaustive ; biais possible vers les plateformes privées |
| Welcome to the Jungle (volumes) (agent B) | https://www.welcometothejungle.com/fr/pages/emploi-developpeur-full-stack | 2026-09-06 | Développeur full stack ; Développeur web ; Développeur | France ; Paris ; Nantes ; Levallois-Perret | Nombre d'offres par métier/ville | Pages métier/ville indexées sans compteur d'offres dans les extraits | Volumes WTTJ par ville et par métier | Requêtes site:welcometothejungle.com/fr/companies pour les offres individuelles (fonctionnent) | Indeed / Hellowork | WTTJ contribue aux offres individuelles mais pas aux volumes |
| Talent.com (agent B) | https://fr.talent.com/jobs/k-d%C3%A9veloppeur-web-d%C3%A9butant-l-france | 2026-09-06 | Développeur web | France ; Île-de-France | Offres individuelles et volumes | Seules des annonces de formation en alternance (Webforce3, Bordeaux et Hauts-de-France) et des pages de liste sans compteur sont indexées ; aucune offre d'entreprise exploitable | Offres d'entreprises et comptes d'offres Talent.com | Requête site:fr.talent.com développeur web emploi | Indeed, Hellowork, France Travail, WTTJ | Talent.com non exploité dans l'échantillon B |
| ChooseYourBoss (agent B) | https://www.chooseyourboss.com | 2026-09-06 | Développeur full stack ; front-end ; back-end | France | Offres individuelles | Aucune page chooseyourboss.com renvoyée par la recherche site: (résultats hors sujet uniquement) | Offres ChooseYourBoss | Requête site:chooseyourboss.com avec OR | Autres plateformes | Plateforme non couverte |
| JobTeaser (agent B) | https://www.jobteaser.com/fr/job-offers/ | 2026-09-06 | Développeur web (stage, alternance) | France | Offres individuelles localisées | 6 pages d'offres indexées (Ceva Santé Animale alternance Ibexa 28/05/2026 ; Thales alternance SDK cartographique WebGL/Angular 08/05/2026 ; Orange stage e-commerce B2B Drupal ; Banque de France stage site internet data science ; Ayvens France alternance Azure 22/04/2026 ; Evodev stage web et mobile) mais aucune localisation dans les titres/extraits : non enregistrées en offres faute de région | Localisation des offres JobTeaser ; volumes | Requête site:jobteaser.com développeur web stage OR alternance | Indeed / Hellowork pour stages et alternances localisés | Le segment stage/alternance grands groupes (Orange, Thales, Banque de France) est visible mais non géolocalisé |
| Hellowork (pages ville sans compteur) (agent B) | https://www.hellowork.com/fr-fr/emploi/metier_developpeur-web-ville_nice-06000.html | 2026-09-06 | Développeur web | Nice ; Toulon ; Metz ; Reims ; Rouen | Nombre d'offres développeur web par ville | Pages ville indexées (Nice 17/10/2025, Toulon 30/05/2026, Metz 19/06/2026, Reims 30/04/2026, Rouen 06/05/2026) mais titres « Voir les dernières offres » sans compteur ; seuls les totaux France sont chiffrés | Comptes par ville pour Nice, Toulon, Metz, Reims, Rouen | Requêtes site:hellowork.com/fr-fr/emplois par ville (offres individuelles obtenues) | Indeed (comptes par ville : Montpellier, Rennes, Strasbourg, Grenoble, Nice, Toulouse) | Volumes de villes moyennes moins précis (Hellowork n'affiche « Plus de N » qu'au-delà d'un seuil) |
| France Travail (requêtes multi-villes : Nouvelle-Aquitaine hors Bordeaux, Hauts-de-France hors Lille, Normandie, Corse, DOM) (agent B) | https://candidat.francetravail.fr/offres/recherche/detail/ | 2026-09-06 | Développeur | Limoges, Poitiers, La Rochelle, Pau, Bayonne ; Amiens, Valenciennes, Arras, Dunkerque, Beauvais ; Caen, Le Havre, Cherbourg, Évreux, Alençon ; Ajaccio, Bastia, Corse, Martinique, Guadeloupe, Guyane | Offres individuelles de développeur dans ces villes | La recherche site: avec OR sur plusieurs villes renvoie quasi exclusivement des offres hors informatique (BTP, commerce, hôtellerie) ; seule une offre Testeur QA à Poitiers (210SPGK) et un poste de formateur DEV à Amiens (exclu) sont apparus ; aucune offre développeur en Corse, Martinique, Guadeloupe ou Guyane | Offres développeur France Travail pour ces villes ; Corse et DOM | Requêtes site:candidat.francetravail.fr par ville isolée plus tôt (Le Mans/Angers, Toulouse/Montpellier, Rennes, Grenoble/Clermont, Dijon/Toulon : fonctionnent mieux avec 2-3 villes) | Indeed et Hellowork pour ces villes | France Travail sous-représente les petites villes dans l'échantillon B ; Corse/DOM restent à 4 offres au total |
| Indeed (villes moyennes via requêtes multi-villes) (agent B) | https://fr.indeed.com/viewjob | 2026-09-06 | Développeur web | Brest, Quimper, Lorient, Vannes, Saint-Brieuc ; Le Mans, Laval, La Roche-sur-Yon, Cholet, Saint-Nazaire ; Orléans, Bourges, Chartres, Blois, Châteauroux ; Pau, Bayonne, Tarbes, Limoges, Angoulême, Niort ; Caen, Cherbourg, Évreux, Saint-Lô, Alençon ; Amiens, Beauvais, Compiègne, Valenciennes, Arras, Dunkerque | Offres individuelles développeur web dans les villes moyennes | Faible rendement : les requêtes site: avec 5-6 villes en OR renvoient surtout des pages Wikipédia et des offres hors informatique ; 5 offres retenues (La Roche-sur-Yon, Croix, Lanester, Toulouse, Rouvignies) ; aucune pour Bretagne ouest, Centre-Val de Loire (hors Tours), Normandie (hors Rouen/Caen déjà couverts) | Offres Indeed pour Brest, Quimper, Lorient, Vannes, Orléans, Bourges, Chartres, Pau, Bayonne, Limoges, Cherbourg, Évreux, Beauvais, Arras, Dunkerque | Requêtes Hellowork et France Travail par ville (meilleur rendement pour Brest, Pau, Limoges, Caen, Amiens, Reims, Tours) | Hellowork (pages ville), France Travail | Les villes moyennes hors métropoles restent couvertes surtout par Hellowork ; les comptes Indeed par ville ne sont disponibles que pour les grandes villes |
| Free-Work (pages thématiques IA) (agent B) | https://www.free-work.com/fr/tech-it/jobs/ia-generative | 2026-09-06 | AI Engineer ; LLM ; IA générative ; RAG ; Agent IA ; Copilot ; Mistral ; LangChain ; Prompt Engineering | France | Missions freelance IA individuelles et nombre de missions par thème | Pages thématiques indexées (LangChain, Prompt Engineering, RAG, Copilot, Mistral, IA Générative, Agent IA) sans compteur dans les titres ; extraits décrivant des missions (pipelines LLM/RAG, Copilot Studio, Qdrant/Weaviate, banque/assurance, 3-6 ans d'expérience) mais non rattachables à une URL individuelle ; 1 mission individuelle retenue (AGH Consulting Toulouse) | Nombre de missions freelance IA par thème ; URLs individuelles des missions décrites | site:free-work.com développeur full stack full remote (3 offres obtenues) | Indeed, LinkedIn, WTTJ pour les offres IA | Le marché freelance IA est sous-représenté dans l'échantillon B |
| Welcome to the Jungle / Indeed (Corse et DOM) (agent B) | https://fr.jooble.org/emploi-developpeur-web/La-R%C3%A9union | 2026-09-06 | Développeur ; Développeur web | La Réunion ; Martinique ; Guadeloupe ; Corse ; Ajaccio ; Saint-Denis (974) | Offres individuelles et volumes développeur en Corse et dans les DOM | WTTJ : aucune offre développeur (seule une offre gestion/recouvrement en Guadeloupe) ; Indeed : un seul compte daté (Développeur, Ingénieur, Guadeloupe : plus de 25 offres au 08/07/2024) ; Jooble : page « Developpeur web à La Réunion 2026 » sans compteur ; mention du groupe noviseas (ESN présente en Guadeloupe, Martinique, Guyane, Réunion) sans URL d'offre | Offres individuelles Corse/Martinique/Guyane ; volumes Réunion, Martinique, Corse | France Travail (2 offres Réunion), Hellowork (2 offres Réunion/Guadeloupe), Indeed viewjob (aucune) | Aucune source exhaustive identifiée | Corse et DOM restent marginaux dans l'échantillon B (4 offres, 1 volume 2024) |
| Data Emploi (dataemploi.francetravail.fr, ROME M1805) (agent D1) | https://dataemploi.francetravail.fr/ | 2026-09-06 | ROME M1805 Études et développement informatique | Normandie, Bretagne, Grand Est (requêtes préparées) | Nombre d'offres, projets de recrutement BMO, part difficile par région | Requêtes non exécutées : quota WebSearch de la session épuisé (200/200) après 45 requêtes D1 ; aucune page dataemploi n'est remontée dans les requêtes France Travail précédentes | Tous les indicateurs régionaux M1805 | Aucun (WebFetch/curl bloqués par le proxy selon D_CONSIGNES) | Fichiers C_regions.jsonl / etudes/regions_donnees.jsonl des agents précédents | Pas de volume régional France Travail daté dans D1 ; à relancer dans une session avec quota disponible |
| France Travail - pages de liste (candidat.francetravail.fr/offres/emploi/... et /offres/recherche?motsCles=) (agent D1) | https://candidat.francetravail.fr/offres/emploi/developpeur-web/caen/s28m7v40 ; https://candidat.francetravail.fr/offres/emploi/developpeur-web/tours/s29m2v26 ; https://candidat.francetravail.fr/offres/emploi/developpeur-web/le-havre/s28m7v14 ; https://candidat.francetravail.fr/offres/emploi/developpeur-web/reunion/s28m7d974 | 2026-09-06 | Développeur web, développeur javascript, développeur front end, développeur symfony, développeur php, développeur informatique | Caen, Calvados, Tours, Indre-et-Loire, Le Havre, Seine-Maritime, La Réunion, Cannes, Hauts-de-Seine, France entière | Nombre d'offres affiché dans le titre ou l'extrait des pages de liste | Les pages de liste France Travail remontent dans les résultats mais leur titre ('Offres d'emploi Développeur web - Informatique et télécoms - Caen / France Travail') ne contient aucun compte ; les extraits résumés n'en donnent pas non plus. Seule exception : 'N offres d'emploi pour <mot-clé>' apparaît pour des mots-clés génériques (ex. '5962 offres d'emploi pour tours', non pertinent) | Stocks d'offres datés par métier × zone sur France Travail | Requêtes site:candidat.francetravail.fr/offres/recherche avec 'offres' et motsCles (non exécutée, quota épuisé) | Comptes datés HelloWork/Indeed (1 volume HelloWork 'Développeur symfony' relevé) | Les volumes France Travail par région restent absents de D1 |
| France Travail - offres individuelles Corse, Antilles-Guyane, Mayotte, Orléans, Amiens, Poitiers/Limoges, Nice/Sophia, Clermont-Ferrand, Vannes/Lorient/Quimper, Le Havre (agent D1) | https://candidat.francetravail.fr/offres/recherche/detail/ | 2026-09-06 | développeur, développeur web, full stack, logiciel, informatique | Ajaccio, Bastia, Martinique, Guadeloupe, Guyane, Mayotte, Orléans, Amiens, Poitiers, Limoges, Nice, Sophia-Antipolis, Clermont-Ferrand, Vannes, Lorient, Quimper, Le Havre | Offres individuelles avec expérience, contrat, salaire | Très peu ou aucune offre de développement indexée : Corse 3 offres (2 datées 2025), Martinique 1, Réunion 4, Mayotte/Guadeloupe/Guyane 0, Orléans 0, Amiens 0, Poitiers/Limoges 0 (seulement testeur QA), Nice 0, Clermont 0, Vannes/Lorient/Quimper 1 (Angular/.NET Quimper), Le Havre 0 (hors GTB/industrie) | Offres dev web dans ces zones | Deux formulations par zone (ville + champs 'Débutant accepté'/'An(s)'/'Salaire', puis motif de titre 'NN - VILLE') | Indeed/HelloWork pour ces zones (agents A/B/C) | Sous-représentation persistante de ces zones dans le corpus France Travail ; le faible nombre est lui-même une observation (marché FT mince hors métropoles) |
| Apec (apec.fr, pages détail-offre) (agent D2) | https://www.apec.fr/candidat/recherche-emploi.html/emploi/detail-offre/ | 2026-09-06 | développeur web / full stack / front / back / PHP-Symfony / Java-Spring / .NET / React-Angular-Vue-Node / Python / mobile / DevOps / QA / software engineer / ingénieur IA-LLM / tech lead | Paris, Lyon, Toulouse, Nantes, Rennes, Lille, Bordeaux, Marseille, Montpellier, Strasbourg, Rouen, Dijon, Grenoble, Nice, Tours, Clermont-Ferrand, Reims, Nancy, Caen, Angers, Brest, Amiens, Metz, Besançon, Limoges, Poitiers, Aix-en-Provence, La Rochelle, Le Mans | Fourchette de salaire (k€ brut annuel), expérience minimale, type de contrat, télétravail, entreprise | Les pages détail-offre remontent bien via WebSearch (titre exact avec ville/département et souvent date de publication), mais le résumé renvoyé par l'outil ne restitue jamais le bloc salaire / expérience / contrat / télétravail / entreprise des offres ; 12 requêtes ciblées sur les termes 'k€ brut annuel', 'brut annuel', 'Minimum 3 ans', 'Débutant accepté', 'A négocier', 'Télétravail partiel' n'ont renvoyé aucun extrait exploitable. | SALAIRE_MINIMUM, SALAIRE_MAXIMUM, EXPERIENCE (hors mention dans le titre : junior/confirmé/senior/expert), TYPE_CONTRAT (hors mention dans le titre), TELETRAVAIL, ENTREPRISE, description de poste | site:cadres.apec.fr (ancien format d'URL), jd.apec.fr, allowed_domains apec.fr, requêtes avec fourchettes précises ('35 - 45 k€'), WebFetch/curl interdits par consigne | Fiche métier Apec 'Développeur' (apec.fr/tous-nos-metiers/informatique/developpeur.html) : 80 % des offres entre 34 et 53 k€ brut annuel, moyenne 43 k€ ; étude Apec 'Les rémunérations des cadres dans 111 familles de métiers' (édition 2025) ; article Le Monde Informatique 'Les salaires des cadres IT analysés par l'Apec en 2025' | Les 162 offres Apec collectées documentent l'intitulé, la technologie, la ville/région et la date, mais pas le salaire individuel : l'analyse salariale Apec devra s'appuyer sur les agrégats de la fiche métier et des études Apec plutôt que sur des offres unitaires. |
| Apec (pages de liste recherche-emploi.html/emploi?motsCles=...) (agent D2) | https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=D%C3%A9veloppeur+web | 2026-09-06 | Développeur web, Développeur full stack, Développeur PHP, Développeur Java, Développeur JavaScript, Développeur informatique | France, Lyon, Nantes, Rennes, Paris, Bourgogne-Franche-Comté, Gironde, Ile-de-France | Nombre d'offres actives ('N offres d'emploi') daté (2024, 2025, septembre 2026) | Les pages de liste Apec sont indexées (titres 'Offres d'emploi Développeur web', 'Offres d'emploi - septembre 2026') mais leur contenu est chargé dynamiquement : aucun compte d'offres n'apparaît dans les titres ni dans les extraits, contrairement à Indeed/HelloWork. | NOMBRE d'offres par intitulé × zone × date | Requêtes 'septembre 2026', 'nombre d'offres 2025', filtres lieux=/fonctions=/salaires=, cadres.apec.fr/liste-offres-emploi-cadres | Études corporate.apec.fr : 31 258 offres de développeurs publiées sur apec.fr (2022, 'Les métiers cadres porteurs en 2023') ; PDF régionaux 'Les offres publiées sur apec.fr' (Île-de-France, Auvergne-Rhône-Alpes, Paca oct. 2023, Bourgogne-Franche-Comté) ; 'Cartographie et analyse territoriale des offres d'emploi cadre par secteur' ; 'Prévisions 2025/2026 de recrutements de cadres en Île-de-France' (volume d'offres IDF déc. 2024-fév. 2025 en baisse de 24 % vs fév. 2023, développement informatique 2e famille de métiers) | Pas de série de stocks Apec datés par ville/intitulé ; les volumes Apec ne peuvent être utilisés qu'au niveau national/régional via les études Apec (à exploiter par l'agent études). |
| Jooble / Talent.com / Jobijoba / Meteojob / Monster / LinkedIn / JobTeaser / Glassdoor / Optioncarriere / Free-Work (agent D4) | fr.jooble.org ; fr.talent.com ; jobijoba.com ; meteojob.com ; monster.fr ; fr.linkedin.com/jobs ; jobteaser.com ; glassdoor.fr ; optioncarriere.com ; free-work.com | 2026-09-06 | aucun (non testées) | aucune | comptes d'offres datés pluriannuels (2024/2025/2026) par intitulé × zone | NON TESTÉES : le budget WebSearch de la session (plafond 200 requêtes, partagé) a été épuisé après 48 requêtes D4, toutes consacrées à Indeed France (source prioritaire) ; 8 requêtes villes moyennes Indeed ont aussi été refusées | séries datées hors Indeed ; villes Nancy, Metz, Reims, Brest, Caen, Le Havre, Dijon, Besançon, Tours, Orléans, Clermont-Ferrand, Annecy, Saint-Étienne, Poitiers, Limoges, Pau, La Rochelle, Amiens, Angers, Le Mans, Ajaccio, Bastia, Saint-Denis Réunion, Fort-de-France, Pointe-à-Pitre (Indeed) ; intitulés Vue/Angular 2024, .NET France 2024, JavaScript, intégrateur web 2025, développeur alternance France 2024, développeur web junior 2024 | aucun (WebFetch/curl bloqués par le proxy, non réessayés conformément aux consignes) | Indeed France (296 comptes datés dans D4_volumes.jsonl) ; fichiers A/B/C_volumes.jsonl pour HelloWork, LinkedIn, Glassdoor, Free-Work, JobTeaser | les séries pluriannuelles restent mono-source (Indeed) ; pas de triangulation inter-plateformes par D4 ; couverture villes moyennes à compléter dans une session ultérieure |
| Free-Work (TJM / rémunération freelance) (agent D5) | https://www.free-work.com/fr/tech-it/jobs/developpeur-fullstack | 2026-09-06 | développeur fullstack, développeur (TJM / €/jour) | Nantes, Paris | TJM ou salaire sur les pages d'offres individuelles | Les requêtes 'TJM' OR '€/jour' ne remontent que des pages de liste et des pages baromètre (ex. 'TJM : Développeur fullstack', moyenne 550 €/jour) ; aucune page d'offre individuelle avec TJM affiché dans l'extrait | TJM par offre, localisation Nantes | site:free-work.com mission freelance 'développeur fullstack' Paris (idem : pages de liste, extraits mentionnant des missions sans URL individuelle) | Offres CDI Free-Work avec fourchette de salaire dans l'extrait (Lyon : 40-60 k€) ; baromètre TJM Free-Work (550 €/jour fullstack, 400 €/jour PHP Paris, jusqu'à 600 €/jour Java) | Le TJM freelance ne peut être documenté qu'au niveau agrégé (baromètre), pas par offre |
| Free-Work (offres IA / LLM) (agent D5) | https://www.free-work.com/fr/tech-it/jobs/large-language-model-llm | 2026-09-06 | développeur LLM / IA générative / agents IA | France | offres individuelles de développeurs mentionnant LLM, RAG, agents IA | Seules des pages de liste par mot-clé (LLM, IA, Agent IA, Copilot, Prompt Engineering, IA Générative) sont indexées ; les extraits décrivent des missions (Senior AI Developer Montpellier, AI Agents Developer Paris banque privée, consultant GenAI assurance) sans URL individuelle | URL, contrat, expérience, TJM par offre | Aucun (budget WebSearch épuisé) | Welcome to the Jungle (offres IA individuelles bien indexées : Padoa, SII, MP Data, Figaro Classifieds, Beamy, Keyrus...) | Le marché freelance IA est sous-représenté dans le fichier d'offres ; à documenter via WTTJ et LinkedIn |
| JobTeaser (agent D5) | https://www.jobteaser.com/fr/job-search/alternance-web-paris | 2026-09-06 | développeur web (stage, alternance) | Paris, Lyon, Nantes, Lille | offres individuelles stage/alternance développeur web | L'indexation privilégie les pages de recherche datées (comptes d'offres exploitables en volumes : 22 alternances web Paris août 2025, 54 dev info Paris février 2026, 3 Lyon / 1 Nantes / 1 Lille juin 2026, 16 web Lille mars 2026) ; seulement 2 offres individuelles remontées (Ayvens, Sopra Steria .NET Lyon) | détail des offres individuelles (durée, rémunération, école) | requête combinée Lyon/Nantes/Lille | Welcome to the Jungle (stages/alternances : Sociabble, Sopra Steria, Docaposte, Innovorder) | JobTeaser sert surtout aux volumes datés (stocks faibles hors Paris), pas au détail des offres |
| Monster, Meteojob, Talent.com, Jooble, LesJeudis, ChooseYourBoss, Glassdoor, cabinets (Hays, Robert Half, Michael Page, Silkhom, Urban Linker, Mobiskill, Nextep, Blue Search) (agent D5) | NC | 2026-09-06 | développeur web / fullstack / front / back | France, villes NEXA et autres métropoles (Toulouse, Montpellier, Rennes, Strasbourg, Grenoble) | offres individuelles avec expérience, contrat, salaire, télétravail, IA | NON TESTÉ : le budget WebSearch de la session (200/200 requêtes, partagé) a été épuisé après la 28e requête de l'agent D5 ; 10 requêtes préparées (Toulouse/Montpellier, Rennes/Strasbourg/Grenoble, LinkedIn junior Paris, LinkedIn senior Lille/Marseille, LesJeudis, ChooseYourBoss, Monster, Meteojob, Talent.com, Jooble) ont été refusées | tout | Aucun (WebFetch/curl bloqués par le proxy) | Urban Linker, Hays, Externatic, AK Recrutement, Grafton, Easy Partner, Objectware, HR-Team, FED apparaissent indirectement via LinkedIn et Free-Work | Couverture D5 limitée à WTTJ, LinkedIn, Free-Work, JobTeaser et Greenhouse ; autres métropoles hors NEXA peu couvertes (Poitiers, Rouffach, Caen, Angoulême, Chamalières, Toulouse, Colomiers, Landivisiau seulement) |
| Indeed (filtre 'Débutant accepté' / 'sans expérience') (agent D7) | https://fr.indeed.com/viewjob | 2026-09-06 | développeur ; développeur web ; développeur full stack | Paris/IDF ; Lyon/Villeurbanne ; Lille/Roubaix/Tourcoing/Lesquin ; Bordeaux/Mérignac/Pessac ; Nantes/Carquefou/Rezé ; Marseille/Aubagne/Vitrolles | offres individuelles (viewjob) mentionnant explicitement 'Débutant accepté' avec contrat/salaire | 8 requêtes 'Débutant accepté' : aucune page viewjob développeur indexée avec cette mention dans les six zones ; seules des pages de liste (comptes datés) ou des offres hors informatique (soins) remontent. Une seule offre 'débutant(e) accepté(e)' trouvée, hors zone (La Roche-sur-Yon). | mention 'Débutant accepté' dans les extraits d'offres développeur ; salaires sur les offres juniors | requêtes 'jeune diplômé', 'sans expérience', 'première expérience', 'junior' + ville ; requêtes suburbs (Bron, Vénissieux, Limonest, Écully, Carquefou, Rezé, Aubagne...) | pages de liste Indeed 'Debutant Accepte, Nantes (44) : plus de 400 emplois' (tous métiers) ; offres 'junior' / alternance / stage individuelles | L'ouverture aux débutants sur Indeed se lit surtout via les intitulés 'junior', 'alternance', 'stage', 'apprenti' plutôt que via le champ 'Débutant accepté' ; le budget WebSearch de la session (200/200) a été atteint après 52 requêtes D7, limitant la collecte à 54 lignes. |
| Apec (agent ia) | https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=D%C3%A9veloppeur+full+stack+et+IA | 2026-09-06 | développeur full stack IA générative | France | offres individuelles (detail-offre) et comptes d'offres | WebSearch ne renvoie que des pages de liste Apec, dont le contenu indexé est un message d'erreur (« Une erreur inattendue est survenue ») ; aucune page detail-offre, aucun compte | offres individuelles Apec, volumes Apec | site:apec.fr detail-offre | Indeed, Welcome to the Jungle, HelloWork | Pas de données Apec (cadres) pour les familles A et B |
| Free-Work, LinkedIn, France Travail, JobTeaser, LesJeudis, ChooseYourBoss, Meteojob, Talent.com, Jooble, Monster (agent ia) | NC | 2026-09-06 | AI Engineer, LLM, DevOps, Cloud, Platform, DevSecOps, Tech Lead (requêtes préparées non exécutées) | France | offres individuelles et volumes | NON TESTEES : quota WebSearch de la session épuisé (200/200) après 12 requêtes de cet agent ; une seule page de liste Free-Work (Claude Code) et une offre LinkedIn sont remontées incidemment | tout le périmètre de ces plateformes | WebFetch/curl bloqués par le proxy (règle) | Aucune dans cette session | Couverture partielle : objectif 80+80 offres non atteint (33 A / 19 B) ; villes Marseille-Aix, Lille (famille B), Nantes/Bordeaux (famille B) peu ou pas couvertes |
| Apec (Nantes) (agent lille) | https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=D%C3%A9veloppeur+FullStack+%C3%A0+Nantes | 2026-09-06 | développeur full stack | Nantes | offres individuelles (detail-offre) et comptes d'offres | WebSearch ne renvoie que des pages de liste (motsCles=...) sans compte d'offres dans le titre ni l'extrait, et une seule page detail-offre située à Nanterre (hors zone) | URLs d'offres individuelles Apec à Nantes ; nombre d'offres | site:apec.fr detail-offre développeur full stack Nantes | Indeed, France Travail, Welcome to the Jungle (offres Nantes collectées) | Aucune offre Apec pour Nantes dans l'échantillon ; sous-représentation des offres cadres Apec sur cette zone |
| HelloWork (agent lille) | https://www.hellowork.com/fr-fr/emplois | 2026-09-06 | développeur web / développeur | Lille, Nantes, Bordeaux | offres individuelles et comptes 'Plus de N offres - date' | Requêtes non exécutées : quota WebSearch de la session épuisé (200/200) avant le lancement des requêtes HelloWork | toutes (offres et volumes HelloWork) | WebFetch/curl bloqués par le proxy (non tentés conformément aux règles) | Aucune | Pas de volumes HelloWork ni d'offres HelloWork pour les trois zones |
| LinkedIn (agent lille) | https://fr.linkedin.com/jobs/view | 2026-09-06 | développeur full stack | Lille, Nantes, Bordeaux | offres individuelles et comptes d'offres | Requêtes non exécutées : quota WebSearch de la session épuisé (200/200) | toutes | Aucun (WebFetch bloqué) | Aucune | Pas de données LinkedIn pour les trois zones |
| Free-Work, Jooble, Talent.com, Meteojob, Monster, JobTeaser, LesJeudis, ChooseYourBoss, Indeed (pages de comptes 'plus de N emplois') (agent lille) | NC | 2026-09-06 | non testés | Lille, Nantes, Bordeaux | offres individuelles et volumes datés 2024/2025/2026 | Non testés : quota WebSearch de la session épuisé (200/200) après 12 requêtes effectuées par cet agent | toutes, y compris l'intégralité du fichier VOLUMES (0 ligne) | Aucun | Aucune | Aucun compte d'offres (stock) disponible pour les trois zones ; échantillon limité à 4 sources (Indeed, France Travail, Apec, WTTJ) |
| LinkedIn (agent lyon) | https://fr.linkedin.com/jobs/view/ | 2026-09-06 | développeur full stack ; développeur web | Lyon ; Marseille | Offres individuelles et volumes | Requête non exécutée : quota WebSearch de session épuisé (200/200) au moment de l'appel | Toutes | Aucun (WebFetch/curl bloqués par le proxy selon REGLES_COLLECTE) | Indeed, France Travail, HelloWork, WTTJ, Apec | Sous-représentation des offres LinkedIn (souvent ESN et grands comptes) pour les deux zones |
| Free-Work (agent lyon) | https://www.free-work.com/ | 2026-09-06 | développeur full stack ; développeur | Lyon ; Marseille ; Aix-en-Provence | Offres freelance/CDI et volumes | Requête non exécutée : quota WebSearch de session épuisé (200/200) | Toutes (notamment TJM freelance) | Aucun | Aucune pour le freelance | Absence de données TJM/freelance pour Lyon et Marseille |
| Jooble (agent lyon) | https://fr.jooble.org/ | 2026-09-06 | non testé | non testé | Volumes et offres | Non testé : quota WebSearch épuisé avant d'atteindre cette plateforme | Toutes | Aucun | Indeed / HelloWork (volumes) | Pas de volume agrégateur de comparaison |
| Talent.com (agent lyon) | https://fr.talent.com/ | 2026-09-06 | non testé | non testé | Volumes et salaires | Non testé : quota WebSearch épuisé | Toutes | Aucun | HelloWork / France Travail (salaires quand indiqués) | Moins de points de salaire |
| Meteojob / Monster / JobTeaser / LesJeudis / ChooseYourBoss (agent lyon) | meteojob.com ; monster.fr ; jobteaser.com ; lesjeudis.com ; chooseyourboss.com | 2026-09-06 | non testé | non testé | Offres individuelles | Non testé : quota WebSearch épuisé | Toutes | Aucun | Indeed, France Travail, HelloWork, WTTJ, Apec | Couverture limitée à 5 sources ; offres stage/jeunes diplômés (JobTeaser) et ESN (LesJeudis) sous-représentées |
| Apec (pages de détail) (agent lyon) | https://www.apec.fr/candidat/recherche-emploi.html/emploi/detail-offre/ | 2026-09-06 | développeur full stack ; développeur | Lyon ; Marseille ; Aix-en-Provence | Détail des offres (entreprise, salaire, expérience) | Partiel : 4 URL d'offres individuelles obtenues (titres seulement) ; les extraits Apec sont du code de template/erreurs JS, aucune donnée de contenu | Entreprise, salaire, expérience, technologies, date | Requêtes ciblant les pages de liste Apec (motsCles=...) : pas de compte affiché | HelloWork / France Travail pour les salaires | Apec inutilisable pour les salaires cadres dans ces zones via WebSearch |
| Apec (Java/Spring) (agent paris) | https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=D%C3%A9veloppeur+Java+Spring | 2026-09-06 | développeur Java Spring Paris | Paris, Île-de-France, Hauts-de-Seine | URLs d'offres individuelles + comptes d'offres datés | Aucune page detail-offre indexée pour Java/Spring : seulement des pages de recherche (listes) sans compte d'offres dans le titre, et une page cadres.apec.fr signalée 'offre n'est plus disponible' | Offres individuelles Java/Spring Paris ; volumes Apec (pas de compte dans les titres) | site:apec.fr detail-offre développeur full stack Paris (5 offres obtenues) | Indeed / HelloWork / France Travail pour Java | Sous-représentation de l'Apec sur le segment Java ; volumes Apec absents |
| HelloWork (volumes via requête générique) (agent paris) | https://www.hellowork.com/fr-fr/emplois/ | 2026-09-06 | Développeur Full Stack Paris | Paris, Île-de-France, Hauts-de-Seine | URLs d'offres individuelles + comptes d'offres datés | La requête 'HelloWork Développeur Full Stack Paris Plus de Offres 2025' a renvoyé des pages Indeed et non HelloWork | Compte HelloWork 'Développeur full stack Paris' daté 2025 | Requêtes site:hellowork.com (fonctionnent : 13 volumes HelloWork obtenus par ailleurs) | Volumes Indeed équivalents | Faible : autres comptes HelloWork disponibles |
| Jooble / Meteojob / Monster / JobTeaser / LesJeudis / ChooseYourBoss (agent paris) | fr.jooble.org ; meteojob.com ; monster.fr ; jobteaser.com ; lesjeudis.com ; chooseyourboss.com | 2026-09-06 | développeur web / full stack / front-end / PHP Symfony / React | Paris, Île-de-France, Hauts-de-Seine | URLs d'offres individuelles + comptes d'offres datés | NON TESTEES : quota WebSearch de la session (200 appels partagés) épuisé après 18 requêtes de cet agent | Offres individuelles et volumes de ces plateformes pour Paris/IDF | WebFetch/curl interdits par les règles (proxy) | Indeed, France Travail, Apec, WTTJ, HelloWork, LinkedIn, Free-Work, Talent.com (couverts) | Couverture partielle des sources ; segments Java/.NET/Python/CMS e-commerce, stages, villes 93/94/78/91/95/77 peu ou pas explorés |
| HelloWork (agent regions) | https://www.hellowork.com/fr-fr/emploi/recherche.html | 2026-09-06 | Développeur web | Occitanie, Bretagne, Grand Est, Normandie, PACA, Auvergne-Rhône-Alpes, Télétravail | Volumes d'offres par région (titres 'Emploi Développeur web <région> - Plus de N offres') et offres individuelles | Requêtes lancées mais NON exécutées : quota WebSearch de la session épuisé (200/200) au moment du lancement | Toutes (volumes et offres HelloWork) | Aucun (WebFetch/curl bloqués par le proxy selon REGLES_COLLECTE) | Indeed (volumes datés 2024-2026 par ville et région) | Pas de contre-mesure HelloWork des stocks régionaux ; les volumes régionaux reposent uniquement sur Indeed |
| France Travail (agent regions) | https://candidat.francetravail.fr/offres/recherche | 2026-09-06 | Développeur web (non testé) | Régions hors IDF/Lyon/Marseille/Lille/Nantes/Bordeaux, télétravail (non testé) | Offres individuelles et volumes régionaux | Non testé : quota WebSearch épuisé avant d'atteindre cette source | Toutes | Aucun | Indeed | Absence de la source publique de référence pour les régions ; sous-représentation probable des PME et collectivités |
| Apec (agent regions) | https://www.apec.fr/candidat/recherche-emploi.html | 2026-09-06 | Développeur web (non testé) | Régions (non testé) | Offres cadres et volumes par région | Non testé : quota WebSearch épuisé | Toutes | Aucun | Indeed | Pas de vue sur les postes cadres régionaux ni sur les salaires Apec |
| Welcome to the Jungle (agent regions) | https://www.welcometothejungle.com/fr/jobs | 2026-09-06 | Développeur web (non testé) | Régions, full remote (non testé) | Offres individuelles startups/scale-ups et full remote | Non testé : quota WebSearch épuisé | Toutes | Aucun | Indeed (offres 'Télétravail') | Sous-représentation des offres startups et full remote |
| LinkedIn / Free-Work / Jooble / Talent.com / Meteojob / Monster / JobTeaser / LesJeudis / ChooseYourBoss (agent regions) | NC | 2026-09-06 | Non testé | Non testé | Offres individuelles et volumes régionaux | Non testé : quota WebSearch de session épuisé (200/200) après 24 requêtes de cet agent | Toutes | Aucun | Indeed | Couverture mono-source (Indeed) pour les régions ; freelance (Free-Work) et jeunes diplômés (JobTeaser) non couverts |

### B.4 — Études et sources documentaires recherchées sans résultat exploitable

| SOURCE | REQUETES | RESULTAT |
|---|---|---|
| France Travail (candidat.francetravail.fr) | Q025 | Pages de liste indexées (Développeur informatique s28m1, Développeur web s28m7 / s29m2, Développeur php s28m6, Développeur front end s29m11, Développeur .net s29m8, Paris, Montpellier) mais aucun nombre d'offres ni date dans les titres/extraits. |
| Apec (apec.fr recherche-emploi) | Q026 | Pages de recherche 'Offres d'emploi Développeur Web Full-Stack', 'Developpeur Full Stack', 'Full stack Developer', stage Full-Stack indexées ; aucun compte ni date dans titres/extraits. |
| Welcome to the Jungle (pages emploi-developpeur*) | Q027 | Pages thématiques (développeur, développeur web, back-end, front-end, java, IA, télétravail) indexées sans nombre d'offres ni date. |
| Onisep / France Travail / Apec — fiche 'développeur augmenté' | Q096 | Aucune fiche métier intitulée 'développeur augmenté' trouvée ; fiches classiques Onisep (developpeur-developpeuse-informatique) et Apec (developpeur) seulement. |
| GitHub Octoverse 2025 — données France | Q089 | Rapport trouvé (international) mais aucun chiffre spécifique à la France dans les extraits. |
| Dares / France Stratégie / CAE — étude IA générative et développeurs 2025-2026 | Q092 | Pas d'étude ciblée développeurs trouvée ; résultats : séminaire Dares IA et emploi (page événement), Métiers 2030, panorama Unédic janv. 2025, étude CESE. |
| Déclarations de dirigeants d'ESN françaises (Capgemini, Sopra Steria, Atos, CGI, Accenture France) sur juniors et IA | Q095 ; Q112 | Aucune interview ou déclaration nominative trouvée ; seulement pages carrières (Sopra Steria 8 500 postes 2026, Capgemini jeunes diplômés) et relais presse (plan RCC Capgemini 2 409 postes). |
| BMO 2026 — FAP 'techniciens d'étude et de développement en informatique' (projets par région) | Q124 | Aucun chiffre trouvé pour cette FAP via WebSearch ; le portail statistiques.francetravail.org/bmo (interactif) n'est pas indexé par métier/région dans les extraits. |
| BMO 2026 — Bretagne, Grand Est, Normandie, Bourgogne-Franche-Comté, Corse (ingénieurs informatique) | Q123 | Seuls des totaux régionaux tous métiers ou des pages d'accueil trouvés ; pas de chiffre par métier informatique. |
| BMO 2026 — bassins Paris, Lyon, Lille, Bordeaux, Nantes, Marseille, Aix, Toulouse (PDF bassin) | Q125 | PDF par bassin existent (ex. Beauvais HDF, La CASA PACA) mais aucun PDF des bassins NEXA n'est remonté dans les résultats. |
| Marseille / Aix-en-Provence — effectifs emploi numérique et recruteurs chiffrés | Q139 | Pages French Tech Aix-Marseille et Invest in Provence trouvées, sans chiffre d'emplois numériques ni nombre de startups dans les extraits. |
| INSEE — population active / emploi total par région (tableau 13 régions 2024-2025) | Q131 ; Q144 | Pages INSEE identifiées (Activité, emploi et chômage 2024/2025 ; Emploi dans les régions ; Insee Focus 373) mais seules quelques valeurs apparaissent dans les extraits (France 30,5 M fin 2024 ; ARA 3,7 M fin 2023). Le tableau complet n'est pas accessible via WebSearch. |
| Numeum — effectifs numérique par région (panorama régional) | Q132 ; Q150 | Aucune ventilation régionale trouvée (Numeum Tour 2025-2026 et données nationales seulement). |
| Apec — offres/recrutements cadres informatique par région (HDF, NAQ, PDL, PACA, Occitanie, Bretagne) | Q128 ; Q129 ; Q143 ; Q148 | Chiffres régionaux trouvés uniquement pour IDF (143 000 cadres, +5 %) et ARA (34 100 en 2025, 35 260 en 2026) ; PDF PACA-Corse identifié sans extrait ; pas de chiffre 'informatique' par région. |
| Free-Work / Welcome to the Jungle — nombre d'offres développeur (comptes datés) | Q029 ; Q027 ; Q195 ; Q196 | Pages de liste indexées sans compte daté dans les titres ; Free-Work donne seulement des comptes non datés dans les extraits (29 'Développement', 8 'Flutter', 15 000+ total) et un TJM fullstack 550 €. |
| BMO 2026 — chiffres par bassin pour Lyon, Bordeaux, Nantes, Marseille, Aix, Toulouse (ingénieurs informatique) | Q125 ; Q146 ; Q181 ; Q187 ; Q188 ; Q189 ; Q190 ; Q191 ; Q197 ; Q198 ; Q199 | Les portails régionaux (observatoire-emploi-ara.fr, -nouvelle-aquitaine.fr, -paysdelaloire.fr, statistiques.francetravail.org/bmo) publient les fiches par bassin mais aucune valeur métier par bassin NEXA n'est remontée dans les extraits WebSearch. Seul le bassin de Lille (BMO 2023 : 5,0 % des intentions) et l'IDF (4 060 projets en 2026) sont chiffrés. |
| Dares — indicateur de tension par région pour 'ingénieurs de l'informatique' | Q130 ; Q149 ; Q177 ; Q200 | Valeurs nationales trouvées (indicateur 1,1 en 2023 ; 42 635 projets ; 67 % difficiles) ; aucune valeur régionale extraite (fiche 'M - Informatique' PDF et arrêté du 21 mai 2025 identifiés mais non lus). |
| INSEE — population active / emploi total pour les 13 régions 2024-2025 (tableau complet) | Q131 ; Q144 ; Q154 ; Q160 ; Q176 | Uniquement : France 30,5 M en emploi fin 2024 ; ARA 3,72 M emplois 2023 ; IDF taux d'emploi 68,4 % et chômage 7,0 % (2024) ; HDF chômage 9,6 % fin 2025 ; population 2021 par région. Le tableau régional complet (séries longues 2025, insee.fr/fr/statistiques/8977307) n'est pas lisible via WebSearch. |
| Data Emploi (dataemploi.francetravail.fr, ROME M1805) |  | Requêtes non exécutées : quota WebSearch de la session épuisé (200/200) après 45 requêtes D1 ; aucune page dataemploi n'est remontée dans les requêtes France Travail précédentes |
| France Travail - pages de liste (candidat.francetravail.fr/offres/emploi/... et /offres/recherche?motsCles=) |  | Les pages de liste France Travail remontent dans les résultats mais leur titre ('Offres d'emploi Développeur web - Informatique et télécoms - Caen / France Travail') ne contient aucun compte ; les extraits résumés n'en donnent pas non plus. Seule exception : 'N offres d'emploi pour <mot-clé>' apparaît pour des mots-clés génériques (ex. '5962 offres d'emploi pour tours', non pertinent) |
| France Travail - offres individuelles Corse, Antilles-Guyane, Mayotte, Orléans, Amiens, Poitiers/Limoges, Nice/Sophia, Clermont-Ferrand, Vannes/Lorient/Quimper, Le Havre |  | Très peu ou aucune offre de développement indexée : Corse 3 offres (2 datées 2025), Martinique 1, Réunion 4, Mayotte/Guadeloupe/Guyane 0, Orléans 0, Amiens 0, Poitiers/Limoges 0 (seulement testeur QA), Nice 0, Clermont 0, Vannes/Lorient/Quimper 1 (Angular/.NET Quimper), Le Havre 0 (hors GTB/industrie) |
| Apec (apec.fr, pages détail-offre) |  | Les pages détail-offre remontent bien via WebSearch (titre exact avec ville/département et souvent date de publication), mais le résumé renvoyé par l'outil ne restitue jamais le bloc salaire / expérience / contrat / télétravail / entreprise des offres ; 12 requêtes ciblées sur les termes 'k€ brut annuel', 'brut annuel', 'Minimum 3 ans', 'Débutant accepté', 'A négocier', 'Télétravail partiel' n'ont |
| Apec (pages de liste recherche-emploi.html/emploi?motsCles=...) |  | Les pages de liste Apec sont indexées (titres 'Offres d'emploi Développeur web', 'Offres d'emploi - septembre 2026') mais leur contenu est chargé dynamiquement : aucun compte d'offres n'apparaît dans les titres ni dans les extraits, contrairement à Indeed/HelloWork. |
| Jooble / Talent.com / Jobijoba / Meteojob / Monster / LinkedIn / JobTeaser / Glassdoor / Optioncarriere / Free-Work |  | NON TESTÉES : le budget WebSearch de la session (plafond 200 requêtes, partagé) a été épuisé après 48 requêtes D4, toutes consacrées à Indeed France (source prioritaire) ; 8 requêtes villes moyennes Indeed ont aussi été refusées |
| Free-Work (TJM / rémunération freelance) |  | Les requêtes 'TJM' OR '€/jour' ne remontent que des pages de liste et des pages baromètre (ex. 'TJM : Développeur fullstack', moyenne 550 €/jour) ; aucune page d'offre individuelle avec TJM affiché dans l'extrait |
| Free-Work (offres IA / LLM) |  | Seules des pages de liste par mot-clé (LLM, IA, Agent IA, Copilot, Prompt Engineering, IA Générative) sont indexées ; les extraits décrivent des missions (Senior AI Developer Montpellier, AI Agents Developer Paris banque privée, consultant GenAI assurance) sans URL individuelle |
| JobTeaser |  | L'indexation privilégie les pages de recherche datées (comptes d'offres exploitables en volumes : 22 alternances web Paris août 2025, 54 dev info Paris février 2026, 3 Lyon / 1 Nantes / 1 Lille juin 2026, 16 web Lille mars 2026) ; seulement 2 offres individuelles remontées (Ayvens, Sopra Steria .NET Lyon) |
| Monster, Meteojob, Talent.com, Jooble, LesJeudis, ChooseYourBoss, Glassdoor, cabinets (Hays, Robert Half, Michael Page, Silkhom, Urban Linker, Mobiskill, Nextep, Blue Search) |  | NON TESTÉ : le budget WebSearch de la session (200/200 requêtes, partagé) a été épuisé après la 28e requête de l'agent D5 ; 10 requêtes préparées (Toulouse/Montpellier, Rennes/Strasbourg/Grenoble, LinkedIn junior Paris, LinkedIn senior Lille/Marseille, LesJeudis, ChooseYourBoss, Monster, Meteojob, Talent.com, Jooble) ont été refusées |
| Indeed (filtre 'Débutant accepté' / 'sans expérience') |  | 8 requêtes 'Débutant accepté' : aucune page viewjob développeur indexée avec cette mention dans les six zones ; seules des pages de liste (comptes datés) ou des offres hors informatique (soins) remontent. Une seule offre 'débutant(e) accepté(e)' trouvée, hors zone (La Roche-sur-Yon). |
| Indeed Hiring Lab – 'AI and job postings: from destruction to creation' (08/07/2026), part des offres mentionnant l'IA en France, GenAI skills in French job postings | Indeed Hiring Lab France software development job postings 2026 (exécutée : URL article et série FRED trouvées, chiffres France absents des extraits) ; Indeed Hiring Lab "from destruction to creation" AI job postings July 2026 software developers France share (non exécutée, quota) ; Indeed Hiring La | URL article et série FRED IHLIDXFRTPSOFTDEVE identifiées mais aucune valeur d'indice ni part IA France dans les extraits ; quota WebSearch épuisé avant approfondissement |
| HelloWork / Hellowork Group – baromètre emploi tech 2026, salaires développeurs | HelloWork baromètre emploi tech 2026 offres développeurs salaires étude (non exécutée, quota) | Non couvert (quota). Seuls deux articles HelloWorkPlace relayant BMO/Apec ont été captés incidemment |
| Welcome to the Jungle études 2026 | aucune exécutée (quota épuisé avant) | Non couvert |
| Free-Work / Freelance-Informatique baromètre freelance tech 2026 | Free-Work baromètre freelance tech 2026 TJM développeur missions (non exécutée, quota) | Non couvert |
| Malt baromètre freelances tech 2026 | Malt baromètre freelances tech 2026 développeurs IA (non exécutée, quota) | Non couvert |
| LinkedIn métiers en croissance France 2026, JobTeaser, Glassdoor | aucune exécutée (quota) | Non couvert |
| Stack Overflow Developer Survey 2026, GitHub Octoverse, JetBrains State of Developer Ecosystem, Gartner, McKinsey | Stack Overflow Developer Survey 2026 AI tools usage results (non exécutée, quota) | Non couvert (international) |
| Stanford 'Canaries in the coal mine' (Brynjolfsson), Anthropic Economic Index | aucune exécutée (quota) | Non couvert (international) |
| Études françaises IA et emploi : France Stratégie, Institut Montaigne, CAE, Bpifrance, France Travail 'IA et emploi', Dares IA développeurs | aucune requête dédiée exécutée (quota) | Non couvert ; seul un article Blog du Modérateur (emploi <30 ans informatique -3 % 2023-2025) et l'analyse Numeum S1 2026 (impact IA limité sur les effectifs) ont été captés |
| France Stratégie / Dares 'Métiers 2030', portraits statistiques Dares, emploi cadres informatique Dares | aucune requête dédiée exécutée (quota) | Non couvert |
| Grande École du Numérique, Onisep, ROME M1805 / ROME 4.0, Talents du numérique, Syntec | aucune exécutée (quota) | Non couvert (une page Syntec présentant l'OPIIEC a été captée incidemment : https://www.syntec.fr/branche-instances/opiiec-observatoire-prospectif-des-metiers-et-des-qualifications/) |
| BMO 2026 – chiffres nationaux par métier 'ingénieurs et cadres d'étude, R&D en informatique' et 'techniciens d'étude et de développement en informatique' | BMO 2026 "ingénieurs et cadres d'étude, R&D en informatique" projets de recrutement ; BMO 2024 France Travail "techniciens d'étude et de développement en informatique" | Pas de chiffre national par métier dans les extraits ; seules données captées : 79 297 projets info-télécoms (BMO 2024, Labo Société Numérique), 84 227 projets numérique 49,5 % difficiles (BMO 2025, Afpa), IDF numérique 15 492 projets 52,5 % difficiles (BMO 2026). Base consultable : https://statistiques.francetravail.org/bmo |
| Apec baromètres trimestriels T1/T2 2026 – valeurs chiffrées | Apec baromètre offres d'emploi cadres 2026 trimestre informatique développeurs | URLs des baromètres T1 et T2 2026 identifiées, mais aucune valeur chiffrée dans les extraits |
| Apec autres régions (Hauts-de-France, Nouvelle-Aquitaine, Pays de la Loire, PACA, Occitanie) | aucune exécutée (quota) ; seules AURA et IDF couvertes | Non couvert |
| Apec métiers en tension informatique 2026 ; Apec salaires 2026 (édition 2026) | Apec salaires informatique 2026 développeur cadres rémunération (exécutée : renvoie l'étude déc. 2024 / relais 2025) | Pas d'édition 2026 identifiée ; données 2024-2025 uniquement |
| Insee note de conjoncture nationale emploi NAF 62 2025-2026 | Insee emploi salarié "programmation, conseil et autres activités informatiques" 2025 2026 évolution | Seule la note régionale IDF T1 2026 (-2,2 % heures rémunérées) captée ; pas de chiffre national dans les extraits |
| Presse : JDN, ZDNet France, Silicon.fr, L'Usine Digitale, Les Echos, BFM, Maddyness, 'job apocalypse développeurs juniors France 2026' | aucune requête dédiée (quota) ; captés incidemment : Le Monde Informatique (3 articles), ChannelNews (2), IT for Business, Programmez, Blog du Modérateur (2), L'Essentiel de l'Éco, News Tank RH (2), TPE Actu | Partiellement couvert via captures incidentes |
| BMO | BMO 2026 Grand Est projets de recrutement France Travail difficiles ; "BMO 2026" "Grand Est" "projets de recrutement" France Travail | Aucun chiffre régional Grand Est dans les extraits ; seul le portail statistiques.francetravail.org/bmo/geo est signalé (non lisible via WebSearch) |
| BMO | "BMO 2026" Corse projets de recrutement France Travail | Aucun chiffre régional Corse dans les extraits |
| BMO | BMO 2026 Hauts-de-France projets de recrutement France Travail chiffres région ; "BMO 2026" "Hauts-de-France" projets de recrutement total région difficiles | Seul le Nord (>68 000) est chiffré ; page régionale existe: https://www.francetravail.org/regions/hauts-de-france/statistiques-analyses/entreprises/enquete-bmo/enquete-besoins-en-main-d-oeuvre-bmo-2026.html?type=article mais chiffre non présent dans l'extrait |
| BMO | BMO 2026 Auvergne-Rhône-Alpes ingénieurs informatique projets de recrutement ; France Travail BMO 2026 Nouvelle-Aquitaine informatique ingénieurs projets ; BMO 2026 Bretagne projets de recrutement France Travail numérique informatique ; BMO 2026 Occitanie projets de recrutement informatique numériqu | Les communiqués régionaux ne détaillent pas les métiers informatiques dans les extraits WebSearch ; le détail existe sur statistiques.francetravail.org/bmo (paramètres fa=code région, fe=M2X90 = famille métier) mais non lisible sans WebFetch. Seule IDF (4 060 ingénieurs R&D info) et Bretagne 2024 (~3 000 info/télécom) obtenues. |
| BMO | "BMO 2026" Occitanie "projets de recrutement" Toulouse Haute-Garonne | Aucun chiffre par bassin obtenu (seulement départements 13, 06, 83, 84, 04, Nord >68 000 ; Haute-Garonne+Hérault = 42 % Occitanie). Recherches par bassin non lancées : budget WebSearch épuisé. |
| BMO |  | Non recherché : budget WebSearch épuisé avant ce thème |
| BMO |  | Seule Occitanie 2025 (218 000) obtenue incidemment ; évolutions 2025->2026 en % disponibles pour IDF (-11,8), NA (-8), Occitanie (-8), PACA (-2,6), Bretagne (-0,1), BFC (-1 660), Normandie (difficultés -5 pts). Recherches BMO 2025 dédiées non lancées : budget épuisé. |
| DARES | Dares tensions marché du travail 2025 "ingénieurs de l'informatique" indicateur de tension par région ; Dares "les tensions sur le marché du travail en 2024" métiers les plus en tension informatique ; Dares tensions 2025 ingénieurs informatique baisse tension région Île-de-France Auvergne-Rhône-Alpe | Requêtes refusées : budget WebSearch de session épuisé (200/200). Aucune donnée Dares collectée. Une synthèse tierce existe (france-carrieres.fr/guides/metiers-en-tension-2026-par-region) repérée dans un résultat antérieur, non exploitée. |
| JOBBOARDS | Hellowork emploi développeur web Occitanie offres nombre ; Indeed emplois développeur Toulouse (31) offres ; Hellowork emploi développeur Lyon offres nombre | Requêtes refusées : budget WebSearch épuisé. Aucun comptage d'offres collecté pour aucune zone. |
| INSEE |  | Non recherché : budget WebSearch épuisé avant ce thème. Ratio offres / 100 000 actifs non calculable. |
| TELETRAVAIL |  | Non recherché : budget WebSearch épuisé avant ce thème. |
| ECOSYSTEMES |  | Non recherché : budget WebSearch épuisé avant ce thème. Seuls indices incidents : Lille (tissu diversifié, numérique cité, Popmood) ; Occitanie (aéronautique, spatial, numérique) ; ARA (dev/chef de projet/infra top 3 Apec). |

### B.5 — Journaux de requêtes

1066 requêtes journalisées (fichiers `collecte/*_journal.txt`). Extrait :

- `site:fr.indeed.com "Développeur web" Toulouse emplois | offres individuelles: 0 | volumes: oui`
- `site:fr.indeed.com "Développeur web" Occitanie "emplois" | offres individuelles: 0 | volumes: oui`
- `site:fr.indeed.com "Développeur web" Montpellier emplois | offres individuelles: 0 | volumes: oui`
- `site:fr.indeed.com "Développeur web" Rennes emplois | offres individuelles: 0 | volumes: oui`
- `site:fr.indeed.com "Développeur web" Strasbourg emplois | offres individuelles: 0 | volumes: oui`
- `site:fr.indeed.com "Développeur web" Bretagne emplois | offres individuelles: 0 | volumes: oui`
- `site:fr.indeed.com "Développeur web" Grenoble emplois | offres individuelles: 0`
- `site:fr.indeed.com "Développeur web" Nice emplois | offres individuelles: 0`
- `site:fr.indeed.com "Développeur web" Rouen emplois | offres individuelles: 0`
- `site:fr.indeed.com "Développeur web" Tours emplois | offres individuelles: 0`
- `site:fr.indeed.com "Développeur web" Dijon emplois | offres individuelles: 0`
- `site:fr.indeed.com "Développeur web" Nancy emplois | offres individuelles: 1`
- `site:fr.indeed.com/viewjob développeur web Toulouse | offres individuelles: 8`
- `site:fr.indeed.com/viewjob développeur full stack Montpellier | offres individuelles: 8`
- `site:fr.indeed.com/viewjob développeur web Rennes | offres individuelles: 5`
- `site:fr.indeed.com/viewjob développeur web Strasbourg | offres individuelles: 3`
- `site:fr.indeed.com/viewjob développeur web Grenoble | offres individuelles: 6`
- `site:fr.indeed.com/viewjob développeur web Nice OR Sophia-Antipolis | offres individuelles: 2`
- `site:fr.indeed.com/viewjob développeur web Rouen OR Caen OR "Le Havre" | offres individuelles: 4`
- `site:fr.indeed.com/viewjob développeur web Tours OR Orléans | offres individuelles: 3`
- `site:fr.indeed.com/viewjob développeur web Dijon OR Besançon | offres individuelles: 8`
- `site:fr.indeed.com/viewjob développeur web Nancy OR Metz OR Reims | offres individuelles: 5`
- `site:fr.indeed.com/viewjob développeur web "télétravail" OR "full remote" OR "100% télétravail" | offres individuelles: 8`
- `site:fr.indeed.com/viewjob développeur web Clermont-Ferrand OR Annecy OR Saint-Étienne | offres individuelles: 3`
- `site:hellowork.com "Emploi Développeur web" Occitanie OR Toulouse "offres" | NON EXECUTEE : budget WebSearch de session épuisé (200/200) | offres individuelles: 0`
- `site:hellowork.com "Emploi Développeur web" Bretagne OR Rennes "offres" | NON EXECUTEE : budget WebSearch épuisé | offres individuelles: 0`
- `site:hellowork.com "Emploi Développeur web" "Grand Est" OR Strasbourg "offres" | NON EXECUTEE : budget WebSearch épuisé | offres individuelles: 0`
- `site:hellowork.com "Emploi Développeur web" Normandie OR Rouen "offres" | NON EXECUTEE : budget WebSearch épuisé | offres individuelles: 0`
- `site:hellowork.com "Emploi Développeur web" "Télétravail" OR "full remote" "offres" | NON EXECUTEE : budget WebSearch épuisé | offres individuelles: 0`
- `site:hellowork.com "Emploi Développeur web" "Provence-Alpes-Côte d'Azur" OR Nice OR "Auvergne-Rhône-Alpes" "offres" | NON EXECUTEE : budget WebSearch épuisé | offres individuelles: 0`
- `site:fr.indeed.com/viewjob développeur web Paris => 8 offre(s) individuelle(s)`
- `site:candidat.francetravail.fr/offres/recherche/detail développeur web Paris => 4 offre(s) individuelle(s)`
- `site:apec.fr detail-offre développeur full stack Paris => 5 offre(s) individuelle(s)`
- `site:welcometothejungle.com/fr/companies développeur full stack Paris CDI => 10 offre(s) individuelle(s)`
- `site:hellowork.com/fr-fr/emplois développeur web Paris => 8 offre(s) individuelle(s)`
- `Indeed "Développeur Web" Paris "plus de" emplois 2026 => 0 offre(s) individuelle(s)`
- `site:fr.indeed.com/viewjob développeur full stack Paris CDI => 9 offre(s) individuelle(s)`
- `site:fr.linkedin.com/jobs/view développeur full stack Paris => 9 offre(s) individuelle(s)`
- `site:free-work.com développeur React Paris => 6 offre(s) individuelle(s)`
- `site:candidat.francetravail.fr/offres/recherche/detail développeur full stack Île-de-France => 6 offre(s) individuelle(s)`
