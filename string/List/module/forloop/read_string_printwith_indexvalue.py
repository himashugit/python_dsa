'''
usr_strng= input("Enter your string: ")
index=0 # index var is defined
for each_char in usr_strng:
    print(f' {each_char} -->{index}')
    index=index+1 # we're increasing index value by 1

'''
import os
req_path= input("Enter your dir path: ")
if os.path.isfile(req_path):
    print(f' the {req_path} is a file pls provide dir ')
else:
    all_f_ds= os.listdir(req_path)
    if len(all_f_ds)==0:
        print(f" the given path {req_path} is empty")
    else:
        req_ex=input("Enter the req file extention .py/.sh/.log/.txt: ")
        req_files=[]
        for each_file in all_f_ds:
            if each_file.endswith(req_ex):
                req_files.append(each_file)
            if len(req_files)==0:
                print(f'There are no {req_ex} files in the location of {req_path}')
            else:
                print(f'There are {len(req_files)} files in the loc of {req_path} with an extention of {req_ex}')
                print(f'the reuired files are: {req_files}')
