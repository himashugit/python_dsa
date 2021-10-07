class person(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print(f' name is {self.name}\n age is {self.age}\n sex is {self.sex}')


person1 = person('himan',33,'male')

# destructir method will call by defalut when object is deleted from mem by Python
#syntax
