""" Strings
    They are sequences of characters enclosed in either single quotes (' ') or double quotes (" ").
    Strings can also be defined using triple quotes (''' ''' or """ """) for multi-line
    strings. Strings are immutable, meaning that once they are created, their values cannot be changed.
    Python provides a variety of string methods and operations to manipulate and work with strings effectively.
"""

# String Creation
single_quoted_string = "Hello, World!"
double_quoted_string = "Python is awesome!"
multi_line_string = """This is a multi-line string.
                    It can span multiple lines."""

# String Concatenation
concatenated_string = single_quoted_string + " " + double_quoted_string
print("Concatenated String:", concatenated_string)

# String Repetition
repeated_string = single_quoted_string * 3
print("Repeated String:", repeated_string)

# String Indexing
first_character = single_quoted_string[0]  # 'H'
last_character = single_quoted_string[-1]  # '!'
print("First Character:", first_character)
print("Last Character:", last_character)

# String Slicing
substring = single_quoted_string[0:5]  # 'Hello'
print("Substring:", substring)

# String Methods
upper_case_string = single_quoted_string.upper()  # 'HELLO, WORLD!'
lower_case_string = single_quoted_string.lower()  # 'hello, world!'
stripped_string = "   Hello, World!   ".strip()  # 'Hello, World!'
replaced_string = single_quoted_string.replace("World", "Python")  # 'Hello, Python!'
split_string = single_quoted_string.split(",")  # ['Hello', ' World!']
print("Upper Case String:", upper_case_string)
print("Lower Case String:", lower_case_string)
print("Stripped String:", stripped_string)
print("Replaced String:", replaced_string)
print("Split String:", split_string)
