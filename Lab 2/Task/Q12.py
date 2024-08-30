list1 = ["a", "b", "c","d"]
list2 = [1, 2, 3,4]
dic = {}

if len(list1) != len(list2):
   print("Both Lists must have the same number of elements")
else:
    for i in range(len(list1)):
        key = list1[i]
        value = list2[i]
        dic[key] = value

print(dic)
