import pandas as pd
import sqlite3

def get_channel_with_max_consecutive_days():
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')

    # Retrieve data from the 'episode' table
    df = pd.read_sql_query('SELECT * FROM episode', conn)

    # Convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

    # Filter episodes for October
    october_episodes = df[(df['date'].dt.month == 10)]

    # Calculate consecutive days for each channel
    october_episodes['date_diff'] = october_episodes['date'].diff().dt.days
    october_episodes['consecutive_days'] = october_episodes.groupby('channel')['date_diff'].cumsum()

    # Find the channel with the greatest number of consecutive days in October
    max_consecutive_days = october_episodes.groupby('channel')['consecutive_days'].max()
    max_channel = max_consecutive_days.idxmax()

    # Close the connection
    conn.close()

    return max_channel, max_consecutive_days[max_channel]

# Call the function to get the channel with the greatest number of consecutive days in October
result, nb_days = get_channel_with_max_consecutive_days()
print(f"The channel with the greatest number of consecutive days in October is: {result} with {nb_days} consecutive days")
