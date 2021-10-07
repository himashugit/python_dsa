'''
def get_result(value): # Parameters/positional argumnets
    result=value+2 # adding 2 in the result var vlaue
    print(f' your number is {result}')
    return None

def main():
  #global value
  num=eval(input("Enter your number: "))
  get_result(num) # Arguments, calling get_result func in the main
  return None 

main()

'''
def get_add(a,b):
    aresult=a+b
    print(f' addition of {a} and {b} is: {aresult}')
    return None
def get_sub(c,d):
    cresult=c-d
    print(f' sub of {c} and {d} is: {cresult}')

def main():
    a=eval(input("Enter your fiest number"))
    b=eval(input("Enter your secondn num"))
    get_add(a,b)
   # get_sub(a,b)
    get_sub(10,5) # you can use both the ways to get values
    return None

main()


