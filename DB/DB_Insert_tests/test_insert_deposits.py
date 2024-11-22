from DB_insert_helper import insert_into

def test_insert_deposit():
    query = """
    INSERT INTO deposits (amount, deposit_date, notes)
    VALUES (%s, %s, %s)
    """
    values = (500.00, "2024-11-21", "Monthly salary")
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_deposit()
