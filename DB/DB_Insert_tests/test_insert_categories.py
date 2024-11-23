from DB_Insert_tests.DB_insert_helper import insert_into

def test_insert_category():
    query = """
    INSERT INTO categories (name, description)
    VALUES (%s, %s)
    """
    values = ("Food", "Expenses related to food and dining.")
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_category()