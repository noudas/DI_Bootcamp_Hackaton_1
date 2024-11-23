

class User:
    def __init__(self, username, first_name, last_name, email, password): #Initializes a user object.
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        
    def create_user(self, db_connection):# Inserts a new user into the database.
        cursor = db_connection.cursor()
        try:
            cursor.execute("""
                    INSERT INTO users (username, first_name, last_name, email, password)
                    VALUES(%s,%s,%s,%s,%s)""",
                    (self.username, self.first_name, self.last_name, self.email, self.password))
            db_connection.commit()
            print("User created successfully!")
        except Exception as error:
            db_connection.rollback()  # Rollback in case of error
            print(f"Error occurred  - While creating user: {error}")
        finally:
            cursor.close()  # Close the cursor
    
    @classmethod
    def get_user_by_id(cls, db_connection, user_id): #Fetches a user by ID.
        cursor = db_connection.cursor()
        try:
            cursor.execute("Select * from users WHERE id = %s",(user_id))
            row = cursor.fetchone()
            if row:
                return cls(row[1], row[2], row[3], row[4], row[5],)
            return None
        finally:
            cursor.close()
            
    def update_user(self, db_connection, new_username, new_email, new_password, user_id): #Updates user information.
        new_username = new_username if new_username is not None else self.username
        new_email = new_email if new_email is not None else self.email
        new_password = new_password if new_password is not None else self.password
        
        cursor = db_connection.cursor()
    
        try:
            cursor.execute(""" 
                        UPDATE users 
                        SET Username = %s, email= %s, password= %s 
                        WHERE user_id = %s""", (new_username , new_email , new_password  , user_id))
            db_connection.commit()
            print("User updated successfully!")
        except Exception as error:
            db_connection.rollback()  # Rollback in case of error
            print(f"Error occurred - While updating user: {error}")
        finally:
            cursor.close()  # Close the cursor
            
    def delete_user(cls, db_connection, user_id):# Deletes a user.
        cursor = db_connection.cursor()
        try:
            cursor.execute(" DELETE FROM users WHERE id = %s",(user_id))
            db_connection.commit()
        finally:
            cursor.close()
         
         