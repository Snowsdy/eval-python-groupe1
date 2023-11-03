import sqlite3
import pandas as panda

def create_tables() -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')
    cursor = conn.cursor()

    # Define the SQL commands to create the tables
    create_episode_table = '''
        CREATE TABLE IF NOT EXISTS episode (
            id INTEGER PRIMARY KEY,
            name TEXT,
            episode_number INTEGER,
            episode_season INTEGER,
            country TEXT,
            channel TEXT,
            date DATE,
            url TEXT
        )
    '''

    create_duration_table = '''
        CREATE TABLE IF NOT EXISTS duration (
            id INTEGER PRIMARY KEY,
            duration_minutes INTEGER,
            episode_id INTEGER,
            FOREIGN KEY (episode_id) REFERENCES episode(id)
        )
    '''

    # Execute the SQL commands to create the tables
    cursor.execute(create_episode_table)
    cursor.execute(create_duration_table)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Tables created.")

# -------------------------------

# new_duration = (<episode_id, duration_minutes>)
def add_new_duration(new_duration) -> None:
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')
    cursor = conn.cursor()

    # Create the query
    cursor.execute("INSERT INTO duration (episode_id, duration_minutes) VALUES (?, ?)", new_duration)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Duration added.")

# -------------------------------

# new_episode = [{
#     'name': 'Test',
#     'episode_number': 1,
#     'episode_season': 1,
#     'date': '03-11-2023',
#     'country': 'France',
#     'channel': 'BFMTV',
#     'url': 'https://www.youtube.com/watch?v=qYYslXRiTAc'
# }]
def add_new_episode(new_episode) -> int | None:
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')
    
    query = panda.DataFrame(new_episode)
    result = query.to_sql(name='episode', con=conn, if_exists='append', index=False, chunksize=None)

    conn.close()
    return result

# -------------------------------

def get_episode_whitout_id(name, episode_number, episode_season, date, country, channel, url):
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')

    # Make the query to get the dataframe
    query = f"SELECT * FROM episode WHERE name = ? AND episode_number = ? AND episode_season = ? AND date = ? AND country = ? AND channel = ? AND url = ?"
    params = (name, episode_number, episode_season, date, country, channel, url)
    dataframe = panda.read_sql(query, con=conn, params=params)

    # Export the data into dict
    episode = dataframe.to_dict(orient='records')

    # Close the connection
    conn.close()

    return episode

# -------------------------------

# month -> 1...12 (1: Janvier / 12: Décembre)
def get_episode_by_month(month):
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')

    # Make the query to get the dataframe
    dataframe = panda.read_sql(f'SELECT * FROM episode', con=conn)

    # Convert the 'date' column to datetime format
    dataframe['date'] = panda.to_datetime(dataframe['date'], format='%d-%m-%Y')

    # Filter episodes for month
    month_episodes = dataframe[dataframe['date'].dt.month == month].copy()

    # Extract just the date part
    month_episodes['date'] = month_episodes['date'].dt.strftime('%d-%m-%Y')

    # Close the connection
    conn.close()

    # Convert the filtered dataframe to a list of dictionaries
    episodes_data = month_episodes.to_dict(orient='records')

    return episodes_data

# -------------------------------

def get_episodes():
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')

    # Make the query to get the dataframe
    dataframe = panda.read_sql(f'SELECT * FROM episode', con=conn)

    # Export the data into dict
    episodes = dataframe.to_dict(orient='records')

    # Close the connection
    conn.close()

    return episodes

# -------------------------------

def get_durations():
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')

    # Make the query to get the dataframe
    dataframe = panda.read_sql(f'SELECT * FROM duration', con=conn)

    # Export the data into dict
    durations = dataframe.to_dict(orient='records')

    # Close the connection
    conn.close()

    return durations

# -------------------------------

def get_duration_by_id(id):
    # Connect to the SQLite database
    conn = sqlite3.connect('data/databases/database.db')

    # Make the query to get the dataframe
    dataframe = panda.read_sql(f'SELECT * FROM duration WHERE id = {id}', con=conn)

    # Export the data into dict
    duration = dataframe.to_dict(orient='records')

    # Close the connection
    conn.close()

    return duration

# -------------------------------

# Testing
#create_tables()
# new_episode = [{
#     'name': 'Test',
#     'episode_number': 1,
#     'episode_season': 1,
#     'date': '03-11-2023',
#     'country': 'France',
#     'channel': 'BFMTV',
#     'url': 'https://www.youtube.com/watch?v=qYYslXRiTAc'
# }]
# episode_id = add_new_episode(new_episode=new_episode)
# get_episode_by_id(id=1)
#episodes = get_episodes()
#november = get_episode_by_month(month=11)
#print(november)