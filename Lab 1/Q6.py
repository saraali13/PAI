ph=float(input("Enter your physics marks"))
ch=float(input("Enter your chemistry marks"))
mt=float(input("Enter your math marks"))
dic={'Subject Name':['Physics','Chemistry','Math'],'Marks':[ph,ch,mt]}
avg=(ph+ch+mt)/3
print(dic)
print(avg)
if ph>ch and ph>mt:
    print("Got highest marks in physics")
elif ch>ph and ch>mt:
    print("Got highest marks in chemistry")
else:
    print("Got highest marks in maths")
