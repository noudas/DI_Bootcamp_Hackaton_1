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

    def execute_query(self, query, params=None):
        try:
            if not self.connection:
                self.connect()

            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Query executed successfully.")
            return cursor.rowcount
        except Exception as error:
            print(f"Error while executing query: {error}")
            self.connection.rollback()
            raise error

    def fetch_results(self, query, params=()):
        try:
            if not self.connection:
                self.connect()

            cursor = self.connection.cursor()
            print(f"Attempting to execute query: {query} with params: {params}")  # Debug print
            
            cursor.execute(query, params)
            
            rows = cursor.fetchall()
            column_names = [d[0] for d in cursor.description]
            result = []
            for row in rows:
                result.append(dict(zip(column_names, row)))
            
            print(f"Fetched {len(rows)} rows")  # Debug print
            
            return result
        except Exception as e:
            print(f"Error fetching results: {e}")  # Debug print
            raise
        finally:
            cursor.close()

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print(f"Disconnected from database: {self.db_name}")
            else:
                print("No active connection to disconnect.")
        except Exception as error:
            print(f"Error while disconnecting from the database: {error}")
