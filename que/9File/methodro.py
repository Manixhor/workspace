class A: 
	def show(self):
		print("A")
		
class B(A):
	def show(self):
		print("B")
		
class C(B,A):
	pass


obj = C()
obj.show()
print(C.mro())