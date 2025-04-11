import pickle
import torch
import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
from torch.utils.data.dataset import Dataset
from tqdm import tqdm

# Charger le modèle BERT pré-entraîné pour l'analyse de sentiment
tokenizer = BertTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = BertForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Si un GPU est disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

class SentimentDataset(Dataset):
    """Dataset pour gérer les textes et leurs tokens."""
    
    def __init__(self, texts, tokenizer, max_len=512):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, item):
        text = self.texts[item]
        encoding = self.tokenizer.encode_plus(
            text,
            add_special_tokens=True,
            max_length=self.max_len,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
        }

def predict_sentiment(texts):
    """Prédit les sentiments à partir des textes."""
    dataset = SentimentDataset(texts, tokenizer)
    dataloader = DataLoader(dataset, batch_size=8)
    
    model.eval()
    predictions = []
    
    with torch.no_grad():
        for batch in tqdm(dataloader, desc="Processing"):
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            
            # Prédiction des sentiments
            outputs = model(input_ids, attention_mask=attention_mask)
            logits = outputs.logits
            preds = torch.argmax(logits, dim=1).cpu().numpy()
            predictions.extend(preds)
    
    return predictions

def load_pickle_file(pickle_filename):
    """Charge les articles depuis un fichier pickle."""
    with open(pickle_filename, 'rb') as pickle_file:
        df = pickle.load(pickle_file)
    return df

def save_with_sentiment(df, sentiment_predictions_corps, sentiment_predictions_title, sentiment_predictions_mixed, output_filename):
    """Sauvegarde les articles avec les prédictions de sentiment dans un nouveau fichier pickle."""
    df['sentiment_corps'] = sentiment_predictions_corps
    df['sentiment_title'] = sentiment_predictions_title
    df['sentiment_mixed'] = sentiment_predictions_mixed
    with open(output_filename, 'wb') as pickle_file:
        pickle.dump(df, pickle_file)
    print(f"Succès : les articles avec leurs sentiments ont été sauvegardés dans {output_filename}.")

if __name__ == "__main__":
    input_pickle_file = "data/relevant_articles/EOLIEN_relevant_articles.pkl"  # Changez ce chemin selon technoà étudier
    df = load_pickle_file(input_pickle_file)

    texts_corps = df['Corps'].tolist()
    sentiment_predictions_corps = predict_sentiment(texts_corps)
    
    texts_titles = df['Titre'].tolist()  
    sentiment_predictions_title = predict_sentiment(texts_titles)
    
    # Calculer la moyenne des sentiments (corps + titre) simple division /2 à ajuster ...?
    sentiment_predictions_mixed = [(corps + title) / 2 for corps, title in zip(sentiment_predictions_corps, sentiment_predictions_title)]
    
    output_pickle_file = "output/SA/EOLIEN_SA.pkl"  # Changez ce chemin selon votre fichier
    save_with_sentiment(df, sentiment_predictions_corps, sentiment_predictions_title, sentiment_predictions_mixed, output_pickle_file)
