num = list(map(int, input("Enter numbers: ").split())) 
#map will covert each string to an int number then then list
#split will split a single string input to list of strings"1 2 3" to "1" "2" "3"

largest_num = max(num)
print("The largest number is:", largest_num)
