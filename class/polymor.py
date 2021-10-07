# Polymorphism allows us to define same methods in diff  classess
# T his process is also known as Mehtod overriiding

class Tomcat():
    def __init__(self,loc,version):
        self.loc=loc
        self.version=version
        return None

    def display(self):
        print("This is from tomcat class")
        print(self.loc)
        print(self.version)
        return None

class Apache(): # here I've duplicate the information from the class Tomcat
    def __init__(self,loc,version):
        self.loc=loc
        self.version=version
        return None

    def display(self):
        print("This is from apache class")
        print(self.loc)
        print(self.version)
        return None




tom_obj=Tomcat('/etc/tomca', '3.2')
tom_obj.display()
apa_obj=Apache('/etc/apace', '4.3')
apa_obj.display()
#apa_obj=apache()

