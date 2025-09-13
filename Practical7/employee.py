print("By 22IT460")
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Basic Salary: ₹{self.salary:.2f}")
class Salary(Employee):
    def __init__(self, emp_id, name, basic_salary):
        super().__init__(emp_id, name, basic_salary)
        self.pf = 0
        self.tds = 0
        self.section_80C = 0
        self.net_salary = 0
    def calculateSalary(self):
        self.pf = 0.12 * self.salary
        self.tds = 0.10 * self.salary
        self.section_80C = 0.05 * self.salary
        total_deductions = self.pf + self.tds + self.section_80C
        self.net_salary = self.salary - total_deductions
    def display_salary_slip(self):
        print("\nSalary")
        self.display()
        print(f"PF (12%): ₹{self.pf:.2f}")
        print(f"TDS (10%): ₹{self.tds:.2f}")
        print(f"80C Investment (5%): ₹{self.section_80C:.2f}")
        print(f"Net Salary: ₹{self.net_salary:.2f}")
emp1 = Salary(101, "Neel", 50000)
emp1.calculateSalary()
emp1.display_salary_slip()