from DB_config.DB_connect import db_connect
from config import Config

def insert_into(query,params):
    """
    Inserts a record into the database.
    """
    connection = None

    try:
        connection = db_connect(Config.DB_NAME)
        cursor = connection.cursor()
        cursor.execute(query,params)
        connection.commit()
        print("Record inserted successfully.")
    except Exception as error:
        print(f"Error while inserting record: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
