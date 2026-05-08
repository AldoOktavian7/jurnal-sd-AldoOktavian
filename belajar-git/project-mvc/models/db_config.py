import os
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv("DB_PASSWORD")

print("Database Password:", db_password)