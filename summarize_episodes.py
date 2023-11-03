import sys
import calendar
import locale
from sql import add_new_episode, get_episodes, get_episode_by_month
from october import count_by_attribute
from algo2 import get_channel_with_max_consecutive_days
from pprint import pp

def process_parameter(param):
    episodes = get_episode_by_month(int(param))
    print(len(episodes), f'episodes seront diffusés pendant le mois de {get_month_name_french(int(param))}.')
    country_count = count_by_attribute(episodes, 'country')
    channel_count = count_by_attribute(episodes, 'channel')

    print(f"C'est {country_count[0][0]} qui diffusera le plus d'épisodes avec {country_count[0][-1]} épisodes.")
    print(f"C'est {channel_count[0][0]} qui diffusera le plus d'épisodes avec {channel_count[0][-1]} épisodes.")

    result, nb_days = get_channel_with_max_consecutive_days(int(param))
    print(f"C'est {result} qui diffusera des épisodes pendant le plus grand nombre de jours consécutifs avec {nb_days} de jours consécutifs.")
   

def get_month_name_french(month_number):
    if 1 <= month_number <= 12:
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')  # Set locale to French
        return calendar.month_name[month_number]
    else:
        return "Invalid month number"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python summarize_episodes.py --month <month>")
    else:
        process_parameter(sys.argv[2])