
class self1:
    def __init__(self):
        print("self1 executed")
        self.a = 90
        self.b = 22

    def add(self):
        return self.a + self.b
    
obj = self1()


print(obj.add())