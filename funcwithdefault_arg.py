'''
def display(a=3): #a=3 is the default arg value we set here
    print("The value of a is" , a)

display()
'''

'''
def add_num(a,b):
    result=a+b
    print("The sum is", result)
add_num(5,6)
'''


def working_server(user="root"):
    print(f' "Working with {user}"')

working_server("web")