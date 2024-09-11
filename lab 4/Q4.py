class Employee:
    def __init__(self):
        self.tax_per = None
        self.name = None
        self.m_salary = None

    def get_data(self, name, m_salary, tax_per):
        self.name = name
        self.m_salary = m_salary
        self.tax_per = tax_per

    def Salary_after_tax(self):
        self.m_salary -= self.m_salary * self.tax_per / 100
        return self.m_salary

    def update_tax_percentage(self, tax):
        self.tax_per = tax
        self.m_salary -= self.m_salary * self.tax_per / 100
        return self.m_salary


E1 = Employee()
E1.get_data("Sara", 2000, 2)
print(E1.Salary_after_tax())
print(E1.update_tax_percentage(3))
