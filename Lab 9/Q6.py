import matplotlib.pyplot as plt
import pandas as pd

Student_Data = {
    'Name': ["Sara", "Ali", "Sakina", "Abbas", "Haider", "Zainab", "Hussain", "Hassan", "Fatima", "Zehra"],
    'Science': [90, 80, 60, 90, 88, 85, 84, 87, 93, 85],
    'Maths': [100, 99, 75, 98, 88, 75, 82, 92, 85, 93]
}
df = pd.DataFrame(Student_Data)

plt.scatter(df['Name'], df['Science'], color='green', label='Science')
plt.scatter(df['Name'], df['Maths'], color='red', label='Maths', marker="*")
plt.xlabel('Student')
plt.ylabel('Marks')
plt.title('Scatter Plot of Math and Science Marks')
plt.legend()
plt.show()
