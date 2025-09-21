class postion:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        print(self.a + self.b + self.c + self.d)
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        print(self.a + self.b + self.c)
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print(self.a + self.b)
    def __init__(self,a):
        self.a = a
        print(self.a)

pos = postion(23)
