from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, n, sal):
        self.name = n
        self.salary = sal

    @abstractmethod
    def calculate_bonus(self):
        pass


class Manager(Employee):
    def __init__(self, n, sal):
        super().__init__(n, sal)
        self.bonus = None

    def calculate_bonus(self):
        self.bonus = self.salary * (20 / 100)
        print(f"Bonus of the manager is: {self.bonus}")

    def hire(self):
        print("Manager is hiring")


class Developer(Employee):
    def __init__(self, n, sal):
        super().__init__(n, sal)
        self.bonus = None

    def calculate_bonus(self):
        self.bonus = self.salary * (10 / 100)
        print(f"Bonus of the developer is: {self.bonus}")

    def write_code(self):
        print("MDeveloper is writing a code")


class SeniorManager(Manager):
    def __init__(self, n, sal):
        super().__init__(n, sal)
        self.bonus = None

    def calculate_bonus(self):
        self.bonus = self.salary * (30 / 100)
        print(f"Bonus of the senior manager is: {self.bonus}")

    def hire(self):
        print("Senior Manager is hiring")


E1=Manager("Ali",68887)
E2=Developer("Abbas",58004)
E3=SeniorManager("Sara",887472)
E1.calculate_bonus()
E1.hire()
E2.calculate_bonus()
E2.write_code()
E3.calculate_bonus()
E3.hire()
