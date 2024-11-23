class Deposits:
    def __init__(self, amount, deposit_date, notes): #Initializes a deposit object.
        self.amount = amount
        self.deposit_date = deposit_date
        self.notes = notes
    def add_deposit(self, db_connection): #Inserts a new deposit record.
        cursor = db_connection.cursor()
        try:
            cursor.execute("""INSERT INTO deposits (amount, deposit_date, notes)
                       VALUES (%s,%s,%s)""",(self.amount, self.deposit_date, self.notes))
            db_connection.commit()
            print("Deposit added successfully!")
        except Exception as error:
            db_connection.rollback()  # Rollback in case of error
            print(f"Error occurred - While adding deposits: {error}")
        finally:
            cursor.close()  # Close the cursor    
    @classmethod
    def get_deposits(cls, db_connection): #Fetches all deposits.
        cursor = db_connection.cursor()
        try:    
            cursor.execute("SELECT * FROM deposits")
            deposits = cursor.fetchall()
            return deposits
        finally:
            cursor.close()  # Close the cursor    

    @classmethod
    def delete_deposit(cls, db_connection, deposit_id): #Deletes a deposit record
        cursor = db_connection.cursor()
        try:
            cursor.execute("DELETE FROM deposits WHERE deposit_id= %s",(deposit_id))
        finally:
            cursor.close()  # Close the cursor  
        