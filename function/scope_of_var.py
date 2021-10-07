def func1():
    #x=60 # local var
    print("Welcome to function")
    print("value of x from func1", x)
    #func2() # calling func2 from func1
    
    return None

def func2():
    print("Thank You!")
    print("value of x from func2", x)
    #func1() Can't call func1from from2
    return None

def main(): # main func to call in your code
    global x # you can call x from any function now
    x=10
    func1() # calling func1 from main
    return None

main()

#x=2 # global var, means you canuse it inside anyfunc
#func1() # this is how we call func
#func2()


