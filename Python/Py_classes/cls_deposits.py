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
            
    @classmethod
    def get_deposits(cls, db_connection): #Fetches all deposits.
        cursor = db_connection.cursor()
        cursor.execute()
    @classmethod
    def delete_deposit(cls, db_connection, deposit_id): #Deletes a deposit record
        cursor = db_connection.cursor()
        cursor.execute()