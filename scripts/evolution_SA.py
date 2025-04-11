import pickle
import pandas as pd
import matplotlib.pyplot as plt
from dateutil import parser

# Dictionnaire de traduction des mois
mois_fr_to_en = {
    'janvier': 'January', 'février': 'February', 'mars': 'March',
    'avril': 'April', 'mai': 'May', 'juin': 'June',
    'juillet': 'July', 'août': 'August', 'septembre': 'September',
    'octobre': 'October', 'novembre': 'November', 'décembre': 'December'
}

def traduire_mois(date_str):
    for fr, en in mois_fr_to_en.items():
        date_str = date_str.lower().replace(fr, en)
    return date_str

def convertir_date(colonne_date):
    def safe_parse(date_str):
        try:
            return parser.parse(traduire_mois(str(date_str)), dayfirst=True)
        except Exception:
            return pd.NaT
    return colonne_date.apply(safe_parse)

def plot_scatter_with_trend(df, technologie_name, window=7):
    """Affiche un scatter plot + ligne de tendance du score de sentiment en fonction du temps."""
    df = df.copy()
    df['Date'] = convertir_date(df['Date'])
    df = df.dropna(subset=['Date']) 
    df = df.sort_values('Date')

    sentiment_cols = ['sentiment_corps', 'sentiment_title', 'sentiment_mixed']
    colors = ['skyblue', 'lightgreen', 'salmon']
    titles = ['Corps', 'Titre', 'Mixte']

    plt.figure(figsize=(14, 10))
    for i, col in enumerate(sentiment_cols):
        plt.subplot(3, 1, i + 1)

        # Scatter plot des points
        plt.scatter(df['Date'], df[col], color=colors[i], alpha=0.5, edgecolors='k', label='Données')

        # Moyenne glissante
        df_rolling = df.set_index('Date')[col].rolling(f'{window}D').mean()
        plt.plot(df_rolling.index, df_rolling.values, color=colors[i], linewidth=2.5, label=f'Moyenne {window} jours')

        plt.title(f"{technologie_name} — Évolution du sentiment ({titles[i]})")
        plt.ylabel("Score de sentiment")
        plt.xlabel("Date")
        plt.grid(True)
        plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    input_pickle = "output/SA/EOLIEN_SA.pkl"  # adapte selon la techno
    technologie_name = "EOLIEN"               #idem à adapyter

    with open(input_pickle, 'rb') as f:
        df = pickle.load(f)

    plot_scatter_with_trend(df, technologie_name, window=50)  # moyenne glissante sur 50 jours
