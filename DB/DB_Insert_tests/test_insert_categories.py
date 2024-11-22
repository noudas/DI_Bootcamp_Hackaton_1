from DB_insert_helper import insert_into

def test_insert_category():
    query = """
    INSERT INTO categories (category_name)
    VALUES (%s)
    """
    values = ("Food",)
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_category()
