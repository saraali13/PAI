def factorial(num):
    if num == 0:
        return 1
    elif num >= 1:
        fact = 1
        for i in range(1, num+1):
            fact *= i
        return fact

n = int(input("Enter a number: "))
print(factorial(n))


