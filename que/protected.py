class School:
	def __init__(self):
		self.name = "Mani"
		self._revenue = 1000000
class Admin(School):
	def revenue(self):
		print(self._revenue)	
		
ad = Admin()
ad.revenue()