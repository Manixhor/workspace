# lcandy = 5
# def candy():
#     global lcandy
#     lcandy = lcandy - 1
#     print(lcandy)

# candy()
lcandy = 5
class Candy1:
    
    def candies(self):
       global lcandy
       lcandy += 5
       print(lcandy)
cls1 = Candy1()
cls1.candies()        
