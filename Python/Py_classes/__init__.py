# __init__.py

# Absolute imports
from Py_classes.cls_DB_connect import DB_Connect
from Py_classes.cls_budget import Budget
from Py_classes.cls_categories import Categories
from Py_classes.cls_deposits import Deposits
from Py_classes.cls_expenses import Expenses
from Py_classes.cls_savings_goal import Saving_Goals
from Py_classes.cls_user import User

# Load environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Optional: You can print or log a message when the package is initialized
print("Py_classes package initialized with environment variables loaded.")
