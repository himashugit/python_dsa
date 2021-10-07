'''
def display(*arg):
    print(arg)
    print(type(arg))
    #type here is tuple and you can take any number of arg value here.

display(4,5,6,7)

'''
def display(*arg):
    for each in arg:
        print(type(each))
    
display(4,4.5,"hi")
# this willl take each var length arg as str,int,float....