def addition(a,b):
    print(f'the sum of {a} and {b} is {a+b}')
    return None

def sub(a,b):
    print(f'the sub of {a} and {b} is {a-b}')

def multi(a,b):
    print(f'multi of {a} and {b} is {a*b}')

def main():
    x=3
    y=4
    sub(x,y)
    addition(x,y)
    multi(x,y)
if __name__ == '__main__': # this is inbuilt var value inside python
    main()