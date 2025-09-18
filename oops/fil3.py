
# class person:
#     Name = None
#     print("class involved")
    

# person1 = person()
# person1.Name = "Akhil"
# print(person1.Name)


class person:
    def __init__(self,name,age,phn):
        self.name = name
        self.age = age
        self.phn = phn 
    
    def display(self):
        print(f"{self.name},{self.age},{self.phn}")

person1 = person("mani",22,43243)
person.display(person1)
print(person1.name)
