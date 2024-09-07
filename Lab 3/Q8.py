try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"Result of division: {result}")

except ZeroDivisionError:
        print("Error: Cannot divide by 0")
except ValueError:
        print("Error: invalid values entered")
except Exception as e:
        print("Error: ", e)
