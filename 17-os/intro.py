"""
OS Module

The os module lets Python interact with the operating system:
filesystem, environment variables, paths, and processes.
"""
import os

# Current working directory — where Python is running from
cwd = os.getcwd()
print("CWD:", cwd)

# List files and folders in a directory
entries = os.listdir(".")
print("Entries:", entries[:5])   # first 5 to keep output short

# Build paths safely (works on Windows and Unix)
path = os.path.join(cwd, "data", "file.txt")
print("Path:", path)

# Check if a path exists
print("Exists:", os.path.exists(path))
print("Is file:", os.path.isfile(path))
print("Is dir:", os.path.isdir(cwd))

# Read an environment variable
home = os.environ.get("HOME", "not set")
print("HOME:", home)

# Create and remove a directory
os.makedirs("tmp_demo", exist_ok=True)
print("Created tmp_demo")
os.rmdir("tmp_demo")
print("Removed tmp_demo")