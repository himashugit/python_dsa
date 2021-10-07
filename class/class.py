
# class is template/blueprint to create an object
# class is the combination of attributes and methods
# we can define Attributes for class and objects.
class employee:
     count = 0 # this is the class attribute and a class variable
     def get_details(self,name,age,salary): #self is by default key inside aclass,get details is a method inside class
         self.name=name # variable
         self.age=age
         self.salary=salary
         self.get_info() # you can call one method inside o=another method
         self.count_for_emp()

         return None
     def count_for_emp(self):
          employee.count=employee.count+1
          return None


     def get_info(self):
         print(f'the name is {self.name} \n age is {self.age} \n salary is {self.salary}') # you can call variable from one mentod to another as we're doing here
         return None

emp1=employee() # this is how you'll call the employee template which you've created as class. Class has objects as employee and it takes attributes,emp1 store in self.

emp2=employee() # emp2 is an object and you're defining your class here to call

emp1.get_details('himan', 33, 500000)
emp2.get_details('geet', 31, 30000)
print(employee.count)
#emp1.get_info()



