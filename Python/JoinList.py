list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# Joining two lists using +

list3 = list1 + list2
print(list3)

# Joining two lists using extend()
li1 = ['x', 'y', 'z']
li2 = [7, 8, 9]

li1.extend(li2)
print(li1)

# Joining two lists using append() in a loop
l1 = ['p', 'q', 'r']
l2 = [100, 200, 300]
for x in l2:
    l1.append(x)
print(l1)