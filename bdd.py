import csv
from sql import create_tables, add_new_episode

# Créer les tables dans la base de données SQLite
create_tables()

with open('data/files/episodes.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Ignorer l'en-tête
    for row in csvreader:
        name, episode_number, episode_season, date, country, channel, url = row
        
        # Vérification pour gérer les valeurs non numériques 'XX'
        if episode_number.isdigit():
            episode_number = int(episode_number)
        else:
            episode_number = None  # Ou une valeur par défaut si nécessaire
        
        if episode_season.isdigit():
            episode_season = int(episode_season)
        else:
            episode_season = None  # Ou une valeur par défaut si nécessaire
        
        new_episode = {
            'name': name,
            'episode_number': episode_number,
            'episode_season': episode_season,
            'date': date,
            'country': country,
            'channel': channel,
            'url': url
        }

        add_new_episode([new_episode])

print("Les données ont été insérées dans la base de données.")
