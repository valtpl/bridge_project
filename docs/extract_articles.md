# Notice d'utilisation : `extract_articles.py`

## 1. Description
Le fichier `extract_articles.py` permet d'extraire des informations spécifiques depuis les fichiers HTML d'europress, notamment :
- Le titre de l'article
- Le contenu de l'article
- La date de publication

Ces informations sont ensuite sauvegardées dans un fichier **pickle** sous forme de DataFrame, ce qui permet de les utiliser facilement pour nos analyses ultérieures.

## 2. Prérequis
bibliothèques nécessaires 
- `pandas`
- `beautifulsoup4`
- `lxml`
- `pickle`


Vous pouvez installer ces dépendances en exécutant la commande suivante dans votre terminal ou votre environnement virtuel Python :
```bash
pip install pandas beautifulsoup4 lxml pickle
```

## 3. Comment utiliser le script
Modifier les paramètres dans le fichier :

- `folder_path` : Remplacez ce chemin par le chemin du dossier contenant les fichiers de la technologie souhaitée.
- `tech_name` : Spécifiez le nom sous lequel vous souhaitez sauvegarder le fichier pickle de sortie. Disponible ensuite dans le dossier output.


