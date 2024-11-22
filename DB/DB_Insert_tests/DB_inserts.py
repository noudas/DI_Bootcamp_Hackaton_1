from DB_Insert_tests.test_insert_budget import test_insert_budget
from DB_Insert_tests.test_insert_categories import test_insert_category
from DB_Insert_tests.test_insert_deposits import test_insert_deposit
from DB_Insert_tests.test_insert_expenses import test_insert_expense
from DB_Insert_tests.test_insert_savings_goals import test_insert_savings_goal
from DB_Insert_tests.test_insert_users import test_insert_user

def inserts_tests():
    """
    Tests the inserts in all of the tables.
    """
    test_insert_user() # Ok
    test_insert_category() # Ok
    test_insert_deposit() 
    test_insert_expense() # Ok
    test_insert_budget()
    test_insert_savings_goal()
