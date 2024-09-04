num = int(input('Enter the length of lists: '))
l1 = []
l2 = []
d = {}

print('Enter elements for list 1: ')
for i in range(num):
    l1.append(int(input()))

print('Enter elements for list 2: ')
for i in range(num):
    l2.append(int(input()))

for i in range(len(l1)):
    d[l1[i]] = l2[i]

try:
    with open('example', 'w') as file:
       file.write(str(d))#error comming that d mustbe a string not dictionary
except Exception as e:
    print(str(e))
