# Comparison Operators in Python

# Equal to (==)
a = 10
b = 10
print(a == b)  # True

# Not equal to (!=)
x = 5
y = 8
print(x != y)  # True

# Greater than (>)
print(x > y)  # False
print(y > x)  # True

# Less than (<)
print(x < y)  # True
print(y < x)  # False

# Greater than or equal to (>=)
print(y >= 8)  # True
print(x >= y)  # False

# Less than or equal to (<=)
print(x <= y)  # True
print(y <= 5)  # False

# Comparison with strings
str1 = "apple"
str2 = "banana"
print(str1 == str2)  # False
print(str1 < str2)   # True (alphabetical order)

# Chained comparisons
num = 15
print(10 < num < 20)  # True
print(5 < num <= 15)  # True