# for loop - used to iterate over a sequence of code (list,tuple, string)
my_list=[1,2,3,4,5,"hi","hello"]
for each in my_list: # this is for loop to print all the values in the my_list one by one
    print(each)

for each_char in "python": # an example of string in loop
    print(each_char)




'''
import os
import sys
path=input("Enter your dir path: ")
if os.path.exists(path):
    df_l=os.listdir(path)
else:
    print("Please provide a valid path")
    sys.exit()

list_of_files_dir=os.listdir(path)
print("all files and dirs: ", list_of_files_dir)
for each_file_or_dir in list_of_files_dir:
    f_d_p=os.path.join(path, each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f' {f_d_p} : ------ is a file')

    else:
      print(f' {f_d_p} : ------  is a dir' )

'''


'''
import os
path=input("Enter your path: ")

if os.path.exists(path):
    print(f"path is: {path}  valid")
    if os.path.isfile(path):
        print(f"The given path {path} is file")
    else:
        print("it is a dir")

else:
    print(f"This path {path} is not valid")
'''

