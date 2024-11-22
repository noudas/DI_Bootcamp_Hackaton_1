from DB_insert_helper import insert_into

def test_insert_savings_goal():
    query = """
    INSERT INTO savings_goals (goal_name, target_amount, current_amount, due_date)
    VALUES (%s, %s, %s, %s)
    """
    values = ("Emergency Fund", 1000.00, 200.00, "2024-12-31")
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_savings_goal()
