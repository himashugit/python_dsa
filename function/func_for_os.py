import os
import time
import platform

def mycode(cmd1, cmd2): # this how we can define the function to get the logic short from the below method (commented out)
    
    print("Please wait cleaning screen...")
    time.sleep(2)
    os.system(cmd1)
    print("Please wait generating list of dir")
    time.sleep(2)
    os.system(cmd2)

if platform.system()=="Windows":
    mycode("cls", "dir")
else:
    mycode("clear", "ls-lrt")


'''
if platform.system()=="Windows":
    print("Please wait cleaning screen...")
    time.sleep(2)
    os.system("cls")
    print("Please wait generating list of dir")
    time.sleep(2)
    os.system("dir")
    
else:
     print("Please wait cleaning screen...")
     time.sleep(2)
     os.system("clear")
     print("Please wait generating list of dir")
     time.sleep(2)
     os.system("ls-lrt")
'''
