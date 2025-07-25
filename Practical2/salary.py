salaries = []
for i in range(1, 6):
    print(f"Enter details for Employee {i}:")
    hours = float(input("  Working hours: "))
    if not (hours >= 0):
        print("  Invalid input. Working hours cannot be negative.")
        hours = 0
    wage = float(input("  Hourly wage: "))
    if not (wage > 0):
        print("  Invalid input. Wage must be greater than 0.")
        wage = 0
    if hours <= 40:
        salary = hours * wage
    else:
        salary = (40 * wage) + ((hours - 40) * wage * 1.5)
    salaries.append(salary)
print("--- Employee Salaries ---")
for i in range(5):
    print(f"Employee {i+1}: ${salaries[i]:.2f}")
