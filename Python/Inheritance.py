class Baba:
    car = "BMW"
    taka = "100 cr"
    home = "10th floor"


class kaka(Baba):
    Brokenphone =  ""
    BrokenHome = ""



k = kaka()
print(k.car)



#Multiple Inheritance
class Father:
    car = "BMW"
    taka = "100 cr"
    home = "10th floor"

class Father2:
    bike = "Yamaha"
    money = "50 cr"
    home = "5th floor"

class Father3:
    boat = "Yacht"
    cash = "200 cr"
    home = "20th floor"


class father4:
    land = "1000 acre"
    cash = "500 cr"
    home = "15th floor"


class Uncle(Father, Father2, Father3, father4):
    pass

U = Uncle()
print(U.land)
print(U.home)
print(U.bike)




#Multilevel Inheritance
class baba:
    car = "BMW"
    taka = "100 cr"
    home = "10th floor"

class son1(baba):
    home = "5th floor"
    phone = "iPhone"

class son2(son1):
    home = "20th floor"
    bike = "Honda"

class son3(son2):
    area = "10 ac"
    laptop = "ASUS"


class son4(son3):
    tab = ""
    cycle = ""


S = son4()
print(S.laptop)
print(S.car)






# Hybrid Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()




    
