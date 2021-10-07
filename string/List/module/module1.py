# A module is afile containing python defintions and statements. That means module containing python function, classes and var
# to install and update your module us pip install modulename
import module # here importing module
import math
#from math import *   this is to import all the option avalaible with math
print(module.my_value) # printing module information..

print(math.pi) # variabled don't have any arguments so no parentheis


# help("modules") to check default modules in python
# help(math) this will give you info about what value of math has function and what take it as var (DATA)
print(math.pow(2,3)) # this is term as func as it takes some arg

# how to use any module(here platform as ex) in your script
import platform
import platform as pt

# how do i list all func & var of a plat modules
#dir() function
print(dir(platform))

# howto get help of a platfomr module ?
#From python cmdline 

print(help(platfomr))


