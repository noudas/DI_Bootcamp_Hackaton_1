import psycopg2
from DB_config.DB_connect import db_connect
from config import Config

def create_table_expenses():
    """
    Creates the expenses table in the database with ON DELETE CASCADE for the category_id foreign key.
    """
    connection = None
    try:
        connection = db_connect(Config.DB_NAME)

        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id SERIAL PRIMARY KEY,
            category_id INT NOT NULL,
            amount NUMERIC(10, 2) NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
        );
        """

        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'expenses' created successfully.")

    except Exception as error:
        print(f"Error while creating the table 'expenses': {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
