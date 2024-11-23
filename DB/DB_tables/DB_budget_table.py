import psycopg2
from DB_config.DB_connect import db_connect
from config import Config

def create_table_budget():
    """
    Creates the budget table in the database.
    """
    connection = None
    try:
        connection = db_connect(Config.DB_NAME)

        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS budget (
            budget_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            total_budget NUMERIC(12, 2) NOT NULL,
            savings NUMERIC(12, 2) DEFAULT 0.00,
            spent_amount NUMERIC(12, 2) DEFAULT 0.00,
            remaining_amount NUMERIC(12, 2) GENERATED ALWAYS AS (total_budget - spent_amount) STORED,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        );
        """

        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'budget' created successfully.")

    except Exception as error:
        print(f"Error while creating the table 'budget': {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
