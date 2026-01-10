#for loop
a = ["apple", "banana", "cherry"]
for x in a:
    print(x)
print("-----")

#looping through the index numbers
a = ["apple", "banana", "cherry"]
for i in range(len(a)):
    print(a[i])

print("-----")

#while loop
a = ["apple", "banana", "cherry"]
i = 0
while i < len(a):
    print(a[i])
    i = i + 1
print("-----")

#list comprehension
a = ["apple", "banana", "cherry"]
[print(x) for x in a]
print("-----")
#looping using enumerate()
a = ["apple", "banana", "cherry"]
for index, value in enumerate(a):
    print(index, value)
print("-----")

#looping using list comprehension with condition
a = ["apple", "banana", "cherry", "kiwi", "mango"]
[print(x) for x in a if "a" in x]
print("-----")

#nested loops
a = ["red", "big", "tasty"]
b = ["apple", "banana", "cherry"]
for x in a:
    for y in b:
        print(x, y)
print("-----")

#looping using zip()
a = ["apple", "banana", "cherry"]
b = ["red", "yellow", "dark red"]
for x, y in zip(a, b):
    print(x, y)
print("-----")

#looping in reverse order
a = ["apple", "banana", "cherry"]
for x in reversed(a):
    print(x)
print("-----")

#looping with sorted()
a = ["banana", "cherry", "apple"]
for x in sorted(a):
    print(x)
print("-----")

#looping with custom sort
a = ["banana", "cherry", "apple"]
for x in sorted(a, key=lambda x: len(x)):
    print(x)
print("-----")

#infinite loop with break
i = 0
while True:
    print(i)
    i += 1
    if i >=10:
        break
print("-----")

#loop with continue
a = ["apple", "banana", "cherry", "kiwi", "mango"]
for x in a:
    if "a" not in x:
        continue
    print(x)
print("-----")

#range with step
for i in range(0, 10, 2):
    print(i)
print("-----")

#looping through a dictionary
a = {"name": "John", "age": 30, "city": "New York"}
for key, value in a.items():
    print(key, value)
print("-----")

#looping through a set
a = {"apple", "banana", "cherry"}
for x in a:
    print(x)