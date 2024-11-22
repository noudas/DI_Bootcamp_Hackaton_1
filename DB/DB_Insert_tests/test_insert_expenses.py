from DB_insert_helper import insert_into

def test_insert_expense():
    query = """
    INSERT INTO expenses (amount, category_id, notes)
    VALUES (%s, %s, %s)
    """
    values = (50.00, 1, "Lunch at Subway")
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_expense()
