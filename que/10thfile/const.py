class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #@classmethod
    def string(Person,data_string):
        name,age = data_string(",")
        return Person(name, int(age))
    
    @classmethod
    def dict(cls,data_dict):
        return cls(data_dict["name"],data_dict["age"])
    
    
p1 = Person("john",20)

print(p1.name,p1.age)
p3 = Person.from_dict({"name": "Bob", "age": 30})