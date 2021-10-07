'''

def greet():
    print("Hello geeti")
    print("How're you?")
    print("what're you making today")

greet()

'''
# func with one parameter 
def greet_with_name(givename):  # this is a parameter
    print(f"Hello, {givename}" )
    print(f"How're you?, {givename}" )
    print("what're you making today")

greet_with_name('geeti') # this is argument

# func with positional kwarg
def greet(name="himanshu", loc="canada"):   
    print(f"my name is {name}")
    print(f"I'm from {loc}")

greet()