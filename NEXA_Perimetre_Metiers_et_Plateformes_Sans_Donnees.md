# NEXA — Périmètre des métiers et plateformes sans données

Étude du marché de l'emploi du développement web en France — journal séparé de la collecte. Date de collecte : 2026-09-06. Voir aussi le fichier Excel (onglet OFFRES_DETAILLEES) et le document Word de synthèse.

## Contexte technique de la collecte

- L'environnement d'exécution ne permettait aucun accès HTTP direct aux sites externes (proxy réseau : toutes les connexions vers les jobboards, France Travail, Apec, data.gouv.fr, INSEE, Dares, Numeum, etc. ont été refusées avec un code 403 au niveau du proxy ; l'API France Travail nécessite en outre une clé OAuth non disponible).
- Seule voie disponible : un moteur de recherche web renvoyant, pour chaque requête, les titres, URL et extraits des pages publiques indexées. Toutes les offres et tous les comptes d'offres proviennent donc de ces pages indexées (pages d'offres individuelles et pages de liste datées des jobboards).
- Le budget de requêtes était plafonné (200 requêtes par session) ; la collecte a été répartie sur plusieurs sessions parallèles. Les journaux de requêtes sont conservés (fichiers *_journal.txt du dossier `collecte/`).
- Conséquences : de nombreux champs (expérience, salaire, télétravail) ne figurent pas dans les extraits et sont notés NC ; les comptes d'offres des pages de liste sont des bornes basses arrondies (« plus de N »).

## PARTIE A — TAXONOMIE DES MÉTIERS

Taxonomie initiale du brief complétée par les métiers découverts pendant la collecte. Nombre d'offres = offres uniques observées dans l'échantillon (328 offres uniques dans le périmètre, 354 lignes brutes).

### Développeur web

- INTITULE_NORMALISE : Développeur web (intitulé générique)
- VARIANTES_FRANCAISES : Développeur web ; Développeuse web ; Développeur internet ; Développeur d'applications web
- VARIANTES_ANGLAISES : Web Developer ; Web Engineer
- TECHNOLOGIES_ASSOCIEES : HTML/CSS, JavaScript, PHP, frameworks web
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Métier de référence
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulé générique du cœur de marché ; regroupé sous 'Développeur web (intitulé générique)' quand aucune techno ni couche n'est précisée.
- OFFRES_OBSERVEES : 43 unique(s) / 50 brute(s)
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
- OFFRES_OBSERVEES : 27 unique(s) / 27 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur front-end React Angular Vue Paris` ; `site:welcometothejungle.com/fr/companies développeur front-end Paris` ; `site:candidat.francetravail.fr/offres/recherche/detail développeur front-end Paris` ; `site:apec.fr detail-offre développeur front-end OR back-end Paris`

### Développeur back-end

- INTITULE_NORMALISE : Développeur back-end
- VARIANTES_FRANCAISES : Développeur back ; Développeur backend ; Développeur serveur
- VARIANTES_ANGLAISES : Back-End Developer ; Backend Engineer ; Server-side Developer
- TECHNOLOGIES_ASSOCIEES : Node.js, PHP/Symfony/Laravel, Java/Spring, .NET, Python/Django, SQL
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Couche serveur, API et données des applications web.
- OFFRES_OBSERVEES : 7 unique(s) / 8 brute(s)
- REQUETES_UTILISEES : `site:apec.fr detail-offre développeur front-end OR back-end Paris`

### Développeur full stack

- INTITULE_NORMALISE : Développeur full stack
- VARIANTES_FRANCAISES : Développeur fullstack ; Développeur full-stack ; Développeur web full stack
- VARIANTES_ANGLAISES : Full Stack Developer ; Full-Stack Engineer
- TECHNOLOGIES_ASSOCIEES : JS/TS + framework back (Node, Symfony, Spring, .NET, Django)
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulé dominant du marché : couvre front et back.
- OFFRES_OBSERVEES : 122 unique(s) / 133 brute(s)
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
- OFFRES_OBSERVEES : 1 unique(s) / 1 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Concepteur développeur d'applications

- INTITULE_NORMALISE : Concepteur développeur d'applications / logiciel
- VARIANTES_FRANCAISES : Concepteur développeur ; Développeur d'applications ; Développeur applicatif ; Développeur informatique
- VARIANTES_ANGLAISES : Application Developer ; Software Developer
- TECHNOLOGIES_ASSOCIEES : Java, .NET, PHP, JavaScript
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulé des titres RNCP et de nombreuses ESN ; inclut le développement d'applications web.
- OFFRES_OBSERVEES : 7 unique(s) / 8 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Développeur JavaScript / TypeScript

- INTITULE_NORMALISE : Développeur JavaScript / TypeScript
- VARIANTES_FRANCAISES : Développeur JS ; Développeur TypeScript ; Développeur Node.js ; Développeur React ; Développeur Angular ; Développeur Vue.js
- VARIANTES_ANGLAISES : JavaScript Developer ; TypeScript Developer ; React Developer ; Angular Developer ; Vue Developer ; Node.js Developer
- TECHNOLOGIES_ASSOCIEES : JavaScript, TypeScript, React, Angular, Vue.js, Node.js, Next.js, NestJS
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Regroupe les intitulés par technologie JavaScript (front et back).
- OFFRES_OBSERVEES : 4 unique(s) / 4 brute(s)
- REQUETES_UTILISEES : `site:free-work.com développeur React Paris` ; `site:fr.indeed.com/viewjob développeur front-end React Angular Vue Paris`

### Développeur PHP / Symfony / Laravel

- INTITULE_NORMALISE : Développeur PHP / Symfony / Laravel
- VARIANTES_FRANCAISES : Développeur PHP ; Développeur Symfony ; Développeur Laravel
- VARIANTES_ANGLAISES : PHP Developer ; Symfony Developer ; Laravel Developer
- TECHNOLOGIES_ASSOCIEES : PHP, Symfony, Laravel, MySQL
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Très forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Écosystème web historique français (ESN, agences, éditeurs).
- OFFRES_OBSERVEES : 14 unique(s) / 15 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur PHP Symfony Paris`

### Développeur Java / Spring (web)

- INTITULE_NORMALISE : Développeur Java / Spring
- VARIANTES_FRANCAISES : Développeur Java ; Développeur Java web ; Développeur Spring ; Développeur Java/JEE
- VARIANTES_ANGLAISES : Java Developer ; Spring Developer ; Java Backend Engineer
- TECHNOLOGIES_ASSOCIEES : Java, Spring Boot, JEE, Hibernate, Angular/React associés
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Java web (Spring) est un des premiers volumes d'offres ; les offres Java embarqué/mainframe sont exclues.
- OFFRES_OBSERVEES : 7 unique(s) / 7 brute(s)
- REQUETES_UTILISEES : `site:apec.fr detail-offre développeur Java Spring Paris` ; `site:fr.indeed.com/viewjob développeur Java Spring Boot Paris`

### Développeur .NET / C#

- INTITULE_NORMALISE : Développeur .NET / C#
- VARIANTES_FRANCAISES : Développeur .NET ; Développeur C# ; Développeur ASP.NET
- VARIANTES_ANGLAISES : .NET Developer ; C# Developer
- TECHNOLOGIES_ASSOCIEES : C#, .NET, ASP.NET Core, SQL Server, Angular/React associés
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Stack web Microsoft, fréquente en ESN et éditeurs.
- OFFRES_OBSERVEES : 7 unique(s) / 7 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur .NET C# Paris`

### Développeur Python / Django

- INTITULE_NORMALISE : Développeur Python / Django
- VARIANTES_FRANCAISES : Développeur Python ; Développeur Django ; Développeur Flask
- VARIANTES_ANGLAISES : Python Developer ; Django Developer
- TECHNOLOGIES_ASSOCIEES : Python, Django, Flask, FastAPI
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Python web ; attention, beaucoup d'offres 'développeur Python' relèvent de la data (exclues si sans composante web).
- OFFRES_OBSERVEES : 4 unique(s) / 4 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur Python Django Paris`

### Développeur CMS / e-commerce

- INTITULE_NORMALISE : Développeur CMS / e-commerce
- VARIANTES_FRANCAISES : Développeur WordPress ; Développeur Drupal ; Développeur Shopify ; Développeur PrestaShop ; Développeur Magento ; Développeur e-commerce
- VARIANTES_ANGLAISES : WordPress Developer ; Drupal Developer ; Shopify Developer ; Magento Developer ; E-commerce Developer
- TECHNOLOGIES_ASSOCIEES : WordPress, Drupal, Shopify, PrestaShop, Magento/Adobe Commerce, Sylius
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Développement sur CMS et plateformes e-commerce ; volumes faibles dans l'échantillon.
- OFFRES_OBSERVEES : 2 unique(s) / 2 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur WordPress OR Shopify OR PrestaShop OR Magento Paris`

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
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Développeur logiciel (autre langage web/back)

- INTITULE_NORMALISE : Développeur logiciel (autre langage web/back)
- VARIANTES_FRANCAISES : Développeur Go ; Développeur Rust ; Développeur Scala
- VARIANTES_ANGLAISES : Go Developer ; Rust Developer
- TECHNOLOGIES_ASSOCIEES : Go, Rust, Scala, Elixir
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Langages back modernes utilisés pour des services web ; ajouté à la marge.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob développeur Python Django Paris`

### Développeur (intitulé générique)

- INTITULE_NORMALISE : Développeur (intitulé générique)
- VARIANTES_FRANCAISES : Développeur ; Développeuse ; Développeur en alternance
- VARIANTES_ANGLAISES : Developer ; Programmer
- TECHNOLOGIES_ASSOCIEES : Non précisé
- FAMILLE : COEUR_DE_MARCHE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Intitulés sans précision de couche ni de techno ; rattachés au cœur de marché mais à lire avec prudence.
- OFFRES_OBSERVEES : 4 unique(s) / 5 brute(s)
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
- OFFRES_OBSERVEES : 2 unique(s) / 2 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Application Developer

- INTITULE_NORMALISE : Concepteur développeur d'applications / logiciel
- VARIANTES_FRANCAISES : Développeur d'applications
- VARIANTES_ANGLAISES : Application Developer
- TECHNOLOGIES_ASSOCIEES : Tous langages
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Regroupé avec 'Concepteur développeur d'applications' dans la normalisation.
- OFFRES_OBSERVEES : 7 unique(s) / 8 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

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
- OFFRES_OBSERVEES : 2 unique(s) / 2 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Développeur mobile

- INTITULE_NORMALISE : Développeur mobile
- VARIANTES_FRANCAISES : Développeur mobile ; Développeur iOS ; Développeur Android ; Développeur Flutter ; Développeur React Native
- VARIANTES_ANGLAISES : Mobile Developer ; iOS/Android Engineer
- TECHNOLOGIES_ASSOCIEES : Swift, Kotlin, Flutter, React Native
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Débouché adjacent naturel des développeurs JS (React Native) ; comptabilisé dans les évolutions, pas dans le cœur.
- OFFRES_OBSERVEES : 11 unique(s) / 11 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Tech Lead / Lead Developer

- INTITULE_NORMALISE : Tech Lead / Lead Developer
- VARIANTES_FRANCAISES : Tech lead ; Lead développeur ; Responsable technique
- VARIANTES_ANGLAISES : Tech Lead ; Lead Developer ; Engineering Manager
- TECHNOLOGIES_ASSOCIEES : Tous
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Évolution à 5+ ans ; cible de la communication Mastère.
- OFFRES_OBSERVEES : 5 unique(s) / 5 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "Tech Lead" développeur web Paris OR Lyon`

### Architecte logiciel / solutions

- INTITULE_NORMALISE : Architecte logiciel / solutions
- VARIANTES_FRANCAISES : Architecte logiciel ; Architecte applicatif ; Architecte solutions
- VARIANTES_ANGLAISES : Software Architect ; Solutions Architect
- TECHNOLOGIES_ASSOCIEES : Architecture, cloud, microservices
- FAMILLE : EVOLUTION_NATURELLE
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS
- JUSTIFICATION : Évolution senior ; cible Mastère.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

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
- OFFRES_OBSERVEES : 9 unique(s) / 9 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "DevOps Engineer" Lyon`

### Cloud Engineer

- INTITULE_NORMALISE : Cloud Engineer
- VARIANTES_FRANCAISES : Ingénieur cloud ; Développeur cloud native
- VARIANTES_ANGLAISES : Cloud Engineer ; Cloud Developer
- TECHNOLOGIES_ASSOCIEES : AWS, Azure, GCP, Kubernetes
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Compétence cloud demandée aux développeurs ; métier propre pour les seniors.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "Cloud Engineer" Nantes OR Bordeaux OR Toulouse OR Lille`

### Platform Engineer

- INTITULE_NORMALISE : Platform Engineer
- VARIANTES_FRANCAISES : Ingénieur plateforme
- VARIANTES_ANGLAISES : Platform Engineer
- TECHNOLOGIES_ASSOCIEES : Kubernetes, IaC
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Évolution du DevOps ; rare dans l'échantillon.
- OFFRES_OBSERVEES : 1 unique(s) / 1 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "Platform Engineer" France`

### Site Reliability Engineer (SRE)

- INTITULE_NORMALISE : Site Reliability Engineer (SRE)
- VARIANTES_FRANCAISES : Ingénieur fiabilité
- VARIANTES_ANGLAISES : SRE ; Site Reliability Engineer
- TECHNOLOGIES_ASSOCIEES : Observabilité, Kubernetes, cloud
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Métier d'exploitation logicielle ; profils seniors.
- OFFRES_OBSERVEES : 9 unique(s) / 10 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "SRE" OR "Site Reliability Engineer" Nantes OR Bordeaux OR Toulouse`

### QA / Test Automation Engineer

- INTITULE_NORMALISE : QA / Test Automation Engineer
- VARIANTES_FRANCAISES : Testeur automaticien ; Ingénieur test ; Ingénieur QA
- VARIANTES_ANGLAISES : QA Automation Engineer ; Test Automation Engineer ; SDET
- TECHNOLOGIES_ASSOCIEES : Cypress, Playwright, Selenium, Jest
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Contrôle qualité, renforcé par l'IA (validation des sorties).
- OFFRES_OBSERVEES : 2 unique(s) / 2 brute(s)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "QA Automation" OR "Test Automation Engineer" France`

### Ingénieur sécurité applicative / DevSecOps

- INTITULE_NORMALISE : Ingénieur sécurité applicative / DevSecOps
- VARIANTES_FRANCAISES : Ingénieur sécurité applicative ; DevSecOps ; Pentester applicatif
- VARIANTES_ANGLAISES : Application Security Engineer ; AppSec ; DevSecOps
- TECHNOLOGIES_ASSOCIEES : OWASP, SAST/DAST, IAM
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Passerelle vers la filière Cybersécurité NEXA.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "DevSecOps" OR "AppSec" OR "sécurité applicative" ingénieur`

### Développeur spécialisé accessibilité

- INTITULE_NORMALISE : Développeur spécialisé accessibilité
- VARIANTES_FRANCAISES : Développeur accessibilité ; Expert RGAA
- VARIANTES_ANGLAISES : Accessibility Developer
- TECHNOLOGIES_ASSOCIEES : RGAA, WCAG, ARIA
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Forte
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Aucune offre dédiée observée ; compétence citée dans quelques offres front.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Développeur Green IT / éco-conception

- INTITULE_NORMALISE : Développeur Green IT / éco-conception
- VARIANTES_FRANCAISES : Développeur éco-conception ; Green IT
- VARIANTES_ANGLAISES : Green Software Engineer
- TECHNOLOGIES_ASSOCIEES : Éco-conception, RGESN
- FAMILLE : SPECIALISATION
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (spécialisation)
- JUSTIFICATION : Aucune offre dédiée observée.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### AI Engineer / Développeur IA

- INTITULE_NORMALISE : AI Engineer / Développeur IA
- VARIANTES_FRANCAISES : Ingénieur IA ; Développeur IA ; Développeur intelligence artificielle ; Ingénieur en intelligence artificielle
- VARIANTES_ANGLAISES : AI Engineer ; AI Developer ; Applied AI Engineer ; Forward Deployed Engineer
- TECHNOLOGIES_ASSOCIEES : Python, LLM, API OpenAI/Mistral/Anthropic, LangChain, RAG, cloud
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne à forte
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Développement d'applications intégrant des modèles ; intitulé le plus fréquent de la famille IA dans l'échantillon.
- OFFRES_OBSERVEES : 18 unique(s) / 18 brute(s)
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
- OFFRES_OBSERVEES : 3 unique(s) / 4 brute(s)
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
- OFFRES_OBSERVEES : 8 unique(s) / 8 brute(s)
- REQUETES_UTILISEES : `site:hellowork.com/fr-fr/emplois "ingénieur IA générative"`

### Développeur RAG / applications LLM

- INTITULE_NORMALISE : Développeur RAG / applications LLM
- VARIANTES_FRANCAISES : Développeur RAG
- VARIANTES_ANGLAISES : RAG Developer
- TECHNOLOGIES_ASSOCIEES : RAG, bases vectorielles, LangChain/LlamaIndex
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Rarement un intitulé autonome ; plutôt une compétence citée.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : `site:fr.indeed.com/viewjob "développeur IA" LLM RAG`

### Développeur d'agents IA

- INTITULE_NORMALISE : Développeur d'agents IA
- VARIANTES_FRANCAISES : Développeur agents IA ; Ingénieur agentique
- VARIANTES_ANGLAISES : AI Agent Developer ; Agentic AI Engineer
- TECHNOLOGIES_ASSOCIEES : Agents, MCP, orchestration
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Émergent ; très peu d'offres.
- OFFRES_OBSERVEES : 1 unique(s) / 1 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### AI Integration / Automation Developer

- INTITULE_NORMALISE : AI Integration / Automation Developer
- VARIANTES_FRANCAISES : Développeur automatisation ; Intégrateur IA
- VARIANTES_ANGLAISES : AI Integration Engineer ; Automation Developer
- TECHNOLOGIES_ASSOCIEES : n8n, Make, API, LLM
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent)
- JUSTIFICATION : Automatisation de processus avec briques IA.
- OFFRES_OBSERVEES : 1 unique(s) / 2 brute(s)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Low-code / No-code Developer

- INTITULE_NORMALISE : Low-code / No-code Developer
- VARIANTES_FRANCAISES : Développeur low-code ; Développeur no-code ; Développeur Power Platform
- VARIANTES_ANGLAISES : Low-code Developer ; No-code Developer
- TECHNOLOGIES_ASSOCIEES : Power Platform, OutSystems, Mendix, Bubble
- FAMILLE : METIER_EMERGENT_IA (adjacent, compté à part)
- PROXIMITE_AVEC_LE_DEV_WEB : Faible à moyenne
- INCLUS_OU_EXCLU : INCLUS (émergent, à la marge)
- JUSTIFICATION : Aucune offre observée dans l'échantillon ; conservé pour veille.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

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
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Machine Learning / Data Engineer

- INTITULE_NORMALISE : Machine Learning / Data Engineer
- VARIANTES_FRANCAISES : Ingénieur machine learning ; Data engineer ; MLOps
- VARIANTES_ANGLAISES : ML Engineer ; Data Engineer ; MLOps Engineer
- TECHNOLOGIES_ASSOCIEES : Python, Spark, MLflow
- FAMILLE : METIER_ADJACENT
- PROXIMITE_AVEC_LE_DEV_WEB : Faible à moyenne
- INCLUS_OU_EXCLU : EXCLU DES VOLUMES (adjacent)
- JUSTIFICATION : Relève de la filière IA & Data ; compté à part.
- OFFRES_OBSERVEES : 0 unique(s) / 0 brute(s) (0 = aucune offre remontée par les requêtes, pas une preuve d'absence sur le marché)
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

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
- REQUETES_UTILISEES : `012`

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
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

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
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

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
- REQUETES_UTILISEES : requêtes génériques par ville et par technologie (voir journaux)

### Autres intitulés normalisés apparus dans la collecte

- Développeur logiciel hors web (embarqué, ERP, BI...) : 6 offre(s) unique(s)

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
| France Travail | 36 | Données obtenues |
| Apec | 16 | Données obtenues |
| Indeed | 156 | Données obtenues |
| LinkedIn | 10 | Données obtenues |
| Welcome to the Jungle | 72 | Données obtenues |
| HelloWork | 28 | Données obtenues |
| Meteojob | 0 | AUCUNE DONNÉE EXPLOITABLE |
| Monster | 0 | AUCUNE DONNÉE EXPLOITABLE |
| Talent.com | 2 | Données partielles |
| JobTeaser | 0 | AUCUNE DONNÉE EXPLOITABLE |
| Jooble | 0 | AUCUNE DONNÉE EXPLOITABLE |
| LesJeudis | 0 | AUCUNE DONNÉE EXPLOITABLE |
| ChooseYourBoss | 0 | AUCUNE DONNÉE EXPLOITABLE |
| Free-Work | 6 | Données partielles |
| Glassdoor | 0 | AUCUNE DONNÉE EXPLOITABLE |
| Site carrière | 1 | Données partielles |
| Autre | 1 | Données partielles |

### B.3 — Journal détaillé des plateformes sans données (par agent de collecte)

| PLATEFORME | URL | DATE_DU_TEST | METIERS_TESTES | ZONES_TESTEES | DONNEES_RECHERCHEES | RESULTAT | DONNEES_MANQUANTES | AUTRES_CHEMINS_TESTES | SOURCE_DE_REMPLACEMENT | IMPACT_SUR_L_ANALYSE |
|---|---|---|---|---|---|---|---|---|---|---|
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

109 requêtes journalisées (fichiers `collecte/*_journal.txt`). Extrait :

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
