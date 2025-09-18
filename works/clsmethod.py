class cookies: 
    # this for normal construtor
    def __init__(self,flavor,size):
        self.flavor = flavor
        self.size = size

    @classmethod
    def small(cls,flavor):
        return cls(flavor,"small")
    
    @classmethod
    def large(cls,flavor):
        return cls(flavor,"large")
    
c0 = cookies("blackcurrant","medium")
print(c0.flavor,c0.size)

c1 = cookies.small("strawberry")
print(c1.flavor,c1.size)
    
c2 = cookies.large("vannila")
print(c2.flavor,c2.size)