def get_add(a,b): # parameter or positional arg
    aresult=a+b
    print(f' the addition of {a} {b} is {aresult}' )

def get_sub(a,b):
    sresult=a-b
    print(f' the sub of {a} {b} is {sresult}')

def main():
    a=eval(input("Enter your first number: "))
    b=eval(input("Enter your second number:"))
    get_add(a,b)
    #get_sub(a,b)
    get_add(1,2)

main()