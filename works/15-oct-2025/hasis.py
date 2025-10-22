
#IS_A function and HAS_A function codes 
class Human:
	pass 
class king(Human):
	pass

class Sword:
	pass
class Horse:
	pass

class King1(Human):
	def __init__(self):
		self.sword = Sword()
		self.horse = Horse()
		
kings = King1()

