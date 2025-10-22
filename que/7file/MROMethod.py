class A:
	def do_something(self):
		print("A does something")
		
class B(A):
def do_something(self):
	print("B does something")
	super().do_something()