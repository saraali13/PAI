def employee(name,monthly_salary=10000):
    monthly_salary=monthly_salary-monthly_salary*0.02
    print(f"Name of Employee: {name}, Salary after tax deduction : {monthly_salary}")

employee("Sara",23000)
employee("Ali")
