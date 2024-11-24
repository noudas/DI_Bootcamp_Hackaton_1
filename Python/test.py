from unittest.mock import patch, MagicMock
from config import Config
from Py_classes import *
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def test_connect_success():
    """Test successful connection to the database."""
    print("Testing successful connection...")

    mock_connection = MagicMock()
    with patch('Py_classes.DB_Connect.connect', return_value=mock_connection):
        db = DB_Connect(db_name=os.getenv("DB_NAME"))
        connection = db.connect()

        assert connection == mock_connection, f"Expected {mock_connection}, but got {connection}"
        mock_connection.close.assert_not_called()

        print("Success! Database connection is established.")

def test_connect_failure():
    """Test failed connection to the database."""
    print("Testing failed connection...")
    
    with patch('Py_classes.DB_Connect.connect', side_effect=Exception("Connection failed")):
        db = DB_Connect(db_name=os.getenv("DB_NAME"))
        
        try:
            connection = db.connect()
            assert False, "Expected an exception, but none was raised."
        except Exception as e:
            assert str(e) == "Connection failed", f"Expected 'Connection failed', but got '{str(e)}'"
            print("Success! Connection failed as expected.")

def test_disconnect():
    """Test successful disconnection from the database."""
    print("Testing successful disconnection...")

    mock_connection = MagicMock()
    db = DB_Connect(db_name=os.getenv("DB_NAME"))
    db.connection = mock_connection

    db.disconnect()

    mock_connection.close.assert_called_once()

    print("Success! Database disconnected successfully.")

def test_disconnect_no_connection():
    """Test disconnect with no active connection."""
    print("Testing disconnection with no active connection...")

    db = DB_Connect(db_name=os.getenv("DB_NAME"))
    db.connection = None

    # Capture print statements (since logging is not set up here)
    with patch('builtins.print') as mock_print:
        db.disconnect()
        mock_print.assert_called_with("No active connection to disconnect.")
    
    print("Success! No connection to disconnect.")

def test_create_user():
    """Test creating a new user."""
    print("Testing create user...")

    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    
    with patch('Py_classes.DB_Connect', autospec=True) as mock_db_class:
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.connect.return_value = mock_connection
        
        # Create a Config instance with mocked environment variables
        class MockConfig:
            DB_NAME_DEFAULT = 'test_database'
            DB_NAME = 'test_database'
            DB_USER = 'test_user'
            DB_PASSWORD = 'test_password'
            DB_HOST = 'localhost'
            DB_PORT = '5432'

        config = MockConfig()

        # Create a User instance
        user = User(
            db=DB_Connect(db_name=config.DB_NAME),
            username='test_user',
            first_name='John',
            last_name='Doe',
            email='john@example.com',
            password='hashed_password'
        )

        # Disable logging temporarily
        with patch('logging.Logger.info') as mock_info, \
             patch('logging.Logger.error') as mock_error:
            
            user.create_user()
            
            mock_cursor.execute.assert_called_once()
            mock_connection.commit.assert_called_once()
            mock_connection.close.assert_called_once()
            
            print("Success! User created successfully.")

def test_get_user_by_id():
    """Test getting a user by ID."""
    print("Testing get user by ID...")

    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    
    with patch('Py_classes.DB_Connect', autospec=True) as mock_db_class:
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.connect.return_value = mock_connection
        
        # Mock the Config to avoid reading from environment variables
        with patch('config.Config', autospec=True) as mock_config_class:
            mock_config = mock_config_class.return_value
            mock_config.get_config.return_value = {'DB_NAME': 'test_database'}
            
            # Set up mock cursor to return sample data
            mock_cursor.fetchone.return_value = [1, 'test_user', 'John', 'Doe', 'john@example.com', 'hashed_password']

            # Get user by ID
            retrieved_user = User.get_user_by_id(DB_Connect(), 1)

            assert isinstance(retrieved_user, User)
            assert retrieved_user.username == 'test_user'
            assert retrieved_user.first_name == 'John'
            assert retrieved_user.last_name == 'Doe'
            assert retrieved_user.email == 'john@example.com'

            print("Success! User retrieved successfully.")

def test_update_user():
    """Test updating a user."""
    print("Testing update user...")

    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    
    with patch('Py_classes.DB_Connect', autospec=True) as mock_db_class:
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.connect.return_value = mock_connection
        
        # Mock the Config to avoid reading from environment variables
        with patch('config.Config', autospec=True) as mock_config_class:
            mock_config = mock_config_class.return_value
            mock_config.get_config.return_value = {'DB_NAME': 'test_database'}
            
            # Create a User instance
            user = User(
                db=DB_Connect(),
                username='test_user',
                first_name='John',
                last_name='Doe',
                email='john@example.com',
                password='hashed_password'
            )

            # Update the user
            user.update_user(new_email='johndoe@example.com')

            mock_cursor.execute.assert_called_once()
            mock_connection.commit.assert_called_once()
            mock_connection.close.assert_called_once()

            print("Success! User updated successfully.")

def test_delete_user():
    """Test deleting a user."""
    print("Testing delete user...")

    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    
    with patch('Py_classes.DB_Connect', autospec=True) as mock_db_class:
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.connect.return_value = mock_connection
        
        # Mock the Config to avoid reading from environment variables
        with patch('config.Config', autospec=True) as mock_config_class:
            mock_config = mock_config_class.return_value
            mock_config.get_config.return_value = {'DB_NAME': 'test_database'}
            
            # Delete a user
            User.delete_user(DB_Connect(), 1)

            mock_cursor.execute.assert_called_once()
            mock_connection.close.assert_called_once()

            print("Success! User deleted successfully.")



if __name__ == '__main__':
    print("Starting tests...\n")
    test_connect_success()
    test_connect_failure()
    test_disconnect()
    test_disconnect_no_connection()
    test_create_user()
    test_get_user_by_id()
    test_update_user()
    test_delete_user()


    print("\nAll tests completed.")
