import psycopg2
from config import Config
from cls_DB_connect import DB_Connect

class Saving_Goals:
    def __init__(self, db: DB_Connect, user_id, goal_name, target_amount, current_amount, due_date):
        """
        Initializes a savings goal with the user's ID and goal details.
        
        :param db: An instance of the DB_Connect class to manage database connections.
        :param user_id: The user ID associated with the goal.
        :param goal_name: The name of the savings goal.
        :param target_amount: The target amount for the savings goal.
        :param current_amount: The current amount saved towards the goal.
        :param due_date: The due date for the goal.
        """
        self.db = db
        self.user_id = user_id
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.due_date = due_date

    def create_goal(self):
        """
        Adds a new savings goal to the database.
        """
        query = """
            INSERT INTO savings (user_id, goal_name, target_amount, current_savings, due_date)
            VALUES (%s, %s, %s, %s, %s)
        """
        params = (self.user_id, self.goal_name, self.target_amount, self.current_amount, self.due_date)
        self.db.execute_query(query, params)

    def update_goal(self, goal_id, new_goal_name=None, new_target_amount=None, new_current_amount=None, new_due_date=None):
        """
        Updates the details of an existing savings goal in the database.
        
        :param goal_id: The ID of the goal to be updated.
        :param new_goal_name: The new name for the goal, if updating.
        :param new_target_amount: The new target amount, if updating.
        :param new_current_amount: The new current amount saved, if updating.
        :param new_due_date: The new due date, if updating.
        """
        new_goal_name = new_goal_name if new_goal_name else self.goal_name
        new_target_amount = new_target_amount if new_target_amount else self.target_amount
        new_current_amount = new_current_amount if new_current_amount else self.current_amount
        new_due_date = new_due_date if new_due_date else self.due_date

        query = """
            UPDATE savings 
            SET goal_name = %s, target_amount = %s, current_savings = %s, due_date = %s, updated_at = CURRENT_TIMESTAMP 
            WHERE goal_id = %s
        """
        values = (new_goal_name, new_target_amount, new_current_amount, new_due_date, goal_id)
        self.db.execute_query(query, values)

    @classmethod
    def delete_goal(cls, db: DB_Connect, goal_id):
        """
        Deletes a savings goal from the database by goal ID.
        
        :param db: An instance of the DB_Connect class.
        :param goal_id: The ID of the goal to delete.
        """
        query = "DELETE FROM savings WHERE goal_id = %s"
        params = (goal_id,)
        db.execute_query(query, params)

    @classmethod
    def get_goals(cls, db: DB_Connect, user_id):
        """
        Fetches all savings goals for a specific user from the database.
        
        :param db: An instance of the DB_Connect class.
        :param user_id: The ID of the user whose goals are to be fetched.
        :return: A list of Saving_Goals instances.
        """
        query = "SELECT * FROM savings WHERE user_id = %s"
        params = (user_id,)
        results = db.fetch_results(query, params)

        if results:
            goals = []
            for row in results:
                goals.append(cls(db, row[1], row[2], row[3], row[4], row[5]))
            return goals
        return []
