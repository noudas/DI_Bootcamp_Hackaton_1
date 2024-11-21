import psycopg2
from psycopg2 import sql
from config import Config
from DB_connnect import db_connect


def db_create(new_db_name):
    """
    Creates a new PostgreSQL database.
    Connects to the default database (e.g., 'postgres') and creates the specified database.
    """

    connection = None
    try:
        connection = db_connect(Config.DB_NAME_DEFAULT)
        if connection is None:
            print("Failed to connect to the default database.")
            return
        
        cursor = connection.cursor()
        # sql.SQL will make it harder to inject code into the DB
        create_db_query =sql.SQL("CREATE DATABASE {db_name}").format(
            # This will create an identifier to make it more private
            db_name = sql.Identifier(new_db_name)
        )

        cursor.execute(create_db_query)
        connection.commit()
        print(f"Database '{new_db_name}' created successfully!")

    except Exception as error:
        print(f"Error while creating the database: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()