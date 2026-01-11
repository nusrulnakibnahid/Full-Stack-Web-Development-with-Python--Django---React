#Normally used this method
num = [1, 2, 3, 4, 5]
for i in num:
    print(i * 2)

# Traditional way using a loop
numbers = []
for i in range(1, 6):
    numbers.append(i * 2)
print(numbers)  # Output: [2, 4, 6, 8, 10]

# Using list comprehension (same result, cleaner syntax)
numbers = [i * 2 for i in range(1, 6)]
print(numbers)  # Output: [2, 4, 6, 8, 10]

# List comprehension with a condition
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Converting strings to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(uppercase_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY']