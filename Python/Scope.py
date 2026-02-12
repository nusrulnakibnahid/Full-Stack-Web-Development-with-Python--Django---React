#Local Scope
def newfunction():
    x = 20
    print(x)

newfunction()


#Global Scope
a = 10
b = 20

def myfunc():
    print(a,b)

myfunc()



#Global Keyword
c = 10
def myfun():
    global c
    c = 20
    print(c)
myfun()