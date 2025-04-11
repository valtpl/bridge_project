# Notice d'utilisation : `sentiment_analysis.py`
Ce script permet d’appliquer une **analyse de sentiment automatique** aux articles seléctionés (titre, corps, et leur combinaison), en utilisant un modèle pré-entraîné BERT multilingue. On génère un fichier `.pkl` contenant les scores de sentiment pour chaque article.

---

## Prérequis 

Installez si besoin les bibliothèques suivantes : 
```bash 
pip install transformers torch pandas tqdm
```

## 1. Modèle utilisé

- [`nlptown/bert-base-multilingual-uncased-sentiment`](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- Sortie : score de 0 à 4
  - `0` = Très négatif
  - `1` = Négatif
  - `2` = Neutre
  - `3` = Positif
  - `4` = Très positif

---

## 2. Entrée

Un fichier `.pkl` contenant nos dataframe en fonction de la technologie. 

Prédiction du sentiment :
- sur le Corps de l’article
- sur le Titre
- puis calcul d’un score moyen ((titre + corps) / 2)

Sauvegarde dans un nouveau fichier pickle avec trois nouvelles colonnes :
- `sentiment_corps`
- `sentiment_title`
- `sentiment_mixed`

## 3. Sortie 

Un fichier .pkl contenant les articles enrichis des scores de sentiment

## 4. Exemple d'exécution
```bash
python sentiment_analysis.py
```
Attention à s'assurer que le chemin d'**entrée/sortie** est correctement défini dans le main.



