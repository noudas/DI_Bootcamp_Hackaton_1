__init__(self, amount, deposit_date, notes): Initializes a deposit object.

add_deposit(self, db_connection): Inserts a new deposit record.

get_deposits(cls, db_connection): Fetches all deposits.

delete_deposit(cls, db_connection, deposit_id): Deletes a deposit record