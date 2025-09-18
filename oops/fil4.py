# #static variable
# class person:
#     sleepingtime = 8

#     def __init__ (self,name,age):
#         self.name = None 
#         self.age = None 
#         self.sleepingtime = 10


# #here we can access class name
# print(person.sleepingtime)
# #here we need to create an object to call constructor value 
# person1 = person("mani",23)
# print(person1.sleepingtime)

#static method 
class car:
    sleepingtime = 8 
    def __init__(self,name,age):
        self.name = car
        self.age = 1
        self.sleepingtime = 10

    @staticmethod 
    def sleep():
        print(car.sleepingtime)

    @classmethod
    def sleep1(cls):
        print(cls.sleepingtime)

    def shutdown(self):
        print(self.sleepingtime)

car.sleep()
car1 = car("ferrari",2)
print(car1.shutdown())

car.sleep1()
car1.shutdown()