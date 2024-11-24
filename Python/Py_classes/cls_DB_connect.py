import psycopg2
from config import Config

class DB_Connect:
    def __init__(self, db_name=None):
        self.db_name = db_name if db_name else Config.DB_NAME
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                database=self.db_name,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                host=Config.DB_HOST,
                port=Config.DB_PORT
            )
            print(f"Connected to database: {self.db_name}")
            return self.connection
        except Exception as error:
            print(f"Error while connecting to the database: {error}")
            return None

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print(f"Disconnected from database: {self.db_name}")
            else:
                print("No active connection to disconnect.")
        except Exception as error:
            print(f"Error while disconnecting from the database: {error}")

    def execute_query(self, query, params=None):
        try:
            connection = self.connect()
            if not connection:
                raise Exception("Failed to establish database connection")

            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            print("Query executed successfully.")
            return cursor.rowcount
        except Exception as error:
            print(f"Error while executing query: {error}")
            connection.rollback()
            raise error

    def fetch_results(self, query, params=None):
        try:
            connection = self.connect()
            if not connection:
                raise Exception("Failed to establish database connection")

            cursor = connection.cursor()
            cursor.execute(query, params)

            if cursor.description:
                result = cursor.fetchall()
                print("Query executed successfully. Results fetched.")
            else:
                print("Query executed successfully. No results to fetch.")

            return result
        except Exception as error:
            print(f"Error while fetching results: {error}")
            raise error
