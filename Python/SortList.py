# Sorting Lists in Python

# Example 1: Sorting a list of numbers in ascending order using sort() method
numbers = [5, 2, 9, 1, 5, 6]
print("Original list:", numbers)
numbers.sort()
print("Sorted list (ascending):", numbers)

# Example 2: Sorting a list of numbers in descending order
numbers = [5, 2, 9, 1, 5, 6]
print("\nOriginal list:", numbers)
numbers.sort(reverse=True)
print("Sorted list (descending):", numbers)

# Example 3: Using sorted() function to create a new sorted list without modifying the original
numbers = [5, 2, 9, 1, 5, 6]
print("\nOriginal list:", numbers)
sorted_numbers = sorted(numbers)
print("New sorted list (ascending):", sorted_numbers)
print("Original list remains unchanged:", numbers)

# Example 4: Sorting a list of strings
fruits = ["banana", "apple", "cherry", "date"]
print("\nOriginal fruits list:", fruits)
fruits.sort()
print("Sorted fruits list (alphabetical):", fruits)

# Example 5: Sorting strings in descending order
fruits = ["banana", "apple", "cherry", "date"]
print("\nOriginal fruits list:", fruits)
fruits.sort(reverse=True)
print("Sorted fruits list (reverse alphabetical):", fruits)
