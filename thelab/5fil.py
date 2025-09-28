class parent:

    def __init__(self):
        self.networth = 10000
    def sing(self):
        print("parent is singing")
    
class child(parent):
    def dance(self):
        print("child is dancing")

cls1 = child()

cls1.dance()
cls1.sing()
print(cls1.networth)

#multiple 