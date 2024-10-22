import numpy as np

#structured data type
student_dtype = np.dtype([
    ('Name', 'U10'),    # Unicode string with max length of 10
    ('Height', 'f4'),   # Float (4 bytes)
    ('Class', 'i4')     # Integer (4 bytes)
])

students = np.array([
    ('Sara', 5.2, 2),
    ('Ali', 6.0, 2),
    ('Abbas', 5.7, 1),
    ('Haider', 5.8, 1),
    ('Sakina', 5.5, 3)
], dtype=student_dtype)

sorted_students = np.sort(students, order=['Class', 'Height'])#class then height

print("Students:")
print(sorted_students)
