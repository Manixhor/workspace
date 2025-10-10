class custom:
	def __init__(self):
		self.items = []
		
	def append(self,value):
		if isinstance(value, int):
			self.items.append(value)
		else:
			raise TypeError("ony integers are allowed")
		
	def remove(self,value):
		if value in self.items:
			self.items.remove(value)
		else:
			raise ValueError(f"{value} not found")
	def pop(self,index=-1):
		if len(self.items) == 0:
			raiseIndexError("Nothing to pop!")
		return self.items.pop(index)
	
	def slice(self,start,end):
		return self.items[start:end]
		
	def __str__(self):
		return str(self.items)
		
		
mylist = custom()


mylist.append(5)
mylist.append(35)
mylist.append(54)
mylist.append(15)
mylist.append(25)
mylist.append(10)
mylist.remove(10)
mylist.pop()


print(mylist)
#printing the 0 to 6 elements ;
print(mylist.slice(0,6))