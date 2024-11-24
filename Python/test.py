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

if __name__ == '__main__':
    print("Starting tests...\n")
    test_connect_success()
    test_connect_failure()
    test_disconnect()
    test_disconnect_no_connection()


    print("\nAll tests completed.")
