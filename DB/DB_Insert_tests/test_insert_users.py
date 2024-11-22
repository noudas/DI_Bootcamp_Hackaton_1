from DB_insert_helper import insert_into

def test_insert_user():
    query = """
    INSERT INTO users (username, first_name, last_name, email, password)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = ("johndoe", "John", "Doe", "johndoe@example.com", "securepassword")
    insert_into(query, values)

if __name__ == "__main__":
    test_insert_user()
