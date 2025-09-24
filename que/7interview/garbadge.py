import gc 

class Toy:
    def __init__(self,name):
        self.name = name 
        print(f"Toy {self.name} is created!")
    def __del__(self):
        print(f"Toy {self.name} is destroyed!")
#is it mandato

t1 = Toy("car")
#here i created a toy function
t2 = t1 
#here i declared to t2 
del t1
#now i deleted  but it will we be stored in t2

print("Toy is still here because t2 is holding it")

del t2 

#here we will force garbage collector to clean up now
gc.collect()

print("now it is cleaned up")