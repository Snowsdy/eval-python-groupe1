import csv
import requests
from bs4 import BeautifulSoup
from sql import get_episode_whitout_id, add_new_duration, get_durations

# Charger l'URL de base
base_url = "https://www.spin-off.fr/"

# Initialiser une liste pour stocker les URLs des épisodes de TF1
tf1_episode_urls = []
tf1_episodes = []
tf1_episodes_with_ids = []

# Lire les URLs des épisodes à partir du fichier CSV pour la chaîne TF1
with open('data/files/episodes.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['channel'] == 'TF1':
            episode_url = row['url']
            full_url = base_url + episode_url
            tf1_episode_urls.append(full_url)
            tf1_episodes.append({
                'name': row['name'],
                'episode_number': row['episode_number'],
                'episode_season': row['episode_season'],
                'date': row['date'],
                'country': row['country'],
                'channel': row['channel'],
                'url': row['url']
            })

# Ajouter à la base de données sqlite :
for tf1_episode in tf1_episodes:
    tf1_episodes_with_ids.append(
        get_episode_whitout_id(
            name=tf1_episode['name'], 
            episode_number=tf1_episode['episode_number'], 
            episode_season=tf1_episode['episode_season'], 
            date=tf1_episode['date'], 
            country=tf1_episode['country'], 
            channel=tf1_episode['channel'], 
            url=tf1_episode['url']
        )[0]
    )

# Initialiser une liste pour stocker les informations sur la durée de l'épisode
tf1_episode_durations = []

# Parcourir les URLs des épisodes de TF1 et récupérer les durées
for episode_url in tf1_episode_urls:
    # Faire une requête HTTP pour obtenir le contenu de la page de l'épisode
    response = requests.get(episode_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extraire la durée de l'épisode à partir de la balise spécifiée
    duration_element = soup.find("div", class_="episode_infos_episode_format")
    if duration_element:
        duration = duration_element.text.strip()
        tf1_episode_durations.append(duration)
    else:
        tf1_episode_durations.append("Durée non disponible")

# Écrire les informations sur la durée des épisodes de TF1 dans un fichier texte
with open('tf1_episode_durations.txt', 'w', encoding='utf-8') as file:
    for index, duration in enumerate(tf1_episode_durations):
        file.write(duration + "\n")
        duration_str = duration.replace('minutes', '')
        new_duration = (int(tf1_episodes_with_ids[index]['id']), int(duration_str))
        add_new_duration(new_duration=new_duration)

print("Les durées des épisodes de TF1 ont été enregistrées dans le fichier 'tf1_episode_durations.txt'.")
print(get_durations())
