import psycopg2
import sys
import os

# Add the parent directory of Py_classes to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Py_classes import DB_Connect, User, Budget, Deposits, Expenses, Categories, Saving_Goals
from config import Config

db = DB_Connect(db_name=Config.DB_NAME)


def user_menu():
    print("User Menu:\n Please select an option from 1-4:")
    while True:
        try:
            user_choice = int(input("""
1. Create new user
2. Find user by ID
3. Update existing user
4. Delete existing user
5. Exit
"""))

            match user_choice:
                case 1:  # Create new user
                    new_username = input("Username:\t")
                    new_first_name = input("First name:\t")
                    new_last_name = input("Last name:\t")
                    new_email = input("Email:\t")
                    new_user_password = input("Password:\t")
                    new_user = User(db, new_username, new_first_name,
                                    new_last_name, new_email, new_user_password)
                    new_user.create_user()

                case 2:  # Find user by ID - SemiBroken - Fix later
                    user_id = int(input("Enter User ID: "))
                    print(f"Attempting to fetch user with ID: {user_id}")  # Debug print
                    user = User.get_user_by_id(db, user_id)
                    
                    if user:
                        print("User found successfully")
                        print(f"\nUser Information:")
                        print(f"ID: {user.user_id}")
                        print(f"Username: {user.username}")
                        print(f"First Name: {user.first_name}")
                        print(f"Last Name: {user.last_name}")
                        print(f"Email: {user.email}")
                        print(f"Created At: {user.created_at}")
                        print(f"Updated At: {user.updated_at}")
                    else:
                        print("No user found with the given ID.")

                case 3:  # Update existing user - BROKEN
                    curr_user_id = int(input("Enter user ID you wish to update"))
                    user = User.get_user_by_id(db, curr_user_id)
                    if not user:
                        print("No user found with the given ID.")
                        continue

                    print("\nUpdate User Information:")
                    new_username = input("Enter new username (or press Enter to skip):\t") or user.username
                    new_email = input("Enter new email (or press Enter to skip):\t") or user.email
                    new_password = input("Enter new password (or press Enter to skip):\t") or user.password

                    User.update_user(user.user_id, new_username, new_email, new_password)
                    print(f"User {user.user_id} updated successfully.")

                case 4:
                    user_id = int(input("Enter User ID"))
                    User.delete_user(db, user_id)
                    print(f"User with ID {user_id} has been deleted.")

                case 5:
                    print("Exiting the menu. Goodbye!")
                    break

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def budget_menu():
    print("Budget Menu:\nPlease select an option from 1-6:")
    while True:
        try:
            budget_choice = int(input("""
1. Create new budget
2. Update existing budget
3. Find existing budget
4. Exit

Your input: """))
            
            match budget_choice:
                case 1:  # create new budget
                    user_id = int(input("Enter user id: "))
                    total_budget = float(input("Enter total budget: "))
                    savings = float(input("Enter amount you wish to save: "))
                    spent_amount = float(input("Enter spent amount: "))
                    new_budget = Budget(db, user_id, total_budget, savings, spent_amount)
                    new_budget.create_budget()
                
                case 2:  # update existing budget
                    user_id = int(input("Enter user id: "))
                    new_total_budget = float(
                        input("Enter new budget total (or leave blank to skip): ") or None)
                    new_savings = float(
                        input("Enter new savings amount (or leave blank to skip): ") or None)
                    new_spent = float(
                        input("Enter new spent amount (or leave blank to skip): ") or None)
                    
                    budget = Budget.get_budget(db, user_id)
                    if budget:
                        budget.update_budget(user_id, new_total_budget, new_savings, new_spent)
                    else:
                        print("No budget found for this user.")
                
                case 3:  # find existing budget
                    user_id = int(input("Enter User ID: "))
                    budget = Budget.get_budget(db, user_id)
                    
                    if budget:
                        print("\nBudget Information:")
                        print(f"User ID: {budget.user_id}")
                        print(f"Total Budget: ${budget.total_budget:.2f}")
                        print(f"Savings: ${budget.savings:.2f}")
                        print(f"Spent Amount: ${budget.spent_amount:.2f}")
                        print(f"Remaining Amount: ${budget.remaining_amount:.2f}")
                    else:
                        print("No budget found for this user.")
                
                case 4:
                    print("Exiting the menu. Goodbye!")
                    break
                
                case _:
                    print("Invalid choice. Please try again.")
            
        except ValueError as ve:
            print(f"An error occurred: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def deposits_menu():
    print("Deposits Menu:\n Please an option from 1-3:")
    while True:
        try:
            print("""
Deposits Menu:
1. Add new deposit
2. Show all deposits
3. Delete deposit
4. Exit
            """)
            dep_choice = int(input("Please select an option: "))

            match dep_choice:
                case 1:
                    user_id = int(input("Enter user ID: "))
                    amount = float(input("Enter deposit amount: "))
                    description = input("Enter description of deposit (optional): ")
                    new_dep = Deposits(db, user_id, amount, description)
                    new_dep.add_deposit()

                case 2:
                    user_id = int(input("Enter user ID: "))
                    deposits = Deposits.get_deposits(db, user_id)
                    if deposits:
                        print("\nDeposits:")
                        for deposit in deposits:
                            print(
                                f"ID: {deposit['deposit_id']}, Amount: {deposit['amount']}, "
                                f"Description: {deposit['description']}"
                            )
                    else:
                        print("No deposits found for this user.")

                case 3:
                    deposit_id = int(input("Enter deposit ID to delete: "))
                    Deposits.delete_deposit(db, deposit_id)

                case 4:  # Exit
                    print("Exiting Deposits Menu.")
                    break

                case _:
                    print("Invalid option. Please select between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as error:
            print(f"An error occurred: {error}")

def expenses_menu():
    print("Expenses Menu:\n Please an option from 1-4:")
    while True:
        try:
            exp_choice = int(input(
                """
1. Add new Expense\n
2. Find expense by id\n
3. Find expenses by category\n
4. Exit
                """
            ))
            match exp_choice:
                case 1:#Add new Expense
                    amount = int(input("Enter deposit amount:\t"))
                    category_name = input("Description of deposit:\t")
                    notes = int(input("Enter notes:\t"))
                    new_exp = Expenses( amount, category_name, notes)
                    new_exp.add_expense()
                case 2:#Find expense by id
                    expense_id = int(input("Enter expense id:\t"))
                    Expenses.get_expense_by_id( db, expense_id)
                case 3:#Find expenses by category
                    category_name = int(input("Enter expense id:\t"))
                    Expenses.get_expenses_by_category(db, category_name)
                case 4:
                    print("Exiting the menu. Goodbye!")
                    break

            raise Exception("Input must be between 1 and 4.")

        except:
            continue
        
def categories_menu():
    """
    Displays a menu for managing categories and executes the selected option.
    """
    while True:
        try:
            print("""
Categories Menu:
1. Add new category
2. Show all categories
3. Update existing category
4. Delete category
5. Exit
            """)
            categories_choice = int(input("Please select an option: "))

            match categories_choice:
                case 1:
                    # Add a new category
                    name = input("Enter the name of the category: ")
                    description = input("Enter the description of the category (optional): ")

                    Categories.create_category(db, name, description)
                    print("Category added successfully!")

                case 2:
                    # Show all categories
                    categories = Categories.get_all_categories(db)
                    if categories:
                        print(f"\nYou have {len(categories)} category{'s' if len(categories) > 1 else ''}:")
                        for idx, category in enumerate(categories, 1):
                            print(f"{idx}. Name: {category.name}, Description: {category.description}")
                    else:
                        print("No categories found.")

                case 3:
                    # Update an existing category
                    categories = Categories.get_all_categories(db)
                    if not categories:
                        print("No categories found to update.")
                        continue

                    print("Select a category to update:")
                    for idx, category in enumerate(categories, 1):
                        print(f"{idx}. Name: {category.name}")

                    category_choice = int(input("Enter the number of the category to update: ")) - 1
                    if category_choice < 0 or category_choice >= len(categories):
                        print("Invalid choice. Please try again.")
                        continue

                    selected_category = categories[category_choice]
                    print(f"Updating category: {selected_category.name}")

                    new_name = input(f"Enter new name (current: {selected_category.name}): ") or selected_category.name
                    new_description = input(f"Enter new description (current: {selected_category.description}): ") or selected_category.description

                    Categories.update_category(db, selected_category.name, new_name, new_description)
                    print("Category updated successfully!")

                case 4:
                    # Delete a category
                    categories = Categories.get_all_categories(db)
                    if not categories:
                        print("No categories found to delete.")
                        continue

                    print("Select a category to delete:")
                    for idx, category in enumerate(categories, 1):
                        print(f"{idx}. Name: {category.name}")

                    category_choice = int(input("Enter the number of the category to delete: ")) - 1
                    if category_choice < 0 or category_choice >= len(categories):
                        print("Invalid choice. Please try again.")
                        continue

                    selected_category = categories[category_choice]
                    Categories.delete_category(db, selected_category.name)
                    print(f"Category '{selected_category.name}' deleted successfully!")

                case 5:
                    # Exit the menu
                    print("Exiting the menu. Goodbye!")
                    break

                case _:
                    print("Invalid option. Please select a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break  # Exit the loop on any unhandled exception

def saving_menu():
    print("Savings Goals Menu:\n Please select an option from 1-5:")
    while True:
        try:
            start_choice = int(input("""
Savings Goals Menu:
Please select an option:
1. Create a new savings goal
2. View all savings goals
3. Update a savings goal
4. Delete a savings goal
5. Exit
"""))

            match start_choice:
                case 1:
                    user_id = int(input("Enter your user ID: "))
                    goal_name = input("Enter the name of the savings goal: ")
                    target_amount = float(input("Enter the target amount: "))
                    current_amount = float(input("Enter the current amount saved: "))
                    due_date = input("Enter the due date (YYYY-MM-DD): ")

                    goal = Saving_Goals.get_goals(db, user_id)
                    if not goal:
                        goal = Saving_Goals(db, user_id, goal_name, target_amount, current_amount, due_date)
                        goal.create_goal()
                        print("Savings goal created successfully!")
                    else:
                        print("A savings goal with this name already exists.")

                case 2:
                    goals = Saving_Goals.get_goals(db, user_id)
                    if goals:
                        print(f"\nYou have {len(goals)} savings goal{'s' if len(goals) != 1 else ''}:")
                        for idx, goal in enumerate(goals, 1):
                            print(f"{idx}. Goal ID: {goal.goal_id}, Name: {goal.goal_name}, Target Amount: ${goal.target_amount:.2f}, Current Amount: ${goal.current_amount:.2f}, Due Date: {goal.due_date}")
                    else:
                        print("No savings goals found.")

                case 3:
                    user_id = int(input("Enter your user ID: "))
                    goals = Saving_Goals.get_goals(db, user_id)
                    if not goals:
                        print("No savings goals found to update.")
                        continue

                    print("Select a goal to update:")
                    for idx, goal in enumerate(goals, 1):
                        print(f"{idx}. Goal ID: {goal.goal_id}, Name: {goal.goal_name}")

                    goal_choice = int(input("Enter the number of the goal to update: ")) - 1
                    if goal_choice < 0 or goal_choice >= len(goals):
                        print("Invalid choice. Please try again.")
                        continue

                    selected_goal = goals[goal_choice]
                    print(f"Updating goal: {selected_goal.goal_name}")

                    new_goal_name = input(f"Enter new name (current: {selected_goal.goal_name}): ") or selected_goal.goal_name
                    new_target_amount = input(f"Enter new target amount (current: ${selected_goal.target_amount:.2f}): ") or selected_goal.target_amount
                    new_current_amount = input(f"Enter new current amount (current: ${selected_goal.current_amount:.2f}): ") or selected_goal.current_amount
                    new_due_date = input(f"Enter new due date (current: {selected_goal.due_date}): ") or selected_goal.due_date

                    updated_rows = Saving_Goals.update_goal(
                        db=db,
                        goal_id=selected_goal.goal_id,
                        new_goal_name=new_goal_name,
                        new_target_amount=float(new_target_amount) if new_target_amount else None,
                        new_current_amount=float(new_current_amount) if new_current_amount else None,
                        new_due_date=new_due_date if new_due_date else None
                    )

                    if updated_rows == 0:
                        print("No rows were updated. The operation may have failed.")
                    else:
                        print(f"Goal updated successfully! {updated_rows} row(s) affected.")

                case 4:
                    user_id = int(input("Enter your user ID: "))
                    goals = Saving_Goals.get_goals(db, user_id)
                    if not goals:
                        print("No savings goals found to delete.")
                        continue

                    print("Select a goal to delete:")
                    for idx, goal in enumerate(goals, 1):
                        print(f"{idx}. Goal ID: {goal.goal_id}, Name: {goal.goal_name}")

                    goal_choice = int(input("Enter the number of the goal to delete: ")) - 1
                    if goal_choice < 0 or goal_choice >= len(goals):
                        print("Invalid choice. Please try again.")
                        continue

                    selected_goal = goals[goal_choice]
                    deleted_rows = Saving_Goals.delete_goal(db, selected_goal.goal_id)
                    if deleted_rows == 0:
                        print("No rows were deleted. The operation may have failed.")
                    else:
                        print(f"Savings goal '{selected_goal.goal_name}' deleted successfully! {deleted_rows} row(s) affected.")

                case 5:
                    print("Exiting the menu. Goodbye!")
                    break

                case _:
                    print("Invalid option. Please select a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

def start_menu():
    print("Main_Menu:\n Please an option from 1-6:")
    while True:
        try:
            start_choice = int(input(
                """
1. User
2. Budget
3. Expense
4. Deposits
5. Categories
6. Savings Goals
7. Exit

Your input: """
            ))
            match start_choice:
                case 1:
                    user_menu()
                case 2:
                    budget_menu()
                case 3:
                    expenses_menu()
                case 4:
                    deposits_menu()
                case 5:
                    categories_menu()
                case 6:
                    saving_menu()
                case 7:
                    print("Exiting the menu. Goodbye!")
                    break
            raise Exception("Input must be between 1 and 7.")

        except:
            continue
        
start_menu()