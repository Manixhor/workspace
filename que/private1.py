class School:
	def __init__(self):
		self.name = "Mani"
		self.place = "hyd"
		self.__reverse = 500000
	def school(self):
		print(self.__reverse)
	def __privateMethod(self):
		print(self.__reverse)
	def publicmethod(self):
		self.__privateMethod()
school1 = School()
print(school1.name)
school1.school()
school1.publicmethod()