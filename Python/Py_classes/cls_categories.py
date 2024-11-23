class Categories:
    def __init__(self, category_name, description): #Initializes a category object.
        self.category_name = category_name
        self.description = description
    def create_category(self, db_connection): #Inserts a new category.
        cursor = db_connection.cursor()
        try:
            cursor.execute("""INSERT INTO categories(name)
                        VALUES (%s,%s)""",(self.category_name, self.description))
            db_connection.commit()
            print("Category created successfully!")
        except Exception as error:
            db_connection.rollback()  # Rollback in case of error
            print(f"Error occurred - While creating category: {error}")
        finally:
            cursor.close()  # Close the cursor
            
        
    @classmethod
    def get_all_categories(cls, db_connection):# Fetches all categories.
        cursor = db_connection.cursor()
        cursor.execute("SELECT * from categories")
        results = cursor.fetchall()#Fetch all results
        categories = [cls(category_name = row[1]) for row in results]
        return categories

    def update_category(self, db_connection, category_id, new_category_name): #Updates a category.
        new_category_name = new_category_name if new_category_name is not None else self.category_name
        cursor = db_connection.cursor()
        try:
            cursor.execute(""" 
                        UPDATE categories 
                        SET name = %s
                        WHERE category_id = %s""",
                        (new_category_name, category_id))
            db_connection.commit()
            print("Category updated successfully!")
        except Exception as error:
            db_connection.rollback()  # Rollback in case of error
            print(f"Error occurred - While updating category: {error}")
        finally:
            cursor.close()  # Close the cursor
    @classmethod
    def delete_category(cls, db_connection, category_id): #Deletes a category.
        cursor = db_connection.cursor()
        cursor.execute(" DELETE FROM users WHERE id = %s",(category_id))
    
    
    
    