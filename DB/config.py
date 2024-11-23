from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Create a Configuration Class to be called in other pages

class Config:
    # Access environment variables
    DB_NAME_DEFAULT = os.getenv("DB_NAME_DEFAULT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
