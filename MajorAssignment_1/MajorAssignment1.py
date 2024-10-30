#Question 1 
def basic_salary(hourly_rate,hours_worked_per_week):
    return 4*hourly_rate*hours_worked_per_week
def overtime_salary(hourly_rate,hours_worked_per_week):
    if hours_worked_per_week>40:
        overtime=hours_worked_per_week-40
        return hourly_rate*1.4*overtime*4
    else:
        return 0
def total_salary(hourly_rate,hours_worked_per_week):
    basic=basic_salary(hourly_rate,hours_worked_per_week)
    overtime=overtime_salary(hourly_rate,hours_worked_per_week)
    return basic+overtime

#Question 2
def tax_amount(basic_salary):
    if basic_salary<60000:
        return (10/100)*basic_salary
    elif basic_salary>60000 and basic_salary<85000:
        return (15/100)*basic_salary
    else:
        return (20/100)*basic_salary

#Question 3
def gross_salary(basic_salary):
    allowances=(20/100)*basic_salary
    tax=tax_amount(basic_salary)
    return basic_salary+allowances-tax

#Question 4
def salary_bracket(gross_salary):
    if gross_salary<50000:
        return "Low income"
    elif gross_salary>50000 and gross_salary<80000:
        return "Middle income"
    else:
        return "High income"
    
#Question 5
def employee_report(employees):
    print(f"{'Employee Name':<15}{'Basic Salary':<15}{'Gross Salary':<15}{'Tax Amount':<15}{'Salary Bracket':<15}")
    print("="*60)
    for employee in employees:
        name, hourly_rate, hours_per_week = employee
        basic = basic_salary(hourly_rate, hours_per_week)
        gross = gross_salary(basic)
        tax = tax_amount(basic)
        bracket = salary_bracket(gross)
        print(f"{name:<15}{basic:<15.2f}{gross:<15.2f}{tax:<15.2f}{bracket:<15}")

#use case for output
employees = []
for i in range(3):
    name = input(f"Enter the name of Employee {i+1}: ")
    hourly_rate = float(input(f"Enter the hourly rate of {name}: "))
    hours_per_week = float(input(f"Enter the hours worked per week by {name}: "))
    employees.append((name, hourly_rate, hours_per_week))
employee_report(employees)
