# Notice d'utilisation : `relevant_articles.py`

## 1. Description
Ce script permet de sélectionner et extraire les articles les plus pertinents concernant une technologie spécifique, à partir d'un fichier pickle. L'extraction se base sur une liste de mots-clés définis et modifiable aux besoins, appliquant une technique de traitement de texte pour évaluer la pertinence des articles à l'aide de la méthode TF-IDF.


## 2. Prérequis
bibliothèques nécessaires 
- `pandas`
- `numpy`
- `scikit-learn` (pour la méthode TF-IDF)
- `nltk` (pour la tokenisation et l'élimination des mots vides)

Vous pouvez installer ces dépendances en exécutant la commande suivante dans votre terminal ou votre environnement virtuel Python :
```bash
pip install numpy pandas scikit-learn nltk
```
La liste de mots-clés utilisée pour la sélection des articles se réfère à des termes concernant l'acceptabilité d'une technologie. Cette liste peut être modifiée pour s'adapter à une autre technologie ou un autre angle d'attaque du sujet d'intérêt.

## 3. Utilisation du script

- `pickle_file_to_process` : changez le chemin du fichier pickle à traiter selon la technologie.

Le script applique les étapes suivantes :
- Charge les articles à partir du fichier pickle spécifié.
- Applique le prétraitement du texte (nettoyage, tokenisation, suppression des mots vides).
- Calcule la matrice TF-IDF pour les mots-clés de la technologie concernée.
- Sélectionne les `top_n` articles les plus pertinents selon les scores TF-IDF.

## 4. Exécution du Script 

1. Modifiez les variables du script pour correspondre à la technologie sur laquelle effectuer la sélection (par exemple, en changeant les mots-clés et le fichier pickle)
2. Exécutez le script avec la commande suivante dans ton terminal :
```bash
python relevant_articles.py
```
Après avoir sélectionné les articles pertinents, le script les sauvegarde dans un fichier `relevant_articles`pickle de sortie.
