"""Operators
These are special symbols that perform operations on variables and values. Python has a variety of operators, including:
- Arithmetic Operators: Used for mathematical operations like addition, subtraction, multiplication, etc.
- Assignment Operators: Used to assign values to variables.
- Comparison Operators: Used to compare values and return a boolean result (True or False).
- Logical Operators: Used to combine conditional statements.
- Identity Operators: Used to compare the memory locations of two objects.
- Bitwise Operators: Used to perform bit-level operations on integers.
- Membership Operators: Used to test if a value is in a sequence (like a list
or a string).
"""

# Arithmetic Operators
a = 10
b = 3
sum = a + b  # Addition
difference = a - b  # Subtraction
product = a * b  # Multiplication
quotient = a / b  # Division
floor_division = a // b  # Floor Division
modulus = a % b  # Modulus
exponentiation = a**b  # Exponentiation
print("Arithmetic Operators:")
print(
    f"Sum: {sum}, Difference: {difference}, Product: {product}, Quotient: {quotient}, Floor Division: {floor_division}, Modulus: {modulus}, Exponentiation: {exponentiation}"
)

# Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3 = 8
x -= 2  # Equivalent to x = x - 2 = 6
x *= 4  # Equivalent to x = x * 4 = 24
x /= 2  # Equivalent to x = x / 2 = 12.0
print("\nAssignment Operators:")
print(f"x after operations: {x}")

# Comparison Operators
p = 10
q = 20
is_equal = p == q  # False
is_not_equal = p != q  # True
is_greater = p > q  # False
is_less = p < q  # True
is_greater_equal = p >= q  # False
is_less_equal = p <= q  # True
print("\nComparison Operators:")
print(
    f"Is Equal: {is_equal}, Is Not Equal: {is_not_equal}, Is Greater: {is_greater}, Is Less: {is_less}, Is Greater or Equal: {is_greater_equal}, Is Less or Equal: {is_less_equal}"
)

# Logical Operators
x = True
y = False
logical_and = x and y  # False
logical_or = x or y  # True
logical_not = not x  # False
print("\nLogical Operators:")
print(
    f"Logical AND: {logical_and}, Logical OR: {logical_or}, Logical NOT : {logical_not}"
)

# Identity Operators
a = [1, 2, 3]
b = a  # b references the same list as a
c = [1, 2, 3]  # c is a different list with the same content
is_same = a is b  # True
is_not_same = a is not c  # True
print("\nIdentity Operators:")
print(f"Is Same: {is_same}, Is Not Same: {is_not_same}")

# Bitwise Operators
x = 5  # Binary: 0101
y = 3  # Binary: 0011
bitwise_and = x & y  # Binary: 0001 (Decimal: 1)
bitwise_or = x | y  # Binary: 0111 (Decimal: 7)
bitwise_xor = x ^ y  # Binary: 0110 (Decimal: 6)
bitwise_not = ~x  # Binary: 1010 (Decimal: -6)
left_shift = x << 1  # Binary: 1010 (Decimal: 10)
right_shift = x >> 1  # Binary: 0010 (Decimal: 2)
print("\nBitwise Operators:")
print(
    f"Bitwise AND: {bitwise_and}, Bitwise OR: {bitwise_or}, Bitwise XOR: {bitwise_xor}, Bitwise NOT: {bitwise_not}, Left Shift: {left_shift}, Right Shift: {right_shift}"
)
