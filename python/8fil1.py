class Person:
    def __init__(self):
        self.__name = None
        self.__age = None
    
    @property
    def age(self):
        if self.__age is None:
            return "empty is not accepted"
        return self.__age
    
    @property
    def name(self):
        if self.__name is None:
            return "name can't be empty"
        return self.__name
    @age.setter
    def age(self,value1):
        self.__age = value1
  
    @name.setter
    def name(self,value):
        if len(value) > 20:
            print("can't be more than 20")
        else:
            self.__name = value
              
    
        
   
per1 = Person()
per1.name = "Mani"
print(per1.name)

per1.age = 22
print(per1.age)


class Nameadding:
    def __init__(self):
        self.__firstname = "rolex"
        self.__lastname = "M"
    
    @property 
    def adding(self):
        return self.__firstname + " " + self.__lastname
    
name = Nameadding()
print(name.adding)