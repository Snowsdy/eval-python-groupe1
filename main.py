import requests
from bs4 import BeautifulSoup
import csv

# URL de la page Web
url = "https://www.spin-off.fr/calendrier_des_series.html"

# Effectuer la requête HTTP et récupérer le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Trouver la table contenant les données des épisodes
table = soup.find("table", class_="padding2")

# Initialiser une liste pour stocker les données des épisodes
episodes_data = []

# Parcourir les lignes de la table et extraire les informations nécessaires
for row in table.find_all("tr"):
    cells = row.find_all("td", class_="nowrap left vmiddle")
    if len(cells) > 1:
        serie = cells[1].text.strip()
        episode_info = row.find_all("td", class_="vmiddle")
        episode_number = episode_info[0].text.strip()
        season_number = episode_info[1].text.strip()
        air_date = episode_info[2].text.strip()
        country = episode_info[3].text.strip()
        channel = episode_info[4].text.strip()
        relative_url = episode_info[0].find("a")["href"]
        episode_url = f"https://www.spin-off.fr/{relative_url}"

        # Ajouter les données de l'épisode à la liste
        episodes_data.append((serie, episode_number, season_number, air_date, country, channel, episode_url))

# Enregistrer les données dans un fichier CSV
with open("data/files/episodes.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=";")
    # Écrire l'en-tête du fichier CSV
    csvwriter.writerow(["Série", "Numéro de l'épisode", "Numéro de la saison", "Date de diffusion", "Pays d'origine", "Chaîne", "URL de l'épisode"])
    # Écrire les données des épisodes dans le fichier CSV
    csvwriter.writerows(episodes_data)
