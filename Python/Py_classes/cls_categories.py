class Categories:
    def __init__(self, db, name, description=None):
        self.db = db
        self.category_id = None
        self.name = name
        self.description = description

    @classmethod
    def get_all_categories(cls, db):
        try:
            query = "SELECT category_id, name, description FROM categories"
            results = db.fetch_results(query)
            
            print(f"Debug: Raw results from database: {results}") 
            
            return [cls(db, row['name'], row['description']) for row in results] if results else []
        except Exception as e:
            print(f"Error fetching categories: {e}")
            return []

    @classmethod
    def create_category(cls, db, name, description=None):
        new_category = cls(db, name, description)
        query = """
            INSERT INTO categories (name, description)
            VALUES (%s, %s)
        """
        params = (new_category.name, new_category.description)
        try:
            db.execute_query(query, params)
            print("Category created successfully!")
        except Exception as error:
            print(f"Error occurred while creating category: {error}")

    @classmethod
    def update_category(cls, db, name, new_name=None, new_description=None):
        query = """
            UPDATE categories 
            SET name = %s, description = %s, updated_at = CURRENT_TIMESTAMP
            WHERE name = %s
        """
        params = (new_name or cls(db).name, new_description or cls(db).description, name)
        try:
            db.execute_query(query, params)
            print("Category updated successfully!")
        except Exception as error:
            print(f"Error occurred while updating category: {error}")

    @classmethod
    def delete_category(cls, db, category_name):
        query = "DELETE FROM categories WHERE name = %s"
        params = (category_name,)
        try:
            db.execute_query(query, params)
            print("Category deleted successfully!")
        except Exception as error:
            print(f"Error occurred while deleting category: {error}")
