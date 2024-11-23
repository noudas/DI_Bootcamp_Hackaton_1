class Saving_Goals:
    def __init__(self, goal_name, target_amount, current_amount, due_date): #Initializes a savings goal.
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.due_date = due_date
    def create_goal(self, db_connection):# Adds a new savings goal.
        cursor = db_connection.cursor()
        cursor.execute("""INSERT INTO savings (amount, category_id, notes)
                       VALUES (%s,%s,%s,%s)""",(self.goal_name, self.target_amount, self.current_amount,self.due_date))
        db_connection.commit()
    def update_goal(self, db_connection, goal_id): ##Updates savings goal details.
        cursor = db_connection.cursor()
        cursor.execute()
        db_connection.commit()
    @classmethod
    def delete_goal(cls, db_connection, goal_id): #Deletes a savings goal.
        cursor = db_connection.cursor()
        cursor.execute()
    @classmethod
    def get_goals(cls, db_connection): #Fetches all savings goals.
        cursor = db_connection.cursor()
        cursor.execute()