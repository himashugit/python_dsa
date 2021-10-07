my_list=[]
print(bool(my_list)) # bool of empty list is always false


my_list1=['heelo', 1,2,2]
print(bool(my_list1)) # bool of data list is True
# you can use index value func to get the list value...
print(my_list1[1])
print(my_list1[-1])
print(my_list1[:-2])

# lists are mutable, strings are immutable

my_list2=[1,2,3,4,5,6]
print(dir(my_list2)) # method/operations available with your list

print(my_list2.index(1))
print(my_list2.count(10))

my_list3=[1,2,3,4,5,6]
my_list3.append(33)
print (my_list3)

