import psycopg2
from DB_config.DB_connect import db_connect
from config import Config

def create_table_savings_goals():
    """
    Creates the savings_goals table in the database.
    """
    connection = None
    try:
        connection = db_connect(Config.DB_NAME)

        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS savings_goals (
            goal_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            goal_name VARCHAR(100) NOT NULL,
            target_amount NUMERIC(12, 2) NOT NULL,
            current_savings NUMERIC(12, 2) DEFAULT 0.00,
            due_date DATE,
            is_achieved BOOLEAN DEFAULT false,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
        );
        """

        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'savings_goals' created successfully.")

    except Exception as error:
        print(f"Error while creating the table 'savings_goals': {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()
