import psycopg2
from config import Config
from Py_classes import DB_Connect, User
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def test_create_user():
    """Test creating a new user."""
    print("Testing create_user method...")

    # Create a sample user
    db = DB_Connect(db_name=os.getenv("DB_NAME"))
    user = User(db, "johndoe", "John", "Doe", "john@example.com", "password123")

    # Call the create_user method
    user.create_user()

    print("create_user method executed successfully.")

def test_get_user_by_id():
    """Test getting a user by ID."""
    print("Testing get_user_by_id method...")

    # Create a sample user
    db = DB_Connect(db_name=os.getenv("DB_NAME"))
    user = User(db, "johndoe", "John", "Doe", "john@example.com", "password123")
    user.create_user()

    # Fetch the user
    fetched_user = User.get_user_by_id(db, 1)

    print(f"Fetched user: {fetched_user}")
    assert fetched_user is not None, "Failed to fetch user"
    assert fetched_user.username == "johndoe", f"Expected username 'johndoe', but got '{fetched_user.username}'"

def test_update_user():
    """Test updating a user."""
    print("Testing update_user method...")

    # Create a sample user
    db = DB_Connect(db_name=os.getenv("DB_NAME"))
    user = User(db, "johndoe", "John", "Doe", "john@example.com", "password123")
    user.create_user()

    # Update the user
    updated_user = User(db, "johndoe", "John", "Doe", "updated@example.com", "new_password")
    updated_user.update_user(new_username="johndoe", new_email="updated@example.com", new_password="new_password")

    # Fetch the updated user
    fetched_user = User.get_user_by_id(db, 1)

    print(f"Fetched updated user: {fetched_user}")
    assert fetched_user is not None, "Failed to fetch updated user"
    assert fetched_user.username == "johndoe", f"Expected username 'johndoe', but got '{fetched_user.username}'"
    assert fetched_user.email == "updated@example.com", f"Expected email 'updated@example.com', but got '{fetched_user.email}'"
    assert fetched_user.password != "password123", "Password should have changed"

def test_delete_user():
    """Test deleting a user."""
    print("Testing delete_user method...")

    # Create a sample user
    db = DB_Connect(db_name=os.getenv("DB_NAME"))
    user = User(db, "johndoe", "John", "Doe", "delete@example.com", "delete_password")
    user.create_user()

    # Delete the user
    User.delete_user(db, 1)

    # Try to fetch the deleted user
    fetched_user = User.get_user_by_id(db, 1)

    print(f"Fetched deleted user: {fetched_user}")
    assert fetched_user is None, "Should not be able to fetch deleted user"

if __name__ == '__main__':
    print("Starting tests...\n")
    
    test_create_user()
    test_get_user_by_id()
    test_update_user()
    test_delete_user()

    print("\nAll tests completed.")
