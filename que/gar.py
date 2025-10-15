class Toy:
	def __init__(self,name):
		self.name = name
		print(f"Toy {self.name} is created")
	def __del__(self):
		print(f"Toy {self.name} is destroyed")
		
t1 = Toy("car")
t2 = Toy("Robot")

del t1
print("End of program")