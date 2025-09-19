
#the question is about inheritance that we create initialize function with certain parameter in print which takes function 
class function:
    def __init__(a,b,c):
        return a + b + c
    
    def __init__(a,b):
        return a + b
    def __init__(a):
        return a 
    
print(function.__init__(3))