# Projet-Python-pour-la-Data-Science

Ce dépôt rassemble le travail réalisé dans le cadre du cours **Python pour la Data Science**.  
Le fichier README facilite la compréhension du projet, des dépendances entre les fichiers et propose un ensemble de ressources utiles.

## Motivation du projet

Notre projet chercher à apporter des élèments de réponse à deux problématiques socio-économiques souvent évoquées par les médias, car elles jouent un rôle significatif, bien que parfois débattu, dans le sentiment de sécurité ressenti dans l’espace public.

**La réduction de l’éclairage urbain la nuit**, justifiée par des économies d’énergie, a suscité des inquiétudes quant à la sécurité des citoyens. Certaines communes, comme Orléans, ont décidé de rétablir l’éclairage face à des tensions sociales croissantes ([source : BFMTV, 09/10/2024](https://rmc.bfmtv.com/actualites/societe/orleans-remet-la-lumiere-la-nuit-on-rallume-parce-que-l-etat-nous-a-envoye-600-migrants-et-sdf_AV-202410090526.html)). D’autres témoignages, notamment à Bordeaux, montrent que l’extinction des lumières peut exacerber le sentiment d’insécurité ([source : TF1 Info, 25/12/2024](https://www.tf1info.fr/societe/video-jt-tf1-je-ne-me-sens-pas-en-securite-a-bordeaux-ces-habitants-demandent-le-retour-de-l-eclairage-la-nuit-2334216.html)). Enfin, cette mesure est diversement perçue selon les contextes locaux ([source : FranceInfo, 06/10/2023](https://www.francetvinfo.fr/replay-radio/le-choix-franceinfo/economies-d-energie-comment-est-percue-l-extinction-des-lumieres-la-nuit-dans-certaines-communes_5509065.html)).

L'utilisation de **caméras de vidéosurveillance**, qui bien que largement déployées, suscitent des débats quant à leur efficacité. Si elles sont parfois utiles pour élucider des infractions, leur impact réel sur la criminalité reste controversé ([source : FranceInfo, 19/12/2023](https://www.francetvinfo.fr/replay-radio/le-vrai-du-faux/les-cameras-de-videosurveillance-sont-elles-vraiment-utiles-pour-lutter-contre-le-narcotrafic_6838112.html) et [source : TF1 Info, 14/12/2023](https://www.tf1info.fr/justice-faits-divers/enquete-video-tf1-videosurveillance-les-cameras-sont-elles-vraiment-efficaces-contre-la-delinquance-police-municipale-gendarmerie-2266405.html)). 

Cette analyse croisée cherche ainsi à apporter un éclairage précis sur l’articulation entre ces deux dispositifs et leur impact réel sur la sécurité publique. D’autres facteurs, tels que le niveau de pauvreté ou le caractère commercial des espaces seront également observés afin de mieux comprendre l'efficacité des levier pour améliorer la sécurité dans les zones urbaines.

## Objectif du projet

L'objectif de ce projet est d'analyser différents facteurs pouvant influencer le taux de criminalité dans les différents arrondissements de la ville de Paris.


## Dépendance entre les notebooks 
Ce projet contient plusieurs notebook pour traiter les différentes bases nécessaires ainsi qu'un notebook principal qui effectue une jointure entre les données principales issues de chaque base et contient le modèle final.

1. **BaseDélinquance.ipynb** :  

   Ce notebook étudie la base décrivant les statistiques de la délinquance à Paris et permet de préparer les données concernant le taux de criminalité dans chaque arrondissement.
   
2. **Basevideprotection.ipynb** :

   Ce notebook réalise une étude statistique et temporelle sur le système de vidéo surveillance à Paris et permet de rassembler des informations sur le nombre de caméras de surveillance par arrondissement pour le modèle final.
   
3. **BaseEclairage_v2.ipynb** : 

   Ce notebook traite des données sur l'éclairage dans la ville de Paris et calcule la densité lumineuse dans les arrondissements afin d'utiliser cette donnée dans le modèle final.
  
4. **BasePauverete.ipynb** :

   Ce notebook contient le traitement effectué sur  3 bases, une contenant le taux de pauvereté, une le nombre des logements sociaux et la 3ème le nombre de commerces dans les arrondissements parisiens afin de rassembles plusieurs variables socio-économiques utiles dans notre modèle final.
  
5. **BaseEclairageLyon.ipynb** :
 
   Ce notebook traite des données sur l'éclairage dans la ville de Lyon. Le but étant d'obtenir plus de points pour notre modèle final de régression en ajoutant la ville de Lyon dans notre étude. Cependant, nous n'avons pas trouvé l'ensemble des variables que nous avons obtenu pour la ville de Paris. Ce qui ne nous a pas permis d'ajouter la ville de Lyon à la base finale. Néanmoins, les résultats obtenus restent intéressants.
  
6. **Main.ipynb** :

  
   Ce notebook rassemble les variables obtenues dans les différents notebooks en une seule base finale sur laquelle nous appliquons un modèle de régression ainsi qu'une Analyse en Composantes Principales afin de déterminer les variables qui influent sur le taux de criminalité dans la ville de Paris.



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
