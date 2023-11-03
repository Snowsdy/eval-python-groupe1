# Importer les bibliothèques nécessaires
import requests
from bs4 import BeautifulSoup
import csv
from pprint import pprint

# URL de la page Web contenant les données des épisodes
url = "https://www.spin-off.fr/calendrier_des_series.html"

# Effectuer une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Trouver la table contenant les données des épisodes (la 8ème table dans ce cas)
tables = soup.find_all("table", class_="padding2")
if len(tables) >= 8:
    target_table = tables[7]

# Initialiser une liste pour stocker les données des épisodes
episodes_data = []

# Parcourir les lignes de la table et extraire les informations nécessaires
for index, row in enumerate(target_table.find_all("tr"), 1):
    if index == 1:
        pass  # Ignorer la première ligne qui contient les en-têtes
    else:
        cells = row.find_all("td", class_="floatleftmobile td_jour")

        for cell in cells:
            # Extraire la date de l'épisode à partir de l'attribut 'id' du div_jour
            div_jour = cell.find('div', class_='div_jour')
            if div_jour:
                episode_id = div_jour['id']
                day = episode_id.split('jour_')[1]

            # Extraire les détails de l'épisode à partir des balises <a> dans la cellule
            for episode in cell.find_all('span', class_='calendrier_episodes'):
                spanContent = episode.find_all('a')
                episode_name = spanContent[0].text
                episode_season = spanContent[1].text.split('.')[0]
                episode_number = spanContent[1].text.split('.')[1]
                
                # Extraire l'URL relative de la page de l'épisode
                episode_url = spanContent[0]['href']

                # Extraire le nom du pays et de la chaîne à partir des balises <img> précédentes
                channel = episode.find_previous('img')['alt']
                country = episode.find_previous('img').find_previous('img')['alt']

                # Ajouter les données de l'épisode à la liste episodes_data
                episodes_data.append({
                    'name': episode_name,
                    'episode_number': episode_number,
                    'episode_season': episode_season,
                    'date': day,
                    'country': country,
                    'channel': channel,
                    'episode_url': episode_url  # Ajouter l'URL relative de la page de l'épisode
                })

# Écrire les données dans un fichier CSV
with open('data/files/episodes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'episode_number', 'episode_season', 'date', 'country', 'channel', 'episode_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(episodes_data)

# Afficher les données extraites
pprint(episodes_data)
