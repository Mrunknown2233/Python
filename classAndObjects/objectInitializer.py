class Employee:
    # defining the properties and assigning them None
    def __init__(self, ID, salary, department):
        self.ID = ID
        self.salary = salary
        self.department = department


# creating an object of the Employee class with default parameters
john = Employee(3789, 2500, "Human Resources")

# Printing properties of john
print("ID :", john.ID)
print("Salary :", john.salary)
print("Department :", john.department)