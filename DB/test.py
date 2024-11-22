from config import Config
from DB_config.DB_create import db_create
from DB_config.DB_connect import db_connect
from DB_tables.DB_user_table import create_table_users
from DB_tables.DB_categories_table import create_table_categories
from DB_tables.DB_expenses_table import create_table_expenses
from DB_tables.DB_budget_table import create_table_budget




def test_config():
    """
    Test to check if the Config class correctly loads environment variables.
    """

    print("Testing Config class...")
    print(f"DB_NAME: {Config.DB_NAME}")
    print(f"DB_USER: {Config.DB_USER}")
    print(f"DB_PASSWORD: {Config.DB_PASSWORD}")
    print(f"DB_HOST: {Config.DB_HOST}")
    print(f"DB_PORT: {Config.DB_PORT}")

def test__db__default_connect():
    """
    Test to check if the database connection works with the default database.
    """
    print("\nTesting database connection...")
    connection = db_connect(Config.DB_NAME_DEFAULT)
    if connection:
        print(f"DB connected successfully!")
        connection.close()
    else:
        print("Connection Failed")

def test_db_creation():
    """
    Test to check if a new database can be created.
    """
    test_db_name = "Hackaton_1"
    print("\nTesting database creation...")
    db_create(test_db_name)

def test_db_create_tables():
    """
    Test to check if a all the tables can be created.
    """
    print("\nTesting tables creation...")
    create_table_users()
    create_table_categories()
    create_table_expenses()
    create_table_budget()

if __name__ == "__main__":
    print("Starting tests...\n")
    test_config()
    test__db__default_connect()
    test_db_creation()
    test_db_create_tables()

    print("\nAll tests completed.")