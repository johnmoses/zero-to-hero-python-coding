"""
Custom Exception Classes

You can build exception hierarchies by subclassing Exception.
Catching a parent class also catches all its subclasses —
useful for grouping related errors under one handler.
"""
import sys

# Define a hierarchy: General is the parent, Specific1/2 are children
class General(Exception):
    """Base exception for this module."""

class Specific1(General):
    """Raised for the first specific error condition."""

class Specific2(General):
    """Raised for the second specific error condition."""


def raiser0():
    raise General("a general error occurred")

def raiser1():
    raise Specific1("specific error type 1")

def raiser2():
    raise Specific2("specific error type 2")


# Catching General also catches Specific1 and Specific2
for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:
        # sys.exc_info()[0] gives the exception class that was raised
        print(f"caught: {sys.exc_info()[0].__name__}")
