class Expenses:
    def __init__(self, amount, category_name, notes): #Initializes an expense object.
       self.amount = amount
       self.category_name = category_name.lower()
       self.notes = notes
    def add_expense(self, db_connection): #Inserts a new expense.
        cursor = db_connection.cursor()
        try:
            cursor.execute("""INSERT INTO expenses (amount, category_id, notes)
                       VALUES (%s,%s,%s)""",(self.amount, self.category_name, self.category_id))
            db_connection.commit()
            print("Expense added successfully!")
        except Exception as error:
            db_connection.rollback()  # Rollback in case of error
            print(f"Error occurred - While adding an expense: {error}")
        finally:
            cursor.close()  # Close the cursor
    @classmethod
    def get_expense_by_id(cls, db_connection, expense_id): #Fetches an expense by ID.
        cursor = db_connection.cursor()
        try:
            cursor.execute("SELECT * FROM expenses WHERE expense_id = %s",(expense_id))
        finally:
            cursor.close()  # Close the cursor
            
    @classmethod    
    def get_expenses_by_category(cls, db_connection, category_id): #Fetches expenses for a specific category.
        cursor = db_connection.cursor()
        try:
            cursor.execute("SELECT * FROM expenses WHERE category_id = %s",(category_id))
        finally:
            cursor.close()  # Close the cursor
    @classmethod
    def delete_expense(cls, db_connection, expense_id): #Deletes an expense.
        cursor = db_connection.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id = %s",(expense_id))
        finally:
            cursor.close()  # Close the cursor