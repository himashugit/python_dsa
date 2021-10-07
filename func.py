# to clean and run the dir list
import os
import time
import platform

def mycode(cmd1,cmd2):

  print("Please wait cleanup in progress")
  time.sleep(2)
  os.system(cmd1)
  print("please wait")
  time.sleep(2)
  os.system(cmd2)

if platform.system()=="Windows":
    mycode("cls","dir")
