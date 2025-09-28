class Parent:
    def drive(self,speed):
        print("parent is driving in",speed)
    
class Child(Parent):
    def drive(self,speed):
        super().drive(speed)
        print("child is driving in",speed-10)

child1 = Child()
child1.drive(50)