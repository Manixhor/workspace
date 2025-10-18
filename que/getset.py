class Person():
	def __init(self):
		self.__name = None
		
	def setName(self,Value):
		self.__name = Value
	def GetName(self):
		return self.__name
		
per = Person()
per.setName("Mani")
print(per.GetName())