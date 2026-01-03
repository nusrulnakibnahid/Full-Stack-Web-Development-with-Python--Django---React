# Method 1: Tuple unpacking (EASIEST - Pythonic way)
a = 5
b = 10
a, b = b, a
print(f"a = {a}, b = {b}")  # Output: a = 10, b = 5


# Method 2: Using a temporary variable
x = 5
y = 10
temp = x
x = y
y = temp
print(f"x = {x}, y = {y}")  # Output: x = 10, y = 5


# Method 3: Using arithmetic (no extra variable, but less readable)
m = 5
n = 10
m = m + n
n = m - n
m = m - n
print(f"m = {m}, n = {n}")  # Output: m = 10, n = 5