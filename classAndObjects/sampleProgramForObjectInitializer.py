
class Employee:
    #here the __init__() works as a object initializer which can also be reffered to constructor in other OOP languages like JAVA and CPP
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department



john = Employee(3789, 2500, "Human Resources")

# Printing properties of john
print("ID :", john.ID)
print("Salary :", john.salary)
print("Department :", john.department)