import psycopg2
from DB.DB_config.DB_connnect import db_connect
from config import Config

connection = db_connect(Config.DB_NAME)

cursor = connection.cursor()

create_table_users_query = """CREATE TABLE users
user_id SERIAL PRIMARY KEY,
username VARCHAR(100) NOT NULL,
first_name varchar(100),
last_name varchar(100),
email VARCHAR(100) NOT NULL,
password VARCHAR(100) NOT NULL,
created_at timestamp DEFAULT CURRENT_TIMESTAMP,
updated_at timestamp DEFAULT CURRENT_TIMESTAMP,
is_active boolean DEFAULT true
"""