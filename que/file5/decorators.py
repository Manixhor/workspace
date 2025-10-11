def log(func):
	def wrapper(*args, **kwargs):
		print(f"calling function: {func.__name__}")
		print(f"Arguments: {args},{kwargs}")
		
		result = func(*args,**kwargs)
		
		print(f"Returned: {result}")
		return result 
	return wrapper

@log
def add(a,b):
	return a + b
	
add(5,3)