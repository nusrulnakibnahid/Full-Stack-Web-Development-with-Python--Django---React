# Constructor

class parentInfo:
    def NahidFamily(self,name,age):

        print(f"my name is {name} and my age is {age}")
p1 = parentInfo()
p1.NahidFamily("Nahid", 25)  
p1.NahidFamily("Nakib", 30)


# Parameterized Constructor
class StudentInfo:
    def __init__(self,name,num):
        
        print(f"My name is {name} and my id number is {num}")

        s1 = StudentInfo("Nahid","1054")

