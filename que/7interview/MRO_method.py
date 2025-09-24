class School1:
    def greet(self):
        print("hello welcome to the school1")
class School2:
    def greet(self):
        print("hello welcome to school2")

class Student(School1,School2):
    def greet(self):
        print("hello i am student")
        super().greet()

s = Student()
s.greet()

print(Student.mro())
