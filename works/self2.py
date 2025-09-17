
class cars:
    i = 10
    def show(self):
        print("self refers to:",self)
        

s = cars()
s.show()
s.j = 100
print(cars.i)

   

s.show()

s2 = cars()
s2.show()
s2.j = 200
s2.show()   