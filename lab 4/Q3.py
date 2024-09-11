class student:
    name=""
    age=""

    def __init__(self,name,age):
        student.name=name
        student.age=age

    def Print_biodata(self):
        print("Student's Bio Data:")
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))


St1=student("Sara","18")
St1.Print_biodata()
