# Type Casting in Python - Converting one data type to another

# 1. Converting to Integer (int)
print("=== Converting to Integer ===")
x = int("10")  # String to int
print(f"int('10') = {x}, type: {type(x)}")

y = int(3.14)  # Float to int (truncates decimal)
print(f"int(3.14) = {y}, type: {type(y)}")

z = int(True)  # Boolean to int
print(f"int(True) = {z}, type: {type(z)}")

# 2. Converting to Float (float)
print("\n=== Converting to Float ===")
a = float("3.14")  # String to float
print(f"float('3.14') = {a}, type: {type(a)}")

b = float(5)  # Integer to float
print(f"float(5) = {b}, type: {type(b)}")

c = float(True)  # Boolean to float
print(f"float(True) = {c}, type: {type(c)}")

# 3. Converting to String (str)
print("\n=== Converting to String ===")
d = str(42)  # Integer to string
print(f"str(42) = '{d}', type: {type(d)}")

e = str(3.14)  # Float to string
print(f"str(3.14) = '{e}', type: {type(e)}")

f = str(True)  # Boolean to string
print(f"str(True) = '{f}', type: {type(f)}")

# 4. Converting to Boolean (bool)
print("\n=== Converting to Boolean ===")
g = bool(1)  # Integer to boolean
print(f"bool(1) = {g}, type: {type(g)}")

h = bool(0)  # Zero is False
print(f"bool(0) = {h}, type: {type(h)}")

i = bool("Hello")  # Non-empty string is True
print(f"bool('Hello') = {i}, type: {type(i)}")

j = bool("")  # Empty string is False
print(f"bool('') = {j}, type: {type(j)}")

# 5. Practical Example
print("\n=== Practical Example ===")
user_age = input("Enter your age: ")  # Input is always a string
age_int = int(user_age)  # Convert to integer
age_float = float(age_int)  # Convert to float
print(f"String: {user_age} | Int: {age_int} | Float: {age_float}")