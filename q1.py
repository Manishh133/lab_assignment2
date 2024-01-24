class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self, employees):
        self.employees = employees

    def print_employees(self):
        for employee in self.employees:
            print(f"{employee.emp_id} \t {employee.name} \t {employee.age} \t {employee.salary}")

    def sort_employees(self, sort_param):
        if sort_param == 1:
            self.employees.sort(key=lambda x: x.age)
        elif sort_param == 2:
            self.employees.sort(key=lambda x: x.name)
        elif sort_param == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter")

# Sample data
employee1 = Employee("161E90", "Ramu", 35, 59000)
employee2 = Employee("171E22", "Tejas", 30, 82100)
employee3 = Employee("171G55", "Abhi", 25, 100000)
employee4 = Employee("152K46", "Jaya", 32, 85000)

employees_list = [employee1, employee2, employee3, employee4]

# Create EmployeeDatabase object
employee_database = EmployeeDatabase(employees_list)

# Get sorting parameter from user
sort_parameter = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))

# Sort and print the result
employee_database.sort_employees(sort_parameter)
employee_database.print_employees()
