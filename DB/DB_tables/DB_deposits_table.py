import psycopg2
from DB_config.DB_connect import db_connect
from config import Config

def create_table_deposits():
    """
    Creates the deposits table in the database.
    """
    connection = None
    try:
        connection = db_connect(Config.DB_NAME)

        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS deposits (
            deposit_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            amount NUMERIC(12, 2) NOT NULL,
            deposit_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            description VARCHAR(255),
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        );
        """

        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'deposits' created successfully.")

    except Exception as error:
        print(f"Error while creating the table 'deposits': {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
