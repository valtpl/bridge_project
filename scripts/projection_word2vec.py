# word2vec_projection.py
import pandas as pd
import numpy as np
import re
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import hdbscan
import plotly.express as px

# Dl les ressources nécessaires
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load du modèle Spacy en fr
nlp = spacy.load("fr_core_news_sm")

def load_corpus(pickle_path):
    """Charge le corpus depuis un fichier pickle."""
    df = pd.read_pickle(pickle_path)
    return df["Corps"].dropna().tolist()


def clean_text(text):
    """Nettoie et lemmatise un texte en français avec Spacy."""
    doc = nlp(text.lower())
    tokens = [
        token.lemma_
        for token in doc
        if not token.is_stop and not token.is_punct and not token.is_digit
    ]
    return tokens


def train_word2vec(corpus, vector_size=100, window=5, min_count=3):
    """Entraîne un modèle Word2Vec sur un corpus tokenisé."""
    return Word2Vec(sentences=corpus, vector_size=vector_size, window=window, min_count=min_count)


def get_top_contributing_words(model, top_n=300):
    """Sélectionne les mots qui contribuent le plus aux 2 premières composantes principales."""
    words = list(model.wv.index_to_key)
    vectors = np.array([model.wv[word] for word in words])

    pca = PCA(n_components=2)
    pca.fit(vectors)

    contributions = np.abs(pca.components_[0]) + np.abs(pca.components_[1])
    top_indices = contributions.argsort()[-top_n:][::-1]

    important_words = [words[i] for i in top_indices]
    important_vectors = np.array([model.wv[word] for word in important_words])
    reduced_vectors = pca.transform(important_vectors)

    return important_words, reduced_vectors


def cluster_and_plot(words, vectors, method='hdbscan', n_clusters=3, html_out="projection.html"):
    """Applique un clustering HDBSCAN et génère une visualisation interactive."""
    if method == 'kmeans':
        model = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = model.fit_predict(vectors)
    elif method == 'hdbscan':
        model = hdbscan.HDBSCAN(min_cluster_size=80)
        clusters = model.fit_predict(vectors)
    else:
        raise ValueError("Méthode de clustering non supportée : utilisez 'kmeans' ou 'hdbscan'.")

    df = pd.DataFrame(vectors, columns=["PC1", "PC2"])
    df['Word'] = words
    df['Cluster'] = clusters

    fig = px.scatter(df, x="PC1", y="PC2", color="Cluster", text="Word",
                     title="Projection des mots selon Word2Vec + PCA")
    fig.update_traces(textposition='top center')
    fig.show()
    fig.write_html(html_out)


if __name__ == "__main__":
    corpus = load_corpus("data/datasets/EOLIEN_articles.pkl") #modif le corpus en fonction de la tehcno souhaitée (FUSION/AGRI/EOLIEN)
    tokenized = [clean_text(article) for article in corpus]

    print("Corpus nettoyé, entraînement du modèle Word2Vec...")
    model = train_word2vec(tokenized)

    print("Extraction des mots importants...")
    words, reduced_vectors = get_top_contributing_words(model, top_n=300)

    print("Clustering et visualisation...")

    # modifier le nom de fichier de sortie en fonction de la techno etudiée
    cluster_and_plot(words, reduced_vectors, method='hdbscan', html_out="output/projection_thematique/EOLIEN_word_projection_hdbscan.html")
