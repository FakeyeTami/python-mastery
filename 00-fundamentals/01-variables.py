""" Variables in Python
    Variables are used to stored data to be referenced and manipulated in a program.
    They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves.
    It is helpful to think of variables as containers that hold information. Their sole purpose is to label and store data in memory.
    This data can then be used throughout your program.
"""

# Examples of different variables in Python

word = "python"
number = 10
coefficient = 2.87
fruits = ["apple", "banana", "cherry"]
ordinals = {1: "first", 2: "second", 3: "third"}


class SomeCustomClass:
    pass


instance = SomeCustomClass()

""" Rules for naming variables in Python:
    1. Variable names can contain letters, numbers, and underscores.
    2. Variable names must start with a letter or an underscore.
    3. Variable names are case-sensitive (e.g., myVariable and myvariable are different variables).
"""

name = "John"  # Valid variable name
_name = "Doe"  # Valid variable name
yearOfBirth = 1990  # Valid variable name
is_student = True  # Valid variable name

1099_filed = False  # Invalid variable name (starts with a number)

""" Best Practices for Naming Variables in Python:
    1. Use descriptive names that convey the purpose of the variable.
    2. Use lowercase letters and underscores for variable names (e.g., my_variable).
    3. Avoid using reserved keywords as variable names (e.g., if, else, while).
"""

temprature = 25  # Good variable name
weight = 54.5  # Good variable name
message = "Hello, World!"  # Good variable name

t = 25 # Bad variable name (not descriptive)
temprature = 25 # Descriptive variable name (good practice)

""" Public vs Private Variables in Python:
    In Python, variables can be classified as public or private based on their naming conventions.
    - Public variables: These variables can be accessed from outside the class. They are defined without any special prefix.
    For example, `public_variable = 10`.
    - Private variables: These variables are intended to be accessed only within the class. They are defined with a single underscore prefix.
    For example, `_private_variable = 20`. However, it is important to note that this is just a convention and does not enforce
"""

_timeout = 30  # Private variable (convention)

def get_timeout():
    return _timeout  # Accessing private variable within the function

def set_timeout(seconds):
    global _timeout
    _timeout = seconds  # Modifying private variable within the function

""" Restricted and Keywords in Python
    These words are reserved by Python and cannot be used as variable names.
    They have special meanings and are part of the Python syntax.
    Some examples of keywords in Python include:
"""
[
    'False',
    'None',
    'True',
    'and',
    'as',
    'assert',
    'async',
    ...,
    'yield'
]
