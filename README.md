# Analyse de Sentiment d’articles de presse (EuroPress) sur des tehcnologies bas-carbone

Ce projet intervient dans le cadre du sujet de recherche suivant : “Increase social acceptability of nuclear fusion, agrivoltaics and offshore wind through national support programmes”. Ici nous avons pour but à analyser les **sentiments exprimés dans la presse** à propos de ces technologies.  
L’objectif est de mesurer et visualiser l’évolution des sentiments associés à ces thématiques dans le temps et selon différentes méthodes. 

---

## Objectifs

- Extraire les sentiments exprimés dans les articles de presse.
- Comparer les résultats en fonction :
  - du **corps** de l’article
  - du **titre**
  - de la **moyenne** des deux
- Produire des **visualisations temporelles** et **distributions** des sentiments.
- Faciliter l’analyse afin d'identifier les leviers et les facteur d'amélioration de l'acceptabilité sociale de ces projets bas-carbone.

---

## Technologies & Librairies

- **Modèle NLP** : [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- **Librairies principales** :
  - `transformers`
  - `torch`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `tqdm`
  - `dateutil`

---

## Documentation

Dans le dossier `docs`, vous trouverez la documentation détaillée sur chaque fonction créée dans les scripts du projet. Cela inclut des explications sur leur fonctionnement, leurs paramètres et leur utilisation. 


---


## Etapes du projet 

### 1. **Scraping des données depuis YouTube et commentaires**
   - Récupérer les données depuis YouTube en utilisant l'API YouTube pour collecter les titres, descriptions et commentaires de vidéos.
   - Scraper des informations pertinentes (titres, descriptions, commentaires) sur une période donnée.
   
### 2. **Extraction des articles depuis une base de données HTML d'Europress**
   - Extraire des articles à partir d'une base de données d'extraits d'Europress en utilisant un moteur de recherche basé sur des mots-clés.
   - Appliquer des critères de sélection pour récupérer uniquement les articles pertinents pour la technologie étudiée.
   
### 3. **Sélection des articles pertinents avec TF-IDF**
   - Utiliser un modèle de **TF-IDF** pour sélectionner les articles les plus pertinents en fonction d'une liste de mots-clés pré-définis.
   - Calculer la pertinence de chaque article en fonction de la fréquence des mots-clés par rapport à son contenu.
   
### 4. **Projection thématique avec Word2Vec**
   - Appliquer la méthode **Word2Vec** pour transformer les articles en vecteurs et les projeter dans un espace thématique.
   - Identifier les sujets principaux du corpus en fonction des similitudes sémantiques entre les mots et les articles.
   
### 5. **Analyse des Sentiments avec BERT**
   - Utiliser un modèle **BERT pré-entraîné** pour effectuer une analyse de sentiment sur les articles récupérés.
   - Appliquer l'analyse de sentiment à la fois sur le **corps de l'article** et sur le **titre** pour obtenir des prédictions détaillées.
   - Calculer un score de sentiment mixte en prenant la moyenne des sentiments du titre et du corps de l'article.
   
### 6. **Visualisation des Sentiments**
   - Générer des **histogrammes** et des visuels pour la répartition des sentiments (très négatif, négatif, neutre, positif, très positif) pour chaque type d'analyse (corps, titre, mixte).
   
### 7. **Visualisation de l'évolution des sentiments au cours du temps**
   - Traiter la **date** des articles et l'analyser par rapport à l'évolution des sentiments.
   - Tracer l’évolution du **score de sentiment** au fil du temps à l’aide de graphiques, incluant une **ligne moyenne** pour dégager la tendance générale.

---

## Contact

Si vous avez des questions ou des suggestions concernant ce projet, n'hésitez pas à me contacter :

- **Nom** : TEMPLE VALENTIN
- **Email** : valentintpl@gmail.com

Je serai ravi de discuter avec vous de ce projet ou de répondre à vos questions !

---
