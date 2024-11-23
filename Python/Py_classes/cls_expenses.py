class Expenses:
    def __init__(self, amount, category_id, notes): #Initializes an expense object.
       self.amount = amount
       self.category_id = category_id
       self.notes = notes
    def add_expense(self, db_connection): #Inserts a new expense.
        cursor = db_connection.cursor()
        cursor.execute("""INSERT INTO expenses (amount, category_id, notes)
                       VALUES (%s,%s,%s)""",(self.amount, self.category_id, self.category_id))
        db_connection.commit()
    @classmethod
    def get_expense_by_id(cls, db_connection, expense_id): #Fetches an expense by ID.
        cursor = db_connection.cursor()
        cursor.execute()
    @classmethod    
    def get_expenses_by_category(cls, db_connection, category_id): #Fetches expenses for a specific category.
        cursor = db_connection.cursor()
        cursor.execute()
    @classmethod
    def delete_expense(cls, db_connection, expense_id): #Deletes an expense.
        cursor = db_connection.cursor()
        cursor.execute()