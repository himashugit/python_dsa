'''
def addition(a,b):
    result = a+b
    return result # this value we're sending back to main func to print
    

def main():
    a = eval(input("Enter your number: "))
    b = eval(input("Enter your 2ndnumber: "))
    result = addition(a,b) # calling addition func & argument value and storing in result
    print(f' "the addition of {a} and {b} is {result}"')

main() # calling main func

'''

def multiply_num_10(value):
    #result = value*10
    #return result
    return value*10

def main():
    num=eval(input("Enter a number:"))
    result=multiply_num_10(num)
    print("The value is: ", result)

main()