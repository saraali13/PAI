def list_multiply(l):
    result=1
    for i in l:
        result*=i
    return result

num_list=[1,2,3,4,5]
print(f"Product of the list: {list_multiply(num_list)}")
