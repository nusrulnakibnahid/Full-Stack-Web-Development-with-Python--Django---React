# Simple way to copy a list in Python

# Original list
original_list = [1, 2, 3, 4, 5]

# Copy the list
copied_list = list(original_list)

# Show the copy works
print("Original:", original_list)
print("Copy:", copied_list)

# Change the copy
copied_list.append(6)

print("After change:")
print("Original:", original_list)
print("Copy:", copied_list)



#Another example
num = [10, 20, 30, 40,  60]
copy = list(num)

print(copy)
