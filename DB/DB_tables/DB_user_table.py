import psycopg2
from DB_config.DB_connect import db_connect
from config import Config
def create_table_users():
    try:
        # Connect to the database using db_connect
        connection = db_connect(Config.DB_NAME)

        # Create a cursor to execute the query
        cursor = connection.cursor()

        # SQL query to create the 'users' table
        create_table_users_query = """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT true
        )
        """ 

        # Execute the SQL query
        cursor.execute(create_table_users_query)
        connection.commit()
        print("Table 'users' created successfully!")

    except Exception as error:
        print(f"Error while creating the table: {error}")

    finally:
        if connection:
            cursor.close()
            connection.close()