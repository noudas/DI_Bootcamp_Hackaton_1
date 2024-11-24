<<<<<<< HEAD
import psycopg2
from config import Config
from cls_DB_connect import DB_Connect

class Deposits:
    def __init__(self, db: DB_Connect, user_id, amount, deposit_date, description=None):
        """
        Initializes a deposit with the provided parameters.

        :param db: An instance of DB_Connect for interacting with the database.
        :param user_id: The user associated with the deposit.
        :param amount: The amount of the deposit.
        :param deposit_date: The date of the deposit.
        :param description: An optional description for the deposit.
        """
        self.db = db
        self.user_id = user_id
        self.amount = amount
        self.deposit_date = deposit_date
        self.description = description

    def add_deposit(self):
        """
        Adds a new deposit to the database.
        """
        query = """INSERT INTO deposits (user_id, amount, deposit_date, description)
                   VALUES (%s, %s, %s, %s)"""
        values = (self.user_id, self.amount, self.deposit_date, self.description)
        try:
            self.db.execute_query(query, values)
            print("Deposit added successfully!")
        except Exception as error:
            print(f"Error occurred while adding deposit: {error}")

    @classmethod
    def get_deposits(cls, db: DB_Connect):
        """
        Fetches all deposit records from the database.

        :param db: An instance of DB_Connect for interacting with the database.
        :return: A list of Deposit objects.
        """
        query = "SELECT deposit_id, user_id, amount, deposit_date, description FROM deposits"
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
        values = (deposit_id,)
        try:
            db.execute_query(query, values)
            print("Deposit deleted successfully!")
        except Exception as error:
            print(f"Error occurred while deleting deposit: {error}")
=======
class Deposits:
    def __init__(self, amount, deposit_date, notes): #Initializes a deposit object.
        self.amount = amount
        self.deposit_date = deposit_date
        self.notes = notes
    def add_deposit(self, db_connection): #Inserts a new deposit record.
        cursor = db_connection.cursor()
        try:
            cursor.execute("""INSERT INTO deposits (amount, deposit_date, notes)
                       VALUES (%s,%s,%s)""",(self.amount, self.deposit_date, self.notes))
            db_connection.commit()
            print("Deposit added successfully!")
        except Exception as error:
            db_connection.rollback()  # Rollback in case of error
            print(f"Error occurred - While adding deposits: {error}")
        finally:
            cursor.close()  # Close the cursor    
    @classmethod
    def get_deposits(cls, db_connection): #Fetches all deposits.
        cursor = db_connection.cursor()
        try:    
            cursor.execute("SELECT * FROM deposits")
            deposits = cursor.fetchall()
            return deposits
        finally:
            cursor.close()  # Close the cursor    

    @classmethod
    def delete_deposit(cls, db_connection, deposit_id): #Deletes a deposit record
        cursor = db_connection.cursor()
        cursor.execute()
>>>>>>> 73aad84698f2328fa75797dc7a71397350b654f3
