from test_insert_budget import test_insert_budget
from test_insert_categories import test_insert_category
from test_insert_deposits import test_insert_deposit
from test_insert_expenses import test_insert_expense
from test_insert_savings_goals import test_insert_savings_goal
from test_insert_users import test_insert_user

def inserts_tests():
    """
    Tests the inserts in all of the tables.
    """
    test_insert_user()
    test_insert_category()
    test_insert_expense()
    test_insert_budget()
    test_insert_savings_goal()
    test_insert_deposit()