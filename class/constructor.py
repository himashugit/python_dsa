# constructor = special method inside your class, called by default whenever you create an object from a class..

class employee():
    count=0 # define var, int value =0 

    def __init__(self): # this is the by default method and you don't need to call to get the output. whenever you add object as below
        # this will addon. In the below obj I've added 2 emp and I'm not calling this method
        
        employee.count=employee.count+1 # adding 1 each time you add a new emp(object)
        #print("This is the by default class call")
    def get_detail(self):
        print("this is the empty calls")
        return None

emp1=employee() # emp1is object inside clase
emp2=employee()
#emp1.get_detail()
print('the numnber of employee called', employee.count)

#emp1.get_detail()