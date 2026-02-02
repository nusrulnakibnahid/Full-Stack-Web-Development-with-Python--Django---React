MySet = {"apple", "banana", "cherry"}
print(MySet)
print(type(MySet))
print(len(MySet))


# Access Set Items
MySet = {"apple", "banana", "cherry"}
for i in MySet:
    print(i)

print ("apple" in MySet) # is apple present in the set (True or False)?




#Add Set Items
NewSet = {'a', 'b', 'c', 'd', 'e'}
NewSet.add('f') #not adding multiple items in same line
print(NewSet)



#Add Sets
Set1 = {'a', 'b', 'c'}
Set2 = {1, 2, 3}
Set1.update(Set2)
print(Set1) 




#Add Any Iterable
ThisSet = {'a', 'b', 'c'}
MyList = [1, 2, 3]
ThisSet.update(MyList)
print(ThisSet)



#Remove Item
MySet = {'a', 'b', 'c', 'd'}
MySet.remove('c')
print(MySet)


#using discard() method
num = {1,2,3,4,5}
num.discard(6)
print (num) # no error even if 6 is not present

#using pop() method
fruits = {'apple', 'banana', 'cherry'}
fruits.pop()
print(fruits)  # removes and returns an arbitrary item


#using clear() method
colors = {'red', 'green', 'blue'}
colors.clear()
print(colors)  # Output: set()



# Loop Sets
Set = {'a', 'b', 'c'}
for i in Set:
    print(i)




#Join Sets
SetA = {'a', 'b', 'c'}
SetB = {1, 2, 3}

SetC = SetA.union(SetB)
print(SetC)

#Join multiple sets with the union() method
Set1 = {'a', 'b', 'c'}
Set2 = {1, 2, 3}
Set3 = {True, False}
Set4 = {'X', 'Y', 'Z'}

Set5 = Set1.union(Set2, Set3, Set4)
print(Set5)


#Use | to join two sets

A = {'a', 'b', 'c'}
B = {1, 2, 3}

C = A|B
print(C)


#Intersection of Sets
SetX = {'a', 'b', 'c', 'd'}
SetY = {'c', 'd', 'e', 'f'}

SetZ = SetX.intersection(SetY)
print(SetZ)

# Difference (The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.)

numbers1 = {1, 2, 3, 4, 5}
numbers2 = {4, 5, 6, 7, 8, 1, 2, 5, 4, 9}

diff = numbers2.difference(numbers1)
print(diff)  # Output: {6, 7, 8, 9} 


# Symmetric Differences (The symmetric_difference() method will return a new set that will contain only the items that are not present in both sets.)
X = {'a', 'b', 'c', 'd'}
Y = {'c', 'd', 'e', 'f'}

Z = X.symmetric_difference(Y)
print(Z)





#frozenset
frozenSet = frozenset(['apple', 'banana', 'cherry'])
print(frozenSet)