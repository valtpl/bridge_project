# Notice d'utilisation : `word2vec_projection.py`

## 1. Description
Le script `word2vec_projection.py` utilise le modèle Word2Vec pour transformer un corpus de textes en vecteurs, effectue une réduction de dimension avec PCA  et applique un clustering (KMeans ou HDBSCAN). Il génère ensuite une visualisation interactive des mots projetés sur un graphique 2D.

## 2. Fonctionnalités
1. **Chargement et nettoyage du corpus** : Le script charge un corpus de textes à partir d'un fichier pickle, nettoie les textes et les lemmatise.
2. **Entraînement de Word2Vec** : Un modèle Word2Vec est entraîné sur le corpus pour générer des vecteurs de mots.
3. **Réduction de dimension** : PCA est utilisé pour réduire la dimension des vecteurs de mots à 2 dimensions.
4. **Clustering** : Le script applique un clustering des mots (KMeans ou HDBSCAN) pour regrouper des mots similaires.
5. **Visualisation** : Une visualisation interactive est générée avec Plotly, où chaque mot est projeté selon ses composantes PC1 et PC2.

## 3. Prérequis
- **Python 3.x**
- Bibliothèques : `pandas`, `numpy`, `nltk`, `spacy`, `gensim`, `sklearn`, `hdbscan`, `plotly`

### 4. Installation des dépendances
```bash
pip install pandas numpy nltk spacy gensim scikit-learn hdbscan plotly
```
## 5. Comment exécuter le script
Le corpus est chargé depuis un fichier pickle. Vous devez modifier le chemin du fichier ```data/datasets/FUSION_articles.pkl``` selon les besoins. Avec soit ```FUSION```, ```EOLIEN``` ou ```AGRI```.

Le fichier HTML (graphique interactif) est généré dans ```output/projection_thematique/FUSION_word_projection_hdbscan.html```. Vous pouvez ajuster le nom et le chemin du fichier de sortie selon la techno.
