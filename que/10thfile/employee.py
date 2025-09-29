class Emp:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary
    
    def calculate_salary(self):
        return self.base_salary
    
    def show_details(self):
        return f"Employee: {self.name},Salary: {self.calculate_salary()}" #to run the calculation () used 

class Manager(Emp):
    def calculate_salary(self):
        return self.base_salary + 5000 
class Developer(Emp):
    def calculate_salary(self):
        return self.base_salary + 3000 

emp1 = Manager("Alice",23000)
emp2 = Developer("chukss",35000)

print(emp1.show_details())
print(emp2.show_details())