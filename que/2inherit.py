class Parent:
	def drive(self):
		print("driving")
	
class Child(Parent):
	def drive(self):
		super
		print("child is driving")