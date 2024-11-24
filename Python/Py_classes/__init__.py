# __init__.py

# Absolute imports
from .cls_DB_connect import DB_Connect
from .cls_budget import Budget
from .cls_categories import Categories
from .cls_deposits import Deposits
from .cls_expenses import Expenses
from .cls_savings_goal import Saving_Goals
from .cls_user import User

# Load environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Optional: You can print or log a message when the package is initialized
print("Py_classes package initialized with environment variables loaded.")
