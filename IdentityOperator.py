# Identity Operator Example

# Example 1: Lists (mutable objects)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)      # True (same content)
print(list1 is list2)      # False (different objects)
print(list1 is list3)      # True (same object reference)

# Example 2: Integers (immutable objects with caching)
a = 256
b = 256
c = 257
d = 257

print(a is b)              # True (Python caches small integers -5 to 256)
print(c is d)              # False (beyond cached range)

# Example 3: None comparison (recommended way)
value = None
print(value is None)       # True (correct usage)
print(value is not None)   # False

# Example 4: String interning
str1 = "hello"
str2 = "hello"
str3 = "".join(["hel", "lo"])

print(str1 is str2)        # True (string interning)
print(str1 is str3)        # False (dynamically created)