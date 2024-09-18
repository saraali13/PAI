import re

text = "hi, sarazaidi@gmail.com kfk hgfr hhr saraali@gmail.com fge * ssara@gmail.com"

splitList = re.split(' ', text)
email = []

for i in splitList:
    if (re.search(".com", i)):
        email.append(i)

print(email)
