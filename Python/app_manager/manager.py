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
                case 1:#Create new user
                    new_username=input("Username:\t")
                    new_first_name=input("First name:\t")
                    new_last_name=input("Last name:\t")
                    new_email=input("Email:\t")
                    new_user_password=input("Password:\t")
                    new_user=User(db, new_username, new_first_name, new_last_name, new_email, new_user_password)
                    new_user.create_user()
                case 2:#Find user by ID
                    user_id = int(input("Enter User ID"))
                    User.get_user_by_id(db, user_id)
                case 3:#Update existing user
                    curr_user_id = int(input("Enter user ID you wish to update"))
                    new_username= input("Enter new username (or leave blank to skip):\t")
                    new_email= input("Enter new email (or leave blank to skip):\t")
                    new_user_password= input("Enter new password (or leave blank to skip):\t")
                    User.update_user(curr_user_id, new_username=None, new_email=None, new_password=None)
                case 4:#Delete existing user
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
                    1. Create new budget\n
                    2. Update existing budget\n
                    3. Find existing budget\n
                """
                                    ))
            match start_choice:
                case 1:#create new budget
                    user_id = int(input("Enter user id:\t"))
                    total_budget = int(input("Enter total budget:\t"))
                    savings = int(input("Enter amount you wish to save:\t"))
                    spent_amount = int(input("Enter spent amount:\t"))
                    new_budget=Budget(db, user_id, total_budget, savings, spent_amount)
                    new_budget.create_budget()
                case 2:# Update existing budget
                    user_id = int(input("Enter user id:\t"))
                    new_budget= int(input("Enter new budget total (or leave blank to skip):\t"))
                    new_savings= int(input("Enter new savings amount (or leave blank to skip):\t"))
                    new_spent= int(input("Enter new speant amount (or leave blank to skip):\t"))
                    Budget.update_budget( user_id, new_total_budget=None, new_savings=None, new_spent_amount=None)
                case 3:#Find existing budget
                    user_id = int(input("Enter User ID"))
                    Budget.get_budget( db, user_id)
               
            raise Exception("Input must be between 1 and 3")
        
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
                case 1:#Add new deposit
                    user_id = int(input("Enter user id:\t"))
                    amount = int(input("Enter deposit amount:\t"))
                    description = input("Description of deposit:\t")
                    new_dep= Deposits(user_id, amount, description)
                    new_dep.add_deposit()
            
                case 2:#Show all deposits
                    user_id = int(input("Enter user id:\t"))
                    Deposits.get_deposits( db: DB_Connect,user_id)
            
                case 3:#Delete deposit
                    deposit_id = int(input("Enter deposit id:\t"))
                    Deposits.delete_deposit(, db: DB_Connect, deposit_id)
               
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
                    1. User\n
                    2. Budget\n
                    3. Expense\n
                  
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
                case 5:
                    pass
            # This block executes if value matches pattern5
                case 6:
                    pass
            # This block executes if value matches pattern6
            
            raise Exception("Input must be between 1 and 6.")
        
        except:
            continue
        





