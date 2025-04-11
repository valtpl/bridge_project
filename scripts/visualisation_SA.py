# plot les resultats de SA en fonction des differentes méthodes
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_pickle_file(pickle_filename):
    """Charge les articles depuis un fichier pickle."""
    with open(pickle_filename, 'rb') as pickle_file:
        df = pickle.load(pickle_file)
    return df

def categorize_sentiments(df):
    """Catégorise les sentiments en 'très négatif', 'négatif', 'neutre', 'positif', 'très positif'."""
    # Mappage pour chaque score de sentiment
    sentiment_map = {
        0: 'très négatif',
        1: 'négatif',
        2: 'neutre',
        3: 'positif',
        4: 'très positif'
    }
    
    df['sentiment_corps_category'] = df['sentiment_corps'].apply(lambda x: sentiment_map.get(x, 'neutre'))
    df['sentiment_title_category'] = df['sentiment_title'].apply(lambda x: sentiment_map.get(x, 'neutre'))
    df['sentiment_mixed_category'] = df['sentiment_mixed'].apply(lambda x: sentiment_map.get(x, 'neutre'))
    
    return df

def plot_sentiment_distribution(df, technologie_name):
    """Affiche l'histogramme des catégories de sentiment"""
    plt.figure(figsize=(15, 10))

    # Défini l'ordre des catégories
    sentiment_order = ['très négatif', 'négatif', 'neutre', 'positif', 'très positif']

    # Histogramme des sentiments pour chaque colonne
    plt.subplot(2, 2, 1)
    sns.countplot(x='sentiment_corps_category', data=df, palette='Blues', order=sentiment_order)
    plt.title(f"Distribution des sentiments (Corps) - {technologie_name}")
    plt.xlabel("Sentiment")
    plt.ylabel("Nombre d'articles")

    plt.subplot(2, 2, 2)
    sns.countplot(x='sentiment_title_category', data=df, palette='Greens', order=sentiment_order)
    plt.title(f"Distribution des sentiments (Titre) - {technologie_name}")
    plt.xlabel("Sentiment")
    plt.ylabel("Nombre d'articles")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_pickle_file = "output/SA/AGRI_SA.pkl"  # Changez ce chemin selon le fichier à étudier
    technologie_name = "AGRI"  # Nom de la technologie IMPORTANT pour affichage ds le titre et suavegarde des graphs

    df = load_pickle_file(input_pickle_file)
    df = categorize_sentiments(df)

    plot_sentiment_distribution(df, technologie_name)
