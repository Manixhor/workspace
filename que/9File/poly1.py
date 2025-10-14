pi = 3.14
class Circle: 
	def __init__(self,radius):
		self.radius = radius
		
	def area(self):
		return pi*self.radius ** 2

class Rectangle:
	def __init__(self,length,breadth):
		self.length = length 
		self.breadth = breadth 
	def area(self):
		return self.length * self.breadth

class triangle:
	def __init__(self,height,base):
		self.base = base
		self.height = height
		#self.height = height 
	def area(self):
			return 0.5* self.base *self.height

shapes = [ 
Circle(5),
Rectangle(4,5),
triangle(3,7)]
def print_areas(shapes): 
	for shape in shapes: 
		print("Area:", shape.area())

print_areas(shapes)
		
		
		

