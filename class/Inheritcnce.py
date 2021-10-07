# Inheritence is a mechanism that allow us to ceate a new class known as child class - that is based upon an existin class - the parent class
# here I wil linherit once class into another one so that method used in once class use inside another class


class Tomcat():
    def __init__(self,loc,version):
        self.loc=loc
        self.version=version
        return None

    def display(self):
        #print("This is from tomcat class")
        print(self.loc)
        print(self.version)
        return None

class Apache(Tomcat): # here I've duplicate the information from the class Tomcat. Tomcat is parent and apache here is child
    def __init__(self,loc,version):
        self.loc=loc
        self.version=version
        return None

tom_obj=Tomcat('/etc/apache', '2.3')
apa_obj=Apache('/etc/tomcat', '2.5')
tom_obj.display()
apa_obj.display()