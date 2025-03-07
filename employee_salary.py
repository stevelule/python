# Define the base class Employee 
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id 
        self.name = name  
        self.salary = salary  
    
    def calculate_salary(self):
        return self.salary  
    
# Define HourlyEmployee subclass
class HourlyEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)  # Base salary set to 0 initially
        self.hourly_rate = hourly_rate  
        self.hours_worked = hours_worked  
    
    def calculate_salary(self):
        self.salary = self.hourly_rate * self.hours_worked  # Calculate salary
        return self.salary

# Define SalariedEmployee subclass
class SalariedEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name, monthly_salary)
    
    def calculate_salary(self):
        return self.salary  

#usage
hourly_emp = HourlyEmployee(1, "Alice", 20, 40) 
salaried_emp = SalariedEmployee(2, "Bob", 3000) 

print(f"{hourly_emp.name}'s Salary: ksh{hourly_emp.calculate_salary()}")
print(f"{salaried_emp.name}'s Salary: ksh{salaried_emp.calculate_salary()}")
