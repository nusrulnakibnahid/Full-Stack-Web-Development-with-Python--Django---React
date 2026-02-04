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

