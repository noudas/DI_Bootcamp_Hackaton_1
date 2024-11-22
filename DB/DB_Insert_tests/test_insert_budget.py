from DB_Insert_tests.DB_insert_helper import insert_into

def test_insert_budget():
    query = """
    INSERT INTO budget (user_id,total_budget, savings, spent_amount)
    VALUES (%s, %s, %s, %s)
    """
    values = (1,1000.00, 200.00, 50.00)
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_budget()
