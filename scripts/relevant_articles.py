# to select only relevant articles from the pkl files of each tech
import re
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def preprocess_text(text):
    """Prétraitement du texte : nettoyage, tokenisation et suppression des mots vides."""
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Enlève les caractères non alphabétiques
    text = text.lower()  # Convertit le texte en minuscules
    tokens = word_tokenize(text)  # Tokenisation
    tokens = [word for word in tokens if word not in stopwords.words('french')]  # Suppression des mots vides
    return ' '.join(tokens)

def load_articles_from_pickle(pickle_filename):
    """Charge les articles à partir d'un fichier pickle."""
    with open(pickle_filename, 'rb') as pickle_file:
        df = pickle.load(pickle_file)
    return df

# Calcul de la matrice TF-IDF pour les mots-clés spécifiés
def compute_tfidf_for_keywords(articles, keywords):
    """Calcule la matrice TF-IDF pour les mots-clés spécifiés."""
    vectorizer = TfidfVectorizer(vocabulary=keywords)  
    tfidf_matrix = vectorizer.fit_transform(articles['Corps_preprocessed'])  # Utilise le texte prétraité pour le calcul TF-IDF
    return tfidf_matrix, vectorizer

# Sélection des articles les plus pertinents en fonction des scores TF-IDF des mots-clés
def select_relevant_articles_by_keywords(tfidf_matrix, top_n=50):
    """Sélectionne les articles les plus pertinents en fonction des scores TF-IDF des mots-clés."""
    scores = np.array(tfidf_matrix.sum(axis=1)).flatten() 
    top_indices = scores.argsort()[-top_n:][::-1]  
    return top_indices

# Sauvegarde des articles pertinents dans un fichier pickle
def save_relevant_articles_to_pickle(df, relevant_indices, output_filename):
    """Sauvegarde les articles pertinents dans un fichier pickle."""
    relevant_articles = df.iloc[relevant_indices]  
    with open(output_filename, 'wb') as pickle_file:
        pickle.dump(relevant_articles, pickle_file)  
    print(f"Succès : {len(relevant_articles)} articles ont été sauvegardés dans le fichier {output_filename}.")

# Liste des mots-clés orientée sur l'acceptabilité à modifier pour une éventuelle nouvelle sélection
mots_cles = [
    "acceptabilité", "acceptation", "adoption", "approbation", "satisfaction", 
    "adéquation", "perception", "opinion", "conseil", "désapprobation", 
    "rejet", "intolérance", "résistance", "opposition", "objection", "refus", 
    "conflit", "désaccord", "hostilité", "incompréhension", "confusion", 
    "mauvaise interprétation", "idée fausse", "mauvais jugement", "mauvaise compréhension"
]

if __name__ == "__main__":
    pickle_file_to_process = "data/datasets/EOLIEN_articles.pkl"  # Changer le chemin en fonction de la techno sur laquelle faire la sélection
    df = load_articles_from_pickle(pickle_file_to_process) 
    
    df['Corps_preprocessed'] = df['Corps'].apply(preprocess_text)  
    
    tfidf_matrix, vectorizer = compute_tfidf_for_keywords(df, mots_cles)
    
    # Sélectionner les articles pertinents
    relevant_indices = select_relevant_articles_by_keywords(tfidf_matrix, top_n=50)
    
    # Sauvegarder les articles pertinents en conservant les textes originaux
    save_relevant_articles_to_pickle(df, relevant_indices, "data/relevant_articles/EOLIEN_relevant_articles.pkl")  # Changer pour chaque techno
