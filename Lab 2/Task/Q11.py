def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
    else:
        print(f"Student named {name} not found")

def average_grade(name):
    if name in students:
        avg = sum(students[name]) / len(students[name])
        print(f"Average grade for {name}: {avg}")
    else:
        print(f"Student named {name} not found")

def add_student(name):
    if name not in students:
        students[name] = []
        print(f"Student {name} added")
    else:
        print(f"Student named {name} already exists")

def remove_student(name):
    if name in students:
        del students[name]
        print(f"Student named {name} removed")
    else:
        print(f"Student named {name} not found")

students = {"Sara": [95, 89], "Ali": [88, 96],"Abbas":[98,87]}

add_student("Jane")
add_grade("Abbas", 95)
average_grade("Ali")
remove_student("Sara")
print(students)
