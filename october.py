import requests
from bs4 import BeautifulSoup
import csv
from pprint import pp
from sql import add_new_episode, get_episodes, get_episode_by_month
def episodes_month(month):
    # URL de la page Web contenant les données des épisodes
    url = f"https://www.spin-off.fr/calendrier_des_series.html?date=2023-{month}"

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
            cells = row.find_all("td", class_="td_jour")

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

                    # Extraire le nom du pays et de la chaîne à partir des balises <img> précédentes
                    channel = episode.find_previous('img')['alt']
                    country = episode.find_previous('img').find_previous('img')['alt']

                    # Extraire l'URL de la classe "liens"
                    episode_url = spanContent[1]['href']
                    episode_url = episode_url.replace("https://www.spin-off.fr/", "")

                    # Ajouter les données de l'épisode à la liste episodes_data
                    episodes_data.append({
                        'name': episode_name,
                        'episode_number': episode_number,
                        'episode_season': episode_season,
                        'date': day,
                        'country': country,
                        'channel': channel,
                        'url': episode_url  # Ajouter l'URL de la page de l'épisode (sans le préfixe)
                    })

    # Écrire les données dans un fichier CSV
    # with open('data/files/episodes_october.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #     fieldnames = ['name', 'episode_number', 'episode_season', 'date', 'country', 'channel', 'url']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerows(episodes_data)

    # Afficher les données extraites
    return episodes_data

episodes_october = episodes_month(10)

# AJout des episodes du mois d'octobre
# add_new_episode(episodes_october)

def count_by_attribute(episodes, attribute):
    count_per_attribute = {}
    for episode in episodes:
        attr = episode[attribute]
        if attr not in count_per_attribute:
            count_per_attribute[attr] = 1
        else:
            count_per_attribute[attr] += 1

    sorted_channels = sorted(count_per_attribute.items(), key=lambda x: x[1], reverse=True)
    top_channels = sorted_channels[:3]

    with open('README.md', 'a+', encoding='utf-8') as file:
        file.write("Trois chaînes qui ont diffusé le plus d'épisodes :\n")
        for channel, episode_count in top_channels:
            file.write(f"{channel}: {episode_count} épisodes\n")

    return top_channels

# Utilisation de la fonction pour compter et trier les épisodes par chaîne
top_channels = count_by_attribute(episodes_october, 'channel')
top_country = count_by_attribute(episodes_october, 'country')

def frequency_words():
    # Supposons que vous avez une liste de noms de séries uniques nommée unique_series_names

    # Création d'une liste de noms de séries uniques
    unique_series_names = set()  # Initialise un ensemble pour les noms de séries uniques

    # Récupération des noms uniques des séries
    for episode in episodes_october:
        unique_series_names.add(episode['name'])  # Ajoute le nom de la série à l'ensemble

    # Analyse des mots dans les noms de séries
    word_frequency = {}
    for series_name in unique_series_names:
        words = series_name.lower().split()  # Sépare les mots et les met en minuscules
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

    # Trie les mots par fréquence
    sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

    # Écrire les mots les plus fréquents dans le fichier README.md
    # with open('README.md', 'a+', encoding='utf-8') as file:
    #     file.write("Mots les plus fréquents dans les noms des séries :\n")
    #     for word, frequency in sorted_words[:15]:  # Écrire les 10 mots les plus fréquents
    #         file.write(f"{word}: {frequency} occurrences\n")
frequency_words()