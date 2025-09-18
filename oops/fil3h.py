#to create a class student details of 5 subjects and give the total marks of the student 
class student:
    def __init__(self,computer = None,science = None,maths = None ,physics = None ,commerce = None):
        self.computer = computer
        self.science = science
        self.physics = physics
        self.commerce = commerce
        self.maths = maths
        pass

    def total(self):
        print(f"marks of student: {self.computer + self.commerce + self.science + self.physics + self.maths}")
    





stu1 = student(34,92,73,81,62)
stu2 = student(34,82,73,51,92)
stu3 = student(34,32,93,51,82)
stu4 = student(34,42,73,61,92)
stu5 = student(34,52,63,71,92)

print(stu1.total())
stu1.total()
stu2.total()
stu3.total()
stu4.total()
stu5.total()