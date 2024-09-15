class Student:
    def __init__(self, name, iid):
        self.st_name = name
        self.st_id = iid

    def get_info(self):
        print(f"Student Name: {self.st_name}\nStudent ID:{self.st_id}")


class Marks(Student):
    marks = []

    def __init__(self, name, iid):
        super().__init__(name, iid)
        self.marks = []

    def courses_marks(self):
        a = int(input('Enter the number of courses: '))
        print("Enter the marks of the courses:")
        for i in range(a):
            self.marks.append(int(input(f"Course {i+1}")))

    def show(self):
        print(self.marks)


class Result(Marks):
    total = 0
    avg=0

    def __init__(self, name, iid):
        super().__init__(name,iid)

    def calculate(self):
        for i in range(len(self.marks)):
            self.total += self.marks[i]

    def info(self):
        self.avg = self.total / len(self.marks)
        print(f"Total marks: {self.total} and Average is: {self.avg}")


res = Result("S. Sara Ali", "23K-0070")
res.get_info()
res.courses_marks()
res.show()
res.calculate()
res.info()
