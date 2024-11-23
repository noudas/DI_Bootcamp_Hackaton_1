class Categories:
    def __init__(self, category_name): #Initializes a category object.
        self.category_name = category_name
    def create_category(self, db_connection): #Inserts a new category.
        cursor = db_connection.cursor()
        cursor.execute("""INSERT INTO categories(name)
                       VALUES (%s)""",(self.category_name))
        db_connection.commit()
    @classmethod
    def get_all_categories(cls, db_connection):# Fetches all categories.
        cursor = db_connection.cursor()
        cursor.execute("SELECT * from categories")
        results = cursor.fetchall()#Fetch all results
        categories = [cls(category_name = row[1]) for row in results]
        return categories

    def update_category(self, db_connection, category_id): #Updates a category.
        cursor = db_connection.cursor()
        cursor.execute()
        db_connection.commit()
    @classmethod
    def delete_category(cls, db_connection, category_id): #Deletes a category.
        cursor = db_connection.cursor()
        cursor.execute()
    
    
    
    