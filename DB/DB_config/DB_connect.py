 # Using the config.py, Config class to get the fata and connect with the DB

import psycopg2
from config import Config

def db_connect(db_name):
    """
    Connects to a PostgreSQL database.
    If db_name is provided, it overrides the default database name from the Config class.
    """
    try:
        # Use the configuration settings from config.py
        connection = psycopg2.connect(
            database= db_name if db_name else Config.DB_NAME,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            host=Config.DB_HOST,
            port=Config.DB_PORT
        )
        print(f"Connected to database: {db_name if db_name else Config.DB_NAME}")
        return connection
    except Exception as error:
        print(f"Error while connecting to the database: {error}")
        return None