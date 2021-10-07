my_Dict={'name':'himan', 'profession':'IT', 1:'one'}
print(my_Dict['name'])
print(my_Dict.get('profession'))
print(my_Dict.get('work')) # this wiill give result as none

my_Dict['two']=2 # this will assign key value to the existing dict
my_Dict['two']=3 # this will update the existing key
'''
print(my_Dict)
print(my_Dict.keys()) # gives you all keys
print(my_Dict.values()) # gives you all values
print(my_Dict.items()) # gives you info about dict
y=my_Dict.copy() # copy will assign a different memeory location for dict.
print(id(y),id(my_Dict)) # you can check memory bit loc
print(y)

'''
'''
my_new_dic={'ant':'animal'}
my_Dict.update(my_new_dic)
print(my_new_dic)

'''

my_key=['a','e','i','o','u']
my_new_key=dict.fromkeys(my_key) # this is how you can create new key from existing one
my_new_key['a']='vowle' # assign value for key
print(my_new_key)


x={}
print(dir(x)) # gives you operation of dict

