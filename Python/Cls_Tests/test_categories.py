import psycopg2
from config import Config
from Py_classes import DB_Connect, Categories

def setup_database():
    # Create a sample category
    db = DB_Connect(db_name=Config.DB_NAME)
    category = Categories(db, "Test Category", "This is a test category")
    category.create_category()

def teardown_database():
    # Delete all categories (you might need to implement this method)
    pass

def test_create_category():
    """Test creating a new category."""
    print("Testing create_category method...")

    setup_database()
    
    # Call the create_category method
    db = DB_Connect(db_name=Config.DB_NAME)
    category = Categories(db, "Test Category", "Another test category")
    category.create_category()

    print("create_category method executed successfully.")

def test_get_all_categories():
    """Test getting all categories."""
    print("Testing get_all_categories method...")

    setup_database()
    
    # Fetch all categories
    db = DB_Connect(db_name=Config.DB_NAME)
    categories = Categories.get_all_categories(db)

    print(f"Fetched {len(categories)} categories:")
    for i, cat in enumerate(categories):
        print(f"{i+1}. Name: {cat.category_name}, Description: {cat.description}")

    assert len(categories) > 0, "No categories fetched"

def test_update_category():
    """Test updating a category."""
    print("Testing update_category method...")

    setup_database()
    
    # Fetch all categories
    db = DB_Connect(db_name=Config.DB_NAME)
    categories = Categories.get_all_categories(db)
    
    if not categories:
        print("No categories found to update.")
        return
    
    # Update the first category
    updated_category = Categories(db, categories[0].category_name)
    updated_category.update_category(categories[0].category_name)

    # Fetch the updated category
    updated_categories = Categories.get_all_categories(db)

    print(f"Fetched {len(updated_categories)} categories after update:")
    for i, cat in enumerate(updated_categories):
        print(f"{i+1}. Name: {cat.category_name}, Description: {cat.description}")

    assert len(updated_categories) == len(categories), "Number of categories should remain the same"
    for cat in updated_categories:
        assert cat.category_name == categories[0].category_name, f"Expected '{categories[0].category_name}', but got '{cat.category_name}'"

def test_delete_category():
    """Test deleting a category."""
    print("Testing delete_category method...")

    setup_database()
    
    # Fetch all categories
    db = DB_Connect(db_name=Config.DB_NAME)
    categories = Categories.get_all_categories(db)
    
    if not categories:
        print("No categories found to delete.")
        return
    
    # Delete the first category
    Categories.delete_category(db, categories[0].category_name)

    # Try to fetch the deleted category
    fetched_categories = Categories.get_all_categories(db)
    
    print(f"Fetched {len(fetched_categories)} categories after deletion:")
    for i, cat in enumerate(fetched_categories):
        print(f"{i+1}. Name: {cat.category_name}, Description: {cat.description}")

    assert len(fetched_categories) == len(categories) - 1, f"Expected {len(categories) - 1} categories after deletion, but got {len(fetched_categories)}"

if __name__ == '__main__':
    print("Starting tests...\n")
    
    setup_database()
    
    test_create_category()
    test_get_all_categories()
    test_update_category()
    test_delete_category()

    teardown_database()  # Uncomment when you implement database cleanup
    
    print("\nAll tests completed.")
