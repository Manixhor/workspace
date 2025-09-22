class a:
    def greet(self):
        return "welcome"
    
class b:
    def greet(self):
        print("hello1")
class c(a,b):
    pass

cls = c()
print(cls.greet())