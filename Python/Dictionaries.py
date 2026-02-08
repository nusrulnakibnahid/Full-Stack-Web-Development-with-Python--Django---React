MyName = {
    "name" : "nahid",
    "Age" : 24,
    "City" : "Dhaka",
}
print(MyName)
print(MyName["name"])
print(type(MyName))


# Another example (access an item)

StudentInfo = {

    "NewStudent" : {
    "name" : "nahid",
    "Age" : 24,
    "student ID" : 1054,
    "faculty" : "SWE"
    },

    "NewStudent2" : {
    "name" : "nakib",
    "Age" : 25,
    "student ID" : 978,
    "faculty" : "SWE"
    },

    "year" : 2024

}
print(StudentInfo ["NewStudent2"] ["Age"])


#Accessing Items
print(StudentInfo ["NewStudent"] ["faculty"])

print(StudentInfo.get("NewStudent")["name"]) # using get() method to access an item

print(StudentInfo.keys()) # to get all the keys in the dictionary


print(StudentInfo.values()) # to get all the values in the dictionary

print(StudentInfo.items()) # to get all the key-value pairs in the dictionary



#Check if Key Exists
if "NewStudent3" in StudentInfo:
    print("Yes, 'NewStudent' is a key in the StudentInfo dictionary.")






#Change Dictionary Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)


# using update() method to change value

thisdict2 =	{
  "brand": "BMW",
  "model": "MM",
  "year": 1964
}
print(thisdict2)
thisdict2.update({"year": 2025})
print(thisdict2)
print(thisdict2["year"])



#Add Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["color"] = "blue"
print(thisdict)



#Remove Items

Newdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
Newdict.pop("brand") # using pop() method to remove an item
print(Newdict)

# using popitem() method to remove the last inserted item
exampledict = {
    "brand": "BMW",
    "model" : "MM",
    "Year" : 2022
    
}
exampledict.popitem()
print(exampledict)



#using del keyword to remove an item
exampledict2  = {
    'name' : 'nahid',
    'id' : 1054,
    'faculty' : 'SWE'
}

del exampledict2['faculty']
print(exampledict2)

del exampledict2 # using del keyword to delete the entire dictionary
# print(exampledict2) # this will raise an error because the dictionary has been deleted


#using clear() method to empty the dictionary
exampledict3 = {
    'name' : 'nakib',
    'id' : 978,
    'faculty' : 'SWE'
}

exampledict3.clear()
print(exampledict3) # this will print an empty dictionary






# Loops in Dictionary
Student = {
    "name": "N",
    "Id" : 978,
    "faculty" : "SWE"
}

for i in Student:
    print(i)


# to print values in a dictionary
for i in Student.values():
    print(i)


# to print key-value pairs in a dictionary
for a in Student.keys():
    print(a)





# items method to loop through key-value pairs
CarBrand = {
    "num1" : "BMW",
    "num2" : "Audi",
    "num3" :"Ford",
    "num4" : "Toyota"
    
}

for x,y in CarBrand.items():
    print(x,y)








#Copy Dictionaries
OriginalDict = {
    "name" : "nahid",
    "Age" : 24,
    "City" : "Dhaka",
}

ExDict = OriginalDict.copy() # using copy() method to copy a dictionary
print(ExDict)

ExDict2 = dict(OriginalDict) # using dict() constructor to copy a dictionary
print(ExDict2)