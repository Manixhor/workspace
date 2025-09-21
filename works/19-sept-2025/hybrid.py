#code hybrid inheritance concept
class A:
    def func1(self):
        print("This is function 1 from class A")
class B(A):
    def func2(self):
        print("This is function 2 from class B")
class C(A):
    def func3(self):
        print("This is function 3 from class C")
class D(B,C):
    def func4(self):
        print("This is function 4 from class D")
obj = D()
obj.func1()
obj.func2()
obj.func3()
obj.func4()