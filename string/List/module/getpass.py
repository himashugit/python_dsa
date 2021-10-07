#getpass() - prompt user for a pass without echoing. The getpass module provides a secure way to handle pass prompt
import getpass
db_pass=getpass.getpass()
print(f'the enterer pass is {db_pass}')

# getuser() = func display login name of the user. This func check the env var LOGNAME, USER<LNAME & USERNAME in order and returns the value of the fist non-empty string.

getpass.getuser





