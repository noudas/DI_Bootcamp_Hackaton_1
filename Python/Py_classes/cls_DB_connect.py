import psycopg2
from config import Config

class DB_Connect:
    """
    A class representing the connection between other classes and the Database
    """
    def __init__(self, db_name=None):
        """
        Initialize the database connection configuration.

        Args:
            db_name (str): Name of the database to connect to. Defaults to Config.DB_NAME.
        """
        self.db_name = db_name if db_name else Config.DB_NAME
        self.connection = None

    def connect(self):
        """
        Connects to a PostgreSQL database.
        If db_name is provided, it overrides the default database name from the Config class.
        """
        try:
            # Use the configuration settings from config.py
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
        """
        Disconnects from the PostgreSQL database if a connection exists.
        """
        try:
            if self.connection:
                self.connection.close()
                print(f"Disconnected from database: {self.db_name}")
            else:
                print("No active connection to disconnect.")
        except Exception as error:
            print(f"Error while disconnecting from the database: {error}")

    def execute_query(self, query, params=None):
        """
        Executes SQL queries that modify the database (e.g., INSERT, UPDATE, DELETE, etc.).

        Args:
            query (str): The SQL query to execute.
            params (tuple): Parameters for the SQL query (optional).
        """
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            print("Query executed successfully.")
        except Exception as error:
            print(f"Error while executing query: {error}")
        finally:
            self.disconnect()

    def fetch_results(self, query, params=None):
        """
        Executes SQL SELECT queries and returns the results.

        Args:
            query (str): The SQL query to execute.
            params (tuple): Parameters for the SQL query (optional).

        Returns:
            list: Fetched results from the database query.
        """
        result = None
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(query, params)

            if cursor.description:
                result = cursor.fetchall()
                print("Query executed successfully. Results fetched.")
            else:
                print("Query executed successfully. No results to fetch.")
        except Exception as error:
            print(f"Error while fetching results: {error}")
        finally:
            self.disconnect()
        return result
