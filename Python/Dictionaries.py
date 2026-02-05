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
