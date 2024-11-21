import psycopg2
from psycopg2 import sql
from config import Config
from DB_config.DB_connect import db_connect

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

        # Enable autocommit to execute CREATE DATABASE
        # The connection.commit() didn`t work so this is the workaround that i managed to find.... 
        # although i don`t like ti since it feels less secure that specifying where i wanted
        connection.set_session(autocommit=True)

        cursor = connection.cursor()
        # Use sql.SQL to safely construct the query
        create_db_query = sql.SQL("CREATE DATABASE {db_name}").format(
            db_name=sql.Identifier(new_db_name)
        )

        cursor.execute(create_db_query)
        print(f"Database '{new_db_name}' created successfully!")

    except Exception as error:
        print(f"Error while creating the database: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
