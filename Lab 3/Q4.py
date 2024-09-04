name = input('Enter your name: ')
cnic = int(input('Enter your cnic number: '))
age = int(input('Enter your age: '))
salary = int(input('Enter your salary: '))

l1 = [name,cnic,age,salary]
try:
    with open('example','w') as file:
        file.write("Bio Data of the Employee:\n")
        for i in range(len(l1)):
            file.write(str(f"{l1[i]} ,"))

    number = int(input('Enter your contact number: '))

    with open('example','a') as file:
        file.write(str(number))
except Exception as e:
    print(str(e))
