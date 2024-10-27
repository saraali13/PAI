import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Student_gender.csv")

gender_distribution = df['Gender'].value_counts()
l=["Male","Female"]

plt.pie(gender_distribution, labels=l,colors=['blue', 'pink'])
plt.title("Gender Distribution Among Students")
plt.show()
