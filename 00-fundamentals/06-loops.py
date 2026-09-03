"""Loops in Python
Loops are used to execute a block of code repeatedly as long as a specified condition is true. Python provides two main types of loops: for loops and while loops.
- for loop: Used to iterate over a sequence (like a list, tuple, or string
) and execute a block of code for each item in the sequence.
- while loop: Used to execute a block of code as long as a specified condition is true. The loop will continue until the condition becomes false.
Python also provides control statements like break and continue to manage the flow of loops. The break statement is used to exit a loop prematurely,
while the continue statement is used to skip the current iteration and move to the next one.
"""

# For Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
