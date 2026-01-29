newTuple = (1, 2, 3, "a", "b", "c")

print(newTuple[-2])


#Allow Duplicates 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple.count("apple")) #counts how many times apple occurs in the tuple


#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Nested Tuple
nestedTuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(nestedTuple[1][1])
print (nestedTuple[2][0])


#Data Types
mixedTuple = (1, "Hello", 3.4)
print(type(mixedTuple))

#Range of Indexes
rangedTuple = ("a", "b", "c", "d", "e", "f", "g")
print(rangedTuple[2:5])
