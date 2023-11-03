def read_episodes_csv():
    # Ouvrir le fichier CSV en mode lecture
    with open("data/files/episodes.csv", 'r', encoding='utf-8') as csvfile:
        # Initialiser une liste pour stocker les données des épisodes en tuples
        episodes_data = []
        # Lire les lignes du fichier CSV
        lines = csvfile.readlines()
        # Parcourir chaque ligne du fichier CSV, en ignorant la première ligne (en-têtes des colonnes)
        for line in lines[1:]:
            # Supprimer les caractères de nouvelle ligne
            line = line.strip()
            # Diviser la ligne en valeurs en utilisant le séparateur de virgule
            values = line.split(',')
            # Vérifier si la valeur de "episode_number" est numérique
            if values[1].isdigit():
                episode_number = int(values[1])
            else:
                episode_number = 0  # ou une autre valeur par défaut selon votre logique
            episode_season = int(values[2])
            date = values[3]
            country = values[4]
            channel = values[5]
            # Ajouter les données à la liste episodes_data en tant que tuple
            episodes_data.append((values[0], episode_number, episode_season, date, country, channel))
    # Retourner la liste de tuples
    return episodes_data

# Utilisation de la fonction pour lire le fichier episodes.csv
episodes_list = read_episodes_csv()

# Afficher la liste de tuples avec les bons types
print(episodes_list)
