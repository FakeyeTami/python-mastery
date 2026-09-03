"""Data Types in Python
Python has several built-in data types that are used to define the kind of value a variable can hold.
Understanding these data types is crucial for effective programming in Python.
"""

# Examples of different data types in Python

# Integer
number = 10

# Float
coefficient = 2.87

# String
word = "python"

# Boolean
is_student = True

# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10, 20)

# Dictionary
ordinals = {1: "first", 2: "second", 3: "third"}

# Set
unique_numbers = {1, 2, 3, 4, 5}

""" Type Conversion in Python:
    Type conversion is the process of converting one data type to another.
    Python provides several built-in functions for type conversion.
"""

# Converting to integer
x = int("10")  # Converts string to integer

# Converting to float
y = float("2.87")  # Converts string to float

# Converting to string
z = str(10)  # Converts integer to string

""" Checking Data Types in Python:
    You can check the data type of a variable using the `type()` function.
"""

print(type(number))  # <class 'int'>
print(type(coefficient))  # <class 'float'>
print(type(word))  # <class 'str'>
print(type(is_student))  # <class 'bool'>

""" Dynamic Typing in Python:
    Python is a dynamically typed language, which means that you do not need to declare the data
    type of a variable explicitly. The interpreter infers the data type based on the value assigned to the variable.
    This allows for more flexibility in programming, but it also requires careful handling of variable types to
    avoid unexpected behavior.
"""
value = "A string"  # Initially a string
print(type(value))  # <class 'str'>

value = 42  # Now an integer
print(type(value))  # <class 'int'>

""" Variable Annotations in Python:
    Python 3.6 introduced variable annotations, which allow you to specify the expected data type
    of a variable. This can help with code readability and can be used by type checkers.
"""
name: str = "Alice"
age: int = 30
languages: list = ["Python", "JavaScript", "C++"]
weight: float = 65.5
favouriteColors: dict[str, str] = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF",
    "yellow": "#FFFF00",
}
