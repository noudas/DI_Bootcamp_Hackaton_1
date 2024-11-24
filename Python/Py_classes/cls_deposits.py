import psycopg2
from config import Config
from Py_classes import DB_Connect

class Deposits:
    def __init__(self, db: DB_Connect, user_id, amount, description=None):
        """
        Initializes a deposit with the provided parameters.

        :param db: An instance of DB_Connect for interacting with the database.
        :param user_id: The user associated with the deposit.
        :param amount: The amount of the deposit.
        :param description: An optional description for the deposit.
        """
        self.db = db
        self.user_id = user_id
        self.amount = amount
        self.description = description

    def add_deposit(self):
        """
        Adds a new deposit to the database.
        """
        query = """INSERT INTO deposits (user_id, amount, description)
                   VALUES (%s, %s, %s)"""
        values = (self.user_id, self.amount, self.description)
        try:
            self.db.execute_query(query, values)
            print("Deposit added successfully!")
        except Exception as error:
            print(f"Error occurred while adding deposit: {error}")

    @classmethod
    def get_deposits(cls, db: DB_Connect,user_id):
        """
        Fetches all deposit records from the database for a user.

        :param db: An instance of DB_Connect for interacting with the database.
        :return: A list of Deposit objects.
        """
        query = "SELECT deposit_id, user_id, amount, description FROM deposits WHERE user_id = %s"
        values = (user_id)
        results = db.fetch_results(query)
        
        # Return a list of Deposit objects
        deposits = [cls(db, row[1], row[2], row[3], row[4]) for row in results]
        return deposits

    @classmethod
    def delete_deposit(cls, db: DB_Connect, deposit_id):
        """
        Deletes a deposit record by its ID.

        :param db: An instance of DB_Connect for interacting with the database.
        :param deposit_id: The ID of the deposit to delete.
        """
        query = "DELETE FROM deposits WHERE deposit_id = %s"
        values = (deposit_id)
        try:
            db.execute_query(query, values)
            print("Deposit deleted successfully!")
        except Exception as error:
            print(f"Error occurred while deleting deposit: {error}")
