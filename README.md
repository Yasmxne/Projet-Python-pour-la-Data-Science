# Projet-Python-pour-la-Data-Science

Ce dépôt rassemble le travail réalisé dans le cadre du cours **Python pour la Data Science**.  
Le fichier README facilite la compréhension du projet et propose un ensemble de ressources utiles.  

## Objectif du projet

L'objectif de ce projet est d'analyser différents facteurs pouvant influencer le taux de criminalité dans les différents arrondissements de la ville de Paris.

## Ressources de données

Voici quelques bases intéressantes pour commencer à travailler :

1. **Éclairage public à Paris**  
   Données d'éclairage public contenant les **Points lumineux EP** et le **Mobilier urbain illuminé (MU)**.  
   [Lien vers les données](https://www.data.gouv.fr/fr/datasets/eclairage-public/)

2. **Statistiques de la délinquance en France**  
   Bases statistiques (communale, départementale et régionale) sur la délinquance enregistrée par la police et la gendarmerie nationales.  
   [Lien vers les données](https://www.data.gouv.fr/fr/datasets/bases-statistiques-communale-departementale-et-regionale-de-la-delinquance-enregistree-par-la-police-et-la-gendarmerie-nationales/)  

   - Cette base contient plusieurs niveaux géographiques. Pour accéder aux données des **arrondissements de Paris**, choisissez la base **communale**.  
   - Étant donné la taille importante du fichier, appliquez un filtre sur la colonne `CODGEO_2024` et sélectionnez les codes INSEE allant de **75101** à **75120**.  

3. **Caméras de vidéoprotection à Paris**  
   Emplacements des caméras de vidéoprotection (données issues du Bulletin Officiel de la ville de Paris, 01/02/2019).  
   [Lien vers les données](https://www.data.gouv.fr/fr/datasets/emplacements-dimplantation-de-cameras-de-videoprotection-bo-ville-de-paris-du-01-02-2019/)  

   - Cette base pourrait nécessiter un traitement préalable en suivant la méthodologie décrite par l'auteur.

4. **Taux de pauvereté à Paris**  
   Structure et distribution des revenus, inégalité des niveaux de vie en 2017.  
   [Lien vers les données](https://www.insee.fr/fr/statistiques/4291712)  

   - Il s'agit d'un fichier zip contenant un dossier avec plusieurs bases, nous choisirons la plus pertinente. Les données doivent être filtrées.
   
5. **Logements sociaux à Paris**  
   Logements sociaux financés à Paris.  
   [Lien vers les données](https://opendata.paris.fr/explore/dataset/logements-sociaux-finances-a-paris/table/?disjunctive.bs&disjunctive.mode_real&disjunctive.nature_programme&disjunctive.ville&disjunctive.code_postal&sort=-bs&basemap=jawg.dark&location=12,48.8592,2.3341)  
   
6. **Commerces en Ile de France**  
   Les commerces par commune ou arrondissement (base permanente des équipements).
   
   - Cette Base nécessite d'être filtrée pour se limiter aux arrondissements parisiens.   
   [Lien vers les données](https://www.data.gouv.fr/fr/datasets/les-commerces-par-commune-ou-arrondissement-base-permanente-des-equipements-idf/)  

   
---

### Note
Pour exploiter ces données, des étapes de nettoyage et de pré-traitement seront nécessaires. Assurez-vous de bien comprendre la structure des bases et les variables qu'elles contiennent avant de commencer l'analyse.