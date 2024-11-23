from config import Config
from Py_config.Py_connect import db_connect



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




if __name__ == "__main__":
    print("Starting tests...\n")
    test_config()
    test__db__default_connect()
    print("\nAll tests completed.")