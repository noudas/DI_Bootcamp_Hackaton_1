import psycopg2
from config import Config
from Py_classes import DB_Connect

class Categories:
    def __init__(self, db: DB_Connect, category_name, description=None):
        """
        Initialize a new category with a name and optional description.

        :param db: An instance of DB_Connect for interacting with the database.
        :param category_name: The name of the category.
        :param description: The optional description of the category.
        """
        self.db = db
        self.category_name = category_name
        self.description = description

    def create_category(self):
        """
        Inserts a new category into the database.
        """
        query = """
            INSERT INTO categories (name, description)
            VALUES (%s, %s)
        """
        params = (self.category_name, self.description)
        try:
            self.db.execute_query(query, params)
            print("Category created successfully!")
        except Exception as error:
            print(f"Error occurred while creating category: {error}")
    
    @classmethod
    def get_all_categories(cls, db: DB_Connect):
        """
        Fetches all categories from the database.
        
        :param db: An instance of DB_Connect for interacting with the database.
        :return: A list of category objects.
        """
        query = "SELECT category_id, name, description FROM categories"
        results = db.fetch_results(query)
        
        categories = [cls(db, row[1], row[2]) for row in results]
        return categories

    def update_category(self, category_id, new_category_name=None, new_description=None):  # Updates a category.
        """
        Updates the details of an existing category in the database.

        :param category_id: The ID of the category to update.
        :param new_category_name: The new name for the category, if provided.
        :param new_description: The new description for the category, if provided.
        """
        new_category_name = new_category_name if new_category_name else self.category_name
        new_description = new_description if new_description else self.description
        
        query = """
            UPDATE categories 
            SET name = %s, description = %s, updated_at = CURRENT_TIMESTAMP
            WHERE category_id = %s
        """
        params = (new_category_name, new_description, category_id)
        try:
            self.db.execute_query(query, params)
            print("Category updated successfully!")
        except Exception as error:
            print(f"Error occurred while updating category: {error}")

    @classmethod
    def delete_category(cls, db: DB_Connect, category_id):
        """
        Deletes a category from the database.

        :param db: An instance of DB_Connect for interacting with the database.
        :param category_id: The ID of the category to delete.
        """
        query = "DELETE FROM categories WHERE category_id = %s"
        params = (category_id,)
        try:
            db.execute_query(query, params)
            print("Category deleted successfully!")
        except Exception as error:
            print(f"Error occurred while deleting category: {error}")
