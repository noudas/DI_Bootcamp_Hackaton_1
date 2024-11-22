from DB_user_table import create_table_users
from DB_categories_table import create_table_categories
from DB_expenses_table import create_table_expenses
from DB_budget_table import create_table_budget
from DB_savings_goal_table import create_table_savings_goals
from DB_deposits_table import create_table_deposits

def initialize_database():
    """
    Initialize the database by creating necessary tables.
    """
    print("\nInitializing database and creating tables...")
    create_table_users()
    create_table_categories()
    create_table_expenses()
    create_table_budget()
    create_table_savings_goals()
    create_table_deposits()
    print("Database initialization complete.")
