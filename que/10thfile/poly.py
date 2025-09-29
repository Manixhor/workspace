#different object can use the same method name but different behavior 
import math
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius ** 2
    
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
shapes = [
    Circle(5),Rectangle(3,2),Triangle(2,31)
]
for shape in shapes:
    print(f"Area: {shape.area()}")