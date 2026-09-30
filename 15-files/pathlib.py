"""
pathlib

Modern alternative to os.path. Paths are objects with methods,
not strings you concatenate manually.
"""
from pathlib import Path


# Current directory
cwd = Path.cwd()
print("CWD:", cwd)

# Build paths safely (works on Windows and Unix)
data_dir = Path("data")
file_path = data_dir / "output.txt"
print("Path:", file_path)

# Check existence
print("Exists:", file_path.exists())

# Create directory
data_dir.mkdir(exist_ok=True)

# Write and read
file_path.write_text("Hello from pathlib")
print("Content:", file_path.read_text())

# File metadata
print("Name:", file_path.name)       # output.txt
print("Stem:", file_path.stem)       # output
print("Suffix:", file_path.suffix)   # .txt
print("Parent:", file_path.parent)   # data

# List all .txt files in a directory
for f in Path(".").glob("*.py"):
    print(f)

# Cleanup
file_path.unlink()
data_dir.rmdir()
