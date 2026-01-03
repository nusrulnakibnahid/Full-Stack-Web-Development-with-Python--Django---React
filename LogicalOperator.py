# Logical Operators in Python

# 1. AND operator - returns True if both conditions are True
age = 25
income = 50000

if age > 18 and income > 30000:
    print("You are eligible for a loan")
else:
    print("You are not eligible")


# 2. OR operator - returns True if at least one condition is True
student_status = True
senior_citizen = False

if student_status or senior_citizen:
    print("You get a discount")
else:
    print("No discount available")


# 3. NOT operator - reverses the boolean value
is_raining = True

if not is_raining:
    print("Let's go outside")
else:
    print("Stay indoors")


# Combining multiple operators
x = 10
y = 20
z = 30

if (x < y and y < z) or (x == 10):
    print("Condition is True")


# Truth table examples
print("\n--- AND Operator ---")
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

print("\n--- OR Operator ---")
print(True or False)    # True
print(False or False)   # False

print("\n--- NOT Operator ---")
print(not True)         # False
print(not False)        # True