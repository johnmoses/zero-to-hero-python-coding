"""
Environment Variables with os.environ

Read config from the environment — never hardcode secrets.
"""
import os


# Read with a fallback default
db_url = os.environ.get("DATABASE_URL", "sqlite:///local.db")
debug = os.environ.get("DEBUG", "false").lower() == "true"
port = int(os.environ.get("PORT", 8000))

print(f"Database: {db_url}")
print(f"Debug mode: {debug}")
print(f"Port: {port}")


# Validate required variables at startup — fail fast with a clear message
def require_env(key: str) -> str:
    value = os.environ.get(key)
    if not value:
        raise EnvironmentError(f"Required environment variable '{key}' is not set")
    return value


try:
    secret = require_env("SECRET_KEY")
except EnvironmentError as e:
    print(f"Config error: {e}")
