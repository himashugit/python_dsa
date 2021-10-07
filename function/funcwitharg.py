'''
def display(*arg): # this is the argument with no fix value. This can  take zero or more value
    for each in arg: # as arg value is in tuple we can use the for loop for all the values we're taking here....
        print(type(each))

    #print(arg)
    return None

display()
display(2,3)
display('test')
'''

def display(**kwarg): # this is the keyword based argument syntax to assign value when calling this func
    print(kwarg)
    return None

display(a=2,b="hi") # here we're providing diffrernt value to each var/para







