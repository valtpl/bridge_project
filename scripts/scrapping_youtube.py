# scrapping youtube comments
import nltk
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import time
import pickle
import os

# Clé API YouTube (remplacer par votre propre clé)  
dev = "AIzaSyDrJDpcCdLEYXyGeZyF6-OzgNnmjDejPi4"

def youtube_search(query, max_results=100, api_key=dev):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Restreind dates aux vidéos publiées entre 2010 et 2020
    published_after = '2010-01-01T00:00:00Z'
    published_before = '2020-12-31T23:59:59Z'

    search_response = youtube.search().list(
        q=query,
        type="video",
        part="id,snippet",
        maxResults=max_results,
        relevanceLanguage="fr",  # Filtre pour garder uniquement videos en fr
        publishedAfter=published_after,
        publishedBefore=published_before
    ).execute()

    videos = []

    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append({
                'title': search_result['snippet']['title'],
                'id': search_result['id']['videoId'],
                'published_at': search_result['snippet']['publishedAt']  
            })

    return videos

def getcomments(video_id, api_key=dev):
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    comments = []
    response = None

    try:
        response = request.execute()

        while response:
            for item in response.get('items', []):
                comment = item['snippet']['topLevelComment']['snippet']
                public = item['snippet']['isPublic']
                comments.append([
                    comment['authorDisplayName'],
                    comment['publishedAt'],
                    comment['likeCount'],
                    comment['textOriginal'],
                    comment['videoId'],
                    public
                ])

            if 'nextPageToken' in response:
                nextPageToken = response['nextPageToken']
                request = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=100, pageToken=nextPageToken)
                response = request.execute()
            else:
                break

    except HttpError as error:
        if error.resp.status == 403 and 'commentsDisabled' in str(error):
            print(f"Comments are disabled for video {video_id}")
        else:
            raise

    if response is None:
        return pd.DataFrame()

    df2 = pd.DataFrame(comments, columns=['author', 'updated_at', 'like_count', 'text', 'video_id', 'public'])
    return df2

def save_comments_to_pickle(comments_df, save_folder, tech_name):
    """Sauvegarde les commentaires collectés dans un fichier pickle."""
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)  
    pickle_filename = os.path.join(save_folder, f"{tech_name}_YTB_comments.pkl")

    try:
        with open(pickle_filename, 'wb') as pickle_file:
            pickle.dump(comments_df, pickle_file)
        print(f"[Succès] {len(comments_df)} commentaires sauvegardés dans {pickle_filename}.")
    except Exception as e:
        print(f"[Erreur] Échec de la sauvegarde dans {pickle_filename}: {e}")

def main(tech_name, save_folder):
    # Recherche des vidéos liées à la techno souhaitée
    results = youtube_search(tech_name, max_results=100)
    video_comments = []
    num_videos = len(results)
    num_comments = 0

    # Récupération des commentaires des vidéos trouvées
    for video in results:
        comments = getcomments(video['id'])
        if not comments.empty:
            comments['title'] = video['title']
            comments['video_published_at'] = video['published_at']  
            video_comments.append(comments)
            num_comments += len(comments)
        # Ajout délai pour éviter de dépasser les quotas de l'API
        time.sleep(1)

    # Crée un DataFrame avec les commentaires collectés
    if video_comments:
        df_bis = pd.concat(video_comments)

        # Sauvegarder les commentaires au format pickle
        save_comments_to_pickle(df_bis, save_folder, tech_name)

        # Affiche le nombre de vidéos et de commentaires traités
        print(f"[Succès] {num_videos} vidéos traitées et {num_comments} commentaires récupérés.")
    else:
        print("[Avertissement] Aucun commentaire récupéré.")

if __name__ == "__main__":
    tech_name = "agrivoltaique"  # Remplacer par la technologie souhaitée
    save_folder = "data/ytb_comments"  # Dossier où les commentaires seront sauvegardés

    main(tech_name, save_folder)
