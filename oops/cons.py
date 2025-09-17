
class person:
    def __init__(self,name=None,age = None):
        self.Name = name
        self.age = age
        
person1 = person(age = 20)
print(person1.Name)
print(person1.age)