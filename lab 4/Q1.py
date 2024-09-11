l1 = ['He','th','i','sal']
l2 = ['llo','is','s','man']
l3 = []
st = ''
for i in range(len(l1)):
    l3.append(l1[i] + l2[i])
    st += l1[i] + l2[i]
    st += ' '
print(l3)
print(st)
