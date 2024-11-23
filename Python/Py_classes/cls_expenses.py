__init__(self, amount, category_id, notes): Initializes an expense object.

add_expense(self, db_connection): Inserts a new expense.

get_expense_by_id(cls, db_connection, expense_id): Fetches an expense by ID.

get_expenses_by_category(cls, db_connection, category_id): Fetches expenses for a specific category.

delete_expense(cls, db_connection, expense_id): Deletes an expense.