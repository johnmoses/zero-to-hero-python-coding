# Files

Data is usually stored in different file formats(.txt, .json, .xml, .csv, .tsv, .excel).

Handling these files involves creating, reading, updating or deleting as required. Below are some of the notations:

- "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
- "a" - Append - Opens a file for appending, creates the file if it does not exist
- "w" - Write - Opens a file for writing, creates the file if it does not exist
- "x" - Create - Creates the specified file, returns an error if the file exists
- "t" - Text - Default value. Text mode
- "b" - Binary - Binary mode (e.g. images)

## Data types and objects

Objects are Python's abstraction for data — variables and constants stored in memory for processing. All objects have identity, type, and value.

### Built-in data types

| Category | Types |
|----------|-------|
| Text | str |
| Numeric | int, float, complex |
| Sequence | list, tuple, range |
| Mapping | dict |
| Set | set, frozenset |
| Boolean | bool |
| Binary | bytes, bytearray, memoryview |
| None | NoneType |

### Dynamic typing

Python variables can change type at runtime:

```py
a = 10          # int
a = 'ABC'       # now str
print(type(a))  # <class 'str'>
```

## JSON

JSON (JavaScript Object Notation) is a lightweight data interchange format. Python's `json` module handles serialization and deserialization:

```py
import json

# Python dict → JSON string
data = {"name": "Joy", "age": 40}
json_str = json.dumps(data)

# JSON string → Python dict
parsed = json.loads(json_str)
print(parsed["age"])  # 40
```
