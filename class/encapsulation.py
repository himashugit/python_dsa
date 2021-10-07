# using oop in Python we can restrict acces to methids and var
# This prevent data from modification which is called encapsulation

class Person(object):
    def assign_name_age(self,age,sex):
        #self.age = age
        self.__age = age
        self.sex = sex
        return None

    def display(self):
        print(self.age,self.sex)
        return None

per1 = Person()
per1.assign_name_age(34,'M')
per1.display()
