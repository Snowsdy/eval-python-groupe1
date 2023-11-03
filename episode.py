import csv
import requests
from bs4 import BeautifulSoup

# Charger l'URL de base
base_url = "https://www.spin-off.fr/"

# Initialiser une liste pour stocker les URLs des épisodes de TF1
tf1_episode_urls = []

# Lire les URLs des épisodes à partir du fichier CSV pour la chaîne TF1
with open('data/files/episodes.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['channel'] == 'TF1':
            episode_url = row['url']
            full_url = base_url + episode_url
            tf1_episode_urls.append(full_url)

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
    for duration in tf1_episode_durations:
        file.write(duration + "\n")

print("Les durées des épisodes de TF1 ont été enregistrées dans le fichier 'tf1_episode_durations.txt'.")
