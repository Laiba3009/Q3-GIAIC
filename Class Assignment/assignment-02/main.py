# Python Operators with Examples

# 1. Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333
print(a % b)  # Modulus (Remainder): 1
print(a ** b) # Exponentiation (10^3 = 1000)
print(a // b) # Floor Division: 3

# 2. Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # 8

# 3. Comparison Operators
y = 10
z = 20
print(y == z)  # False
print(y != z)  # True
print(y > z)   # False
print(y < z)   # True
print(y >= 10) # True
print(z <= 20) # True

# 4. Logical Operators
p = True
q = False
print(p and q)  # False
print(p or q)   # True
print(not p)    # False

# 5. Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 is list3)   # True (same object)
print(list1 is list2)   # False (different objects, same values)
print(list1 == list2)   # True (same values)

# 6. Membership Operators
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)      # True
print(10 not in numbers) # True

# 7. Bitwise Operators
m = 10  # 1010 in binary
n = 6   # 0110 in binary
print(m & n)  # 2  (0010 - AND)
print(m | n)  # 14 (1110 - OR)
print(m ^ n)  # 12 (1100 - XOR)
print(~m)     # -11 (NOT)
print(m << 2) # 40 (Left Shift)
print(m >> 2) # 2  (Right Shift)
