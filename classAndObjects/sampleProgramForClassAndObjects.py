class Employee:
    # defining the properties and assigning them None
    ID = None
    salary = None
    department = None


# cerating an object of the Employee class
john = Employee()

# assigning values to properties of john - an object of the Employee class
john.ID = 3789
john.salary = 2500
john.department = "Human Resources"

# Printing properties of john
print("ID =", john.ID)
print("Salary", john.salary)
print("Department:", john.department)