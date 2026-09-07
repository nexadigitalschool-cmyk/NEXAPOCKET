# NEXA — Périmètre des métiers du Marketing Digital et plateformes sans données

**Étude :** Observatoire du marché de l'emploi du marketing digital en France · **Date de collecte :** 7 septembre 2026

Ce fichier constitue le **journal séparé de la collecte**. Il contient la taxonomie complète des métiers retenus et écartés (partie A) et le relevé des plateformes et chemins d'accès testés sans résultat exploitable (partie B). Ces éléments n'alourdissent volontairement pas le document de synthèse Word.

**Volumétrie de la collecte :** 507 lignes d'offres collectées · 504 offres uniques après dédoublonnage (taux de doublons 0.6 %) · 495 dans le périmètre marketing digital · 446 au cœur du marketing digital hors métiers adjacents · 12 exclues comme faux positifs · 90 stocks d'offres datés · 38 sources documentaires.

**Statuts de dédoublonnage observés :** OFFRE_UNIQUE : 504 · OFFRE_PROBABLEMENT_IDENTIQUE : 3

---

## PARTIE A — TAXONOMIE DES MÉTIERS

### A.0 Méthode de classification

Chaque intitulé brut d'offre est passé dans un jeu de **64 règles ordonnées** (des plus spécifiques aux plus générales) qui produisent trois valeurs : un métier normalisé, une famille et un niveau de technicité de base. Le niveau de technicité final est ensuite recalculé à partir des compétences réellement détectées dans le titre et l'extrait de l'offre, selon l'échelle suivante :

| Niveau | Définition | Déclencheurs |
|---|---|---|
| 1 | Généraliste / exécution | Publication réseaux sociaux, rédaction simple, emailing simple, coordination, animation, mise à jour de contenus |
| 2 | Expertise canal | SEO, SEA, Paid Social, CRM, e-commerce, content strategy, influence, plateformes publicitaires |
| 3 | Performance / data / automation | GA4, GTM, tracking, attribution, CRO, CRM automation, dashboards, segmentation, no-code, agents IA |
| 4 | MarTech / data / systèmes | CDP, SQL, BigQuery, data warehouse, API, gouvernance de la donnée, Python |

Une offre atteint le niveau 4 dès qu'une compétence de niveau 4 est détectée ; le niveau 3 requiert deux compétences de niveau 3 (ou une seule si le métier est déjà de technicité de base 3).

### A.1 Familles retenues

| Famille | Offres uniques | Part du périmètre | Technicité moyenne | Alternance | Débutants + juniors |
|---|---|---|---|---|---|
| `COEUR_GENERALISTE` | 111 | 22.4 % | 1.42 | 40.5 % | 47.7 % |
| `ACQUISITION_PERFORMANCE` | 85 | 17.2 % | 2.09 | 14.1 % | 17.6 % |
| `SEO_SEA` | 51 | 10.3 % | 2.0 | 11.8 % | 17.6 % |
| `METIER_ADJACENT` | 49 | 9.9 % | 1.53 | 34.7 % | 49.0 % |
| `SOCIAL_MEDIA` | 39 | 7.9 % | 1.03 | 25.6 % | 38.5 % |
| `CRM_LIFECYCLE` | 36 | 7.3 % | 2.5 | 16.7 % | 30.6 % |
| `DATA_ANALYTICS_CRO` | 31 | 6.3 % | 2.45 | 3.2 % | 16.1 % |
| `CONTENT_BRAND` | 29 | 5.9 % | 1.66 | 6.9 % | 20.7 % |
| `ECOMMERCE` | 28 | 5.7 % | 2.11 | 14.3 % | 21.4 % |
| `MARTECH_MARKETING_OPS` | 17 | 3.4 % | 2.82 | 0.0 % | 11.8 % |
| `METIER_IA_EMERGENT` | 10 | 2.0 % | 2.4 | 0.0 % | 10.0 % |
| `PRODUCT_MARKETING` | 9 | 1.8 % | 2.0 | 0.0 % | 0.0 % |

À ces familles s'ajoute `EXCLU_DU_PERIMETRE` : 12 offres écartées comme faux positifs (voir A.4).

### A.2 Fiches métiers observés dans l'étude

#### Growth Marketing Manager / Growth Manager

- **FAMILLE :** `ACQUISITION_PERFORMANCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.12 (moyenne observée sur 42 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Alternance - Growth marketing, lead génération & évènementiel (H/F) · Alternance Growth Marketing - SpeedPark x Games Factory · Alternance Growth Marketing F/H · Alternance – Growth Marketing & Events – B2B SaaS (H/F) · Alternant(e) Marketing Digital & Growth (H/F) · Chargé Growth Marketing
- **COMPETENCES_ASSOCIEES :** B2B · CRM (générique) · KPI / reporting / analyse de performance · HubSpot · Tracking / data layer / plan de taggage · Google Tag Manager / GTM · Réseaux sociaux (organique) · Google Analytics 4 / GA4
- **OUTILS_ASSOCIES :** Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 42 offres uniques (8.5 % du périmètre), issues de 4 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail marketing digital`
  - `site:fr.indeed.com/viewjob "acquisition" OR "growth" OR "performance" marketing CDI startup scale-up Paris 2026`
  - `site:fr.indeed.com/viewjob "growth marketing" OR "growth manager" France CDI`
  - `site:fr.indeed.com/viewjob "responsable marketing digital" Paris CDI 2026`

#### Traffic Manager

- **FAMILLE :** `ACQUISITION_PERFORMANCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.05 (moyenne observée sur 22 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Alternance Marketing Digital E-commerce (H/F) - Assistant Traffic Manager · CDI - Acquisition & Traffic Manager H/F · CDI - Lead Traffic Manager (H/F) · Consultant e-business & Traffic manager (H/F) · Traffic Manager · Traffic Manager / Consultant Paid Media
- **COMPETENCES_ASSOCIEES :** SEA / Paid Search · SEO · Meta Ads / Facebook Ads · E-commerce / gestion de site · Programmatique / DV360 · TikTok Ads · Réseaux sociaux (organique) · Pilotage budgétaire / média
- **OUTILS_ASSOCIES :** Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 22 offres uniques (4.4 % du périmètre), issues de 4 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail "traffic manager" OR "e-commerce" OR "growth" 2026`
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance marketing digital OR webmarketing 2026`
  - `site:fr.indeed.com/viewjob "traffic manager" OR "acquisition manager" CDI`
  - `site:www.hellowork.com/fr-fr/emplois "traffic manager" OR "social ads" OR "paid" CDI province France 2026`

#### Responsable / Chargé Acquisition

- **FAMILLE :** `ACQUISITION_PERFORMANCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 8 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternance - Assistant(e) Marketing et Acquisition Digitale (H/F) · CDI – Responsable Acquisition & Marketing Digital · Chargé(e) d'Acquisition & Relations Entreprises – Alternance (H/F) · Chef de Projets Campagnes Acquisition · Consultant Acquisition Digitale (H/F) · Responsable Acquisition
- **VARIANTES_ANGLAISES :** Chargé Acquisition & Traffic Management
- **COMPETENCES_ASSOCIEES :** SEO · Réseaux sociaux (organique) · Meta Ads / Facebook Ads · Google Ads · Gestion de projet · SEA / Paid Search · Programmatique / DV360 · KPI / reporting / analyse de performance
- **OUTILS_ASSOCIES :** Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 8 offres uniques (1.6 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM" HubSpot OR Salesforce OR Brevo chargé marketing France`
  - `site:fr.indeed.com/viewjob "consultant marketing digital" OR "consultant acquisition" agence CDI France`
  - `site:fr.indeed.com/viewjob "responsable e-commerce" OR "trafic" OR "acquisition" alternance Lyon Toulouse Nice Montpellier 2026`
  - `site:fr.indeed.com/viewjob "responsable marketing digital" Paris CDI 2026`

#### Media Buyer / Paid Media

- **FAMILLE :** `ACQUISITION_PERFORMANCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.4 (moyenne observée sur 5 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Media Buyer & Planner - Offline & Online (CDD) · Media Buyer - Télétravail · Trader media Programmatique - Alternance (H/F)
- **VARIANTES_ANGLAISES :** Consultant Paid Media F/H · Responsable Productivité & Investissement Media H/F
- **COMPETENCES_ASSOCIEES :** KPI / reporting / analyse de performance · API / webhook / intégrations · SEA / Paid Search · Stratégie marketing · Programmatique / DV360 · Business / ROI / revenue · Pilotage budgétaire / média
- **OUTILS_ASSOCIES :** Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 5 offres uniques (1.0 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "acquisition" OR "growth" OR "performance" marketing CDI startup scale-up Paris 2026`
  - `site:fr.indeed.com/viewjob "performance marketing" OR "media buyer" OR "paid media" CDI France`
  - `site:fr.indeed.com/viewjob "responsable e-commerce" OR "trafic" OR "acquisition" alternance Lyon Toulouse Nice Montpellier 2026`

#### Consultant / Manager Paid Social

- **FAMILLE :** `ACQUISITION_PERFORMANCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 4 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Consultant Paid Social Senior H/F · Consultant Social Ads · Expert Social Ads - Stratégie Créa & Performance (Meta / TikTok) · Senior Social Ads Manager [CDI]
- **COMPETENCES_ASSOCIEES :** Réseaux sociaux (organique) · SEO · SEA / Paid Search · Snapchat / Pinterest Ads
- **OUTILS_ASSOCIES :** Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 4 offres uniques (0.8 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "paid social" OR "social ads" OR "programmatique" France CDI agence média`
  - `site:fr.indeed.com/viewjob "paid social" OR "social ads" specialist CDI France`

#### Performance Marketing Manager

- **FAMILLE :** `ACQUISITION_PERFORMANCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 3 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Performance Marketing Manager · Performance Marketing Manager - Gaming · Performance Marketing Manager, Paris
- **COMPETENCES_ASSOCIEES :** non renseignées dans les extraits
- **OUTILS_ASSOCIES :** Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 3 offres uniques (0.6 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "acquisition" OR "growth" OR "performance" marketing CDI startup scale-up Paris 2026`
  - `site:fr.indeed.com/viewjob "marketing automation" specialist OR manager CDI France`
  - `site:www.hellowork.com/fr-fr/emplois "growth" OR "acquisition" OR "performance" marketing CDI Paris 2026`

#### Demand / Lead Generation Manager

- **FAMILLE :** `ACQUISITION_PERFORMANCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 1 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Responsable web & digital marketing (Lead generation) F/H
- **COMPETENCES_ASSOCIEES :** non renseignées dans les extraits
- **OUTILS_ASSOCIES :** Google Ads, Meta Ads, LinkedIn Ads, TikTok Ads, Microsoft Ads, Amazon Ads, DV360, Campaign Manager 360, GA4, GTM, Looker Studio
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 1 offres uniques (0.2 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "responsable acquisition" OR "demand generation" OR "lead generation" France`

#### Chargé de Marketing Digital

- **FAMILLE :** `COEUR_GENERALISTE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 1.17 (moyenne observée sur 36 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternance Chargé de Web-Marketing · Apprentissage - Chargé(e) de Marketing Digital Opérationnel · CHARGE(E) DÉVELOPPEMENT COMMERCIAL & MARKETING DIGITAL (H/F) · Chargé / Chargée marketing digital (H/F) · Chargé Marketing Digital & Communication H/F · Chargé Marketing Digital (H/F)
- **VARIANTES_ANGLAISES :** Chargé de Marketing Digital Alternance (Mastère Manager du Développement d'Entreprise)
- **COMPETENCES_ASSOCIEES :** Création de contenu / rédaction · SEO · CRM (générique) · Gestion de projet · KPI / reporting / analyse de performance · Réseaux sociaux (organique) · Emailing / newsletters / push · SEA / Paid Search
- **OUTILS_ASSOCIES :** WordPress, CMS, Google Analytics 4, Google Tag Manager, HubSpot, Canva, suite Adobe, Google Ads, Meta Ads
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 36 offres uniques (7.3 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance marketing digital OR webmarketing 2026`
  - `site:candidat.francetravail.fr/offres/recherche/detail marketing digital`
  - `site:fr.indeed.com/viewjob "AI marketing" OR "IA générative" marketing manager France 2026`
  - `site:fr.indeed.com/viewjob "CRO" OR "conversion rate optimization" OR "AB testing" marketing CDI France`

#### Assistant / Alternant Marketing Digital

- **FAMILLE :** `COEUR_GENERALISTE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 1.19 (moyenne observée sur 26 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** ALTERNANCE ASSISTANT(E) MARKETING DIGITAL - Marseille · ALTERNANCE MARKETING DIGITAL – MASTER 1 OU 2 · Alternance - Chargé(e) de Marketing Digital H/F · Alternance - Chef(fe) de projet Marketing Digital · Alternance Chargé de Marketing Digital · Alternance Chargé·e de Projets Webmarketing
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** Réseaux sociaux (organique) · Création de contenu / rédaction · CRM (générique) · Vidéo / motion / création visuelle · KPI / reporting / analyse de performance · Marketing automation · Emailing / newsletters / push · Gestion de projet
- **OUTILS_ASSOCIES :** WordPress, CMS, Google Analytics 4, Google Tag Manager, HubSpot, Canva, suite Adobe, Google Ads, Meta Ads
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 26 offres uniques (5.3 % du périmètre), issues de 4 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance marketing digital OR webmarketing 2026`
  - `site:candidat.francetravail.fr/offres/recherche/detail marketing digital`
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" CDI`
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" Nantes OR Rennes OR Toulouse OR Strasbourg`

#### Chef de projet Marketing Digital / Digital

- **FAMILLE :** `COEUR_GENERALISTE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 20 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** ALTERNANCE - Assistant Chef de Projet Digital (H/F) · Alternance - Chef de Projet Marketing Digital Plateforme BtoB (H/F) · Alternance - Chef de projets marketing digital f/h (H/F) · Alternance Chef de projet marketing Digital (H/F) · Assistant Chef de projet Marketing Digital (H/F) Contrat d'alternance · CHEF DE PROJET WEBMARKETING
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** Gestion de projet · Réseaux sociaux (organique) · Création de contenu / rédaction · SEO · Shopify / PrestaShop / Magento / WordPress · HubSpot · CRM (générique) · B2B
- **OUTILS_ASSOCIES :** WordPress, CMS, Google Analytics 4, Google Tag Manager, HubSpot, Canva, suite Adobe, Google Ads, Meta Ads
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 20 offres uniques (4.0 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail "responsable marketing digital" OR "chef de projet digital" 2026`
  - `site:candidat.francetravail.fr/offres/recherche/detail alternance marketing digital OR webmarketing 2026`
  - `site:fr.indeed.com/viewjob "chef de projet digital" OR "coordinateur marketing digital" CDI France`
  - `site:fr.indeed.com/viewjob "chef de projet marketing digital" alternance`

#### Chargé de Communication Digitale

- **FAMILLE :** `COEUR_GENERALISTE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 1.13 (moyenne observée sur 15 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternance Assistant en Communication et Marketing (F/H) · Alternance Chargé de communication/Marketing (H/F) · Alternant Communication et Marketing H/F · CDD/CDI - Chargé de communication digitale H/F · CHARGÉ(E) DE COMMUNICATION DIGITALE - H/F · Chargé de Marketing et Communication Digitale Alternance
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** Vidéo / motion / création visuelle · Réseaux sociaux (organique) · SEO · Netlinking / contenu SEO · Création de contenu / rédaction · Meta Ads / Facebook Ads · Google Ads · E-commerce / gestion de site
- **OUTILS_ASSOCIES :** WordPress, CMS, Google Analytics 4, Google Tag Manager, HubSpot, Canva, suite Adobe, Google Ads, Meta Ads
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 15 offres uniques (3.0 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM" OR "marketing" alternance Lyon OR Villeurbanne 2026 offre`
  - `site:fr.indeed.com/viewjob "SEA" OR "Google Ads" OR "Meta Ads" alternance OR stage France 2026`
  - `site:fr.indeed.com/viewjob "SEO" OR "content" OR "CRM" stage 2026 marketing digital Paris`
  - `site:fr.indeed.com/viewjob "chargé de communication digitale" OR "communication digitale" CDI France 2026`

#### Responsable / Directeur Marketing Digital

- **FAMILLE :** `COEUR_GENERALISTE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 12 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** RESPONSABLE INNOVATION MARKETING DIGITAL F/H · Responsable Communication et Marketing Digital Marché Industriel · Responsable Marketing Digital · Responsable Marketing Digital & Data Produits Négoce F/H (H/F) · Responsable Marketing Digital Confirmé - Télétravail · Responsable Marketing Digital H/F
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** Stratégie marketing · B2B
- **OUTILS_ASSOCIES :** WordPress, CMS, Google Analytics 4, Google Tag Manager, HubSpot, Canva, suite Adobe, Google Ads, Meta Ads
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 12 offres uniques (2.4 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail "responsable marketing digital" OR "chef de projet digital" 2026`
  - `site:candidat.francetravail.fr/offres/recherche/detail marketing digital`
  - `site:fr.indeed.com/viewjob "SEA" OR "Google Ads" OR "Meta Ads" alternance OR stage France 2026`
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" OR "responsable acquisition" Bordeaux (33) CDI`

#### Responsable Digital

- **FAMILLE :** `COEUR_GENERALISTE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 2 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Responsable Digital (H/F)
- **VARIANTES_ANGLAISES :** Digital Manager Junior F/H
- **COMPETENCES_ASSOCIEES :** KPI / reporting / analyse de performance
- **OUTILS_ASSOCIES :** WordPress, CMS, Google Analytics 4, Google Tag Manager, HubSpot, Canva, suite Adobe, Google Ads, Meta Ads
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 2 offres uniques (0.4 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail "traffic manager" OR "e-commerce" OR "growth" 2026`
  - `site:fr.indeed.com/viewjob "responsable digital" OR "digital manager" OR "e-business" CDI France 2026`

#### Content Manager / Content Marketing Manager

- **FAMILLE :** `CONTENT_BRAND`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 16 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternance Communication & Création de Contenu Digital et IA H/F · Chargé Marketing Digital & Création de Contenu (H/F)
- **VARIANTES_ANGLAISES :** Apprenti(e) content manager H/F · CDI : Social media & content manager · Community Manager / Content Creator – TikTok & Insta · Community Manager Senior & Content Creator (H/F) – ODY · Content Manager · Content Manager & Copywriter Groupe F/H
- **COMPETENCES_ASSOCIEES :** Création de contenu / rédaction · Réseaux sociaux (organique) · Influence / partenariats créateurs · B2B · Vidéo / motion / création visuelle · Excel / Google Sheets · Emailing / newsletters / push · SEO
- **OUTILS_ASSOCIES :** CMS, outils rédactionnels, suite Adobe, outils de montage vidéo, plateformes d'influence
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 16 offres uniques (3.2 % du périmètre), issues de 4 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail marketing digital`
  - `site:fr.indeed.com/viewjob "community manager" OR "social media manager" CDI 2026`
  - `site:fr.indeed.com/viewjob "community manager" OR "social media" CDI Lille OR Nantes OR Toulouse 2026`
  - `site:fr.indeed.com/viewjob "content manager" OR "content marketing manager" CDI France`

#### Influence / Influencer Marketing Manager

- **FAMILLE :** `CONTENT_BRAND`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 1.0 (moyenne observée sur 10 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Chargé(e) de Marketing d'Influence (H/F) · Chargé(e) de communication digitale et d'influence H/F · Chef de projet Influence H/F · Chef(fe) de projet influence · INFLUENCE MARKETING JUNIOR (H/F/X)
- **VARIANTES_ANGLAISES :** Assistant(e) Social Media & Influence (H/F - stage 4 à 6 mois) · Freelance Influencer Marketing Specialist (French) · Influencer Manager · Social media & influence manager (f/h) · Sr. Influencer & Brand Experience Manager - France
- **COMPETENCES_ASSOCIEES :** Influence / partenariats créateurs · Gestion de projet · Réseaux sociaux (organique) · KPI / reporting / analyse de performance · Tracking / data layer / plan de taggage · E-commerce / gestion de site
- **OUTILS_ASSOCIES :** CMS, outils rédactionnels, suite Adobe, outils de montage vidéo, plateformes d'influence
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 10 offres uniques (2.0 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "chargé de communication digitale" OR "communication digitale" CDI France 2026`
  - `site:fr.indeed.com/viewjob "influence" OR "influenceurs" marketing manager CDI France`
  - `site:fr.indeed.com/viewjob "influence" OR "social media" OR "content" alternance 2026 Paris Lyon`
  - `site:fr.indeed.com/viewjob "social media manager" OR "responsable réseaux sociaux" Lyon OR Bordeaux OR Nantes OR Marseille`

#### Content Strategist / Brand Content Manager

- **FAMILLE :** `CONTENT_BRAND`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 3 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Brand Strategist / Concepteur·rice Brand Content · Content Strategist H/F · Social Media Brand Content Manager
- **COMPETENCES_ASSOCIEES :** Réseaux sociaux (organique)
- **OUTILS_ASSOCIES :** CMS, outils rédactionnels, suite Adobe, outils de montage vidéo, plateformes d'influence
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 3 offres uniques (0.6 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "brand content" OR "copywriter" OR "content strategist" marketing France CDI`
  - `site:fr.indeed.com/viewjob "content manager" OR "content marketing manager" CDI France`

#### CRM Manager / Responsable CRM

- **FAMILLE :** `CRM_LIFECYCLE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.53 (moyenne observée sur 17 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternant(e)/Stagiaire Marketing CRM (H/F) · Chef de Projet CRM · Chef.fe de projet CRM F/H · Expert CRM, fidélisation et voix du client Gémo H/F
- **VARIANTES_ANGLAISES :** CRM / SalesOps Manager (H/F/X) · CRM DOMAIN MANAGER H/F · CRM Lead · CRM Manager · CRM Manager - Braze / Anglais courant H/F · CRM Manager H/F
- **COMPETENCES_ASSOCIEES :** CRM (générique) · Marketing automation · Segmentation / scoring / nurturing · HubSpot · Salesforce / Marketing Cloud / Pardot · Anglais · B2C · Braze
- **OUTILS_ASSOCIES :** HubSpot, Salesforce et Marketing Cloud, Pardot, Braze, Klaviyo, Brevo, Adobe Campaign, ActiveCampaign, Splio, Dotdigital, Actito, Dartagnan
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 17 offres uniques (3.4 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM manager" OR "responsable CRM" CDI France`
  - `site:fr.indeed.com/viewjob "CRM" HubSpot OR Salesforce OR Brevo chargé marketing France`
  - `site:fr.indeed.com/viewjob "CRM" OR "lifecycle" OR "rétention" manager e-commerce retail France CDI 2026`
  - `site:fr.indeed.com/viewjob "CRM" OR "marketing digital" CDI Rennes OR Angers OR Tours OR Dijon OR Reims`

#### Chargé / Assistant CRM

- **FAMILLE :** `CRM_LIFECYCLE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.25 (moyenne observée sur 8 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternance Chargé·e CRM et Développement Marketing Digital · Assistant CRM & Graphiste · Assistant Marketing digital & CRM (H/F) - stage ou alternance · CRM & Clienteling Assistant Europe (H/F) · Chargé de Marketing Digital & CRM - Alternance · Chargé de campagnes CRM en Alternance (F/H)
- **VARIANTES_ANGLAISES :** Growth Marketing Assistant CRM (Stage / Alternance)
- **COMPETENCES_ASSOCIEES :** CRM (générique) · Power BI / Tableau / Looker · Salesforce / Marketing Cloud / Pardot · KPI / reporting / analyse de performance · SQL · Marketing automation · Python · Vidéo / motion / création visuelle
- **OUTILS_ASSOCIES :** HubSpot, Salesforce et Marketing Cloud, Pardot, Braze, Klaviyo, Brevo, Adobe Campaign, ActiveCampaign, Splio, Dotdigital, Actito, Dartagnan
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 8 offres uniques (1.6 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM" HubSpot OR Salesforce OR Brevo chargé marketing France`
  - `site:fr.indeed.com/viewjob "chargé de marketing" OR "assistant marketing" digital alternance septembre 2026 France`
  - `site:fr.indeed.com/viewjob marketing digital OR growth OR CRM Lille (59) OR "Hauts-de-France" CDI`
  - `site:www.hellowork.com/fr-fr/emplois "CRM" OR "e-commerce" OR "digital" alternance Bordeaux OR Nantes OR Marseille 2026`

#### CRM Campaign Manager

- **FAMILLE :** `CRM_LIFECYCLE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.5 (moyenne observée sur 4 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** CRM & Campaign Manager (H/F) · CRM Campaign Manager (F-H) · Campaign Manager CRM · Campaign Manager CRM (H/F) - Adobe Campaign/Dartagnan
- **COMPETENCES_ASSOCIEES :** CRM (générique) · Marketing automation · ActiveCampaign / Mailchimp / Splio / Dotdigital / Actito · Brevo / Sendinblue · Salesforce / Marketing Cloud / Pardot · HubSpot · Adobe Campaign · KPI / reporting / analyse de performance
- **OUTILS_ASSOCIES :** HubSpot, Salesforce et Marketing Cloud, Pardot, Braze, Klaviyo, Brevo, Adobe Campaign, ActiveCampaign, Splio, Dotdigital, Actito, Dartagnan
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 4 offres uniques (0.8 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "email marketing" OR "emailing" OR "campaign manager" CRM France CDI`
  - `site:fr.indeed.com/viewjob marketing digital OR growth OR CRM Lille (59) OR "Hauts-de-France" CDI`
  - `site:www.hellowork.com/fr-fr/emplois growth OR acquisition OR CRM manager Lyon OR Nantes OR Bordeaux`
  - `site:www.welcometothejungle.com/fr/companies "CRM Manager" OR "Lifecycle" OR "Marketing Automation" CDI`

#### Lifecycle / CRM Lifecycle Manager

- **FAMILLE :** `CRM_LIFECYCLE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.0 (moyenne observée sur 3 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Chef de projet CRM / CRM Lifecycle Manager · Lifecycle CRM Manager B2B · Senior Lifecycle Marketing Manager
- **COMPETENCES_ASSOCIEES :** CRM (générique) · Segmentation / scoring / nurturing · B2B · Gestion de projet · Business / ROI / revenue
- **OUTILS_ASSOCIES :** HubSpot, Salesforce et Marketing Cloud, Pardot, Braze, Klaviyo, Brevo, Adobe Campaign, ActiveCampaign, Splio, Dotdigital, Actito, Dartagnan
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 3 offres uniques (0.6 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM" OR "lifecycle" OR "rétention" manager e-commerce retail France CDI 2026`
  - `site:www.welcometothejungle.com/fr/companies "CRM Manager" OR "Lifecycle" OR "Marketing Automation" CDI`

#### CRM & Automation Manager

- **FAMILLE :** `CRM_LIFECYCLE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.0 (moyenne observée sur 2 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** CRM & Automation manager F/H · Senior CRM Manager - Automation
- **COMPETENCES_ASSOCIEES :** Marketing automation · CRM (générique) · HubSpot · Segmentation / scoring / nurturing
- **OUTILS_ASSOCIES :** HubSpot, Salesforce et Marketing Cloud, Pardot, Braze, Klaviyo, Brevo, Adobe Campaign, ActiveCampaign, Splio, Dotdigital, Actito, Dartagnan
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 2 offres uniques (0.4 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "marketing automation" specialist OR manager CDI France`
  - `site:www.welcometothejungle.com/fr/companies "CRM Manager" OR "Lifecycle" OR "Marketing Automation" CDI`

#### Campaign Manager

- **FAMILLE :** `CRM_LIFECYCLE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 2 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Chargé(e) de campagnes digitales & influence Junior (H/F)
- **VARIANTES_ANGLAISES :** Campaign manager F/M
- **COMPETENCES_ASSOCIEES :** Influence / partenariats créateurs
- **OUTILS_ASSOCIES :** HubSpot, Salesforce et Marketing Cloud, Pardot, Braze, Klaviyo, Brevo, Adobe Campaign, ActiveCampaign, Splio, Dotdigital, Actito, Dartagnan
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 2 offres uniques (0.4 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" OR "responsable acquisition" Bordeaux (33) CDI`
  - `site:fr.indeed.com/viewjob "email marketing" OR "emailing" OR "campaign manager" CRM France CDI`

#### Web / Digital Analyst

- **FAMILLE :** `DATA_ANALYTICS_CRO`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.62 (moyenne observée sur 13 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Alternance - Web Analyst (F/H) · CDI - Web Analyst H/F · Digital Analyst · Digital Analyst Confirmé · Global Data and Analytics Manager · Senior Digital Analyst (x/f/m)
- **COMPETENCES_ASSOCIEES :** Tracking / data layer / plan de taggage · Looker Studio / dashboards · KPI / reporting / analyse de performance · CRO / optimisation de conversion · Power BI / Tableau / Looker · SQL · Google Tag Manager / GTM · BigQuery / data warehouse
- **OUTILS_ASSOCIES :** Google Analytics 4, Google Tag Manager, Looker Studio, Matomo, Adobe Analytics, Amplitude, Mixpanel, Piano Analytics, SQL, BigQuery, Power BI, AB Tasty, Kameleoon, Contentsquare, Hotjar
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 13 offres uniques (2.6 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "data analyst" marketing OR "analytics manager" OR "tracking specialist" France CDI`
  - `site:fr.indeed.com/viewjob "web analyst" OR "digital analyst" OR "marketing data analyst" CDI`
  - `site:www.hellowork.com/fr-fr/emplois "data analyst" marketing OR "web analyst" OR "analytics" CDI France`

#### Data Analyst (finalité marketing)

- **FAMILLE :** `DATA_ANALYTICS_CRO`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.25 (moyenne observée sur 8 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** CDI - DATA ANALYST - H/F · Data Analyst · Data Analyst F/H · Data Analyst Junior (H/F) · Data Analyst expérimenté H/F - Nantes · Stage - Data Analyst Junior (F/H)
- **COMPETENCES_ASSOCIEES :** Business / ROI / revenue · Looker Studio / dashboards · Power BI / Tableau / Looker · KPI / reporting / analyse de performance
- **OUTILS_ASSOCIES :** Google Analytics 4, Google Tag Manager, Looker Studio, Matomo, Adobe Analytics, Amplitude, Mixpanel, Piano Analytics, SQL, BigQuery, Power BI, AB Tasty, Kameleoon, Contentsquare, Hotjar
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 8 offres uniques (1.6 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "data analyst" marketing OR "analytics manager" OR "tracking specialist" France CDI`
  - `site:www.hellowork.com/fr-fr/emplois "data analyst" marketing OR "web analyst" OR "analytics" CDI France`

#### Marketing / Growth Data Analyst

- **FAMILLE :** `DATA_ANALYTICS_CRO`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 6 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Data Analyst Marketing (F/H/X) · HAVAS MEDIA FRANCE - CDI - DATA ANALYST - CHARGÉ DE DATA OPERATIONS & REPORTING MARKETING - H/F · Lead Marketing Data Analyst (x/f/m) · Marketing Data Analyst (F/H) · Marketing Data Analyst - CDI - Lille/Lyon/Paris · Senior Marketing Analyst
- **COMPETENCES_ASSOCIEES :** CRM (générique) · KPI / reporting / analyse de performance · Business / ROI / revenue
- **OUTILS_ASSOCIES :** Google Analytics 4, Google Tag Manager, Looker Studio, Matomo, Adobe Analytics, Amplitude, Mixpanel, Piano Analytics, SQL, BigQuery, Power BI, AB Tasty, Kameleoon, Contentsquare, Hotjar
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 6 offres uniques (1.2 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "data analyst" marketing OR "analytics manager" OR "tracking specialist" France CDI`
  - `site:www.hellowork.com/fr-fr/emplois "data analyst" marketing OR "web analyst" OR "analytics" CDI France`
  - `site:www.welcometothejungle.com/fr/companies "Data Analyst" OR "Marketing Ops" OR "RevOps" CDI Paris 2026`
  - `site:www.welcometothejungle.com/fr/companies "SEO" OR "Analytics" OR "Data Analyst marketing" CDI France`

#### CRO / Conversion Specialist

- **FAMILLE :** `DATA_ANALYTICS_CRO`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.0 (moyenne observée sur 4 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** Consultant CRO - (IT) / Freelance · Consultant Chargé de Campagnes / CRO H/F · Expert E-commerce Shopify / Optimisation de Conversion (CRO) – H/F
- **VARIANTES_ANGLAISES :** E-commerce Merchandising & CRO Manager
- **COMPETENCES_ASSOCIEES :** CRO / optimisation de conversion · A/B testing / expérimentation · E-commerce / gestion de site · Marketplaces · E-merchandising / catalogue produits · Shopify / PrestaShop / Magento / WordPress
- **OUTILS_ASSOCIES :** Google Analytics 4, Google Tag Manager, Looker Studio, Matomo, Adobe Analytics, Amplitude, Mixpanel, Piano Analytics, SQL, BigQuery, Power BI, AB Tasty, Kameleoon, Contentsquare, Hotjar
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 4 offres uniques (0.8 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRO" OR "conversion rate optimization" OR "AB testing" marketing CDI France`
  - `site:fr.indeed.com/viewjob "e-commerce" OR "marketplace" manager Nantes OR Lille OR Lyon CDI`

#### E-commerce Manager / Responsable e-commerce

- **FAMILLE :** `ECOMMERCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 23 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** ASSISTANT.E E-Commerce & Marketing Digital · Alternance Assistant(e) E-Commerce & Communication digitale · Assistant responsable E-Commerce Orange F/H · Assistant(e) Chef(fe) de Projets e-commerce - Alternance · CHEF(FE) DE PROJET INFORMATIQUE DIGITAL ET E-COMMERCE (H/F) · Chargé de Marketing Digital & E-commerce (H/F) - Alternance
- **VARIANTES_ANGLAISES :** Chargé de Contenus E-Commerce / Content Manager · Content Manager International Ecommerce · E-COMMERCE PROJECT MANAGER ESPAGNE (F/H) · E-Commerce Manager · E-Commerce Product Manager · E-Commerce Specialist H/F - CDI - Paris
- **COMPETENCES_ASSOCIEES :** E-commerce / gestion de site · Marketplaces · SEO · Business / ROI / revenue · Création de contenu / rédaction · CRM (générique) · KPI / reporting / analyse de performance · Gestion de projet
- **OUTILS_ASSOCIES :** Shopify, PrestaShop, Magento, marketplaces Amazon et Cdiscount, outils de gestion de flux produits, e-merchandising
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 23 offres uniques (4.6 % du périmètre), issues de 4 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail "traffic manager" OR "e-commerce" OR "growth" 2026`
  - `site:fr.indeed.com/viewjob "SEO" OR "content" OR "CRM" stage 2026 marketing digital Paris`
  - `site:fr.indeed.com/viewjob "e-commerce manager" OR "responsable e-commerce" CDI`
  - `site:fr.indeed.com/viewjob "e-commerce" OR "marketplace" manager Nantes OR Lille OR Lyon CDI`

#### Marketplace Manager / Specialist

- **FAMILLE :** `ECOMMERCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.0 (moyenne observée sur 3 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Assistant(e) E-Commerce/Marketplace (H/F) · Chargé(e) de Projet Digital — Data, Catalogue & Marketplace
- **VARIANTES_ANGLAISES :** Stagiaire E-commerce & Marketplace Manager
- **COMPETENCES_ASSOCIEES :** Marketplaces · E-commerce / gestion de site · E-merchandising / catalogue produits · KPI / reporting / analyse de performance · Marketing automation · No-code / automatisation (Zapier, Make, n8n) · Business / ROI / revenue · API / webhook / intégrations
- **OUTILS_ASSOCIES :** Shopify, PrestaShop, Magento, marketplaces Amazon et Cdiscount, outils de gestion de flux produits, e-merchandising
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 3 offres uniques (0.6 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "marketplace manager" OR "e-merchandiser" OR "digital commerce" France`
  - `site:fr.indeed.com/viewjob "prompt" OR "agents IA" OR "automatisation" marketing no-code Make n8n Zapier France`

#### E-merchandiser

- **FAMILLE :** `ECOMMERCE`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 2 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** E-merchandiser - CDI · E-merchandiser F/H
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** E-merchandising / catalogue produits · KPI / reporting / analyse de performance · Tracking / data layer / plan de taggage
- **OUTILS_ASSOCIES :** Shopify, PrestaShop, Magento, marketplaces Amazon et Cdiscount, outils de gestion de flux produits, e-merchandising
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 2 offres uniques (0.4 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM" OR "lifecycle" OR "rétention" manager e-commerce retail France CDI 2026`
  - `site:fr.indeed.com/viewjob "marketplace manager" OR "e-merchandiser" OR "digital commerce" France`

#### Revenue Operations Manager (RevOps)

- **FAMILLE :** `MARTECH_MARKETING_OPS`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.25 (moyenne observée sur 8 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** Consultant.e RevOps / Sales Ops - CRM - Confirmé/Senior · Director, Revenue Operations
- **VARIANTES_ANGLAISES :** RevOps & CRM Manager (H/F) · RevOps Manager · Revenue Operations Manager · Revops & CRM Manager · Senior RevOps Manager
- **COMPETENCES_ASSOCIEES :** Business / ROI / revenue · CRM (générique) · Stratégie marketing · Segmentation / scoring / nurturing · Marketing automation · Salesforce / Marketing Cloud / Pardot
- **OUTILS_ASSOCIES :** Customer Data Platform (Adobe Experience Platform, Salesforce Data Cloud, Sitecore CDP, BlueConic, Treasure Data, Imagino), Salesforce, HubSpot, BigQuery, Databricks, APIs, Zapier, Make, n8n
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 8 offres uniques (1.6 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "marketing operations" OR "revenue operations" OR "RevOps" France`
  - `site:www.hellowork.com/fr-fr/emplois growth OR acquisition OR CRM manager Lyon OR Nantes OR Bordeaux`
  - `site:www.welcometothejungle.com/fr/companies "Data Analyst" OR "Marketing Ops" OR "RevOps" CDI Paris 2026`

#### Marketing Automation Manager / Spécialiste

- **FAMILLE :** `MARTECH_MARKETING_OPS`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.25 (moyenne observée sur 4 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** Chargé de Marketing Automation h/f · Chef de projet CRM Expert Marketing Automation H/F - CDI · Responsable CRM, Marketing Automation et Fidélité (Ubigi) H/F
- **VARIANTES_ANGLAISES :** Marketing automation manager (H/F)
- **COMPETENCES_ASSOCIEES :** Marketing automation · CRM (générique) · HubSpot · B2B · CDP / Customer Data Platform · Gestion de projet · Business / ROI / revenue · Salesforce / Marketing Cloud / Pardot
- **OUTILS_ASSOCIES :** Customer Data Platform (Adobe Experience Platform, Salesforce Data Cloud, Sitecore CDP, BlueConic, Treasure Data, Imagino), Salesforce, HubSpot, BigQuery, Databricks, APIs, Zapier, Make, n8n
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 4 offres uniques (0.8 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM manager" OR "responsable CRM" CDI France`
  - `site:fr.indeed.com/viewjob "marketing automation" specialist OR manager CDI France`

#### Sales Operations Manager

- **FAMILLE :** `MARTECH_MARKETING_OPS`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.67 (moyenne observée sur 3 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Sales Operations Analyst, Paris · Sales Operations Manager · Senior Sales Operations Manager
- **COMPETENCES_ASSOCIEES :** Business / ROI / revenue · SQL · B2B · Google Tag Manager / GTM · Segmentation / scoring / nurturing
- **OUTILS_ASSOCIES :** Customer Data Platform (Adobe Experience Platform, Salesforce Data Cloud, Sitecore CDP, BlueConic, Treasure Data, Imagino), Salesforce, HubSpot, BigQuery, Databricks, APIs, Zapier, Make, n8n
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 3 offres uniques (0.6 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "marketing operations" OR "revenue operations" OR "RevOps" France`
  - `site:www.welcometothejungle.com/fr/companies "Data Analyst" OR "Marketing Ops" OR "RevOps" CDI Paris 2026`

#### Expert Customer Data Platform (CDP)

- **FAMILLE :** `MARTECH_MARKETING_OPS`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 4.0 (moyenne observée sur 1 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** Expert(e) technique Customer Data Platform F/H
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** Power BI / Tableau / Looker · SQL · E-commerce / gestion de site · Salesforce / Marketing Cloud / Pardot · CDP / Customer Data Platform · BigQuery / data warehouse
- **OUTILS_ASSOCIES :** Customer Data Platform (Adobe Experience Platform, Salesforce Data Cloud, Sitecore CDP, BlueConic, Treasure Data, Imagino), Salesforce, HubSpot, BigQuery, Databricks, APIs, Zapier, Make, n8n
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 1 offres uniques (0.2 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CDP" OR "customer data platform" OR "server-side" OR "BigQuery" marketing France`

#### Marketing Operations Manager

- **FAMILLE :** `MARTECH_MARKETING_OPS`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 1 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Campaign & Marketing Operations Associate - Paris or London
- **COMPETENCES_ASSOCIEES :** non renseignées dans les extraits
- **OUTILS_ASSOCIES :** Customer Data Platform (Adobe Experience Platform, Salesforce Data Cloud, Sitecore CDP, BlueConic, Treasure Data, Imagino), Salesforce, HubSpot, BigQuery, Databricks, APIs, Zapier, Make, n8n
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 1 offres uniques (0.2 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "email marketing" OR "emailing" OR "campaign manager" CRM France CDI`

#### Assistant / Chargé Marketing (généraliste)

- **FAMILLE :** `METIER_ADJACENT`
- **INCLUS_OU_EXCLU :** INCLUS (tracé mais hors volumes du cœur)
- **NIVEAU_TECHNICITE :** 1.11 (moyenne observée sur 19 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** PERIPHERIQUE
- **VARIANTES_FRANCAISES :** (H/F) Chargé(e) de Développement business et Marketing en Alternance · ALTERNANCE MARKETING INTERNATIONAL H/F · ASSISTANT MARKETING H/F · Alternance - Assistant.e Marketing · Alternance - Marketing · Alternance Assistant Marketing Communication & Digital
- **VARIANTES_ANGLAISES :** Alternance Chargé de Content Marketing F/H · Manager, Global Marketing Programs (France)
- **COMPETENCES_ASSOCIEES :** SEO · Réseaux sociaux (organique) · Business / ROI / revenue · Création de contenu / rédaction · HubSpot · CRM (générique) · Emailing / newsletters / push · Vidéo / motion / création visuelle
- **OUTILS_ASSOCIES :** CRM, outils de prospection, PipeDrive, HubSpot, outils marketing généralistes
- **JUSTIFICATION :** Identifié et tracé, mais **non comptabilisé dans les volumes du cœur marketing digital** : débouché possible pour un diplômé marketing, sans relever du marketing digital au sens strict. Observé sur 19 offres uniques (3.8 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM" OR "marketing" alternance Lyon OR Villeurbanne 2026 offre`
  - `site:fr.indeed.com/viewjob "SEO" OR "content" OR "CRM" stage 2026 marketing digital Paris`
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" Nantes OR Rennes OR Toulouse OR Strasbourg`
  - `site:fr.indeed.com/viewjob "chargé de marketing" OR "assistant marketing" digital alternance septembre 2026 France`

#### Responsable / Directeur Marketing (généraliste)

- **FAMILLE :** `METIER_ADJACENT`
- **INCLUS_OU_EXCLU :** INCLUS (tracé mais hors volumes du cœur)
- **NIVEAU_TECHNICITE :** 2.06 (moyenne observée sur 18 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** PERIPHERIQUE
- **VARIANTES_FRANCAISES :** Alternant - Assistant Responsable Marketing Opérationnel - F/H · Assistant(e) Chef de Projet Marketing H/F - Alternance · CDI : Responsable Marketing · Chef de Projet Marketing / Chargé de Marketing confirmé H/F · Chef-fe de Projet Marketing (H/F) · Directeur/rice Marketing & Digital H/F
- **VARIANTES_ANGLAISES :** Head of Marketing (F/H) · Head of Marketing (Mobile) · Marketing Manager Entreprise/ABM – CDI - Lille/Lyon/Paris · Marketing Manager France (m/f/d) · Seller Marketing Manager
- **COMPETENCES_ASSOCIEES :** Gestion de projet · E-commerce / gestion de site · B2B · Business / ROI / revenue · Marketing automation · Agents IA / prompt engineering · No-code / automatisation (Zapier, Make, n8n) · Création de contenu / rédaction
- **OUTILS_ASSOCIES :** CRM, outils de prospection, PipeDrive, HubSpot, outils marketing généralistes
- **JUSTIFICATION :** Identifié et tracé, mais **non comptabilisé dans les volumes du cœur marketing digital** : débouché possible pour un diplômé marketing, sans relever du marketing digital au sens strict. Observé sur 18 offres uniques (3.6 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail "traffic manager" OR "e-commerce" OR "growth" 2026`
  - `site:fr.indeed.com/viewjob "CRO" OR "conversion rate optimization" OR "AB testing" marketing CDI France`
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" Nantes OR Rennes OR Toulouse OR Strasbourg`
  - `site:fr.indeed.com/viewjob "marketing automation" specialist OR manager CDI France`

#### Business Developer / SDR

- **FAMILLE :** `METIER_ADJACENT`
- **INCLUS_OU_EXCLU :** INCLUS (tracé mais hors volumes du cœur)
- **NIVEAU_TECHNICITE :** 1.43 (moyenne observée sur 7 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** PERIPHERIQUE
- **VARIANTES_FRANCAISES :** Business Developper (H/F) - Alternance · CHARGE DE DEVELOPPEMENT COMMERCIAL H/F Alternance · COORDINATEUR COMMERCIAL & MARKETING EN ALTERNANCE (F/H) · Directeur Commercial & Marketing H/F · Responsable Performance Commerciale H/F - CDI - Hybride · SDR (H/F) - Alternance
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** CRM (générique) · B2B · Business / ROI / revenue · Tracking / data layer / plan de taggage · HubSpot
- **OUTILS_ASSOCIES :** CRM, outils de prospection, PipeDrive, HubSpot, outils marketing généralistes
- **JUSTIFICATION :** Identifié et tracé, mais **non comptabilisé dans les volumes du cœur marketing digital** : débouché possible pour un diplômé marketing, sans relever du marketing digital au sens strict. Observé sur 7 offres uniques (1.4 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "CRM" OR "marketing digital" CDI Rennes OR Angers OR Tours OR Dijon OR Reims`
  - `site:fr.indeed.com/viewjob "CRM" OR "marketing" alternance Lyon OR Villeurbanne 2026 offre`
  - `site:fr.indeed.com/viewjob "SEA" OR "Google Ads" OR "Meta Ads" alternance OR stage France 2026`
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" OR "responsable acquisition" Bordeaux (33) CDI`

#### Chef de projet Trade Marketing

- **FAMILLE :** `METIER_ADJACENT`
- **INCLUS_OU_EXCLU :** INCLUS (tracé mais hors volumes du cœur)
- **NIVEAU_TECHNICITE :** 1.0 (moyenne observée sur 3 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** PERIPHERIQUE
- **VARIANTES_FRANCAISES :** CDI - TRADE MARKETING - CHEF DE PROJET - H/F · CHEF DE PROJET TRADE MARKETING · Chef de Projet Trade Marketing au sein d'ARGEDIS
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** Gestion de projet · Anglais
- **OUTILS_ASSOCIES :** CRM, outils de prospection, PipeDrive, HubSpot, outils marketing généralistes
- **JUSTIFICATION :** Identifié et tracé, mais **non comptabilisé dans les volumes du cœur marketing digital** : débouché possible pour un diplômé marketing, sans relever du marketing digital au sens strict. Observé sur 3 offres uniques (0.6 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "trade marketing" OR "marketing produit" OR "chef de produit digital" France CDI`

#### Chef de produit / Product Manager

- **FAMILLE :** `METIER_ADJACENT`
- **INCLUS_OU_EXCLU :** INCLUS (tracé mais hors volumes du cœur)
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 2 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** PERIPHERIQUE
- **VARIANTES_FRANCAISES :** CHEF DE PRODUIT EDITION · Chef de Produits h/f
- **VARIANTES_ANGLAISES :** aucune variante anglaise observée
- **COMPETENCES_ASSOCIEES :** E-merchandising / catalogue produits · Gestion de projet · Business / ROI / revenue
- **OUTILS_ASSOCIES :** CRM, outils de prospection, PipeDrive, HubSpot, outils marketing généralistes
- **JUSTIFICATION :** Identifié et tracé, mais **non comptabilisé dans les volumes du cœur marketing digital** : débouché possible pour un diplômé marketing, sans relever du marketing digital au sens strict. Observé sur 2 offres uniques (0.4 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "trade marketing" OR "marketing produit" OR "chef de produit digital" France CDI`

#### Consultant SEO / GEO

- **FAMILLE :** `METIER_IA_EMERGENT`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.2 (moyenne observée sur 5 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** Consultant H/F SEO GEO · Consultant SEO / GEO · Consultant SEO/GEO - CDI - Paris · Consultant.e SEO / GEO - Full Remote or Paris H/F
- **VARIANTES_ANGLAISES :** Community Manager, Spécialiste Agents IA & GEO / SEO (H/F)
- **COMPETENCES_ASSOCIEES :** SEO · GEO / AEO / AI Search · Agents IA / prompt engineering · Réseaux sociaux (organique)
- **OUTILS_ASSOCIES :** ChatGPT, Claude, Gemini, Copilot, Midjourney, Adobe Firefly, n8n, Make, Zapier, outils GEO/AEO, agents IA, MCP
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 5 offres uniques (1.0 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail community manager OR SEO OR CRM 2026`
  - `site:fr.indeed.com/viewjob "SEO" OR "SEA" OR "acquisition" alternance 2026 Paris Lyon Bordeaux Nantes`
  - `site:fr.indeed.com/viewjob "consultant SEO" OR "SEO manager" CDI`
  - `site:www.welcometothejungle.com/fr/companies "SEO" OR "Analytics" OR "Data Analyst marketing" CDI France`

#### RevOps — AI, Data & Automation

- **FAMILLE :** `METIER_IA_EMERGENT`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.0 (moyenne observée sur 2 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** RevOps & AI Automation Analyst (H/F/X) · RevOps Manager – AI, Data & Automation
- **COMPETENCES_ASSOCIEES :** Marketing automation · Stratégie marketing · IA appliquée au marketing (packshot, création, workflow)
- **OUTILS_ASSOCIES :** ChatGPT, Claude, Gemini, Copilot, Midjourney, Adobe Firefly, n8n, Make, Zapier, outils GEO/AEO, agents IA, MCP
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 2 offres uniques (0.4 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:www.welcometothejungle.com/fr/companies "Data Analyst" OR "Marketing Ops" OR "RevOps" CDI Paris 2026`

#### AI Marketing / AI Content Manager

- **FAMILLE :** `METIER_IA_EMERGENT`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 3.0 (moyenne observée sur 1 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** AI Content Manager H/F
- **COMPETENCES_ASSOCIEES :** Marketing automation · IA appliquée au marketing (packshot, création, workflow) · Réseaux sociaux (organique)
- **OUTILS_ASSOCIES :** ChatGPT, Claude, Gemini, Copilot, Midjourney, Adobe Firefly, n8n, Make, Zapier, outils GEO/AEO, agents IA, MCP
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 1 offres uniques (0.2 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "content manager" OR "content marketing manager" CDI France`

#### Growth Manager IA

- **FAMILLE :** `METIER_IA_EMERGENT`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 1 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Growth Manager IA H/F
- **COMPETENCES_ASSOCIEES :** non renseignées dans les extraits
- **OUTILS_ASSOCIES :** ChatGPT, Claude, Gemini, Copilot, Midjourney, Adobe Firefly, n8n, Make, Zapier, outils GEO/AEO, agents IA, MCP
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 1 offres uniques (0.2 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "growth marketing" OR "growth manager" France CDI`

#### SEO/SEA/GEO — AI Visibility Manager

- **FAMILLE :** `METIER_IA_EMERGENT`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 1 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** SEO SEA GEO AI Visibility Manager E-Commerce
- **COMPETENCES_ASSOCIEES :** SEO · SEA / Paid Search · E-commerce / gestion de site · GEO / AEO / AI Search
- **OUTILS_ASSOCIES :** ChatGPT, Claude, Gemini, Copilot, Midjourney, Adobe Firefly, n8n, Make, Zapier, outils GEO/AEO, agents IA, MCP
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 1 offres uniques (0.2 % du périmètre), issues de 1 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:www.hellowork.com/fr-fr/emplois SEO OR SEA OR "traffic manager" OR "social media" CDI 2026`

#### Product Marketing Manager

- **FAMILLE :** `PRODUCT_MARKETING`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 9 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** FORTE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** App Product Marketing Manager · CDD - PRODUCT MARKETING MANAGER Go To Market - H/F · Product Marketing Manager · Product Marketing Manager - CDI - Paris Based · Product Marketing Manager - H/F (CDI) · Product Marketing Manager, Product & Virality
- **COMPETENCES_ASSOCIEES :** KPI / reporting / analyse de performance · Stratégie marketing
- **OUTILS_ASSOCIES :** HubSpot, Salesforce, outils de recherche utilisateur, outils de go-to-market, analytics produit
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 9 offres uniques (1.8 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "product marketing manager" CDI France 2026`
  - `site:www.hellowork.com/fr-fr/emplois "e-commerce manager" OR "content manager" OR "product marketing" CDI`
  - `site:www.welcometothejungle.com/fr/companies "Product Marketing Manager" OR "Content" OR "Social Media" CDI Paris Lyon`

#### Consultant / Manager SEO

- **FAMILLE :** `SEO_SEA`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 25 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternance - Chargé(e) de Webmarketing & SEO · Assistant chef de projet SEO H/F en alternance · Chargé de Marketing Digital SEO Communication · Chargée/Chargé marketing (F/H) - Expert SEO Pôle Digital (H/F) · Chef de Projet SEO F/H - Alternance · Consultant SEO
- **VARIANTES_ANGLAISES :** Alternant(e) Marketing / Content (H/F) - SEO · Growth Analyst - SEO · SENIOR DATA ANALYST SEO - H/F (Unnest) · SEO Lead - CDD 13 months · SEO MANAGER · SEO Specialist
- **COMPETENCES_ASSOCIEES :** SEO · Gestion de projet · SEO technique · Création de contenu / rédaction · SEA / Paid Search · Business / ROI / revenue · Vidéo / motion / création visuelle · Tracking / data layer / plan de taggage
- **OUTILS_ASSOCIES :** Google Search Console, Semrush, Ahrefs, Screaming Frog, Oncrawl, Majestic, Google Ads, Microsoft Ads, données structurées, Core Web Vitals
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 25 offres uniques (5.1 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "SEO" OR "SEA" OR "acquisition" alternance 2026 Paris Lyon Bordeaux Nantes`
  - `site:fr.indeed.com/viewjob "SEO" OR "content" OR "CRM" stage 2026 marketing digital Paris`
  - `site:fr.indeed.com/viewjob "SEO" OR "content" OR "acquisition" Nantes OR Rennes OR Angers CDI marketing`
  - `site:fr.indeed.com/viewjob "consultant SEO" OR "SEO manager" CDI`

#### Consultant / Manager SEA (Paid Search)

- **FAMILLE :** `SEO_SEA`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 17 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** AGENCE 79 - CDI - CONSULTANT SEA SENIOR - H/F · Consultant SEA Senior H/F · Consultant SEO SEA · Consultant(e) SEA (CDI) – Paris · Consultant/e Acquisition SEA - CDI Cadre - Paris 02 · HAVAS MARKET - CDI - CONSULTANT SEA SENIOR - H/F
- **VARIANTES_ANGLAISES :** ALTERNANCE (BAC+5) - Traffic Manager SEA (Google Ads) - F/H · Consultant(e) Paid Search / SEA - Senior (H/F) · Consultant·e Social Ads & Google Ads · Search Consultant - CDI · Senior Paid Search Consultant · Senior Paid Search Consultant - Paris
- **COMPETENCES_ASSOCIEES :** SEA / Paid Search · Google Ads · Meta Ads / Facebook Ads · E-commerce / gestion de site · Réseaux sociaux (organique) · Microsoft / Bing Ads · LinkedIn Ads · SEO
- **OUTILS_ASSOCIES :** Google Search Console, Semrush, Ahrefs, Screaming Frog, Oncrawl, Majestic, Google Ads, Microsoft Ads, données structurées, Core Web Vitals
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 17 offres uniques (3.4 % du périmètre), issues de 4 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail "traffic manager" OR "e-commerce" OR "growth" 2026`
  - `site:fr.indeed.com/viewjob "SEA" OR "Google Ads" OR "Meta Ads" alternance OR stage France 2026`
  - `site:fr.indeed.com/viewjob "consultant SEA" OR "SEA manager" OR "Google Ads" specialist CDI`
  - `site:fr.indeed.com/viewjob "paid social" OR "social ads" OR "programmatique" France CDI agence média`

#### Consultant SEA / SMA / Paid Media

- **FAMILLE :** `SEO_SEA`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 2.0 (moyenne observée sur 9 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** ALTERNANCE - Assistant(e) Webmarketing SEA/SMA (H/F) · CONSULTANT SEA/SMA · Consultant SEA et SMA F/H · Consultant SEA/SMA - Paris H/F · Stage Consultant SEA/SMA Junior
- **VARIANTES_ANGLAISES :** Consultant Paid Media (SEA/SMA) - Full Remote or Paris H/F · Consultant(e) Paid Media (SEA/SMA) - Leadgen · Consultant(e) Paid Media (SEA/SMA) Sénior · Expert Paid Media (SMA + SEA) - H/F
- **COMPETENCES_ASSOCIEES :** SEA / Paid Search · Réseaux sociaux (organique) · Google Ads · Microsoft / Bing Ads · Snapchat / Pinterest Ads · Meta Ads / Facebook Ads · Programmatique / DV360
- **OUTILS_ASSOCIES :** Google Search Console, Semrush, Ahrefs, Screaming Frog, Oncrawl, Majestic, Google Ads, Microsoft Ads, données structurées, Core Web Vitals
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 9 offres uniques (1.8 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "SEA" OR "Google Ads" OR "Meta Ads" alternance OR stage France 2026`
  - `site:fr.indeed.com/viewjob "consultant SEA" OR "SEA manager" OR "Google Ads" specialist CDI`
  - `site:www.welcometothejungle.com/fr/companies "SEA" OR "Paid Search" OR "Media" consultant CDI France`

#### Community Manager

- **FAMILLE :** `SOCIAL_MEDIA`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 1.04 (moyenne observée sur 24 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** aucune variante française observée
- **VARIANTES_ANGLAISES :** Alternance - Community Manager - Social Media · Alternance - Community manager H/F · Alternance Community Manager (H/F) · Assistante commerciale - Community manager - H/F · COMMUNITY MANAGER (H/F) · COMMUNITY MANAGER - CDI (F/H)
- **COMPETENCES_ASSOCIEES :** Réseaux sociaux (organique) · Création de contenu / rédaction · SEO · Vidéo / motion / création visuelle
- **OUTILS_ASSOCIES :** Meta Business Suite, Instagram, TikTok, LinkedIn, YouTube, Pinterest, outils de planification éditoriale
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 24 offres uniques (4.8 % du périmètre), issues de 2 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:candidat.francetravail.fr/offres/recherche/detail community manager OR SEO OR CRM 2026`
  - `site:fr.indeed.com/viewjob "chargé de marketing digital" Nantes OR Rennes OR Toulouse OR Strasbourg`
  - `site:fr.indeed.com/viewjob "community manager" OR "social media manager" CDI 2026`
  - `site:fr.indeed.com/viewjob "community manager" OR "social media" CDI Lille OR Nantes OR Toulouse 2026`

#### Social Media Manager / Specialist

- **FAMILLE :** `SOCIAL_MEDIA`
- **INCLUS_OU_EXCLU :** INCLUS
- **NIVEAU_TECHNICITE :** 1.0 (moyenne observée sur 15 offres)
- **PROXIMITE_AVEC_MARKETING_DIGITAL :** CENTRALE
- **VARIANTES_FRANCAISES :** Alternance Journaliste / Vidéaste Réseaux sociaux (Culture & Lifestyle)
- **VARIANTES_ANGLAISES :** Alternance - Social Media Manager (H/F) · Alternant(e) Communication & Marketing / Social Media · Assistant social media manager en alternance H/F · Chargé Marketing Digital & Social Media - Alternance · Chef de projet Social Media H/F (Stage) · Consultant marketing digital SMA (social media) - Montpellier CDI H/F
- **COMPETENCES_ASSOCIEES :** Réseaux sociaux (organique) · Vidéo / motion / création visuelle · Business / ROI / revenue · Gestion de projet · Pilotage budgétaire / média · E-commerce / gestion de site
- **OUTILS_ASSOCIES :** Meta Business Suite, Instagram, TikTok, LinkedIn, YouTube, Pinterest, outils de planification éditoriale
- **JUSTIFICATION :** Métier du périmètre marketing digital, retenu dans les volumes. Observé sur 15 offres uniques (3.0 % du périmètre), issues de 3 plateforme(s) différente(s).
- **REQUETES_UTILISEES :**
  - `site:fr.indeed.com/viewjob "influence" OR "social media" OR "content" alternance 2026 Paris Lyon`
  - `site:fr.indeed.com/viewjob "paid social" OR "social ads" OR "programmatique" France CDI agence média`
  - `site:fr.indeed.com/viewjob "paid social" OR "social ads" specialist CDI France`
  - `site:fr.indeed.com/viewjob "social media manager" OR "responsable réseaux sociaux" Lyon OR Bordeaux OR Nantes OR Marseille`

### A.3 Métiers de la taxonomie initiale non observés dans la collecte

Ces intitulés figuraient dans la cartographie de départ mais **aucune offre individuelle correspondante n'a été trouvée** sur les pages publiques indexées. Leur absence est un résultat en soi : elle indique que ces dénominations ne sont pas utilisées par les employeurs français, ou que leur volume est trop faible pour remonter dans les moteurs.

| Intitulé recherché | Famille visée | Résultat | Lecture |
|---|---|---|---|
| User Acquisition Manager | `ACQUISITION_PERFORMANCE` | Aucune offre isolée | Le poste existe (Performance Marketing Manager Gaming chez Voodoo mentionne l'user acquisition) mais l'intitulé n'est pas autonome en France. |
| Growth Hacker | `ACQUISITION_PERFORMANCE` | 2 offres, uniquement en alternance | Intitulé résiduel, employé surtout par des organismes de formation et non par des annonceurs. |
| Demand Generation Manager | `ACQUISITION_PERFORMANCE` | Aucune offre sous cet intitulé exact | Le concept apparaît dans les descriptions (lead generation, Artur'In) mais pas dans les titres français. |
| Search Engine Marketing Specialist | `SEO_SEA` | Aucune offre | Le marché français utilise SEA, Paid Search ou Traffic Manager. |
| Technical SEO Specialist | `SEO_SEA` | Aucune offre sous cet intitulé | Le SEO technique est une compétence citée (offre SEO Manager Bagneux) et non un métier autonome. |
| SEO Content Manager | `SEO_SEA` | Aucune offre sous cet intitulé | Recouvert par Content Manager avec composante SEO. |
| Paid Acquisition Specialist | `ACQUISITION_PERFORMANCE` | Aucune offre | Recouvert par Traffic Manager et Consultant Paid Media. |
| Creator Partnerships Manager | `CONTENT_BRAND` | Aucune offre | Le marché français utilise Influence Manager ou Chef de projet influence. |
| Responsable Partenariats Influence | `CONTENT_BRAND` | Aucune offre | Idem. |
| Customer Marketing Manager | `CRM_LIFECYCLE` | Aucune offre sous cet intitulé | Recouvert par CRM Manager et Lifecycle Manager. |
| Loyalty Manager | `CRM_LIFECYCLE` | 1 offre (Expert CRM, fidélisation et voix du client, Gémo) | Intitulé rare, la fidélisation est intégrée aux postes CRM. |
| Email Marketing Specialist | `CRM_LIFECYCLE` | Aucune offre autonome | L'emailing est une composante des postes CRM et Campaign Manager. |
| E-commerce Acquisition Manager | `ECOMMERCE` | Aucune offre | Recouvert par Traffic Manager E-commerce et Chargé de marketing e-commerce. |
| Digital Commerce Manager | `ECOMMERCE` | Aucune offre | Le marché français utilise E-commerce Manager. |
| Customer Data Analyst | `DATA_ANALYTICS_CRO` | Aucune offre à finalité marketing | Les Data Analyst sans finalité marketing ont été exclus du périmètre. |
| Web Analytics Consultant | `DATA_ANALYTICS_CRO` | Aucune offre sous cet intitulé | Recouvert par Web Analyst et Digital Analyst. |
| Tagging Specialist / Analytics Implementation Specialist | `DATA_ANALYTICS_CRO` | Aucune offre | Le tracking et le taggage sont des compétences, jamais des intitulés autonomes en France. |
| CRO Manager | `DATA_ANALYTICS_CRO` | Aucune offre sous cet intitulé | Le CRO n'existe pas comme métier autonome : 7 mentions au total, toujours comme composante d'un poste. |
| MarTech Specialist / MarTech Manager | `MARTECH_MARKETING_OPS` | Aucune offre sous cet intitulé | Le marché français utilise Marketing Operations, RevOps ou Expert CDP. |
| Marketing Automation AI Specialist | `METIER_IA_EMERGENT` | Aucune offre | Intitulé non employé en France en 2026. |
| AI Growth Specialist / AI-Powered Growth Marketer | `METIER_IA_EMERGENT` | Aucune offre (1 seul Growth Manager IA) | Le marché n'a pas encore stabilisé de dénomination. |
| Prompt Specialist appliqué au marketing | `METIER_IA_EMERGENT` | Aucune offre marketing | Les offres mentionnant le prompt engineering sont des postes tech/produit. |
| GenAI Content Specialist / AI CRM Specialist / AI Marketing Operations | `METIER_IA_EMERGENT` | Aucune offre | Intitulés non observés sur le marché français. |
| Generative Engine Optimization Specialist / Answer Engine Optimization Specialist | `METIER_IA_EMERGENT` | Aucune offre sous ces intitulés complets | Le marché utilise l'abréviation GEO, accolée à SEO : Consultant SEO/GEO, SEO SEA GEO AI Visibility Manager. |
| AI Search Specialist | `METIER_IA_EMERGENT` | Aucune offre | Recouvert par les intitulés SEO/GEO. |

### A.4 Faux positifs exclus du périmètre

Les règles d'exclusion ont été appliquées **avant** toute classification métier, afin d'éviter de gonfler artificiellement les volumes.

| Motif d'exclusion | Exemples réellement rencontrés | Offres |
|---|---|---|
| Non classé | — | 9 |

**Point d'analyse important.** L'exclusion des postes « tech/produit IA » est le résultat méthodologique le plus significatif de cette partie. La recherche ciblée sur les agents IA, le no-code, Make, n8n et Zapier fait remonter huit offres, dont **six sont des postes techniques ou produit** et non des postes marketing. Le marché de l'orchestration d'agents IA et de l'automatisation no-code existe bien en France en 2026, mais il est aujourd'hui capté par des profils tech, pas par des marketeurs. Ce constat est repris dans le test de l'hypothèse H9 du document de synthèse.

D'autres catégories de faux positifs annoncées dans le cadrage n'ont produit aucune offre à exclure, faute d'avoir été ramenées par les requêtes : graphiste, communication institutionnelle pure, relations presse traditionnelles, événementiel sans composante digitale, support client, vendeur e-commerce en magasin.

### A.5 Journal des requêtes de collecte d'offres

85 requêtes distinctes ont produit au moins une offre individuelle retenue.

| Requête | Offres retenues |
|---|---|
| `site:www.hellowork.com/fr-fr/emplois "marketing digital" CDI` | 10 |
| `site:fr.indeed.com/viewjob "social media manager" OR "responsable réseaux sociaux" Lyon OR Bordeaux OR Nantes OR Marseille` | 10 |
| `site:candidat.francetravail.fr/offres/recherche/detail community manager OR SEO OR CRM 2026` | 10 |
| `site:fr.indeed.com/viewjob "traffic manager" OR "acquisition manager" CDI` | 9 |
| `site:fr.indeed.com/viewjob "consultant SEO" OR "SEO manager" CDI` | 9 |
| `site:fr.indeed.com/viewjob "community manager" OR "social media manager" CDI 2026` | 9 |
| `site:fr.indeed.com/viewjob "content manager" OR "content marketing manager" CDI France` | 9 |
| `site:fr.indeed.com/viewjob "consultant SEA" OR "SEA manager" OR "Google Ads" specialist CDI` | 9 |
| `site:candidat.francetravail.fr/offres/recherche/detail marketing digital` | 9 |
| `site:www.welcometothejungle.com/fr/companies growth OR acquisition marketing emploi Paris` | 9 |
| `site:fr.indeed.com/viewjob alternance "marketing digital" OR "growth" OR "CRM" 2026 Lyon Nantes Lille` | 9 |
| `site:www.welcometothejungle.com/fr/companies "Product Marketing Manager" OR "Content" OR "Social Media" CDI Paris Lyon` | 9 |
| `site:www.hellowork.com/fr-fr/emplois SEO OR SEA OR "traffic manager" OR "social media" CDI 2026` | 9 |
| `site:www.hellowork.com/fr-fr/emplois "chargé de marketing digital" OR "webmarketing" alternance 2026` | 9 |
| `site:www.welcometothejungle.com/fr/companies "Data Analyst" OR "Marketing Ops" OR "RevOps" CDI Paris 2026` | 9 |
| `site:www.hellowork.com/fr-fr/emplois "growth" OR "acquisition" OR "performance" marketing CDI Paris 2026` | 9 |
| `site:fr.indeed.com/viewjob "responsable marketing digital" Paris CDI 2026` | 8 |
| `site:fr.indeed.com/viewjob "growth marketing" OR "growth manager" France CDI` | 8 |
| `site:fr.indeed.com/viewjob "web analyst" OR "digital analyst" OR "marketing data analyst" CDI` | 8 |
| `site:www.welcometothejungle.com/fr/companies "CRM Manager" OR "Lifecycle" OR "Marketing Automation" CDI` | 8 |
| `site:fr.indeed.com/viewjob "chargé de marketing digital" Nantes OR Rennes OR Toulouse OR Strasbourg` | 8 |
| `site:fr.indeed.com/viewjob "webmarketing" OR "webmarketeur" OR "chargé webmarketing" France CDI` | 8 |
| `site:fr.indeed.com/viewjob marketing digital Marseille OR "Aix-en-Provence" CDI alternance` | 8 |
| `site:fr.indeed.com/viewjob "chargé de communication digitale" OR "communication digitale" CDI France 2026` | 8 |
| `site:www.welcometothejungle.com/fr/companies alternance OR stage marketing growth CRM 2026` | 8 |
| `site:fr.indeed.com/viewjob "responsable marketing" OR "digital marketing manager" CDI Lyon OR Grenoble OR Annecy` | 8 |
| `site:www.hellowork.com/fr-fr/emplois "e-commerce manager" OR "content manager" OR "product marketing" CDI` | 8 |
| `site:www.hellowork.com/fr-fr/emplois "data analyst" marketing OR "web analyst" OR "analytics" CDI France` | 8 |
| `site:www.welcometothejungle.com/fr/companies "SEA" OR "Paid Search" OR "Media" consultant CDI France` | 8 |
| `site:www.welcometothejungle.com/fr/companies "SEO" OR "Analytics" OR "Data Analyst marketing" CDI France` | 7 |
| `site:candidat.francetravail.fr/offres/recherche/detail alternance marketing digital OR webmarketing 2026` | 7 |
| `site:fr.indeed.com/viewjob "chargé de marketing digital" OR "responsable acquisition" Bordeaux (33) CDI` | 7 |
| `site:www.welcometothejungle.com/fr/companies "Traffic Manager" OR "Paid" OR "Acquisition" CDI Lyon Bordeaux Nantes Lille` | 7 |
| `site:fr.indeed.com/viewjob "data analyst" marketing OR "analytics manager" OR "tracking specialist" France CDI` | 7 |
| `site:fr.indeed.com/viewjob "SEO" OR "content" OR "CRM" stage 2026 marketing digital Paris` | 7 |
| `site:fr.indeed.com/viewjob "chef de projet digital" OR "coordinateur marketing digital" CDI France` | 7 |
| `site:fr.indeed.com/viewjob "CRM" OR "marketing" alternance Lyon OR Villeurbanne 2026 offre` | 7 |
| `site:candidat.francetravail.fr/offres/recherche/detail "responsable marketing digital" OR "chef de projet digital" 2026` | 7 |
| `site:fr.indeed.com/viewjob "e-commerce manager" OR "responsable e-commerce" CDI` | 6 |
| `site:fr.indeed.com/viewjob "marketing automation" specialist OR manager CDI France` | 6 |
| `site:fr.indeed.com/viewjob "marketing operations" OR "revenue operations" OR "RevOps" France` | 6 |
| `site:fr.indeed.com/viewjob "CRM" HubSpot OR Salesforce OR Brevo chargé marketing France` | 6 |
| `site:www.hellowork.com/fr-fr/emplois growth OR acquisition OR CRM manager Lyon OR Nantes OR Bordeaux` | 6 |
| `site:fr.indeed.com/viewjob "SEO" OR "SEA" OR "acquisition" alternance 2026 Paris Lyon Bordeaux Nantes` | 6 |
| `site:fr.indeed.com/viewjob marketing digital OR webmarketing Nantes (44) CDI alternance 2026` | 6 |
| `site:fr.indeed.com/viewjob "marketplace manager" OR "e-merchandiser" OR "digital commerce" France` | 6 |
| `site:www.welcometothejungle.com/fr/companies "Marketing Manager" OR "Head of Growth" OR "Head of Marketing" CDI France 2026` | 6 |
| `site:candidat.francetravail.fr/offres/recherche/detail "traffic manager" OR "e-commerce" OR "growth" 2026` | 6 |
| `site:fr.indeed.com/viewjob "chargé de marketing" OR "assistant marketing" digital alternance septembre 2026 France` | 6 |
| `site:www.hellowork.com/fr-fr/emplois "CRM" OR "e-commerce" OR "digital" alternance Bordeaux OR Nantes OR Marseille 2026` | 6 |
| `site:fr.indeed.com/viewjob "trade marketing" OR "marketing produit" OR "chef de produit digital" France CDI` | 6 |
| `site:fr.indeed.com/viewjob "community manager" OR "social media" CDI Lille OR Nantes OR Toulouse 2026` | 6 |
| `site:www.hellowork.com/fr-fr/emplois "traffic manager" OR "social ads" OR "paid" CDI province France 2026` | 6 |
| `site:fr.indeed.com/viewjob "chargé de marketing digital" CDI` | 5 |
| `site:fr.indeed.com/viewjob "influence" OR "influenceurs" marketing manager CDI France` | 5 |
| `site:fr.indeed.com/viewjob marketing digital OR growth OR CRM Lille (59) OR "Hauts-de-France" CDI` | 5 |
| `site:fr.indeed.com/viewjob "email marketing" OR "emailing" OR "campaign manager" CRM France CDI` | 5 |
| `site:fr.indeed.com/viewjob "SEA" OR "Google Ads" OR "Meta Ads" alternance OR stage France 2026` | 5 |
| `site:fr.indeed.com/viewjob "responsable e-commerce" OR "trafic" OR "acquisition" alternance Lyon Toulouse Nice Montpellier 2026` | 5 |
| `site:fr.indeed.com/viewjob "influence" OR "social media" OR "content" alternance 2026 Paris Lyon` | 5 |
| `site:fr.indeed.com/viewjob "chef de projet marketing digital" alternance` | 4 |
| `site:fr.indeed.com/viewjob "product marketing manager" CDI France 2026` | 4 |
| `site:fr.indeed.com/viewjob "CRO" OR "conversion rate optimization" OR "AB testing" marketing CDI France` | 4 |
| `site:fr.indeed.com/viewjob "CRM" OR "lifecycle" OR "rétention" manager e-commerce retail France CDI 2026` | 4 |
| `site:www.welcometothejungle.com/fr/companies "E-commerce" OR "Influence" OR "Brand" CDI France 2026 marketing` | 4 |
| `site:fr.indeed.com/viewjob "paid social" OR "social ads" OR "programmatique" France CDI agence média` | 4 |
| `site:fr.indeed.com/viewjob "CRM manager" OR "responsable CRM" CDI France` | 3 |
| `site:fr.indeed.com/viewjob "paid social" OR "social ads" specialist CDI France` | 3 |
| `site:fr.indeed.com/viewjob "performance marketing" OR "media buyer" OR "paid media" CDI France` | 3 |
| `site:fr.indeed.com/viewjob "e-commerce" OR "marketplace" manager Nantes OR Lille OR Lyon CDI` | 3 |
| `site:fr.indeed.com/viewjob "chargé de marketing" digital PME industrie B2B CDI province 2026` | 3 |
| `site:fr.indeed.com/viewjob "SEO" OR "content" OR "acquisition" Nantes OR Rennes OR Angers CDI marketing` | 3 |
| `site:fr.indeed.com/viewjob "responsable marketing digital" OR "digital marketing" stage 2026 France` | 3 |
| `site:www.welcometothejungle.com/fr/companies "CRM" OR "Growth" OR "Acquisition" CDI Lyon OR Bordeaux OR Nantes OR Lille 2026` | 3 |
| `site:fr.indeed.com/viewjob "acquisition" OR "growth" OR "performance" marketing CDI startup scale-up Paris 2026` | 3 |
| `site:fr.indeed.com/viewjob "AI marketing" OR "IA générative" marketing manager France 2026` | 2 |
| `site:fr.indeed.com/viewjob "prompt" OR "agents IA" OR "automatisation" marketing no-code Make n8n Zapier France` | 2 |
| `site:fr.indeed.com/viewjob "brand content" OR "copywriter" OR "content strategist" marketing France CDI` | 2 |
| `site:fr.indeed.com/viewjob "marketing digital" Occitanie OR "Grand Est" OR Normandie OR Bretagne CDI` | 2 |
| `site:fr.indeed.com/viewjob "responsable digital" OR "digital manager" OR "e-business" CDI France 2026` | 2 |
| `site:fr.indeed.com/viewjob marketing digital OR CRM OR SEO OR growth CDI 2026 Toulouse OR Montpellier OR Nice OR Strasbourg` | 2 |
| `site:fr.indeed.com/viewjob "CRM" OR "marketing digital" CDI Rennes OR Angers OR Tours OR Dijon OR Reims` | 2 |
| `site:fr.indeed.com/viewjob "responsable acquisition" OR "demand generation" OR "lead generation" France` | 1 |
| `site:fr.indeed.com/viewjob "consultant marketing digital" OR "consultant acquisition" agence CDI France` | 1 |
| `site:fr.indeed.com/viewjob "CDP" OR "customer data platform" OR "server-side" OR "BigQuery" marketing France` | 1 |

---

## PARTIE B — PLATEFORMES ET CHEMINS D'ACCÈS SANS DONNÉES EXPLOITABLES

### B.0 Contrainte technique générale

**Seul l'outil de recherche web a fonctionné pendant toute la collecte.** Les accès HTTP directs aux sites (WebFetch, curl) sont bloqués par le proxy de l'environnement, et aucune clé d'API n'était disponible. Toutes les données proviennent donc des **titres, URL et extraits de pages publiques indexées par un moteur de recherche**. Cette contrainte a trois conséquences, signalées partout où elles s'appliquent dans les livrables :

1. Les champs absents des extraits sont notés `NC` et n'ont jamais été déduits — d'où 30,1 % de contrats et 52,9 % de niveaux de séniorité non renseignés.
2. Les comptes de compétences sont des **bornes basses** : un extrait ne restitue qu'une fraction du contenu de l'offre.
3. Les **séries historiques annuelles comparables n'ont pas pu être reconstituées** par métier : les pages de listes sont indexées à des dates hétérogènes et sous des libellés de requête différents.

### B.1 Plateformes et chemins testés sans résultat exploitable

#### Apec — offres individuelles

- **PLATEFORME :** Apec — offres individuelles
- **URL :** https://www.apec.fr/candidat/recherche-emploi.html/emploi
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** Marketing digital, responsable marketing digital, directeur marketing digital, alternance marketing digital
- **ZONES_TESTEES :** France, toutes régions
- **DONNEES_RECHERCHEES :** Offres individuelles avec entreprise, contrat, expérience, salaire
- **RESULTAT :** Seules des **pages de résultats de recherche** ont été indexées, sans contenu d'offre exploitable. Une seule page de détail d'offre est remontée (Responsable Marketing Digital F/H, Nice), sans extrait suffisant pour renseigner les champs.
- **DONNEES_MANQUANTES :** Entreprise, contrat, expérience, salaire, compétences des offres cadres Apec
- **AUTRES_CHEMINS_TESTES :** Requêtes `site:apec.fr detail-offre`, requêtes par intitulé, requêtes par fonction
- **SOURCE_DE_REMPLACEMENT :** **Études Apec utilisées à la place**, et elles constituent les sources les plus fiables de l'étude : L'intelligence artificielle en commercial-marketing (mars 2026), Les cadres et l'IA (mai 2026), Les métiers cadres porteurs 2026, Baromètres trimestriels 2026, référentiels métiers Marketing et Commercial.
- **IMPACT_SUR_L_ANALYSE :** **Impact réel mais compensé.** L'absence d'offres Apec individuelles prive l'échantillon d'une vision spécifiquement cadre du marché. Les études Apec, mobilisées massivement, apportent en revanche les données d'évolution et d'impact de l'IA que l'échantillon ne pouvait pas produire.

#### LinkedIn Jobs

- **PLATEFORME :** LinkedIn Jobs
- **URL :** https://fr.linkedin.com/jobs
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** Marketing digital, growth, CRM, SEO, SEA, paid social
- **ZONES_TESTEES :** France, villes NEXA
- **DONNEES_RECHERCHEES :** Offres individuelles
- **RESULTAT :** Aucune page `linkedin.com/jobs/view` exploitable n'est remontée dans les résultats indexés sur l'ensemble des requêtes lancées.
- **DONNEES_MANQUANTES :** Totalité des champs
- **AUTRES_CHEMINS_TESTES :** Requêtes `site:fr.linkedin.com/jobs/view` avec plusieurs combinaisons de métiers et de villes
- **SOURCE_DE_REMPLACEMENT :** Indeed, Welcome to the Jungle, HelloWork et France Travail, qui couvrent les mêmes employeurs
- **IMPACT_SUR_L_ANALYSE :** **Faible.** LinkedIn est fortement redondant avec les autres plateformes pour les intitulés recherchés ; les employeurs identifiés (agences, scale-ups, grands groupes) sont présents dans l'échantillon via les autres sources.

#### Talent.com

- **PLATEFORME :** Talent.com
- **URL :** https://fr.talent.com
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** Marketing digital, CRM
- **ZONES_TESTEES :** France, plusieurs départements
- **DONNEES_RECHERCHEES :** Offres individuelles et comptes d'offres
- **RESULTAT :** Seules des **pages de liste par ville** sont indexées (`fr.talent.com/jobs/k-marketing-digital-l-...`), sans compte d'offres daté dans le titre ni contenu d'offre individuelle.
- **DONNEES_MANQUANTES :** Volumes datés et offres individuelles
- **AUTRES_CHEMINS_TESTES :** Requêtes par ville et par intitulé
- **SOURCE_DE_REMPLACEMENT :** Indeed et HelloWork pour les volumes datés
- **IMPACT_SUR_L_ANALYSE :** **Nul.** Talent.com est un agrégateur : ses offres proviennent des plateformes déjà couvertes.

#### Jooble

- **PLATEFORME :** Jooble
- **URL :** https://fr.jooble.org
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** Marketing digital, consultant marketing digital, chef de produit marketing digital
- **ZONES_TESTEES :** Nantes et autres villes
- **DONNEES_RECHERCHEES :** Volumes d'offres et offres individuelles
- **RESULTAT :** Des comptes sont bien affichés mais **jugés non exploitables** : « Consultant marketing digital Nantes : 1 831 offres », « Chef produit marketing digital Nantes : 7 275 offres ». Ces valeurs relèvent d'un appariement lexical très lâche sur un agrégateur revendiquant plus de 20 000 sites sources, sans dédoublonnage.
- **DONNEES_MANQUANTES :** Volumes fiables
- **AUTRES_CHEMINS_TESTES :** Requêtes par ville et par intitulé
- **SOURCE_DE_REMPLACEMENT :** Indeed et HelloWork, dont les comptes sont datés et cohérents entre eux
- **IMPACT_SUR_L_ANALYSE :** **Nul, décision volontaire.** Retenir ces comptes aurait gravement faussé l'estimation du marché nantais. Ils sont explicitement écartés.

#### Meteojob, Monster, JobTeaser, Free-Work, ChooseYourBoss, LesJeudis

- **PLATEFORME :** Meteojob, Monster, JobTeaser, Free-Work, ChooseYourBoss, LesJeudis
- **URL :** —
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** Marketing digital, growth, CRM, SEO
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Offres individuelles
- **RESULTAT :** Aucune page d'offre exploitable remontée sur les requêtes lancées.
- **DONNEES_MANQUANTES :** Totalité des champs
- **AUTRES_CHEMINS_TESTES :** Requêtes `site:` sur chaque domaine, combinées à plusieurs intitulés
- **SOURCE_DE_REMPLACEMENT :** Indeed, Welcome to the Jungle, HelloWork, France Travail
- **IMPACT_SUR_L_ANALYSE :** **Faible.** Free-Work, ChooseYourBoss et LesJeudis sont orientés IT et freelance technique, donc peu pertinents pour le marketing digital ; JobTeaser aurait pu enrichir la vision stage et alternance, déjà bien couverte par Indeed et HelloWork (103 offres d'alternance dans l'échantillon).

#### Sites carrières d'entreprises et ATS (Greenhouse, Workday)

- **PLATEFORME :** Sites carrières d'entreprises et ATS (Greenhouse, Workday)
- **URL :** —
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** Growth, paid social, CRM, product marketing
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Offres individuelles
- **RESULTAT :** Des pages Greenhouse sont bien remontées (WPP Media, Sony Music France, Artefact, Oliver, The Orchard) mais **sans extrait exploitable** permettant de renseigner les champs de la grille de collecte.
- **DONNEES_MANQUANTES :** Entreprise confirmée, contrat, expérience, compétences
- **AUTRES_CHEMINS_TESTES :** Requêtes `site:job-boards.greenhouse.io` combinées aux intitulés métiers
- **SOURCE_DE_REMPLACEMENT :** Les mêmes employeurs sont présents dans l'échantillon via Welcome to the Jungle (Artefact, WPP Media/GroupM, Havas) et Indeed
- **IMPACT_SUR_L_ANALYSE :** **Faible.** Les employeurs concernés sont couverts par ailleurs.

#### API France Travail (offres d'emploi v2)

- **PLATEFORME :** API France Travail (offres d'emploi v2)
- **URL :** https://francetravail.io
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** Ensemble des codes ROME du marketing digital
- **ZONES_TESTEES :** France entière
- **DONNEES_RECHERCHEES :** Séries d'offres datées, volumes par métier et par région
- **RESULTAT :** **Aucune clé d'API disponible** dans l'environnement et accès HTTP direct bloqué par le proxy.
- **DONNEES_MANQUANTES :** Séries annuelles comparables 2024-2025-2026 par métier et par région, nombre de candidats par offre, durée de publication
- **AUTRES_CHEMINS_TESTES :** Aucun chemin alternatif possible sans authentification
- **SOURCE_DE_REMPLACEMENT :** Pages d'offres individuelles France Travail indexées (39 offres collectées) et stocks de listes Indeed et HelloWork datés
- **IMPACT_SUR_L_ANALYSE :** **Impact fort et assumé.** C'est la principale limite de l'étude : sans cette API, les **évolutions annuelles par métier ne peuvent pas être calculées**. Toutes les affirmations d'évolution du document de synthèse s'appuient donc sur des études publiées (Apec, Fevad, SRI, BMO) et jamais sur l'échantillon d'offres. Cette limite est signalée dans les hypothèses H1 et H5, dans les colonnes EVOLUTION des trois onglets Excel, et dans l'encadré de décision.

#### Insee — populations actives régionales

- **PLATEFORME :** Insee — populations actives régionales
- **URL :** https://www.insee.fr
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** —
- **ZONES_TESTEES :** Régions administratives
- **DONNEES_RECHERCHEES :** Population active par région pour normaliser les volumes
- **RESULTAT :** Aucune donnée précise n'a été collectée pendant l'étude.
- **DONNEES_MANQUANTES :** Population active régionale exacte et datée
- **AUTRES_CHEMINS_TESTES :** Non testé faute de temps de collecte disponible
- **SOURCE_DE_REMPLACEMENT :** Ordres de grandeur usuels utilisés à la place
- **IMPACT_SUR_L_ANALYSE :** **Modéré et explicitement tracé.** La colonne `OFFRES_POUR_100_000_ACTIFS` de l'onglet REGIONS_METIERS est marquée `ESTIMATION` : elle permet une comparaison relative entre régions mais ne doit pas être citée comme une donnée.

#### Numeum, OPCO Atlas, Grande École du Numérique, France Num, IAB France, Union des Marques, CPA

- **PLATEFORME :** Numeum, OPCO Atlas, Grande École du Numérique, France Num, IAB France, Union des Marques, CPA
- **URL :** —
- **DATE_DU_TEST :** 2026-09-07
- **METIERS_TESTES :** —
- **ZONES_TESTEES :** France
- **DONNEES_RECHERCHEES :** Études sectorielles complémentaires sur les métiers du marketing
- **RESULTAT :** Non atteints : la collecte documentaire a été concentrée sur les producteurs de données les plus directement pertinents.
- **DONNEES_MANQUANTES :** Éclairages complémentaires sur les compétences et la formation
- **AUTRES_CHEMINS_TESTES :** Recherches thématiques génériques
- **SOURCE_DE_REMPLACEMENT :** Apec, France Travail, Dares, Fevad, SRI/UDECAM/Oliver Wyman, Alliance Digitale/EY, observatoires salariaux
- **IMPACT_SUR_L_ANALYSE :** **Faible.** Les sources mobilisées couvrent le marché du travail, le marché publicitaire, l'e-commerce, le poids économique de la filière et l'impact de l'IA — soit l'ensemble des dimensions nécessaires à la décision.

### B.2 Requêtes lancées sans offre exploitable

- `site:fr.indeed.com/viewjob "email marketing" OR "CRM specialist" OR "Klaviyo" OR "Braze" France`
  - 0 offre individuelle (résultats hors périmètre : itjobswatch UK, builtin, wikipedia). Requête trop chargée en OR + noms d'outils. Remplacée par des requêtes par outil isolé.
- `site:fr.jooble.org OR site:fr.talent.com "marketing digital" offre emploi Nantes`
  - Pages de liste uniquement. Comptes Jooble jugés NON EXPLOITABLES (agrégation très large : "Consultant marketing digital Nantes = 1831 offres", "Chef produit marketing digital Nantes = 7275 offres" — appariement lexical trop lâche, sans dédoublonnage). Non retenus dans les volumes.
- `site:fr.indeed.com/viewjob "e-commerce" OR "CRM" OR "acquisition" Nantes OR "Loire-Atlantique" emploi`
  - 0 offre marketing digital retenue. Résultats hors périmètre : préparateur/livreur e-commerce, gestionnaire carrière, intégrateur CRM Efficy (IT), consultant Odoo (ERP). Signal à retenir : la requête "e-commerce/CRM/acquisition Nantes" ne fait pas remonter d'offres marketing — faiblesse relative du marché nantais sur ces intitulés (à confirmer par les volumes).
- `site:fr.indeed.com/viewjob "prompt" OR "agents IA" OR "automatisation" marketing no-code Make n8n Zapier France`
  - 8 offres trouvées mais SEULES 2 ont une finalité marketing (Directeur Marketing & Digital Saint-Fons ; Chargé de projet digital Data/Catalogue/Marketplace Toulouse). Les 6 autres sont des postes TECH/PRODUIT (Stage Développeur d'agents IA, Product Builder IA & No-Code, Product Builder IA Rennes, Alternant Ingénieur IA & Automatisation, Agent Builder AI/GenAI freelance, Développeur Intégrations API & IA/Agents MCP) : exclues du périmètre marketing (EXCLU_DU_PERIMETRE). CONSTAT ANALYTIQUE MAJEUR : le marché de l'orchestration d'agents IA et de l'automatisation no-code existe bien en France en 2026, mais il est majoritairement capté par des profils tech/produit, PAS par des profils marketing. À intégrer au test de H9.
- `site:fr.indeed.com/viewjob "chargé de fidélisation" OR "customer marketing" OR "retention manager" France`
  - Comptes "Fidélisation clients" (18 000+), "Chargé Client Fidélisation" (6 000+) et "Responsable Fidélisation Clients" (6 000+) NON RETENUS : ces requêtes captent massivement des postes de relation client / service client / téléconseil sans finalité marketing. Seuls les comptes CRM Marketing Manager (800+) et Responsable CRM Fidélisation (1 000+) sont conservés, avec réserve.
- `site:fr.indeed.com/viewjob "CRO" OR "AB Tasty" OR "Kameleoon" OR "Contentsquare" OR "Hotjar" France emploi`
  - 1 seule offre pertinente (Consultant BI confirmé Paris, mentionnant des partenariats AB Tasty / Kameleoon / Contentsquare). Les autres résultats sont hors périmètre (commercial, assistant commercial, communication événementielle). CONSTAT : les outils de CRO/testing sont TRÈS PEU cités explicitement dans les intitulés et extraits d'offres françaises indexées — le CRO existe surtout comme composante d'un poste (e-commerce, growth, analytics) et non comme métier autonome à volume significatif.

### B.3 Comptes de volumes écartés

| Compte affiché | Source | Motif de l'écartement |
|---|---|---|
| Consultant marketing digital Nantes : 1 831 offres | Jooble | Appariement lexical trop lâche sur un agrégateur sans dédoublonnage ; incohérent avec les 82 offres Indeed pour Nantes. |
| Chef produit marketing digital Nantes : 7 275 offres | Jooble | Idem, valeur manifestement non significative. |
| Fidélisation clients : 18 000+ offres | Indeed | La requête capte massivement des postes de relation client, service client et téléconseil sans finalité marketing. |
| Chargé Client Fidélisation : 6 000+ offres | Indeed | Idem. |
| Responsable Fidélisation Clients : 6 000+ offres | Indeed | Idem. |

Les comptes **CRM Marketing Manager (800+)** et **Responsable CRM Fidélisation (1 000+)** ont en revanche été conservés, avec réserve explicite sur la largeur du périmètre lexical.

---

## Note finale sur la fiabilité

Pour chaque résultat important des livrables, les métadonnées suivantes sont conservées : source, date, périmètre, taille d'échantillon, statut observé ou estimé, niveau de confiance. Aucune offre, aucun volume, aucune évolution et aucune URL n'a été inventé. Les valeurs absentes des extraits sont notées `NC` et n'ont jamais été complétées par déduction. Les estimations sont marquées `ESTIMATION` et leur mode de calcul est documenté à l'endroit où elles apparaissent.