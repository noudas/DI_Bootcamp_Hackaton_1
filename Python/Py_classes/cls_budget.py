import psycopg2
from config import Config
from Py_classes import DB_Connect

class Budget:
    def __init__(self, db: DB_Connect, user_id, total_budget, savings=0.00, spent_amount=0.00):
        """
        Initializes a Budget object with basic attributes and a DB_Connect instance.
        
        :param db: An instance of the DB_Connect class to manage database connections.
        :param user_id: The ID of the user associated with the budget.
        :param total_budget: The total budget amount.
        :param savings: The amount of savings (default is 0.00).
        :param spent_amount: The amount spent from the budget (default is 0.00).
        """
        self.db = db
        self.user_id = user_id
        self.total_budget = total_budget
        self.savings = savings
        self.spent_amount = spent_amount

    def create_budget(self):
        """
        Inserts a new budget record into the database using the execute_query method.
        """
        query = """
            INSERT INTO budget (user_id, total_budget, savings, spent_amount)
            VALUES (%s, %s, %s, %s)
        """
        params = (self.user_id, self.total_budget, self.savings, self.spent_amount)
        self.db.execute_query(query, params)

    def update_budget(self, user_id, new_total_budget=None, new_savings=None, new_spent_amount=None):
        """
        Updates the budget values in the database using the execute_query method.
        
        :param new_total_budget: The new total budget value, if updating.
        :param new_savings: The new savings value, if updating.
        :param new_spent_amount: The new spent amount value, if updating.
        """
        new_total_budget = new_total_budget if new_total_budget is not None else self.total_budget
        new_savings = new_savings if new_savings is not None else self.savings
        new_spent_amount = new_spent_amount if new_spent_amount is not None else self.spent_amount

        query = """
            UPDATE budget 
            SET total_budget = %s, savings = %s, spent_amount = %s, updated_at = CURRENT_TIMESTAMP
            WHERE user_id = %s
        """
        params = (new_total_budget, new_savings, new_spent_amount, user_id)
        self.db.execute_query(query, params)

    @classmethod
    def get_budget(cls, db: DB_Connect, user_id):
        """
        Fetches the current budget for a user from the database using the fetch_results method.
        
        :param db: An instance of the DB_Connect class.
        :param user_id: The ID of the user whose budget is to be fetched.
        :return: An instance of Budget if the budget is found, None otherwise.
        """
        query = "SELECT * FROM budget WHERE user_id = %s"
        params = (user_id,)
        results = db.fetch_results(query, params)

        if results:
            row = results[0] 
            return cls(db, row[1], row[2], row[3], row[4])
        return None
