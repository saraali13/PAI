import matplotlib.pyplot as plt

students = ["Sara", "Ali", "Sakina", "Abbas", "Haider", "Zainab"]
heights = [70, 80, 73, 84, 87, 76]
clr = ["Purple", "red", "blue", "green", "yellow", "pink"]

# Bar Chart
plt.figure()  # for creating 2 separate figs
plt.bar(students, heights, color=clr)
plt.xlabel('Students')
plt.ylabel('Height')
plt.title('Student Height data')
plt.show()

# Pie Chart
plt.figure()  # first we'll close the bar graph then pie graph will appear automatically
plt.pie(heights, labels=students, colors=clr)
plt.title('Student Heights Distribution')
plt.show()
