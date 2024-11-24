import psycopg2
from config import Config
from Py_classes import DB_Connect


class Expenses:
    def __init__(self, db: DB_Connect, amount, category_name, notes= None):
        """
        Initialize an expense with amount, category_name, and notes.
        
        :param db: An instance of DB_Connect for interacting with the database.
        :param amount: The amount of the expense.
        :param category_name: The category of the expense (string).
        :param notes: Optional notes for the expense.
        """
        self.db = db
        self.amount = amount
        self.category_name = category_name.lower()
        self.notes = notes
        self.category_id = self.get_category_id(self.category_name)

    def get_category_id(self, category_name):
        """
        Fetches the category_id from the database based on category name.
        
        :param category_name: The category name.
        :return: The category_id corresponding to the category name.
        """
        query = "SELECT category_id FROM categories WHERE LOWER(name) = %s"
        result = self.db.fetch_results(query, (category_name,))
        
        if result:
            return result[0]['category_id']
        return None


    def add_expense(self):
        """
        Adds a new expense to the database.
        """
        if not self.category_id:
            print(f"Error: Category '{self.category_name}' not found!")
            return
        
        query = """
            INSERT INTO expenses (amount, category_id, notes)
            VALUES (%s, %s, %s)
        """
        values = (self.amount, self.category_id, self.notes)  # category_id is now an integer
        try:
            self.db.execute_query(query, values)
            print("Expense added successfully!")
        except Exception as error:
            print(f"Error occurred while adding an expense: {error}")

        
    @classmethod
    def get_expense_by_id(cls, db: DB_Connect, expense_id):
        """
        Fetches an expense by its ID.
        
        :param db: An instance of DB_Connect for interacting with the database.
        :param expense_id: The ID of the expense to fetch.
        :return: The expense record or None if not found.
        """
        query = "SELECT * FROM expenses WHERE expense_id = %s"
        result = db.fetch_results(query, (expense_id,))
        return result
    
    

    @classmethod
    def delete_expense(cls, db: DB_Connect, expense_id):
        """
        Deletes an expense from the database.
        
        :param db: An instance of DB_Connect for interacting with the database.
        :param expense_id: The ID of the expense to delete.
        """
        query = "DELETE FROM expenses WHERE expense_id = %s"
        try:
            db.execute_query(query, (expense_id,))
            print("Expense deleted successfully!")
        except Exception as error:
            print(f"Error occurred while deleting an expense: {error}")
