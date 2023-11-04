# Evaluation Python Groupe n°1

## Réalisé par

- P. Mehdi
- V. Mathieu
- C. Vincenzo

## Config

### Installer les dépendances (& la version de Python utilisée)

```bash
pyenv install $(cat runtime.txt)
pyenv exec pip install -r requirements.txt
```

## Choix du code

### Vincenzo

Pour ma part, j'ai choisi de m'occuper de toute la partie SQL. Etant très à l'aise avec les requêtes, je pouvais faire en sorte de faciliter le travail de mes camarades en leur proposant de multiples fonctions répondant à leurs besoins.

Concernant mon code, j'ai opté pour une approche simple, en me servant de choses basiques (ajout de data uniquement en utilisant sqlite3), et j'ai opté ensuite sur l'utilisation du module `pandas` pour le reste de mes fonctions.

### Mehdi

De mon côté, je me suis laissé tenté par le Scrapping. Ayant déjà pratiqué python dans mon entreprise notamment selenium pour de la configuration automatisé de produit, j'ai l'habitude de rechercher des balises pour intéragir avec elles. Récuperer des informations pratiques, les stockers non pas dans des csv mais dans des txt ou json pour une utilisaion ultérieure dans d'autres scripts python. 

Mon code peut être résumé par : 
- l'Initialisation de lists
- Boucler dessus
- Supprimer des éléments
- Diviser des éléments
- Ajouter des données
- Ouvrir des fichiers
- Sauvegarder des éléments
- Réutilisé ces éléments
  

### Mathieu

J'ai décidé de faire la partie "algorithmie" car j'ai bien aimé faire cette partie lors des tps et c'est aussi parce que je n'ai pas l'habitude d'avoir besoin d'autant de reflexion par rapport à l'entreprise. J'ai également fait beaucoup d'algorithmie lors de mes études et c'est ce qui m'a beaucoup aidé. J'ai également essayé de créer des fonctions qui peuvent être réutiliser pour certaines questions?

## Réponses aux questions

> Toutes les questions ont été traités

### "Pensez à bien utiliser cette commande dans le même terminal que celui que vous utilisez pour exécuter vos fichiers .py .“

Il est très important de respecter cette consigne car, depuis le terminal, nous faisons appel à l'éxécutable pyenv, dont nous pouvons définir les versions (globale et locale) de python utilisée. Une fois celle-ci défini, il est alors impératif d'exécuter les scripts depuis ce même terminal afin de ne pas exécuter avec la version global de python mais bien avec la version locale, qui sont toutes deux disctinctes l'une de l'autre.

### Trois chaînes qui ont diffusé le plus d'épisodes

- Netflix: 471 épisodes
- TF1: 158 épisodes
- Disney+: 118 épisodes

### Trois pays qui ont diffusé le plus d'épisodes

- Etats-Unis: 1439 épisodes
- France: 423 épisodes
- Canada: 288 épisodes

### Mots les plus fréquents dans les noms des séries

- 'the': 23 occurrences
- 'of': 7 occurrences
- 'de': 3 occurrences
- 'american': 3 occurrences
- 'les': 3 occurrences
- '(2023)': 3 occurrences
- 'all': 2 occurrences
- 'horror': 2 occurrences
- 'la': 2 occurrences
- 'park': 2 occurrences
- 'in': 2 occurrences
- 'good': 2 occurrences
- '(2022)': 2 occurrences
- 'soko': 2 occurrences
- 'à': 2 occurrences
