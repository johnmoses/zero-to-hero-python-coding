"""
python-dotenv

Loads variables from a .env file into os.environ at startup.
Install: pip install python-dotenv
"""
from dotenv import load_dotenv
import os


# Load .env from the current directory
load_dotenv()

db_url = os.getenv("DATABASE_URL")
secret = os.getenv("SECRET_KEY")
debug = os.getenv("DEBUG", "false").lower() == "true"

print(f"DB URL: {db_url}")
print(f"Secret: {secret}")
print(f"Debug: {debug}")
