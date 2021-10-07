def myfunc1():
    x1=60 # local variable
    myfunc2()
    print("welcome to func")
    print("the value of func1", x1)

def myfunc2():
    print("Thank you")
    print("the vlue of func2", x)

x=10 # global var
myfunc1()
myfunc2()

# local var has priority over global

