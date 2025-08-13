class student:
    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and i am {self.age},old")


R = input()
a = int(input())
s1 = student(R,a)
s1.introduce()