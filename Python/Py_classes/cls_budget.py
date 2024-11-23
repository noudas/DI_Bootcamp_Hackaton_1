class Budget:
    def __init__(self, total_budget, savings, spent_amount): #Initializes a budget object.
        self.total_budget = total_budget
        self.savings = savings
        self.spent_amount = spent_amount
    def create_budget(self, db_connection): #Inserts a new budget record.
        cursor = db_connection.cursor()
        cursor.execute("""INSERT INTO budget (total_budget, savings, spent_amount)
                       VALUES (%s,%s,%s)""",(self.total_budget, self.savings, self.spent_amount))
        db_connection.commit()
    def update_budget(self, db_connection):# Updates budget values.
        cursor = db_connection.cursor()
        cursor.execute()
        db_connection.commit()
    @classmethod
    def get_budget(cls, db_connection): #Fetches the current budget.
        cursor = db_connection.cursor()
        cursor.execute()
        db_connection.commit()