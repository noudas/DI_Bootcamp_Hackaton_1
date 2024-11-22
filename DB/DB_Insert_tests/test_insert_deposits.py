from DB_Insert_tests.DB_insert_helper import insert_into

def test_insert_deposit():
    query = """
    INSERT INTO deposits (user_id,amount, deposit_date, description)
    VALUES (%s, %s, %s, %s)
    """
    values = (1, 500.00, "2024-11-21", "Monthly salary")
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_deposit()
