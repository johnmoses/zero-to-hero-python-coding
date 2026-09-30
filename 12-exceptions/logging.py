"""
Logging

Use logging instead of print() in real applications.
Gives you levels, timestamps, file output, and easy on/off switching.
"""
import logging


# Basic config — outputs to console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logging.debug("Debug: detailed diagnostic info")
logging.info("Info: general flow of the program")
logging.warning("Warning: something unexpected but not breaking")
logging.error("Error: something failed")
logging.critical("Critical: program may not recover")


# Log to a file
logging.basicConfig(
    filename="app.log",
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s",
    force=True,
)

def divide(a, b):
    if b == 0:
        logging.error("Division by zero attempted: a=%s, b=%s", a, b)
        return None
    result = a / b
    logging.info("divide(%s, %s) = %s", a, b, result)
    return result

print(divide(10, 2))
print(divide(10, 0))
