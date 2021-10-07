# A constructor is a special method that is called by default whenever you creare an obj from a class.

class Emp():
    count=0 # defining var count value as 0
    def __init__(self,name,age,salary): # you can get this info without calling this func as well.
        Emp.count=Emp.count+1
        #print("This is init...") # this will print even if we're not calling init method
        self.name=name
        self.age=age
        self.salary=salary
        self.get_det()
        return None

    def get_det(self):
        print(f' the name is {self.name} \nthevage is {self.age} \nsalary is {self.salary}')
        return None

emp2=Emp('hi',33,39000) # thid is how you call init method which takes 3 arg
emp1=Emp('himan',33,38000)
#emp1.get_det() # calling this inside init method so no need to call it here                         
print("the numner of emp", Emp.count) # this will  give you count of emp define as object
