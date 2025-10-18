#to create a class student details of 5 subjects and give the total marks of the student 
class student:
    computer = None
    science = None 
    maths = None 
    physics = None 
    commerce = None

    def total(self):
        print(f"total_marks is : {self.computer + self.science + self.maths + self.physics + self.commerce}")

stu1 = student()
stu1.commerce = 90
stu1.maths = 80
stu1.science = 70
stu1.physics = 50
stu1.computer = 60

stu1.total()

stu2 = student()
stu2.commerce = 95
stu2.maths = 85
stu2.science = 75
stu2.physics = 55
stu2.computer = 65
stu2.total()

result = []



print(result)