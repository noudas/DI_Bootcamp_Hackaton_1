from Py_classes import *
from config import Config
import psycopg2
import os
import config

db = DB_Connect(db_name=Config.DB_NAME)

def user_menu():
    print("User Menu:\n Please an option from 1-4:")
    while True:
        try:
            start_choice=int(input(
                """
                    1. Create new user\n
                    2. Find user by ID\n
                    3. Update existing user\n
                    4. Delete existing user\n
                """
                                    ))
            match start_choice:
                case 1:
                    new_username=input("Username:\t")
                    new_first_name=input("First name:\t")
                    new_last_name=input("Last name:\t")
                    new_email=input("Email:\t")
                    new_user_password=input("Password:\t")
                    new_user=User(db, new_username, new_first_name, new_last_name, new_email, new_user_password)
                    new_user.create_user()
                case 2:
                    user_id = int(input("Enter User ID"))
                    User.get_user_by_id(db, user_id)
                case 3:
                    curr_user_id = int(input("Enter user ID you wish to update"))
                    new_username= input("Enter new username (or leave blank to skip):\t")
                    new_email= input("Enter new email (or leave blank to skip):\t")
                    new_user_password= input("Enter new password (or leave blank to skip):\t")
                    
                    User.update_user(curr_user_id, new_username=None, new_email=None, new_password=None)
                case 4:
                    user_id = int(input("Enter User ID"))
                    User.delete_user(db, user_id)
                    
              
            
            raise Exception("Input must be between 1 and 4.")
        
        except:
            continue
        
def budget_menu():
    print("Budget Menu:\n Please an option from 1-6:")
    while True: 
        try:
            start_choice = int(input(
                """
                    1. Start new budget\n
                    2. Update existing budget\n
                    3. Find existing budget\n
                """
                                    ))
            match start_choice:
                case 1:
                    user_id = int(input("Enter user id:\t"))
                    total_budget = int(input("Enter total budget:\t"))
                    savings = int(input("Enter amount you wish to save:\t"))
                    spent_amount = int(input("Enter spent amount:\t"))
                case 2:
                    user_id = int(input("Enter user id:\t"))
                    new_budget= int(input("Enter new budget total (or leave blank to skip):\t"))
                    new_savings= int(input("Enter new savings amount (or leave blank to skip):\t"))
                    new_spent= int(input("Enter new speant amount (or leave blank to skip):\t"))
                    Budget.update_budget( user_id, new_total_budget=None, new_savings=None, new_spent_amount=None)
                case 3:
                    user_id = int(input("Enter User ID"))
                    Budget.get_budget( db, user_id)
               
            raise Exception("Input must be between 1 and .")
        
        except:
            continue
def deposits_menu():
    print("Deposits Menu:\n Please an option from 1-3:")
    while True: 
        try:
            start_choice = int(input(
                """
                    1. Add new deposit\n
                    2. Show all deposits\n
                    3. Delete deposit\n
                """
                                    ))
            match start_choice:
                case 1:
                    pass
            # This block executes if value matches pattern1
                case 2:
                    pass
            # This block executes if value matches pattern2
                case 3:
                    pass
            # This block executes if value matches pattern3
               
            raise Exception("Input must be between 1 and 3.")
        
        except:
            continue


def expenses_menu():
    print("Expenses Menu:\n Please an option from 1-4:")
    while True: 
        try:
            start_choice = int(input(
                """
                    1. Add new Expense\n
                    2. Find expense by id\n
                    3. Find expenses by category\n
                """
                                    ))
            match start_choice:
                case 1:
                    pass
            # This block executes if value matches pattern1
                case 2:
                    pass
            # This block executes if value matches pattern2
                case 3:
                    pass
            # This block executes if value matches pattern3
         
            
            raise Exception("Input must be between 1 and 4.")
        
        except:
            continue
def categories_menu():
    print("Categories Menu:\n Please an option from 1-4:")
    while True: 
        try:
            categories_choice = int(input(
                """
                    1. Add new category \n
                    2. Show all categories\n
                    3. Update Existing category\n
                    4. Delete category\n
                """
                                    ))
            match categories_choice:
                case 1:
                    pass
            # This block executes if value matches pattern1
                case 2:
                    pass
            # This block executes if value matches pattern2
                case 3:
                    pass
            # This block executes if value matches pattern3
                case 4:
                    pass
            # This block executes if value matches pattern4
              
            
            raise Exception("Input must be between 1 and 4.")
        
        except:
            continue


def saving_menu():
    print("Deposits Menu:\n Please an option from 1-3:")
    while True: 
        try:
            start_choice = int(input(
                """
Savings Goals Menu:
Please select an option:
1. Create a new savings goal
2. View all savings goals
3. Update a savings goal
4. Delete a savings goal
5. Exit
                  
                """
                                    ))
            match start_choice:
                case 1:
                    user_id = int(input("Enter your user ID: "))
                    goal_name = input("Enter the name of the savings goal: ")
                    target_amount = float(input("Enter the target amount: "))
                    current_amount = float(input("Enter the current amount saved: "))
                    due_date = input("Enter the due date (YYYY-MM-DD): ")

                    goal = Saving_Goals(db, user_id, goal_name, target_amount, current_amount, due_date)
                    goal.create_goal()
                    print("Savings goal created successfully!")
                
                case 2:
                    user_id = int(input("Enter your user ID to view goals: "))
                    goals = Saving_Goals.get_goals(db, user_id)
                    if goals:
                        print(f"\nYou have {len(goals)} savings goal(s):")
                        for idx, goal in enumerate(goals, 1):
                            print(f"{idx}. {goal.goal_name} - Target: ${goal.target_amount}, "
                                  f"Saved: ${goal.current_amount}, Due: {goal.due_date}")
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
                        print(f"{idx}. {goal.goal_name}")
                    
                    goal_choice = int(input("Enter the number of the goal to update: ")) - 1
                    if goal_choice < 0 or goal_choice >= len(goals):
                        print("Invalid choice. Please try again.")
                        continue

                    selected_goal = goals[goal_choice]
                    print(f"Updating goal: {selected_goal.goal_name}")

                    new_goal_name = input(f"Enter new name (current: {selected_goal.goal_name}): ") or selected_goal.goal_name
                    new_target_amount = input(f"Enter new target amount (current: {selected_goal.target_amount}): ") or selected_goal.target_amount
                    new_current_amount = input(f"Enter new current amount (current: {selected_goal.current_amount}): ") or selected_goal.current_amount
                    new_due_date = input(f"Enter new due date (current: {selected_goal.due_date}): ") or selected_goal.due_date

                    selected_goal.update_goal(
                        goal_id=selected_goal.goal_id,
                        new_goal_name=new_goal_name,
                        new_target_amount=float(new_target_amount),
                        new_current_amount=float(new_current_amount),
                        new_due_date=new_due_date
                    )
                    print("Savings goal updated successfully!")
                
                case 4:
                    # Delete a savings goal
                    user_id = int(input("Enter your user ID: "))
                    goals = Saving_Goals.get_goals(db, user_id)
                    if not goals:
                        print("No savings goals found to delete.")
                        continue
                    
                    print("Select a goal to delete:")
                    for idx, goal in enumerate(goals, 1):
                        print(f"{idx}. {goal.goal_name}")
                    
                    goal_choice = int(input("Enter the number of the goal to delete: ")) - 1
                    if goal_choice < 0 or goal_choice >= len(goals):
                        print("Invalid choice. Please try again.")
                        continue

                    selected_goal = goals[goal_choice]
                    Saving_Goals.delete_goal(db, selected_goal.goal_id)
                    print(f"Savings goal '{selected_goal.goal_name}' deleted successfully!")

                case 5:
                    print("Exiting the menu. Goodbye!")
                    break

                case _:
                    print("Invalid option. Please select a number between 1 and 5.")


        except ValueError:
            print("Invalid input. Please enter a valid number.")

        except:
            continue

def start_menu():
    print("Main_Menu:\n Please an option from 1-6:")
    while True: 
        try:
            start_choice = int(input(
                """
                    1. User\n
                    2. Budget\n
                    3. Expense\n
                    4. Deposits\n
                    5. Categories\n
                    6. Savings Goals\n
                """
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
            
            raise Exception("Input must be between 1 and 6.")
        
        except:
            continue
        
