import sys

if len(sys.argv) !=3:
    print("Usage")
    print(f'{sys.argv[0]} <your req string> <lower|upper|title>')
    sys.exit()

usr_strn=sys.argv[1]
usr_action=sys.argv[2]

if usr_action=="lower":
    print(usr_strn.lower())
elif usr_action=="upper":
    print(usr_strn.upper())
elif usr_action=="title":
    print(usr_strn.title())
else:
    print("your option is invalid. Pls select valid option -  upper|lower|title")

print(sys.argv) # this will give you script namr and cmdline argument info
