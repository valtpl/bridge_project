# extrcat_articles.py
import os
import re
import pickle
import pandas as pd
from bs4 import BeautifulSoup


def extract_and_save_articles(folder_path, tech_name):
    """
    Extrait les titres, les corps et les dates des articles des fichiers HTML dans un dossier donné
    et les sauvegarde dans un fichier pickle.
    """
    articles = []

    if not os.path.isdir(folder_path):
        print(f"[Erreur] Le dossier {folder_path} n'existe pas.")
        return

    title_classes = ['titreArticle']
    body_classes = ['docOcurrContainer']
    date_classes = ['DocHeader']

    date_pattern = re.compile(r'\b(\d{1,2})\s+(\w+)\s+(\d{4})\b')

    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as cfile:
                    soup = BeautifulSoup(cfile, 'lxml')

                    titles = soup.find_all('div', class_=title_classes)
                    bodies = soup.find_all('div', class_=body_classes)
                    dates = soup.find_all('span', class_=date_classes)

                    for title_tag, body_tag, date_tag in zip(titles, bodies, dates):
                        title = title_tag.get_text(strip=True) if title_tag else ""
                        body = body_tag.get_text(strip=True) if body_tag else ""
                        date_raw = date_tag.get_text(strip=True) if date_tag else ""

                        match = date_pattern.search(date_raw)
                        date = " ".join(match.groups()) if match else "Date inconnue"

                        if title:
                            articles.append({
                                "Titre": title,
                                "Corps": body,
                                "Date": date
                            })

            except Exception as e:
                print(f"[Erreur] Lecture du fichier {file_path} : {e}")
        else:
            print(f"[Info] Ignoré : {filename} n'est pas un fichier HTML valide.")

    df = pd.DataFrame(articles)
    pickle_filename = f"data/datasets/{tech_name}_articles.pkl"

    try:
        with open(pickle_filename, 'wb') as f:
            pickle.dump(df, f)
        print(f"[Succès] {len(df)} articles sauvegardés dans : {pickle_filename}")
    except Exception as e:
        print(f"[Erreur] Sauvegarde échouée dans {pickle_filename} : {e}")

if __name__ == "__main__":
    folder_path = "data/extract_europress/eolien"  # Remplacer par le chemin vers le dossier de HTML d'europress
    tech_name = "EOLIEN"  # Remplacer par le nom de la techno pour sauvegarde du fichier
    
    extract_and_save_articles(folder_path, tech_name)

