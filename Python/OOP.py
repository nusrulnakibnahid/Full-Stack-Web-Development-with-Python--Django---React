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




# New Example 
# Instance methods
class Method:
    def InstanceMethod(self):
        print("This is an instance method")

# Class methods
    @classmethod
    def ClassMethod(cls):
        print("This is a class method")

# Static methods
    @staticmethod
    def StaticMethod():
        print("This is a static method")

M1 = Method()
M1.InstanceMethod()
M1.ClassMethod()
Method.StaticMethod()



# Abstraction 
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# a = Animal()  # TypeError: Can't instantiate abstract class
d = Dog()
d.sound()
c = Cat()
c.sound()


# Polymorphism
class Vahicle:
    def __init__(self,Model,Brand,component):
        self.Model = Model
        self.Brand = Brand
        self.component = component

class plane(Vahicle):
    pass


p1 = plane("Boeing 747", "Boeing", "Engine")
print(p1.Model)
print(p1.Brand)


class Car(Vahicle):
    pass

c1 = Car("Model S", "Tesla", "Battery")
print(c1.Brand)