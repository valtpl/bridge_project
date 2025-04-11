# Notice d'utilisation : `youtube_scraping.py`

## 1. Description
Ce script permet de récupérer les commentaires des vidéos YouTube liées à une technologie donnée et de sauvegarder ces commentaires dans un fichier **pickle**. Il utilise l'API de YouTube pour rechercher les vidéos, récupérer les commentaires et les enregistrer dans un format structuré.

## 2. Prérequis
- **Clé API YouTube** : Ce script nécessite une clé API PERSO valide pour accéder à l'API YouTube.
- **Bibliothèques Python** :
  - `google-api-python-client` pour interagir avec l'API YouTube.
  - `pandas` 
  - `pickle` 
  
Installez les bibliothèques nécessaires avec la commande suivante :
```bash
pip install google-api-python-client 
```
## 3. Utilisation
```tech_name``` : Remplacez cette variable par le nom de la technologie pour rechercher les vidéos associées (par exemple "fusion nucléaire").
```save_folder``` : Indiquez le dossier où vous souhaitez sauvegarder le fichier pickle contenant les commentaires

Le script crée un fichier .pkl dans le dossier spécifié, contenant un DataFrame de pandas avec le titre de la vidéo, les commentaires, les auteurs, les dates de publication et les "like counts".

On retrouve nos fichiers .pkl créés dans le repo ```/data```, il est possible de les visualiser en utiliser le notebook ```outils.ipynb``` dans le repo ```/scripts```.