l=[]
sum = 0
num = int(input('Enter the length of list:'))
x=int(input("enter a number"))
ans = []
for i in range(num):
    l.append(int(input("enter the number: ")))

for j in range(num):
    if l[j] >= x:
        ans.append(l[j])

print(ans)
