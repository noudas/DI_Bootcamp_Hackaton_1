# DI_Bootcamp_Hackaton_1


**The budget management app provides users with a streamlined solution to track their finances by recording all expenses and deposits. Users can categorize transactions for easy analysis, helping them identify overspending and make informed budget adjustments. This intuitive tool empowers users to take control of their financial health.**

*Project Created for the Developer Institute Javascript / Python Fullstack course*

This project is a Python-based solution built with PostgreSQL as the database backend. It is organized into two main sections: the database (DB) folder and the Python folder.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Environment Setup](#environment-setup)
6. [Usage](#usage)

---

## Getting Started

To get started with this project, clone the repository:

```bash
git clone https://github.com/noudas/DI_Bootcamp_Hackaton_1/
```

---

## Requirements

Ensure you have the following installed on your system:

* Python 3.x
* PostgreSQL

## Installation

1. Navigate to the project directory:

```bash
cd DI_Bootcamp_Hackaton_1
```

2. Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

Required packages:

```bash
psycopg2==2.9.10
python-dotenv==1.0.1
```

3. Set up your PostgreSQL database using the .env configuration file.


# Project Structure
## DB Folder

The DB folder contains all the scripts necessary to set up and manage the database.

* DB_config

    - DB_connect.py: Handles database connection.
    - DB_create.py: Creates the database.

* DB_Insert_tests

    - DB_insert_helper.py: Helper functions for database inserts.
    - DB_inserts.py: Script for bulk inserts into the database.
    - test_insert_budget.py: Tests specific inserts into the Budget table
    - test_insert_categories.py: Tests specific inserts into the Categories table
    - test_insert_deposits.py: Tests specific inserts into the Deposits table
    - test_insert_expenses.py: Tests specific inserts into the Expebses table
    - test_insert_users.py: Tests specific inserts into the Users table

* DB_tables

    - DB_budget_table.py: Budget table schema.
    - DB_categories_table.py: Categories table schema.
    - DB_deposits_table.py: Deposits table schema.
    - DB_expenses_table.py: Expenses table schema.
    - DB_initializer.py: Initializes all database tables.
    - DB_user_table.py: User table schema.

* Additional files:

    - .env: Environment configuration file.
    - config.py: General configuration file.
    - tests.py: Contains test cases for the project.



## Python Folder
The Python folder contains the core application logic, class definitions, and configuration scripts.

* app_manager
    - manager.py: The main script to manage application workflows.

* Cls_Tests

    - test_categories.py: Unit tests for the cls_categories.py module.
    - test_user.py: Unit tests for the cls_user.py module.
    - test.py: Centralized test script to run all tests.

* Py_classes
    - __init__.py: Initializes the Python class package.
    - cls_budget.py: Defines the Budget class for budget-related operations.
    - cls_categories.py: Defines the Categories class to manage categories.
    - cls_DB_connect.py: Handles database connectivity for Python classes.
    - cls_deposits.py: Defines the Deposits class for deposit-related operations.
    - cls_expenses.py: Defines the Expenses class to manage expenses.
    - cls_user.py: Defines the User class to manage user data and operations.

* Py_config
    - Py_connect.py: Manages configuration settings for connecting to the database.

* Additional files:

    - .env: Environment configuration file.
    - config.py: General configuration file.
    - test.py: Contains tests for the Python modules.


## Environment Setup

Create a .env file in the project root directory with the following content:

```bash
DB_NAME_DEFAULT=postgres
DB_NAME=Hackaton_1
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
```

Replace yourpassword with the appropriate password for your PostgreSQL instance.

## Usage
To set up and test the project, follow these steps:

Run tests.py in the DB folder to create the database, tables, and test inserts:

```bash
python tests.py
```

Run manager.py in the Python folder to run the program:

```bash
python ./app_manager/manager.py
```

