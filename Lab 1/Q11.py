eng=float(input("Enter english marks"))
cmp=float(input("Enter computer marks"))
mt=float(input("Enter math marks"))
dic={
    "English":eng,
    "Computer":cmp,
    "Maths":mt
}
marks=sum(dic.values())
avg=marks/3
per=(marks/300)*100

print(dic)
print("Total Marks: ",marks)
print("Average Marks: ",int(avg))
print("Percentage: ",per)
