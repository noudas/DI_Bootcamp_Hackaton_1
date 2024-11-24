import psycopg2
from config import Config
from Py_classes import DB_Connect

class User:
    """
    A class representing a user and associated operations in the database.
    """

    def __init__(self, db: DB_Connect, username, first_name, last_name, email, password):
        """
        Initializes a User object with basic attributes and a DB_Connect instance.
        
        :param db: An instance of the DB_Connect class to manage database connections.
        :param username: The username of the user.
        :param first_name: The first name of the user.
        :param last_name: The last name of the user.
        :param email: The email address of the user.
        :param password: The password for the user.
        """
        self.db = db
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def create_user(self):
        """
        Inserts a new user into the database using the DB_Connect class.
        """
        query = """
            INSERT INTO users (username, first_name, last_name, email, password)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (self.username, self.first_name, self.last_name, self.email, self.password)
        self.db.execute_query(query, params)

    @classmethod
    def get_user_by_id(cls, db: DB_Connect, user_id):
        """
        Fetches a user by ID from the database using the DB_Connect class.
        
        :param db: An instance of the DB_Connect class.
        :param user_id: The ID of the user to fetch.
        :return: An instance of User if the user is found, None otherwise.
        """
        query = "SELECT * FROM users WHERE user_id = %s"
        params = (user_id,)
        results = db.fetch_results(query, params)

        if results:
            row = results[0]
            return cls(db, row[1], row[2], row[3], row[4], row[5])
        return None

    def update_user(self, new_username=None, new_email=None, new_password=None):
        """
        Updates user information in the database using the DB_Connect class.
        
        :param new_username: The new username, if updating.
        :param new_email: The new email address, if updating.
        :param new_password: The new password, if updating.
        """
        new_username = new_username if new_username else self.username
        new_email = new_email if new_email else self.email
        new_password = new_password if new_password else self.password

        query = """
            UPDATE users 
            SET username = %s, email = %s, password = %s 
            WHERE username = %s
        """
        params = (new_username, new_email, new_password, self.username)
        self.db.execute_query(query, params)

    @classmethod
    def delete_user(cls, db: DB_Connect, user_id):
        """
        Deletes a user from the database using the DB_Connect class.
        
        :param db: An instance of the DB_Connect class.
        :param user_id: The ID of the user to delete.
        """
        query = "DELETE FROM users WHERE user_id = %s"
        params = (user_id,)
        db.execute_query(query, params)