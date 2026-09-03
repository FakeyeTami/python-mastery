"""Conditionals
Conditionals are used to make decisions in the code based on certain conditions.
The main conditional statements in Python are if, elif, and else.
- if: Used to execute a block of code if a specified condition is true.
- elif: Used to check multiple conditions after the initial if statement.
- else: Used to execute a block of code if none of the previous conditions are true
Python also supports nested conditionals, where you can have an if statement inside another if statement.
"""

# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is less than or equal to 5")

# Grouping Statements
# You can group multiple statements together using indentation. All statements within the same block should have the same level of indentation.
if x > 5:
    print("x is greater than 5")
    print("This is part of the same block")
else:
    print("x is not greater than 5")
    print("This is part of the else block")

# Conditonal Expressions (Ternary Operator)
# Python supports conditional expressions, also known as the ternary operator, which allows you to write
result = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(result)

# The pass Statement
# The pass statement is a null operation; it is used as a placeholder in situations where a
pass
