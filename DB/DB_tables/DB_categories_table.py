import psycopg2
from DB_config.DB_connect import db_connect
from config import Config

def create_table_categories():
    """
    Creates the categories table in the database.
    """
    connection = None
    try:
        connection = db_connect(Config.DB_NAME)

        cursor = connection.cursor()
        create_table_categories_query = """
        CREATE TABLE IF NOT EXISTS categories (
            category_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL UNIQUE,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        cursor.execute(create_table_categories_query)
        connection.commit()
        print("Table 'categories' created successfully.")

    except Exception as error:
        print(f"Error while creating the table 'categories': {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
