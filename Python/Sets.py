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