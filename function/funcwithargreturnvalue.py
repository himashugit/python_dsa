'''
def add_num(a,b):
    result=a+b
    return result # here we're returning the value in result and result on the main func has addition...

def main():
    a=eval(input("Enter your first num : "))
    b=eval(input("Enter your sec num : "))
    result=add_num(a,b)
    print(f'addition of your number is {result}')

main()
'''

    
def multiply_num(c,d):
    result1=c*d
    
    return result1

def main():
    a=eval(input("Enter your num1: "))
    b=eval(input("Enter your num2: "))

    result1=multiply_num(a,b)
    print("multiplication of these two number", result1)

main()
#multiply_num(3,4)
