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


#Access Tuple Items
thistuple = ("apple", "banana", "cherry", "mango")
print(thistuple[1])  
print(thistuple[-1])
print(thistuple[0:2])
print(thistuple[-3:-1])
print(thistuple[:2])

#Update Tuples 
thistuple = ("apple", "banana", "cherry", "mango", "kiwi", "pineapple")
a = list(thistuple)
print(a)

a.append("watermelon")
thistuple = tuple(a)
print(thistuple)


#Unpack Tuple 
fruits = ("apple", "banana", "cherry")
(a, b, c) = fruits
print(a)
print(c)


#Unpack Tuple (Using Asterisk*)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry", "blueberry", "blackberry")

(*green, yellow, red) = fruits


print(green)
print(yellow)
print(red)


#loop Truple
thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)


#Loop Through the Index Numbers
thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
    print(thistuple[i])


#Using a While Loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i+1



#Join Tuples

#join two tuples
tuple1 = ('a', 'b', 'c')
tuple2 = (1,2,3)

tuple3 = tuple1+tuple2
print(tuple3)


#Multiply Tuples
fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2
print (mytuple)

# example 2 for #Multiply Tuples
nums = (1, 2, 3)
mytuple = nums * 3
print(mytuple)

# Delete Tuple
thistuple = ("apple", "banana", "cherry")
del thistuple


#Tuple count() Method
thistuple = (1, 2, 2, 2, 2, 4, 5)
a = thistuple.count(2)
print(a)


#Tuple index() Method
thistuple = (1, 2, 3, 4, 5, 2)
b = thistuple.index(3)
print(b)