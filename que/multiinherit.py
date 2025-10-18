#Multiple and multilevel inheritance 

# class GrandParent:
#     def swim(self):
#         print("grand can swim")

# class Parent:
#     def sing(self):
#         print("paren can sing")

# class Child(Parent,GrandParent):
#     def dance(self):
#         print("child can dance")

# cls1 = Child()
# cls1.dance()




class GrandParent:
    def swim(self):
        print("grand can swim")

class Relative(GrandParent):
    def drive(self):
        print("relative can drive")

class Parent(GrandParent):
    def sing(self):
        print("paren can sing")

class Child(Parent,Relative):
    def dance(self):
        print("child can dance")

cls1 = Child()
cls1.drive()
#here child can't access the parent 

cls2 = Parent()
cls2.swim()
