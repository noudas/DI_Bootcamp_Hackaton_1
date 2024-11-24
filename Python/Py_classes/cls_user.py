import psycopg2
from config import Config
from Py_classes import DB_Connect

class User:
    def __init__(self, db: DB_Connect, username, first_name, last_name, email, password):
        self.db = db
        self.user_id = None
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_at = None
        self.updated_at = None

    @classmethod
    def get_user_by_id(cls, db: DB_Connect, user_id):
        print(f"Fetching user with ID: {user_id}")  # Debug print
        query = "SELECT * FROM users WHERE user_id = %s"
        params = (user_id,)
        
        try:
            results = db.fetch_results(query, params)
            print(f"Results fetched: {results}")  # Debug print
            
            if results:
                row = results[0]
                print(f"Fetched row: {row}")  # Debug print
                return cls(db, row['username'], row['first_name'], row['last_name'], row['email'], row['password'])
            else:
                print("No user found with the given ID.")
        except Exception as e:
            print(f"Error fetching user: {e}")  # Debug print
        return None

    def update_user(self, db: DB_Connect , curr_user_id, new_username=None, new_email=None, new_password=None):
        try:
            if not db:
                self.db.connect()

            query = """
            UPDATE users 
            SET username = %s, email = %s, password = %s, updated_at = CURRENT_TIMESTAMP 
            WHERE user_id = %s
            """
            params = (new_username or self.username, new_email or self.email, new_password or self.password, curr_user_id)
            
            self.db.execute_query(query, params)

            updated_user = User.get_user_by_id(db, curr_user_id)
            
            if updated_user:
                print(f"User {curr_user_id} updated successfully.")
                print(f"Updated Information:")
                print(f"Username: {updated_user.username}")
                print(f"Email: {updated_user.email}")
                print(f"Updated At: {updated_user.updated_at}")
            else:
                print("Failed to update user information.")
        except Exception as e:
            print(f"Error updating user: {e}")  # Debug print

    @classmethod
    def delete_user(cls, db: DB_Connect, user_id):
        query = "DELETE FROM users WHERE user_id = %s"
        params = (user_id,)
        db.execute_query(query, params)

    def create_user(self):
        if not self.db.connection:
            self.db.connect()

        query = """
            INSERT INTO users (username, first_name, last_name, email, password, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        """
        params = (self.username, self.first_name, self.last_name, self.email, self.password)
        
        self.db.execute_query(query, params)
