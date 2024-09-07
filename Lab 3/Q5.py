import json

l=[]
eq=False
d = {}
n = int(input("Enter the number of people in the dictionary: "))

for _ in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    d[name] = age

try:
    with open('ex.json', 'w') as file:
        json.dump(d, file)
    print("Dictionary saved")
except Exception as e:
    print("Error: ", e)


try:
    with open('ex.json','r') as file:
        l = json.load(file)
        maxAge = list(l.values())[0]#let's suppose that the value at 1st index is the highest
        for age in l.values():
            if maxAge < age:
                maxAge = age
        print('Max age is: ',maxAge)

        for i in l:
            for j in l:
                if l[i] == l[j] and i != j:
                    same = l[i]
                    eq = True
                    break
            if eq:
                break

        if eq:
            print('Same age is:', same)
        else:
            print("No people with the same age.")
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("Error in reading the file.")
except Exception as e:
    print(str(e))
