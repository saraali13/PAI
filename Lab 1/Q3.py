l=[]
count = 0
num = int(input('Enter the length of list:'))

for i in range(num):
    l.append(int(input("enter the number: ")))

for j in range(num):
    if l[j] % 2 == 0:
        count += 1

print(count)
