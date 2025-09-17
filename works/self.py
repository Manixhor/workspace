class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = None

    def bark(self):
        print(f"{self.name} is barking")

d1 = dog("tommy",2)
d2 = dog("sheru",4)

d1.bark()
d2.bark()