import os

def main():
   path = input("Enter your desire path: ")
   print("The current path is: ", os.getcwd())
   try:
       os.chdir(path)
       print("working dir is: ", os.getcwd())
   except FileNotFoundError:
        print("Given file is not a correct file")

   except PermissionError:
        print("Sorry you don't have access")

if __name__ == '__main__':
    main()