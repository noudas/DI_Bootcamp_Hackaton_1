

class User:
    def __init__(self, username, first_name, last_name, email, password): #Initializes a user object.
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        
    def create_user(self, db_connection):# Inserts a new user into the database.
        cursor = db_connection.cursor()
        cursor.execute("""
                    INSERT INTO users (username, first_name, last_name, email, password)
                    VALUES(%s,%s,%s,%s,%s)""",
                    (self.username, self.first_name, self.last_name, self.email, self.password))
        db_connection.commit()
    
            
    @classmethod
    def get_user_by_id(cls, db_connection, user_id): #Fetches a user by ID.
        cursor = db_connection.cursor()
        cursor.execute("Select * from users WHERE id = %s",(user_id))
        row = cursor.fetchone()
        if row:
            return cls(row[1], row[2], row[3], row[4], row[5],)
        return None
        
    def update_user(self, db_connection, user_id): #Updates user information.
        cursor = db_connection.cursor()
        cursor.execute(""" 
                       UPDATE users 
                       SET Username = %s,first_name= %s, last_name= %s, email= %s, password= %s""",
                       (self.username, self.first_name, self.last_name, self.email, self.password))
        db_connection.commit()
        
    def delete_user(cls, db_connection, user_id):# Deletes a user.
         cursor = db_connection.cursor()
         cursor.execute(" DELETE FROM users WHERE id = %s",(user_id))
         db_connection.commit()
         
         