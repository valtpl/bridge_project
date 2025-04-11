# Notice d'utilisation : `visualisation.py`

Ce script permet de **visualiser la distribution des sentiments** détectés dans notre jeu d'articles en fonction de différentes méthodes d’analyse (`titre`, `corps`, `moyenne des deux`). Il repose sur les résultats produits par un script d’analyse de sentiment (voir `sentiment_analysis.py`).

## Prérequis 

Installez si besoin les bibliothèques suivantes : 
```bash 
pip install pandas matplotlib seaborn
```

---

## 1. Fonctionnalités

- Charge un fichier `.pkl` contenant les scores de sentiment.
- Catégorise les scores en :
  - `0` → très négatif
  - `1` → négatif
  - `2` → neutre
  - `3` → positif
  - `4` → très positif
- Génére des histogrammes comparatifs pour :
  - Le **corps** de l’article
  - Le **titre** de l’article

---

## 2. Entrée attendue

Un fichier pickle `.pkl` contenant un DataFrame pandas avec les colonnes suivantes :
- `sentiment_corps` (score 0-4)
- `sentiment_title` (score 0-4)
- `sentiment_mixed` (score moyen)

## 3. Sorties

Une visualisation matplotlib/seaborn s’affiche avec :

- Un histogramme des sentiments détectés dans les `corps`
- Un histogramme des sentiments détectés dans les `titres`

---

## 4. Utilisation
Assurez-vous d’avoir modifié la variable `input_pickle_file` avec le bon chemin, et `technologie_name` avec le nom de la technologie analysée (pour les titres des graphiques).





