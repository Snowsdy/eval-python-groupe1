import sys
import calendar
import locale
from sql import get_episode_by_month
from october import count_by_attribute
from algo2 import get_channel_with_max_consecutive_days

def process_parameter(param):
    # Getting episodes from database :
    episodes = get_episode_by_month(param)

    # 1st print
    print(len(episodes), f'episodes seront diffusés pendant le mois de {get_month_name_french(param)}.')

    # Getting the first three countries/channels which has the greatest number of episodes :
    country_count = count_by_attribute(episodes, 'country')
    channel_count = count_by_attribute(episodes, 'channel')

    # Then print it :
    print(f"C'est {country_count[0][0]} qui diffusera le plus d'épisodes avec {country_count[0][-1]} épisodes.")
    print(f"C'est {channel_count[0][0]} qui diffusera le plus d'épisodes avec {channel_count[0][-1]} épisodes.")

    # Finally, getting the channel which has the greatest number of episodes depending of the most consecutive days :
    result, nb_days = get_channel_with_max_consecutive_days(param)
    # Then, print it :
    print(f"C'est {result} qui diffusera des épisodes pendant le plus grand nombre de jours consécutifs avec {nb_days} de jours consécutifs.")

def get_month_name_french(month_number):
    if 1 <= month_number <= 12:
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')  # Set locale to French
        return calendar.month_name[month_number]
    else:
        return "Invalid month number"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python summarize_episodes.py --month <number>")
    else:
        if 1 <= int(sys.argv[2]) <= 12:
            process_parameter(int(sys.argv[2]))
        else:
            print("Invalid argument: month needs to be between 1 and 12.")